---
layout:        post
title:         "Jmeter | 提取响应值并设为全局变量"
subtitle:      "使用 JSON 提取器获取响应字段值、设置全局变量和引用"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
    - API 测试
---

### 一、背景
&emsp;&emsp;想让 Jmeter 像 postman 一样有设置全局变量的能力，因为有些时候需要将上一个接口获取到的数据作为下一个接口的参数来使用。在 Jmeter 中，可以将响应字段设置为全局变量，这样就可以跨请求使用，实现联动。      

<br>
<br>

### 二、操作
###### 1、分析查看结果树
由以下查看结果树中的 HTTP 响应来看，我希望把 totalCount 这个字段作为全局变量，从而在其他接口中引用此 totalCount 的值。     
![](\img\in-post\post-jmeter\2022-07-21-jmeter-json-1.png) 

<br>

###### 2、使用JSON提取器


###### 3、设置全局变量

###### 4、使用全局变量

