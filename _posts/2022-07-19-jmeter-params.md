---
layout:        post
title:         "Jmeter | 用户自定义变量"
subtitle:      "使用自定义变量增加 JDBC 请求中 SQL 语句的灵活性"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
    - API 测试
---

### 一、用户自定义变量
&emsp;&emsp;顾名思义，就是用户自定义的变量，作用于当前线程组，可以用作当前线程组的全局变量。目的在于，增加 JDBC 请求中 SQL 查询语句的灵活性，不用写死字段值。    

<br>
<br>

### 二、操作步骤
###### 1、添加用户自定义变量
![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-1.png)    

![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-2.png)     

<br>

###### 2、使用用户自定义变量
![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-3.png)     

<br>

###### 3、查看结果树
![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-4.png) 