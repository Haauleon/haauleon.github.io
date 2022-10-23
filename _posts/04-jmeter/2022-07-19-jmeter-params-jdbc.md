---
layout:        post
title:         "Jmeter | JDBC 请求设置参数值"
subtitle:      "使用 Parameter Value 进行多值传递"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
---

### 一、Parameter Value
&emsp;&emsp;JDBC 请求中， Query 的参数值可以用 `?` 作为占位符，可以通过 `Parameter Value` 设置参数值，多个值之间以逗号隔开，按顺序传递到 Query 语句中的占位符即可。

<br>
<br>

### 二、操作步骤
###### 1、使用 Parameter
![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-jdbc-1.png)    

<br>

###### 2、查看结果树
![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-jdbc-2.png)     

![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-jdbc-3.png) 