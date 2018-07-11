Title: [OpenCV][OCR] Tesseract OCR on OpenCV 3.0
Date: 2015-11-03 09:30
Modified: 2015-11-03 09:30
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [OpenCV][OCR] Tesseract OCR on OpenCV 3.0


# Tesseract on Linux

OpenCV 3.0 有整合TesseractOCR的API
但這部份是不在mainline裡面的~ 而是放在*opencv_contrib* project的*text* module裡
而且text module預設是沒有TesseractOCR的~
以下是enable OpenCV 3.0 Tesseract的步驟 & 使用範例

## 安裝 Leptonica

官網: http://www.leptonica.com/
Source: http://www.leptonica.com/download.html

Tesseract需要Leptonica這個影像處理的library
目前需要1.71以上
如果是Ubuntu 14以下的話，apt-get上的版本太舊，需要自己compile & install

## 安裝 Tesseract Library

Git: https://github.com/tesseract-ocr/tesseract
安裝完Leptonica之後
直接照著說明compile並install就可以了

## OpenCV contrib modules

Git:
https://github.com/Itseez/opencv_contrib

下載 OpenCV 3.0 和 opencv contrib 的source之後(對 兩個都要下載)
照著他的說明使用cmake安裝就OK
如果環境裡漏掉某個module需要的lib，但是你用不到那個module的話，也可以disable那個module跳過編譯
例如要disable dnn module:
```
cmake -DOPENCV_EXTRA_MODULES_PATH=<opencv_contrib>/modules -DBUILD_opencv_dnn=OFF <opencv_source_directory>
```
Module list:
https://github.com/Itseez/opencv_contrib/tree/master/modules

這邊要注意
在下完cmake之後要確定有沒有出現```-- Tesseract: YES```的訊息
如果沒有出現表示cmake找不到Tesseract lib，可能是lib安裝位置不正確或是安裝失敗

## 使用Tesseract

這裡有相關範例
https://github.com/Itseez/opencv_contrib/blob/master/modules/text/samples/segmented_word_recognition.cpp
https://github.com/Itseez/opencv_contrib/blob/master/modules/text/samples/webcam_demo.cpp

注意，model的部份還是要自行放在指定的路徑
預設是```/usr/local/share/tessdata/```
或是指定env variable ```TESSDATA_PREFIX```到你存放model的tessdata folder的位置(一定要取名為```tessdata```)
(如果是```/home/username/tessdata```的話，就要設成```/home/username```)
或是在使用API時指定相對路徑
``` cpp
Ptr<OCRTesseract> ocr = OCRTesseract::create(
	"/home/test/tessdata",  //where you store the models
  "eng"
  "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ");
```

這裡有些現成的model可以使用
https://github.com/tesseract-ocr/tessdata

----------------------------

# Tesseract package for Android

Ref: http://gaut.am/making-an-ocr-android-app-using-tesseract/

有人將Tessearact本身和他需要的lib打包+作成Android JNI
Tess-two
https://github.com/rmtheis/tess-two

## 使用方法

這邊我是在Android Studio的Project使用
因為Android Studio NDK支援還是常常有問題=  ="
所以我是手動ndk-build library

1. Import 整個tess-two為一個module
File -> New -> Import module -> 選Tess-two的folder

2. Disable auto NDK build
這邊是用NDK-build的plugin，但不使用他的auto build功能 [Ref: 如何安裝NDK plugin](http://solring-blog.logdown.com/posts/305623-android-to-androidstudio-ndk-plugin-usage)
修改在tess-two module底下會自動產生的*build.gradle*:
``` c
// 在android括號下加這幾行
sourceSets{
        main{
            jni.srcDirs = [] //disable auto ndk-build
        }
    }
```

3. NDK build tess-two
方法一樣請參考[這邊](http://solring-blog.logdown.com/posts/305623-android-to-androidstudio-ndk-plugin-usage)

4. 把tess-two module加進其他module的dependency裡面
這樣就完成啦~

Tess-two的詳細使用方法可以參考以下ref:
- Stack Overflow: https://stackoverflow.com/questions/tagged/tess-two
- tesseract-ocr: https://groups.google.com/forum/#!forum/tesseract-ocr