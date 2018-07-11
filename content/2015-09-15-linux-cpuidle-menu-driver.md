Title: [Linux] cpuidle menu driver & I/O latency predict driver
Date: 2015-09-15 05:47
Modified: 2015-09-15 05:47
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [Linux] cpuidle menu driver & I/O latency predict driver


# CPU idle driver
基本上是利用各種數據去預測接下來的cpu idle時間，以選擇適當的CPU idle state
CPU idle的state數量，idle時電流，switch時間都可以拿來衡量

# 為何不能想睡就睡?
既然idle state很省電，為何不能逮到機會就想辦法進idle睡呢?

1. Switch overhead
跟據關掉的東西的數量程度，每個idle等級要進入和出來的時間都不一樣
睡的越沉，醒的越慢
要是一直睡睡醒醒，反而會多花時間又耗電

2. 系統目前不容忍睡太死
跟Linux PM Framework有關
有時候系統會需要很即時的反應(e.g. DMA)，這個時候也不能睡太死

# Menu driver

Reference: 
http://www.wowotech.net/pm_subsystem/cpuidle_menu_governor.html
http://lxr.free-electrons.com/source/drivers/cpuidle/governors/menu.c

## menu

目前普遍的cpuidle driver
**超級簡化**來說，就是在系統允許的idle時間以內
用目前已知的**下一次timer距離、上次實際的idle時間、i/o task queue長度、i/o種類、cpu loading**來估計適合的idle時間 & 
另外也有偵測periodic event的機制
但基本精神是: 用上一次實際idle時間慢慢修正factor，乘上已知的下次timer時間

### menu_select

主要選擇idle state的function

**Steps**

1. Call ```pm_qos_request``` 得到CPU和DMA可接受的delay(latency_req)
2. Call ```menu_update```，用**上一次實際idle的時間**更正上一次使用的factor
3. 取得nohz下預計的sleep時間```next_timer_us``` & 目前在I/O wait queue的task數量```iowaiters``` 
4. 用3的結果來取得factor
	Governor會根據next_timer_us和有沒有iowaiters來個別maintain不同的factor，共有12個
5. 計算預計的idle時間```predicted_us```: 
``` c
data->predicted_us = DIV_ROUND_CLOSEST_ULL((uint64_t)data->next_timer_us *
                                        data->correction_factor[data->bucket],
                                        RESOLUTION * DECAY);
```
6. 用5的結果和iowaiters和cpuload，算出另一個最大可接受delay
	```predicted_us / (1 + 2 * loadavg +10 * iowaiters) ```
  和1算的取min值
  基本精神是**越忙越不能delay**
	
7. 用估計出來的idle時間(predicted_us)和可接受的delay(latency_req)選擇適合的idle state
``` c
for (i = CPUIDLE_DRIVER_STATE_START; i < drv->state_count; i++) {
                 struct cpuidle_state *s = &drv->states[i];
                 struct cpuidle_state_usage *su = &dev->states_usage[i];
 
                 if (s->disabled || su->disable)
                         continue;
                 if (s->target_residency > data->predicted_us)
                         continue;
                 if (s->exit_latency > latency_req)
                         continue;
                 data->last_state_idx = i;
         }
```

### menu_update

跟據上一次實際idle的時間 update上一次使用的factor
大至上是: factor = old_factor * ( 實際 / 預計下一次 idle timer)

選擇factor是根據**預計idle時間的長短**和**有沒有io waiting的task**決定
因為**不同預計時間對factor的反應程度**不同
初始預計時間越長，factor對實際值的影響就越大(base比較大嘛)
對長預計時間剛好的factor，用在短預計時間上可能就會矯正過度
所以某範圍的預計時間會被分到同個**bucket**，共用同個factor
有io wait task的話就會加權，分到比較長的預計時間bucket

目前是用指數分法 10^(n-1) ~ 10^n 已內的為一個bucket
有io waiter的話 n += 6


## I/O tracker cpuidle driver

Ref: 
http://events.linuxfoundation.org/sites/events/files/slides/IOlatencyPrediction.pdf

### Problem of menu driver

基本上Menu driver用已知的time來預測下一次的itle時間
並用之前實際因為其他interrupt而提早的idle時間來調整
........算是非常簡單的learning
而且是建立在**一段時間內的interrupt數量間隔差不多**的前提下
這樣的作法有幾個問題:

1. 把所有的interrupt都一起算，混在一起可能會將原本有period的interrupt忽略or算錯period
2. 需要時間收斂
3. 如果換CPU的話，收斂過程要重來

### I/O Tracking cpu driver

因此Lenaro PM team的人就提出 **預測I/O idle time**的想法，因為:
- I/O時間(e.g. HD, Flash)是固定or非常接近的
	例如固定block size W/R的I/O wait time是差不多的
- 一口氣read/write大量data時，就會是一連串類似的I/O time or 有重複的pattern
- CPU migration也沒有關係，因為是根據I/O time算的

![ssd-iotime.png](http://user-image.logdown.io/user/13673/blog/12890/post/300400/9ayfcScLQcGZnYaQCxOi_ssd-iotime.png)

### Implement

1. 對每個Task，紀錄被I/O block的時間
2. 將I/O block時間分成好幾個區間(bucket)，統計次數
3. 將bucket跟據現在距上次hit的時間排序
4. 估計下次I/O block time ```next_io_event```時，就取距離最近越常發生的(?
```Score = nrhits / (pos + 1)²```

![IOTrackingCPUIdle.png](http://user-image.logdown.io/user/13673/blog/12890/post/300400/sPFcKASwQWKDLZiXq1QB_IOTrackingCPUIdle.png)

5. 如果有多個task在wait，取最小的估計時間
6. 一樣從timer system取得```next_timer_event```
7. 預計**idle time = min(next_timer_event, next_io_event)**

跟據他的實驗結果，這樣猜測的準卻度可以比menu driver好上很多
而且這樣的設計可以和schedule綁在一起(在要進idle or I/O queue時做預測)  
以後也可以做更準確的預測(e.g. predict I/O time per hardware device)

