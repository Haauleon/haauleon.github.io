---
layout:        post
title:         "Jmeter | 数据库接口测试"
subtitle:      "使用 Jmeter 进行数据库测试"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
    - API 测试
---

### 一、Jmeter 数据库测试
&emsp;&emsp;Jmeter 支持基于 JDBC 对数据库进行测试，它可以帮助我们建立连接池，同时提供程序来执行我们给出的 SQL 语句，并且可以进行参数化。为了在 Jmeter 中成功设置数据库连接池，首先需要安装数据库支持的 JDBC 驱动，各厂家的数据库都提供了 JDBC 驱动，可以在对应的官网获取。我当前的公司使用的是 MySql 数据库。      

<br>
<br>

### 二、JDBC 连接池设置
###### 1、下载 JDBC 驱动
进入 MySql 下载专区 [https://dev.mysql.com/downloads/](https://dev.mysql.com/downloads/)，选择 `Connector/J` 进入驱动下载页面 [https://dev.mysql.com/downloads/connector/j/](https://dev.mysql.com/downloads/connector/j/)。       
