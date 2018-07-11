Title: [Linux] Execution檔shared library 名稱錯誤
Date: 2015-12-22 06:51
Modified: 2015-12-22 06:51
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [Linux] Execution檔shared library 名稱錯誤


用NDK使用prebuilt library編execution時意外產生奇觀:

``` sh
$ readelf -d test-audio
Dynamic section at offset 0x35b54 contains 30 entries:
  Tag        Type                         Name/Value
 0x00000003 (PLTGOT)                     0x36ed4
 ......
 0x00000001 (NEEDED)                     Shared library: [D:/DL/audioWorkspace//obj/local/armeabi-v7a/libkaldifeats.so]
 0x00000001 (NEEDED)                     Shared library: [libvieswip_wrapper.so]
 0x00000001 (NEEDED)                     Shared library: [libvieswip.so]
 0x00000001 (NEEDED)                     Shared library: [libstdc++.so]
 0x00000001 (NEEDED)                     Shared library: [libm.so]
 0x00000001 (NEEDED)                     Shared library: [libc.so]
 0x00000001 (NEEDED)                     Shared library: [libdl.so]
 0x0000001a (FINI_ARRAY)                 0x360f8
 ......
```

Shared library居然出現Window整個檔案路徑!?
而且其他自己包的shared lib都沒事，就只有第一個出意外
一開始還以為是Android.mk寫錯
結果後來發現是第一個lib沒有SONAME的關係
``` sh
$ readelf -d libkaldifeats.so | grep SONAME
$ (nothing...)
```
趕緊用`-Wl,-soname,libkaldifeats.so`補加SONAME就解決啦~


