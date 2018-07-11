Title: [Linux] Ubuntu 12.04.5 install g++-4.8 up
Date: 2015-10-01 09:30
Modified: 2015-10-01 09:30
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [Linux] Ubuntu 12.04.5 install g++-4.8 up


筆記一下~
Ubuntu 12.04.5要update g++的話要額外加ppa

而且12.04預設是沒有add-apt-repository的 (很神秘...
要先安裝python-software-properties

``` sh
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install g++-4.8
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 50
```

ref:
http://askubuntu.com/questions/271388/how-to-install-gcc-4-8
