Title: [Android][轉] AndroidStudio NDK plugin使用方法
Date: 2015-10-21 01:16
Modified: 2015-10-21 01:16
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [Android][轉] AndroidStudio NDK plugin使用方法


https://8085studio.wordpress.com/2015/04/25/android-studio-ndk-jni/

- Setting --> Tools --> External tools
	可新增編輯 NDK build 和 Javah，步驟請參考連結
  
1. 新增 NDK Build
``` 
Name: NDK Build
Group: NDK
Description: NDK Build
Options: 全打勾
Show in: 全打勾
Tools Settings:
Program: NDK目錄ndk-build.cmd
Parameters: NDK_PROJECT_PATH=$ModuleFileDir$/build/intermediates/ndk NDK_LIBS_OUT=$ModuleFileDir$/src/main/jniLibs NDK_APPLICATION_MK=$ModuleFileDir$/src/main/jni/Application.mk APP_BUILD_SCRIPT=$ModuleFileDir$/src/main/jni/Android.mk V=1
Working directory: $SourcepathEntry$
```
2. Javah
```
Name: Javah
Group: NDK
Description: Javah
Options: 全打勾
Show in: 全打勾
Tools Settings:
Program: Java JDK目錄binjavah.exe
Parameters: -v -jni -d $ModuleFileDir$srcmainjni $FileClass$
Working directory: $SourcepathEntry$
```

- 使用javah: 在有native method的class上按右健跑javah

- 使用NDK build要在**module的jni folder**上按右鍵跑Ndk build，不是在project folder上

- disable auto gradle ndk build
在```build.gradle```裡的android下加上:
```
sourceSets{
        main{
            jni.srcDirs = [] //disable auto ndk-build
        }
    }
```