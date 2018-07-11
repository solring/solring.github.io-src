Title: 文字辨識相關
Date: 2015-10-13 13:34
Modified: 2015-10-13 13:34
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) 文字辨識相關


## Android 環境設定

- 在AndroidStudio上用OpenCV SDK
http://stackoverflow.com/questions/27406303/opencv-in-android-studio

1. Download latest OpenCV sdk for Android from OpenCV.org and decompress the zip file.
2. Import OpenCV to Android Studio, From File -> New -> Import Module, choose sdk/java folder in the unzipped opencv archive.
3. Update build.gradle under imported OpenCV module to update 4 fields to match your project build.gradle a) compileSdkVersion b) buildToolsVersion c) minSdkVersion and 4) targetSdkVersion.
4. Add module dependency by Application -> Module Settings, and select the Dependencies tab. Click + icon at bottom, choose Module Dependency and select the imported OpenCV module.
5. For Android Studio v1.2.2, to access to Module Settings : in the project view, right-click the dependent module -> Open Module Settings
6. Copy libs folder under sdk/native to Android Studio under app/src/main. In Android Studio, rename the copied libs directory to jniLibs and we are done.
Step (6) is since Android studio expects native libs in app/src/main/jniLibs instead of older libs folder. For those new to Android OpenCV, don't miss below steps
```
include static{ System.loadLibrary("opencv_java"); } 
```
(Note: for OpenCV version 3 at this step you should instead load the library opencv_java3.)
For step(5), if you ignore any platform libs like x86, make sure your device/emulator is not on that platform.

- Android Camera
http://blog.csdn.net/yanzi1225627/article/details/8605061
http://ibuzzlog.blogspot.tw/2012/08/how-to-do-real-time-image-processing-in.html
https://developer.qualcomm.com/software/snapdragon-sdk-android/facial-processing/user-guide

"最后提醒的是，如果程序中加入了previewCallback，在surfaceDestroy释放camera的时候，最好执行myCamera.setOneShotPreviewCallback(null); 或者myCamera.setPreviewCallback(null);中止这种回调，然后再释放camera更安全。"

- Android camera & screen座標
http://blog.csdn.net/yanzi1225627/article/details/38098729


## OpenCV Text detection

- MSER
http://www.mathworks.com/help/vision/examples/automatically-detect-and-recognize-text-in-natural-images.html#zmw57dd0e38
https://en.wikipedia.org/wiki/Maximally_stable_extremal_regions
http://www.micc.unifi.it/delbimbo/wp-content/uploads/2011/03/slide_corso/A34%20MSER.pdf

不錯的中文解釋
http://blog.sciencenet.cn/blog-1327159-849648.html

- Canny Edge Detector
http://docs.opencv.org/doc/tutorials/imgproc/imgtrans/canny_detector/canny_detector.html

- 把camera preview轉Mat, 灰階化
http://www.jayrambhia.com/blog/opencv-android-image/

Android onPreviewFrame傳回來的data是YUV4:2:0的形式

- OpenCV image rotation
http://opencv-code.com/quick-tips/how-to-rotate-image-in-opencv/

- YUV to RGB
http://stackoverflow.com/questions/25666120/converting-from-yuv-colour-space-to-rgb-using-opencv
一開始YUV Matrix的size不能亂設，不然轉換的時候會跑掉:P

## OCR lib

- Tesseract
https://github.com/tesseract-ocr/tesseract

