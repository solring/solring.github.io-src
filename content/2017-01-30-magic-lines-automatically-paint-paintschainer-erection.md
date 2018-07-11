Title: 神奇的線稿自動上色PaintsChainer - 架設
Date: 2017-01-30 02:13
Modified: 2017-01-30 02:13
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) 神奇的線稿自動上色PaintsChainer - 架設


過年發現這個神奇的Project!
https://github.com/taizan/PaintsChainer
因為太神了+官方server爆流量(?) 就想要自己架來玩玩
紀錄一下艱辛的過程...

# 環境
Windows 10
Nvidia GeForce GTX960m

# Set up Windows
因為有用到CUDA，如果使用的電腦沒有C開發環境，就需要整個重新架設

## 下載並安裝Visual C++
不想裝IDE的話，使用[Windows Visual C++ 2015 Build tools](http://landinghub.visualstudio.com/visual-cpp-build-tools)就夠了

### NOTE:
後來我有遇到Runtime時找不到```cl.exe```之類的問題
好像把VC的bin 加進PATH之後就解決了
C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin

## 安裝Windows Kits
**!!!!!!!很重要!!!!!!!!!**
需要安裝Windows Kits 並將他的include和lib加進環境變數
[Windows 10載點](https://developer.microsoft.com/zh-tw/windows/downloads/windows-10-sdk)
否則會在Runtime時遇到以下error:
```
......
Files (x86)/Microsoft Visual Studio 14.0/VC/bin/../../VC/INCLUDE\\crtdefs.h"\r\nC:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/bin/../../VC/INCLUDE\crtdefs.h(10): fatal error C1083: Cannot open include file: 'corecrt.h': No such file or directory\r\n
......
```
安裝完畢後，需要另外新增INCLUDE & LIB兩個環境變數
(這是爛招XD 但是目前這樣最快~~~)
![PATH.png](http://user-image.logdown.io/user/13673/blog/12890/post/1365466/koQL7A91Qji5LCKs3UOo_PATH.png)
CUDA討論區有[相關post](https://devtalk.nvidia.com/default/topic/969047/cuda-8-vs2015-corecrt-h-error/?offset=7)

# Setup CUDA & cuDNN
我是使用**CUDA 8.0.44** & **CUDNN 8.0** for win10
其中下載完cudnn之後
要把裡面的**include,bin,lib**裡的檔案都copy到CUDA底下相對應的資料夾

# Setup Python Chainer & Other packages

## 小技巧: 在Windows下同時使用Python 2 & 3
由於原project使用Python 3，因此以下的package都要裝在Python 3裡面
在Window環境中都安裝完python 2和3的話
可以直接在cmd裡面使用```py``` 這個cmd(在安裝python3時會安裝)指定要使用python 2還是3 
``` sh
$ py -2 xxx.py
```
同理，要用pip安裝套件到python 3的話:
``` sh
$ py -3 -m pip install xxxx
```
這樣就可以指定要安裝套件到哪啦~
(當然還是推薦用virtualenv啦)

## Chainer
**!!!!!!!很重要!!!!!!!!!**
如果在正確安裝完CUDA和CUDNN之前就先安裝chainer的話，就會吃到錯誤的```CUDA_PATH```
Runtime的時候會噴error並提醒你重裝
總之一定要照順序安裝啦
``` sh
$ py -3 -m pip install chainer --no-cache-dir -vvvv
```

## PIL
(Currently not used in PaintsChain)
其實他的名字叫pillow...
```
$ py -3 -m pip install pillow
```
http://stackoverflow.com/questions/28155028/installing-pil-for-python-3-4

## Prebuilt cv2 for Python3
現在可以直接用pip安裝的只有Python 2的
但是有好心人有prebuilt好Python 3版本，並用wheel package的方式release出來給人下載~
Instruction
http://lsw.gapp.nthu.edu.tw/note/installation-of-opencv3-1-python3-5-with-windows
載點
http://www.lfd.uci.edu/~gohlke/pythonlibs/
```
// download the wheel file first
$ py -3 -m pip install opencv_python-3.2.0-cp36-cp36m-win_amd64.whl
```

## Numpy and other packages
直接用pip安裝就OK啦~

![demo](https://68.media.tumblr.com/93ac7fbc3292a788ea175dee27b67d9c/tumblr_oklgg16N5c1vxv7jho2_r1_1280.png)
差不多這樣就可以跑啦
Github上也有更新越來越多安裝資訊了
目前也有一堆人跳下去了，有問題應該都可以在上面發問＆找答案

code study還是留到下一篇.....