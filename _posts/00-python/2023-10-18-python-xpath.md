---
layout:        post
title:         "爬虫 | xpath 定位方法详解"
subtitle:      "python + selenium + xpath 定位方法详解"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 前言
&emsp;&emsp;selenium 中的 xpath 有八大定位策略，分别是 id、name、class name、tag name、link text、partial link text、xpath、css 。那么我们今天呢主要来讲讲八大定位策略中的 xpath 的定位方法。

<br>
<br>

### 一、xpath基本定位用法
#### 1.1 使用id定位
```python
driver.find_element_by_xpath('//input[@id="kw"]') 
```

[]()

<br>

#### 1.2 使用class定位
```python
driver.find_element_by_xpath('//input[@class="s_ipt"]')
```

[]()

<br>

#### 1.3 其他方式结合xpath定位
通过常用的 8 种方式结合 xpath 均可以定位（name、tag_name、link_text、partial_link_text）以上只列举了 2 种常用方式哦。           

<br>
<br>

### 二、xpath相对路径/绝对路径定位
#### 2.1 相对定位
以 `//` 开头 如：       
```
//form//input[@name="phone"]
```





<br>
<br>
---
相关链接：    
[python—selenium —xpath定位方法详解](https://blog.csdn.net/qishuzdh/article/details/124847147)