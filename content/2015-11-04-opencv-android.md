Title: [OpenCV][Android] Build OpenCV Android SDK & enable OpenCL
Date: 2015-11-04 08:22
Modified: 2015-11-04 08:22
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [OpenCV][Android] Build OpenCV Android SDK & enable OpenCL


## 設NDK環境變數
``` sh
export ANDROID_NDK=/path/to/your/ndk
```

## 修改cmake參數
到opencv的source root
修改 *platforms/scripts/cmake_android_arm.sh*
加上```-DWITH_OPENCL=ON```
如果要加build opencv contrib也可以改在這裡

## 執行script
```
cd platform
./script/cmake_android_arm.sh
```
執行完後會在*platform*底下出現*build_android_arm*的資料夾
要修改資料夾路徑可以在*platforms/scripts/cmake_android_arm.sh*裡面修改

## Make
進去*build_android_arm*直接make
```
cd build_android_arm
make -j4
```
NOTE: 這邊我有遇到一個奇怪的error
```
/usr/include/eigen3/unsupported/Eigen/src/MatrixFunctions/MatrixExponential.h:284:61: error: there are no arguments to 'log2' that depend on a template parameter, so a declaration of 'log2' must be available [-fpermissive]
	m_squarings = (max)(0, (int)ceil(log2(m_l1norm / maxnorm)));   
......
/usr/include/eigen3/unsupported/Eigen/src/MatrixFunctions/MatrixExponential.h:284:61: error: 'log2' was not declared in this scope
```
大致上是找不到log2這個function的意思
仔細看*MatrixExponential.h* 發現最前面有log2的宣告
``` cpp
#ifdef _MSC_VER
template <typename Scalar> Scalar log2(Scalar v) { using std::log; return log(v)/log(Scalar(2)); }
#endif
```
看起來是為了補充 Microsoft c+ compiler缺的log2
可能預設ndk用的std lib也沒有log2
為了方便，我這邊就--很dirty--的直接把ifdef那兩行註解掉 : P
直接用這裡寫的log2

## 在java專案裡使用
編好之後，原本 opencv android sdk 裡附的 *opencv_java3.so* 就在 *build_android_arm/lib* 裡
替換掉專案裡的*opencv_java3.so*就可以了
(當然，在java層要記得load :P)

另外也需要把用到的的*opencv_contrib* headers放到sdk裡
或是一起放到jni資料夾裡, 自己在Android.mk裡面加include路徑
就可以在jni c++ source裡面用opencv_contrib裡面的東西了~
