Title: [DL] Caffe install on Ubuntu 12.04
Date: 2015-10-13 03:38
Modified: 2015-10-13 03:38
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [DL] Caffe install on Ubuntu 12.04


Ref:
http://www.bubuko.com/infodetail-688569.html

# 安裝dependent package:
``` sh
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libboost-all-dev libhdf5-serial-dev

# glog
wget https://google-glog.googlecode.com/files/glog-0.3.3.tar.gz
tar zxvf glog-0.3.3.tar.gz
cd glog-0.3.3
./configure
make && make install
# gflags
wget https://github.com/schuhschuh/gflags/archive/master.zip
unzip master.zip
cd gflags-master
mkdir build && cd build
export CXXFLAGS="-fPIC" && cmake .. && make VERBOSE=1
make && make install
# lmdb
wget https://github.com/wizawu/lmdb/archive/lmdb.master.zip
unziplmdb.master.zip
cdlmdb.master/libraries/liblmdb
make && make install
```

# 安裝OpenBLAS

參考 https://github.com/xianyi/OpenBLAS/wiki/Installation-Guide

這邊我選用gfortran當Fortran compiler
```
make FC=gfortran
```

但安裝gfortran之後，一直遇到找不到libgfortran的問題 (-lgfortran失敗)
**解決方法**: 用 update-alternatives 在/usr/lib/下加libgfortran.so
```
update-alternatives --install /usr/lib/libgfortran.so libgfortran /[path to your libgfortran]/[libgfortran] 1
```

# 安裝cuda GPU driver
不是我裝的XD 先跳過

# 安裝OpenCV

這邊我選擇安裝2.4 
因為Ubuntu 12.04太舊了...3.0會出現一堆相容性問題

直接到這個github下載相對應版本的安裝script，放到要安裝的資料夾run就可以了
https://github.com/jayrambhia/Install-OpenCV/tree/master/Ubuntu/2.4

另外也有ArchLinux和RedHat的版本

# 編譯caffe

**NOTE: 以下的問題是發生在同時安裝了 OpenCV 2.4和3.0的機器上**
可能是link時版本相衝的問題
在另一台只有安裝OpenCV 2.4的 server上就沒有問題

下載下來後，首先要修改Makefile.config
``` sh
## Refer to http://caffe.berkeleyvision.org/installation.html
# Contributions simplifying and improving our build system are welcome!

# cuDNN acceleration switch (uncomment to build with cuDNN).
USE_CUDNN := 1

# CPU-only switch (uncomment to build without GPU support).
# CPU_ONLY := 1

# To customize your choice of compiler, uncomment and set the following.
# N.B. the default for Linux is g++ and the default for OSX is clang++
# CUSTOM_CXX := g++

# CUDA directory contains bin/ and lib/ directories that we need.
CUDA_DIR := /usr/local/cuda
# On Ubuntu 14.04, if cuda tools are installed via
# "sudo apt-get install nvidia-cuda-toolkit" then use this instead:
# CUDA_DIR := /usr

# CUDA architecture setting: going with all of them.
# For CUDA < 6.0, comment the *_50 lines for compatibility.
CUDA_ARCH := -gencode arch=compute_20,code=sm_20 \
		-gencode arch=compute_20,code=sm_21 \
		-gencode arch=compute_30,code=sm_30 \
		-gencode arch=compute_35,code=sm_35 \
		-gencode arch=compute_50,code=sm_50 \
		-gencode arch=compute_50,code=compute_50

# BLAS choice:
# atlas for ATLAS (default)
# mkl for MKL
# open for OpenBlas
BLAS := open
# Custom (MKL/ATLAS/OpenBLAS) include and lib directories.
# Leave commented to accept the defaults for your choice of BLAS
# (which should work)!
# BLAS_INCLUDE := /path/to/your/blas
# BLAS_LIB := /path/to/your/blas

# Homebrew puts openblas in a directory that is not on the standard search path
# BLAS_INCLUDE := $(shell brew --prefix openblas)/include
# BLAS_LIB := $(shell brew --prefix openblas)/lib

# This is required only if you will compile the matlab interface.
# MATLAB directory should contain the mex binary in /bin.
# MATLAB_DIR := /usr/local
# MATLAB_DIR := /Applications/MATLAB_R2012b.app

# NOTE: this is required only if you will compile the python interface.
# We need to be able to find Python.h and numpy/arrayobject.h.
PYTHON_INCLUDE := /usr/include/python2.7 \
		/usr/lib/python2.7/dist-packages/numpy/core/include
# Anaconda Python distribution is quite popular. Include path:
# Verify anaconda location, sometimes it's in root.
# ANACONDA_HOME := $(HOME)/anaconda
# PYTHON_INCLUDE := $(ANACONDA_HOME)/include \
		# $(ANACONDA_HOME)/include/python2.7 \
		# $(ANACONDA_HOME)/lib/python2.7/site-packages/numpy/core/include \

# We need to be able to find libpythonX.X.so or .dylib.
PYTHON_LIB := /usr/lib
# PYTHON_LIB := $(ANACONDA_HOME)/lib

# Homebrew installs numpy in a non standard path (keg only)
# PYTHON_INCLUDE += $(dir $(shell python -c 'import numpy.core; print(numpy.core.__file__)'))/include
# PYTHON_LIB += $(shell brew --prefix numpy)/lib

# Uncomment to support layers written in Python (will link against Python libs)
# WITH_PYTHON_LAYER := 1

# Whatever else you find you need goes here.
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial /usr/local/cuda/cudnn-6.5-linux-x64-v2
LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu/hdf5/serial /usr/local/cuda/cudnn-6.5-linux-x64-v2

# If Homebrew is installed at a non standard location (for example your home directory) and you use it for general dependencies
# INCLUDE_DIRS += $(shell brew --prefix)/include
# LIBRARY_DIRS += $(shell brew --prefix)/lib

# Uncomment to use `pkg-config` to specify OpenCV library paths.
# (Usually not necessary -- OpenCV libraries are normally installed in one of the above $LIBRARY_DIRS.)
# USE_PKG_CONFIG := 1

BUILD_DIR := build
DISTRIBUTE_DIR := distribute

# Uncomment for debugging. Does not work on OSX due to https://github.com/BVLC/caffe/issues/171
# DEBUG := 1

# The ID of the GPU that 'make runtest' will use to run unit tests.
TEST_GPUID := 0

# enable pretty build (comment to see full commands)
Q ?= @
```

其中 ```CPU_ONLY``` & ```USE_CUDNN``` 可以用來控制要不要只使用CPU & 要不要用CUDNN加速

- 有個issue會找不到hdf5.h和他的lib
	把 /usr/include/hdf5/serial 加入 INCLUDE_DIRS
	/usr/lib/x86_64-linux-gnu/hdf5/serial 加入 LIBRARY_DIRS 就可以修好
	如果libhdf5和他的header不是安裝在上述位置的話，可能要找一下並改成你的安裝位置

- 如果要使用cuDnn的話也要加進他的header file和shared lib路徑
	這裡是```/usr/local/cuda/cudnn-6.5-linux-x64-v2```

- 另外在compile過程中可能會出現找不到cv::imread和cv::imdecode functions
	解決方法參考 https://github.com/BVLC/caffe/issues/2288
	主要是opencv imgdecode lib沒有被包進來
	修改Makefile，在USE_OPENCL那一段的LIBRARIES加上lib:
``` 
ifeq ($(USE_OPENCV), 1)                                                                    
  LIBRARIES += opencv_core opencv_highgui opencv_imgproc opencv_imgcodecs
endif  
```

	另外make test的時候也會遇到同樣問題，但這次是因為```-lcaffe```使用到opencv imgcodecs等的lib
	所以應該要放在前面
	將```TEST_XX_BINS```的 ```-l$(PROJECT)``` 跟 ```$(LDFLAGS)``` 對調即可
```
-o $@ $(LINKFLAGS) -l$(PROJECT) $(LDFLAGS) -Wl,-rpath,$(ORIGIN)/../lib
```

有關ld link shared library的順序:
http://stackoverflow.com/questions/45135/why-does-the-order-in-which-libraries-are-linked-sometimes-cause-errors-in-gcc

