Title: [Linux] Linux page cache
Date: 2015-09-15 08:50
Modified: 2015-09-15 08:50
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [Linux] Linux page cache


Reference:
http://www.westnet.com/~gsmith/content/linux-pdflush.htm

# 怎麼看Page cache使用情況?

從procsys查看: ```/proc/meminfo```
```
MemTotal:        3041412 kB
MemFree:          202200 kB
Buffers:          137432 kB
Cached:          1466296 kB
...
Dirty:                 0 kB
...
```
其中Cached就是現在Page cached的大小
Dirty就是被write的部份，如果Dirty pages被寫回去的話就會歸零

# Page cache相關參數

1. ```/proc/sys/vm/dirty_writeback_centisecs```
(0.01 second) 每隔多久pdflush會起來把expire的dirty page寫回去
預設500 (5 seconds)

2. ```/proc/sys/vm/dirty_expire_centiseconds```
(0.01 second) Dirty page expire的期限
預設3000 (30 seconds)

3. ```/proc/sys/vm/dirty_background_ratio```
當Dirty page的大小超過"目前可用的RAM"幾percent會強制把dirty page寫回去
其中"目前可用的RAM" = MemFree + Cached - Mapped

4. ```dirty_writeback_centisecs```
據說太複雜了 被disable?

