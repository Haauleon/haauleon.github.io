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
![](\img\in-post\post-jmeter\2022-07-19-jmeter-params-save-1.png)    