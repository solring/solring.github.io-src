Title: 使用Pelican架設技術筆記Blog (1)
Date: 2018-07-12 21:33
Modified: 2018-07-12 21:33
Category: Python
Tags: pelican
Slug: building-personal-blog-with-pelican-1
Authors: Solring Lin
Summary: 一直以來都是把技術筆記放在Logdown上，但他後來就沒有再繼續維護了，還是移出來好。技術文件嘛，我主要需求是...

# 某天我想不開...

一直以來都是把技術筆記放在Logdown上，但他後來就沒有再繼續維護了，還是移出來好。
技術文件嘛，我主要需求是:

* 貼code要方便+漂亮 (有syntax highlight)
* 要可以用Markdown寫!!! (非常堅持) 

原本是有想要放[Medium](https://medium.com/)，又潮又漂亮。
然而他不能用markdown.....
老牌的Blogger也不太符合需求......好吧如此Geek的requirement看來還是要自己來滿足了。

*(題外話，我架完站的瞬間發現Tumblr可以用markdown + 有支援code block, highlight好像也可以設定...)*

Survey了一下，自架技術Blog最受歡迎的方案應該算是[Jekyll + Github pages](https://jekyllrb.com/)。資源多又穩定，而且聽說很快。但我不知怎麼腦袋壞掉...
應該說，覺得還是用比較熟的Python和有碰過的jinja2 template engine會比較好自己客製化，
就決定採用[Pelican](https://blog.getpelican.com/)這個Static Site Generator來試著架在**Github pages**上啦~~~


# Pelican Blog 架設流程

以下會以[官方文件](http://docs.getpelican.com/en/3.7.1/index.html)和我查到的[這個流程](https://fedoramagazine.org/make-github-pages-blog-with-pelican/)為主，
並說明一些要注意or調整的地方 (撞過的牆和一堆毛) : /。

## 環境設定

* Windows: Python 3.7/2.7.15 (官方安裝包裝下去就是了，兩個都可用)
* Mac OS: Python 2.7.15

使用`virtualenv`建立虛擬環境後安裝官網建議的package:

``` sh
$ pip install markdown pelican typogrify
```

官方Build tool之一的`fabric`不需要，原因之後會提到~


## 新建立Pelican Site

先照文件產生一個template site:

```
$ pelican-quickstart
```

接下來他會問一系列問題，設定以下幾個:

* Where do you want to create your new web site? (hit Enter)
* URL prefix: http://username.github.io
* Generate a Fabfile/Makefile: Yes (for most users)
* Auto-reload & simpleHTTP script: Yes (for most users)
* Upload mechanisms: choose No for all except Github Pages
* Is this your personal page (username.github.io)? Yes

之後就會出現這樣的目錄結構:

```
yourproject/
├── content
│   └── (pages)
├── output                  # 產生的網站在這
├── develop_server.sh
├── fabfile.py              # fabric build tool用的檔案
├── Makefile
├── pelicanconf.py          # Main settings file
└── publishconf.py          # Settings to use when ready to publish
```


## Github pages發布設定

我參考[Fedora社群的文章](https://fedoramagazine.org/make-github-pages-blog-with-pelican/)，
沒有使用官方github page發布工具`ghp-pages`。

根據Github pages的說明，你需要建一個名叫`xxxxx.github.io`的repo (xxxxx就是你的github帳號)，
將static site整個放到repo的`master` branch上，之後就可以使用*xxxxx.github.io*這個網址來拜訪你的網站

(這邊指的是**User page**的設定，另外有**Project page**可以使用不同的網址，但設定方法不同，請參考官網~)

### 準備網站source repo

不是網站本身的repo`xxxxx.github.io`，而是放你的pelican project。

先將剛剛創好的pelican目錄init成git repo，或是先在github創好repo再clone下來放進去都可以。
``` sh
$ git clone https://github.com/your_username/your_pelican_project.git
$ cd your_pelican_project
$ pelican-quickstart
```

所以到這邊github上應該會多兩個repo: 一個是`xxxxx.github.io`，另一個是他的source repo。
![repos](https://i.imgur.com/af0rC6n.png)

### 設定submodule

原本submodule主要是用來處理用到其他repo-的library之類的dependency問題，
除了可以用來track該library的更新情況以外，
也可以紀錄*目前這個commit使用的library是對應到哪個版本*，詳細解說可直接參考[官方](https://git-scm.com/book/zh-tw/v1/Git-%E5%B7%A5%E5%85%B7-%E5%AD%90%E6%A8%A1%E7%B5%84-Submodules)。

不過這邊被拿來記錄output出來的website是對應到哪個source版本。
也就是說submodule裡的東西是depends on main repo，有點反過來的感覺。

首先在**source repo**裡init submodule。
**NOTE:** 
你需要先刪除pelican創的`output/` folder
``` sh
$ git submodule add https://github.com/your_username/you_username.github.io.git output
```

之後應該可以在repo根目錄裡看到新增了`.gitmodules`這個檔案和`output/`這個folder
裡面會是另一個獨立repo，git remote應該可以看到他指向你的網站repo。

`.gitmodules`的內容:
```
[submodule "output"]
	path = output
	url = git@github.com:solring/solring.github.io.git
```

另外，為了避免每次pelican build的時候都重新創一個output folder蓋掉整個submodule。
需要修改`publishconf.py`，將這個變數設為false:
``` python
DELETE_OUTPUT_DIRECTORY = False
```

**NOTE:** 
另一個比較需要注意的一點是，之後在別的地方clone你的main repo時
不會馬上連submodule都一起clone下來，需要另外下指令:

``` sh
$ git submodule init
$ git submodule update
```

## Build Website

### 使用make build 

如果要使用Python2的話要先改一下`Makefile`的`PY`參數，將python3改成python:

``` bash
PY?=python
```

然後就可以直接build和跑起來了~

```
$ make html && make serve
```

### 使用fabric

在Windows上我有嘗試用fabric來build，但他使用的API是v1太舊，已經無法使用現在直接安裝的fabric。
(請參考[這篇](https://unix.stackexchange.com/questions/443643/import-error-fabric-api))
嘗試著安裝fabric v1 package也會遇到以下的問題
```
......\pelican-env2\lib\site-packages\fabric\main.py", line 13, in <module>
    from operator import isMappingType
ImportError: cannot import name 'isMappingType' from 'operator' (c:\users\solring\projects\pelican-env2\lib\operator.py)
```

要porting到fabric v2又實在太麻煩XD 於是我就直接用官方build指令，一樣也可以成功產生網站。
```
pelican content -s publishconf.py
```

## 發布到Github Pages上

如果Submodule已經設定完畢的話，你的`output/` folder應該已經是個獨立的repo。
commit完之後直接push上去即可發布網站。
``` sh
$ cd output
$ git commit -m "my site ver. n"
$ git push origin master
```

至於source本身要等到output commit完並上傳之後再commit+push。
這樣該commit就會記錄好，這個版本的source是對應到哪個版本的site(commit)。

**NOTE:**
發布到Github page上後有遇到過css style吃不到的問題。查看了一下source發現style sheet的路徑是http絕對路徑:
``` html
<link rel="stylesheet" type="text/css" href=http://solring.github.io/theme/css/main.css>
......
```

這應該是在`publishconf.sh`中設定到site url的關係。Local跑的時候因為不會用到site url所以不會有這個問題。
將設定改成這樣就沒問題了:
``` python
SITEURL = ''
RELATIVE_URLS = True
```

-----

以上~ 應該就可以有個Pelican官方的sample site放在你的Github Page上啦~
下一篇再繼續介紹怎麼寫文章和設定Theme。
