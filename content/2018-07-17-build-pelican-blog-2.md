Title: 使用Pelican架設技術筆記Blog (2)
Date: 2018-07-17 19:49
Modified: 2018-07-17 19:49
Category: Python
Tags: pelican
Slug: building-personal-blog-with-pelican-2
Authors: Solring Lin
Summary: 接續上一次架站的過程，接下來要開始搬文章和裝飾Blog啦...

接續上一次架站的過程，接下來要開始搬文章和裝飾Blog啦~


## 寫(搬)文章

參考[官方文件](http://docs.getpelican.com/en/3.7.1/content.html)，文章格式*reStructuredText*, *Markdown*, *html*，
將檔案直接放在`content/`目錄下就可以了。

文件Metadata各有相對應的格式。
例如我這邊使用的Markdown格式如下:
``` md
Title: My super title
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Short version for index and feeds

This is the content of my super blog post.
```

* `Slug`指該文章的local url (預設不是用檔名)。也可以用regular-expression來抽filename產生出來，但我還沒試過XD
* `Summary`指文章列表裡，除標題外顯示的預覽或是abstract。
* `Category`是唯一的文章分類。除了直接指定以外，還會用文章的*上一層folder名*來決定。
* `Tags`可以有多個，由','分開

格式上跟Logdown打包下來的markdown檔案很類似，簡單寫個script轉換一下就OK啦~


## 設定 & 客製化Themes

Pelican改Theme的方法滿簡單，只要修改`pelicanconf.py`裡的`THEME`變數到指定的PATH就可以了。
絕對路徑或相對路徑都可以。
``` python
THEME= '../Flex/'
#THEME= '/Users/solring/GitWorkspace/nest/'
```

(官方也有`pelican-themes`這個工具可以管理theme，但我沒有用 :P)

[Pelican Themes](http://pelicanthemes.com/)這個網站有前人貢獻的各種Theme可以挑選，
選一個喜歡的並從github上clone下來，照文件設定`pelicanconf.py`就可以啦~

個人挑選的時候主要考慮:

* 要可以客製化syntax highlight的顏色主題，畢竟是拿來貼code的嘛。
* 有tag和category列表，好整理&查找
* 文件要清楚，設定要簡潔。有的文件真的不清楚or感覺有誤，很困擾XD"

後來就選定了[Flex](https://github.com/alexandrevicenzi/Flex)這個主題啦~
版面簡潔，官方wiki也相當清楚。

###修改主題

[Pelican Theme](http://docs.getpelican.com/en/3.7.1/themes.html)主要的目錄結構如下:
```
├── static
│   ├── css
│   └── images
└── templates
    ├── archives.html         // to display archives
    ├── period_archives.html  // to display time-period archives
    ├── article.html          // processed for each article
    ├── author.html           // processed for each author
    ├── authors.html          // must list all the authors
    ├── categories.html       // must list all the categories
    ├── category.html         // processed for each category
    ├── index.html            // the index (list all the articles)
    ├── page.html             // processed for each page
    ├── tag.html              // processed for each tag
    └── tags.html             // must list all the tags. Can be a tag cloud.
```

使用的是Jinja2 template engine。
css的部分目錄結構沒有規定，大家都長的不太一樣XD

Flex使用的是*Less*來gen css，只要修改`static/static/stylesheet/`中的`style.less`和`variables.less`，
再用`lessc`compile成`style.min.css`就可以了~
```
$ lessc style.less style.min.css
```

這樣應該就可以cover顏色、字體大小等大部分的修改。

另外因為中文預設新細明體太難看，我參考了[這篇](https://free.com.tw/google-fonts-noto-sans-cjk-webfont/)將字型改為**Noto Sans TC**。
只要修改`variables.less`，import指定的css file和修改font family變數設定就可以了~ 

[參考commit](https://github.com/solring/Flex/commit/157f4541564b18df5d36dfb3411a6d57fd1f2390)
