---
layout:        post
title:         "Python3 | 占位符 _"
subtitle:      "只循环不使用变量的优美方式"
date:          2017-11-01
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
---

## 背景
&emsp;&emsp;有时候只想创建一个循环，但是不想去使用变量的值，不使用变量的话又会造成浪费，另外 IDE 也会提示定义的变量没有被用到。     

<br><br>

## 使用技巧
###### 一、for 循环
&emsp;&emsp;`for _ in range(n)` 语法仅用于创建一个循环。使用 `_` 占位符表示不在意变量的值，只用于循环遍历 n 次，无法打印变量值。           
<br>

实例：                    
```python
for _ in range(5):
    print("美滋滋")
```
<br>

运行结果：                       
```
美滋滋
美滋滋
美滋滋
美滋滋
美滋滋
```
<br><br>

###### 二、列表
&emsp;&emsp;在一个序列中只想取头和尾，也可以使用占位符 `_` ,`*` 表示有 0 或多个。      
<br>

```python
nums = [1,2,3,4,5]
head, *_, tail = nums
print("head = {}".format(head))
print("tail = {}".foramt(tail))
print("type(_) = {}".foramt(type(_)))
print("_ = {}".format(_))
```
<br>

运行结果：
```
head = 1
tail = 5
type(_) = <class 'list'>
_ = [2, 3, 4]
```