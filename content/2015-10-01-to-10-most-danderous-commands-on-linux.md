Title: [轉] 好用的Linux commands
Date: 2015-10-01 23:44
Modified: 2015-10-01 23:44
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [轉] 好用的Linux commands


兵器大全(?
http://www.tecmint.com/10-most-dangerous-commands-you-should-never-execute-on-linux/

-----

同場加映好用的Linux指令
http://www.tecmint.com/10-most-dangerous-commands-you-should-never-execute-on-linux/

- sudo !!
自動將上一個指令用sudo執行
當run完一串指令才發現權限不足時很好用lol

- shuf
shuffle lines
```
# ls 
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
```
```
#  ls | shuf (shuffle Input)
Music 
Documents 
Templates 
Pictures 
Public 
Desktop 
Downloads 
Videos
```

- mtr
traceroute + ping
可能需要額外安裝

- ss
socket information

- tree
印出目前位置的子目錄結構
``` sh
|-- Desktop 
|-- Documents 
|   `-- 37.odt 
|-- Downloads 
|   |-- attachments.zip 
|   |-- ttf-indic-fonts_0.5.11_all.deb 
|   |-- ttf-indic-fonts_1.1_all.deb 
|   `-- wheezy-nv-install.sh 
|-- Music 
|-- Pictures 
|   |-- Screenshot from 2013-10-22 12:03:49.png 
|   `-- Screenshot from 2013-10-22 12:12:38.png 
|-- Public 
|-- Templates 
`-- Videos 
10 directories, 23 files
```

- pstree
印出目前在跑的process的child process結構
tree版ps

- ^someString^otherString
把上一個指令的某字串換成另一字串
當打了一長串指令發現裡面打錯一小段的時候超好用的!

- > file.txt
清空某個文字檔

- at
超快速排程
```
# echo "ls -l > /dev/pts/0" | at 14:012
```

- stat file.txt
顯示file資訊
Size, Blocks, Access Permission, Date-time of file last access, Modify, change, etc.

- 