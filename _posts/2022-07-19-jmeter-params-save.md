---
layout:        post
title:         "Jmeter | JDBC 请求设置响应变量值"
subtitle:      "请求成功后，提取响应中的值并保存作为自定义变量来使用"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
    - API 测试
---

### 一、Variable names
&emsp;&emsp;JDBC 请求中， 查询 SQL 返回结果的数据储存的变量名，返回几列就有几个变量名。所以 select 语句不能用 `select * from ...` 而是用 `select id, title from ...`，然后将 id 和 title 保存为 `Variable names` 响应变量。      

<br>
<br>

### 二、操作步骤
###### 1、使用 Variable names
如下图，将 id 和 title 这两列的值分别用变量 id 和 title 来存储。     
![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-save-1.png)    

<br>

###### 2、查看结果树
从结果树中查看该 JDBC 请求的响应值，分别有 id 和 title 这两列。     
![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-save-2.png)  

<br>

###### 3、添加 debug sampler
添加一个 debug sampler 查看变量 id 和 title 的值。变量 id 中存储了返回的总行数，用 `id_#=3` 表示，存储了这个字段在每一行中的值，id 对应的第一个字段第一行就是 `id_1`，后面需要用到这个数据时就可以用 `${id_1}` 引用。              
![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-save-3.png)       

![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-save-4.png)     

![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-save-5.png)    

<br>

###### 4、引用动态变量值
![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-save-6.png)       

![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-save-7.png)     