Title: [DL] Convolutional Neural Network
Date: 2015-09-30 12:09
Modified: 2015-09-30 12:09
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [DL] Convolutional Neural Network


感想: 這東西真的是玄學啊~~~~~~

ref: 
http://www.iro.umontreal.ca/~pift6266/H10/notes/deepintro.html
http://deeplearning.net/tutorial/lenet.html

-----

# Background of Neural Network

就是嘗試模擬神經元的方式去辨識物體
每個神經元指會對特定的signal(feature)做出反應，傳給其他神經元，最後有個high level的結果

那要怎麼知道，為了辨識出東西(貓or早餐or樓下鄰居)，哪個神經元應該對哪個訊號有反應呢? 
A: **用Train的**
這就是ML裡面 feature learning/Representation learning 的部份

在NN中，某neuron h會對其他neuron or input x做反應
至於反應要多大呢? 就由 ```Weight(w)``` + ```Bias(b)``` + ```linear function```決定
也可以說，neuron的 Weight(w)+Bias(b)決定了他會對哪個feature有反應
**要Train的部份就是對每個input的Weight(w)+Bias(b)**



# Convolutional Neural Network (CNN)

傳統fully-connected的Neural network如果套在影像辨識上
就會發生很恐怖的事情:
假設有40000個Neuron 對上 200w像素的影像
每個pixel都會有一個對應的 w 和 b
就有40000 x 200w x 2 個參數要train
........Overhead實在是很大

所以CNN就發想出幾個idea:

## Locally connected (Sparse Connectivity)

模擬visual cortex的行為
每個視覺neuron一次只能對某塊sub-region``` receptive field```做反應
**作用就像是某個feature的filter**

所以CNN中不需要整張圖片的pixel都connect到某個neuron上
一個neuron的input可能只是圖片上的某個區域```field```
他所對應的**參數數量就減少到該field的pixel數量**

## Multilayer Neural Network

一樣也是模擬visual cortex，就是neuron有很多層```layer```囉
在CNN裡，同一層的neuron之間是沒有link的 
兩個layer可以形成一個[Restricted Boltzmann machine](https://en.wikipedia.org/wiki/Restricted_Boltzmann_machine)

## Shared Weight 

(這個名詞我覺得很難反應原理 :P)
指的是**input不同位置的neuron的weight可以是相同的**

接續receptive field的概念
因為neuron只能filter某個sub-region
如果希望在整張照片找feature，就必須用這個filter一次只掃一部份，掃過整張圖片
具體的方法就是將這個filter(neuron)重複apply到所有區域
因為**決定filter特性的是W和B**
所以**將filter重複apply的方法就是讓多個neuron使用同樣的W和B** (Shared weight就是從這邊來的)
這些apply相同filter的neuron output組成的就是```feature map```

![Filter bank就是weight和bias, Feature map是用某個filter的neuron的集合](http://user-image.logdown.io/user/13673/blog/12890/post/302641/V21DnAAeTKiOirZRFKhT_dl2.png)
Filter bank就是weight和bias, Feature map是用某個filter的neuron的集合

## Multiple Convolutions

在某layer的neuron的來源可以是多張上一layer的feature map
物理意義應該是表示**這個feature是由多個上一層的feature組成的**
所以越低layer的feature通常是線段之類的primitive element
而越高layer的則是越high level的feature (e.g. 眼睛)

![Sample convolutional layer](http://deeplearning.net/tutorial/_images/cnn_explained.png)

![low layer features](http://user-image.logdown.io/user/13673/blog/12890/post/302641/DsAYpgsTH63BTPVm8q6g_dl-filters1.png)
Low layer features

![high layer features](http://user-image.logdown.io/user/13673/blog/12890/post/302641/aaOb1565R8a5f4RSYxLj_dl-filters2.png)
High layer features

## Pooling, Subsampling

1. Pooling: 
幾個pixel取平均變成新的pixel
有smoothing的功能?

2. Subsampling: 
Pooling時跳著做
本來可能是每shift一個pixel做一次，變成shift兩格才做
可以降低維度(資料量)

# Backpropogation (backward propagation)
先定義一個loss function (W, B as variables)
然後用opt. function(e.g. gradient decent)找loss function的最小值

## Gradiend decent
https://zh.wikipedia.org/wiki/%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D%E6%B3%95
從某一點開始逼近最小值時，因為梯度相當於斜率，所以沿著梯度下降是最快的
```mathjax
\mathbf{x}_{n+1}=\mathbf{x}_n-\gamma_n \nabla F(\mathbf{x}_n),\ n \ge 0.
```
一直逼近到`$ \mathbf{x} $`為最小為止

如果到套用到CNN某一層neuron的話就像是
```mathjax
(\mathbf{W},\mathbf{B})_{n+1}=(\mathbf{W},\mathbf{B})_n-\gamma_n \nabla F(\mathbf{W}_n, \mathbf{B}_n),\ n \ge 0.
```
//Notation應該是不太對XD 之後再改
其中function `$ F(\mathbf{W}_n, \mathbf{B}_n) $`是loss function
loss function要可微分，才能算梯度
連帶也表示不同層的activation function也要可以微分

令某一層的activation function `$ a(X) $`
帶入一個train input X得到的答案是y
改把W, B看成變數的話就是 `$ A(W, B)=y $`
假設正確答案是y'
Loss function `$ F(W, B)=y'-y=y'-A(W, B) $`
因此更新W, B的方法就是算出`$ y'-A(W, B) $`梯度之後，乘一個比率減回去



