---
layout:        post
title:         "xpath | 语法简明教程"
subtitle:      "positon()范围值选择等等等等"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 1. XPath简介
&emsp;&emsp;XPath (XML Path Language) 是由国际标准化组织 W3C 指定的，用来在 XML 和 HTML 文档中选择节点的语言。目前主流浏览器 (chrome、firefox，edge，safari) 都支持 XPath 语法，xpath 有 1 和 2 两个版本，目前浏览器支持的是 xpath 1 的语法。          

<br>
<br>

### 2. XPath语法
#### 2.1 根结点
1、xpath 语法中，整个HTML文档根节点用 `/` 表示，如果我们想选择的是根节点下面的 html 节点，则可以在搜索框输入：     
```
/html
```   

2、如下面的表达式表示选择 html 下面的 body 下面的 div 元素，`/` 表示直接子节点关系：      
```
/html/body/div
```

<br>

#### 2.2 绝对路径选择
&emsp;&emsp;从根节点开始的，到某个节点，每层都依次写下来，每层之间用 `/` 分隔的表达式，就是某元素的绝对路径。上面的 xpath 表达式 `/html/body/div`，就是一个绝对路径的 xpath 表达式。            

<br>

#### 2.3 相对路径选择
1、有的时候，我们需要选择网页中某个元素， 不管它在什么位置 。比如，选择示例页面的所有标签名为 div 的元素，xpath 只需要在前面加 `//` , 表示从当前节点往下寻找所有的后代元素,不管它在什么位置。所以 xpath 表达式，应该这样写：   
```
//div
```

2、`//` 符号也可以继续加在后面，比如，要选择所有的 div 元素里面的所有的p元素 ，不管 div 在什么位置，也不管 p 元素在 div 下面的什么位置，则可以这样写：           
```
//div//p
```

3、如果，要选择所有的 div 元素里面的直接子节点 p，xpath 就应该这样写：          
```
//div/p
```

<br>

#### 2.4 通配符
&emsp;&emsp;如果要选择所有 div 节点的所有直接子节点，可以使用表达式（`*` 是一个通配符，对应任意节点名的元素）：        
```
//div/*
```

<br>

#### 2.5 根据属性选择
&emsp;&emsp;xpath 可以根据属性来选择元素，根据属性来选择元素的格式是：     
```
[@属性名='属性值']
```

注意：     
1. 属性名注意前面有个 `@`；
2. 属性值一定要用引号，可以是单引号，也可以是双引号；

<br>

###### 2.5.1 根据id属性选择
&emsp;&emsp;选择 id 为 west 的元素，可以这样：           
```
//*[@id='west']
```

<br>

###### 2.5.2 根据class属性选择
1、选择所有select元素中class为single_choice的元素，可以这样：       
```
//select[@class='single_choice']
```

2、如果一个元素 class 有多个，比如 `<p id="beijing" class='capital huge-city'>北京</p>`，如果要选它，对应的 xpath 就应该是：         
```
//p[@class="capital huge-city"]
```
不能只写一个属性，像这样 `//p[@class="capital"]` 则不行。          

<br>

###### 2.5.3 根据其他属性
&emsp;&emsp;同样的道理，我们也可以利用其它的属性选择。比如选择具有multiple属性的所有页面元素，可以这样：        
```
//*[@multiple]
```

<br>

###### 2.5.4 属性值包含字符串
1、要选择 style 属性值包含 color 字符串的页面元素，可以这样：          
```
//*[contains(@style,'color')]
```

2、要选择 style 属性值以 color 字符串开头的页面元素，可以这样：         
```
//*[starts-with(@style,'color')]
```

3、要选择 style 属性值以某个字符串结尾的页面元素 ，大家可以推测是 `//*[ends-with(@style,'color')]`， 但是，很遗憾，这是 xpath 2.0 的语法 ，目前浏览器都不支持。              

<br>

#### 2.6 按次序选择
xpath可以根据次序选择元素。

###### 2.6.1 选取第几个子元素
1、直接在方括号中使用数字表示次序比如要选择 p 类型第 2 个的子元素，就是：      
```
//p[2]
```
注意，选择的是 p 类型第 2 个的子元素，不是第 2 个子元素，并且是 p 类型。           

2、再比如，要选取父元素为 div 中的 p 类型第 2 个子元素：            
```
//div/p[2]
```

3、也可以选择第 2 个子元素，不管是什么类型，采用通配符 `*`。比如选择父元素为 div 的第 2 个子元素，不管是什么类型，可这样表示：         
```
//div/*[2]
```

<br>

###### 2.6.2 选取倒数第几个子元素
1、比如选取 p 类型倒数第 1 个子元素：         
```
//p[last()]
```

2、选取 p 类型倒数第 2 个子元素：        
```
//p[last()-1]
```

3、选择父元素为 div 中 p 类型倒数第 3 个子元素：           
```
//div/p[last()-2]
```

<br>

###### 2.6.3 范围选择
1、xpath 还可以选择子元素的次序范围。比如选取 option 类型第 1 到 2 个子元素：             
```
//option[position()<=2]
或者
//option[position()<3]
```

2、选择 class 属性为 multi_choice 的前 3 个子元素：             
```
//*[@class='multi_choice']/*[position()<=3]
```

3、选择 class 属性为 multi_choice 的后 3 个子元素：          
```
//*[@class='multi_choice']/*[position()>=last()-2]
```

为什么不是 `last()-3` 呢？ 因为：         
(1) `last()` 本身代表最后一个元素             
(2) `last()-1` 本身代表倒数第 2 个元素             
(3) `last()-2` 本身代表倒数第 3 个元素                

<br>

#### 2.7 组选择
&emsp;&emsp;组选择，可以同时使用多个表达式，多个表达式选择的结果都是要选择的元素，xpath 的组选择语法是用竖线隔开多个表达式。          

1、比如，要选所有的 option 元素和所有的 h4 元素，可以使用：         
```
//option | //h4
```

2、再比如，要选所有的 class 为 single_choice 和 class 为 multi_choice 的元素，可以使用：          
```
//*[@class='single_choice'] | //*[@class='multi_choice']
```

<br>

#### 2.8 选择父节点
1、xpath 可以选择父节点，某个元素的父节点用 `/..` 表示。比如要选择 id 为 china 的节点的父节点，可以这样写：          
```
//*[@id='china']/.. 
```
当某个元素没有特征可以直接选择，但是它有子节点有特征， 就可以采用这种方法，先选择子节点，再指定父节点。           

2、还可以继续找上层父节点，比如：           
```
/*[@id='china']/../../..
```

<br>

#### 2.9 兄弟节点选择
1、xpath 也可以选择后续兄弟节点，用这样的语法 `following-sibling::`。比如要选择 class 为 single_choice 的元素的所有后续兄弟节点：           
```
//*[@class='single_choice']/following-sibling::*
```

2、如果，要选择后续节点中的 div 节点，就应该这样写：         
```
//*[@class='single_choice']/following-sibling::div
```

3、xpath 还可以选择前面的兄弟节点，用这样的语法 `preceding-sibling::`，比如要选择 class 为 single_choice 的元素的所有前面的兄弟节点：            
```
//*[@class='single_choice']/preceding-sibling::*
```

<br>

#### 2.10 注意点
要在某个元素内部使用 xpath 选择元素，需要在 xpath 表达式最前面加个点，像这样：            
```
.//p
```

<br>
<br>
---
相关链接：    
[https://blog.csdn.net/CZD__CZD/article/details/120488450](https://blog.csdn.net/CZD__CZD/article/details/120488450)