Title: [Android][Hack] 工具＆步驟整理
Date: 2015-11-24 07:08
Modified: 2015-11-24 07:08
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [Android][Hack] 工具＆步驟整理


如果懶得從AOSP上抓下來自己編的話 這邊有一些prebuild tools：

## Various prebuild tools...
http://web.djodjo.org/?a=download:android:tools:x86_linux:alltools

## Unpack/pack system.img

simg2img, make_ext4fs
https://github.com/EpicAOSP/make_ext4

Steps:
http://muzso.hu/2012/08/10/how-to-pack-and-unpack-system.img-and-userdata.img-from-an-android-factory-image

如果遇到 error: do_inode_allocate_extents 類似的問題 可能是img size設錯
http://www.ithao123.cn/content-5224672.html

## Unpack/pack ramdisk.img

Unpack
```
mkdir ramdisk
cd ramdisk
gunzip -c ../ramdisk.img | cpio -i
```

Pack
```
# in ramdisk dir 
find . | cpio -o -H newc | gzip > ../ramdisk.img
```

## Make boot.img

ref: 
http://blog.djodjo.org/?p=536

```
mkbootimg --kernel [kernel file] --ramdisk [ramdisk file] --output [output img]
```
如果要指定block size等參數：
```
mkbootimg --kernel [kernel file] --ramdisk [ramdisk file]\
--base 0x10000000 –pagesize 2048 –kernel_offset 0x00008000 –ramdisk_offset 0x01000000 \
--output [output img] 
```

如何得到offsets:
http://blog.djodjo.org/?p=195
