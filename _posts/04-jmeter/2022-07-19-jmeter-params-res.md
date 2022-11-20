---
layout:        post
title:         "Jmeter | JDBC 请求设置响应数组"
subtitle:      "请求成功后，通过设置 Result variable name 将 SQL 查询成功的结果保存在一个数组里"
author:        "Haauleon"
header-img:    "img/in-post/post-jmeter/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Jmeter
    - 数据库
---

### 一、Result variable name
&emsp;&emsp;JDBC 请求成功后，可以通过设置 `Result variable name` 自定义响应结果变量名的方式，将 SQL 查询成功的响应值存为一个数组，查询的每一行都是数组的一个元素。            

<br>
<br>

### 二、操作步骤
###### 1、设置响应结果数组
&emsp;&emsp;如下图，将 SQL 查询成功的响应值存为一个数组，设置数组名为 result。     

![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-res-1.png)    

<br>

###### 2、添加调试取样器
&emsp;&emsp;调试取样器相当于控制台，用来打印输入 JDBC 请求中所有用到的变量名和变量值。养成一个习惯就是：如果添加的请求中涉及到引用动态值或者设置变量时，需要在该请求后面添加一个调试取样器用来打印调试变量。         

![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-res-2.png) 

###### 3、添加查看结果树
![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-res-3.png) 