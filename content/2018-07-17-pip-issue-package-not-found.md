Title: TLS過舊導致pip安裝套件失敗(找不到package)
Date: 2018-07-17 19:51
Modified: 2018-07-17 19:51
Category: Python
Tags: pelican
Slug: pip-issue-package-not-found
Authors: Solring Lin
Summary: 主要原因是python TLS過舊，很多package site都不支援TLS 1.0了...

拿老mac來用的時後馬上撞到主環境和virtualenv的pip什麼東西都找不到。囧。

後來找到這個[Issue](https://blog.csdn.net/qq_18863573/article/details/80118496)。
總之就是 Python.org sites 终止支持TLS1.0和1.1，TLS需要>=1.2才能抓到東西~

### 解決方法

因為pip首先死，不能用pip update。
所以我就先從官網下載最新python install一口氣打掉，
反正順便更新openssl那些的。

還可以點點script更新PATH之類的，方便XD
![install package](https://images.plurk.com/1Mw8E3hJvCsi8u3DiJeNT9.png)

然後再upgrade pip和virtualenv, done.
``` sh
$ pip install --upgrade pip
$ pip install --upgrade virtualenv
```
