Title: GNU LD Script - OVERLAY 和 AT的神奇用法
Date: 2016-03-10 12:23
Modified: 2016-03-10 12:23
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) GNU LD Script - OVERLAY 和 AT的神奇用法


GNU ld linker有設計一套專用的script，可以讓programmer自訂你link出來的東西長什麼樣(?
從Memory的layout、code RO/RW data的位置、Load前和實際上run的address等等
這樣的工具在Embedded System很常用到

詳細的用法可以參照[手冊](http://www.math.utah.edu/docs/info/ld_3.html)和這位大大整理的[導讀](http://wen00072-blog.logdown.com/posts/246070-study-on-the-linker-script-2-setcion-command)

## OVERLAY
這個功能應該只有Embedded比較會用到XD
主要就是讓兩個不同的code/data可以放在同一地方跑

不同於手冊的範例也可以這樣寫
``` ld
MEMORY {
  ROM : ORIGIN = 0x00000000, LENGTH = 8K
  RAM : ORIGIN = 0x00002000, LENGTH = 120K
}

SECTION {
　...
	OVERLAY : {
  	.text1 { *(.text1) }
  } > RAM AT > ROM
  ...
}
```
這樣這個Section的LMA就會和其他Section照順序被排進RAM，而LMA則是照順序排進ROM
**但要注意的是，這樣做的話在OVERLAY後面的section的LMA也會被自動排進ROM**
在後面的section手動用`> RAM`也無效，要再研究一下有沒有其他辦法設定
