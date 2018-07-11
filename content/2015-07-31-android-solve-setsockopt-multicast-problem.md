Title: [Android] 解決setsockopt在multicast的問題
Date: 2015-07-31 11:14
Modified: 2015-07-31 11:14
Category: Archive
Tags: [android]
Authors: Solring Lin
Summary: (archive) [Android] 解決setsockopt在multicast的問題


參考以下這一篇
http://developerweb.net/viewtopic.php?id=5784

原因是Android開Wi-Fi AP Mode之後
系統把routing table寫死成只有內網(192.168.xx)才有route
因為目前預設的multicast IP是寫死成224.0.1.187

setsocketopt找不到route就失敗了

Work around:
```
route add -net 224.0.0.0 netmask 224.0.0.0 dev ap0
```
查看有沒有加成功
```
cat /proc/net/route
```

-----

後來有在AOSP上發現相關issue，但是目前被放置中...
http://code.google.com/p/android/issues/detail?id=40003
