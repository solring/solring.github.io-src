Title: [Note] 機器學習速遊
Date: 2015-12-12 01:08
Modified: 2015-12-12 01:08
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [Note] 機器學習速遊


SlideShare: http://www.slideshare.net/tw_dsconf/ss-56071386

# Learning from Data

ML: improving some **performance measure** with **experience computed** from data

## Scenarios
- Rapid decision
- Unknwon situation
- Hard to define the solution/cannot find solution 
- Massive scale
e.g. ML is a route to realize AI

## Thrive of ML
收集資料越來越容易
資料越來越多
計算越來越便宜


## Nodation
input: *x*
output: *y*
unknown pattern: *f: x -> y* //未知的完美的規則或答案 
training example: *D*
hypothesis: *g: x -> y* //可能的規則

http://www.slideshare.net/tw_dsconf/ss-56071386/13?src=clipshare

## Essence of ML
- 可能有pattern
- 很難手動找規則or其他解法
- 有data

## Q & A
- hypothesis set & training data 會受到domain knowledge影響
- hypothesis set理想上不會更新，大小非常大; 實務上會由人手動改變
- f 這邊假設是唯一不變的 (we dnot know~ 
- 什麼時候要用semi-supervised learning? 要有多少label才能做supervised?
supervised比較簡單，可以拿來當baseline
在來試semi-supervised
- 什麼時候用regression or multi classification
可以先用regression試試，在從問題看有沒有可能用multi classification做來improve performance

## Binary classification
是非題(?

## Multi classification
選擇題

## Regression
答案是continuous的(實數)
e.g. 今天的濕度 -> 明天氣溫會幾度到底度

## Reinforcement learning
不能直接標記什麼結果是對的
用間接的index去標記結果?
e.g. 廣告推薦：user點擊推薦的廣告 -> 獎勵

## Steps
1. choose error measure
2. choose hypothesis set 
	e.g. linear classifier(perceptron
3. optimize error

## Gerneralization
通常簡單的hypothesis也可以gerneralization


# Fundamental Machine Learning Models

## Linear Regression
``` mathjax
h(x) = w^Tx
```
E(w): residuals (e.g. squared error
E(w)要是一個quadratic convex
基本算法：找min(E(w)) => 找E(w)微分=0的地方 (closed-form solution
=> w = x'y

簡單，有理論基礎，快速
可以拿來當baseline

## Logistic Regression
未來發生ＸＸＸ的機率有多少？ 答案是在[0,1]之間
Soft binary classification
用logistic function把分數轉換成機率,轉換到[0,1]的區間
```mathjax
h(w) = \theta(w^Tx)
```
E(w) : Maximum likelyhood (cross-entropy)
find min(E(w) => gradient decent

http://www.slideshare.net/tw_dsconf/ss-56071386/65?src=clipshare

## Nonlinear Transformation
有的時候用一般線性binary classification切不開
solution 想辦法把data 的space轉到另一個有linear model的space (Feature transform)
h(x) = 某種非線性函數
h'(x) = sign(w^Tz)

## Decision Tree


# Hazard of Overfitting
VC dimension: 模型複雜度
複雜度上昇 -> in-sample error 下降 -> 複雜度代價(造成的error)上昇
Eout <= Ein + Overhead from complexity

**Reasons of overfitting**

- Noise太多
- 總共的training data太少

**Tips**

- 先從簡單安全的model(linear model)開始
- data cleaning/pruning: 清除noise
- data hinting: 增加資料量
- regularization
- validation

**將複雜度的方法**
- 降維
- refine Feature transform

## Data Manipulation and Regularization

### Data cleaning/pruning
可能有用
現有的ML algo有的已經可以避掉noise

### Data hinting
把現有的training data（在沒有影響的情況下）修改一下擴充
=> 自己生資料

### Regularization
Minimizing Augmented Error
``` mathjax
E_{aug}(w) = E_{in}(w) + \frac{\lambda}{n} w^Tw, \\
w^Tw: regularizer
\lambda: regularization parameter
```
怎麼選lambda可以由validation決定

### Validation
把部分data set留下來在第一次training後做驗證(測驗)，再拿驗證結果選擇最後model

1. 拿training data 用多algo learn出多個model
2. 用validation model選出最好的algo
3. 再拿所有的data用選出來的algo learn出最終的model

- 隨機選取
- training data & validation data要分開

V-fold Cross-Validation
(V-1)/V data 拿來train, 1/V 拿來validation

## Principles

1. Occam's Razor
對data的解釋(model)越簡單越好

2. Sampling Bias
如果data有bias, 學出來的東西也會有bias

3. Visual Data Snooping
“偷看資料”
可能會自己把model調的太複雜


# Modern Machine Learning Models

## SVM
找跟sample data們都最遠的分隔線(largest-margin)
同時minimize separation error
已經有regularization(待證明

non-linear + 資料量大的話比較不適合

Gaussian SVM: 用Gaussian kernel 做 Feature Transformation

## Random Forest

1. 抽樣
2. 做出n顆decision tree
3. 投票

內建有feature selection

### Feature selection

去掉多餘或無關的feature
方法一： Ramdom test
故意塞在某個feature維度noise，效果差越多越重要


## Adaptive Boosting

有點類似decision tree?
先用某個algo(regression, classification...)train某個model (更精確地說是某種feature transformation)
算出正確label和model算出的label的"距離"
再拿"距離"和input(x), 正確label(y)重複放進algo算出新model
最後再把這些model(transformation)組合起來
通常是用linear regression


# References

KDDCup
http://kddcup2015.com/information.html

Semi-supervised learning
http://pages.cs.wisc.edu/~jerryzhu/pub/sslicml07.pdf

Scikit-learn
https://github.com/scikit-learn/scikit-learn
http://scikit-learn.org/stable/index.html

