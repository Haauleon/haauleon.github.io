---
layout:        post
title:         "Python3 | SQLAlchemy学习"
subtitle:      "SQLAlchemy是一个基于Python实现的ORM框架"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - SQLAlchemy
---


### 一、SQLAlchemy简介
&emsp;&emsp;SQLAlchemy 是一个基于 Python 实现的 ORM 框架。该框架建立在 DB API之上，使用关系对象映射进行数据库操作，简言之便是：<mark>将类和对象转换成SQL，然后使用数据 API 执行 SQL 并获取执行结果</mark>。    

<br>

#### 1、与Django中models的区别
&emsp;&emsp;很多小伙伴说 SQLAlchemy 不如 Django 的 models 好用，这里我们需要知道。Models 其实只是配置和使用比较简单，毕竟是 Django 自带的 ORM 框架，但是兼容性远不如 SQLAchemy，真正算得上全面的 ORM 框架必然是 SQLAlchemy。               
&emsp;&emsp;无论使用什么 ORM 框架，其实都是为了方便不熟练数据库使用的同学，最推荐的还是使用原生的 SQL 语句，也建议大家攻克 SQL 难关。          

<br>
<br>

#### 2、SQLAlchemy组成
组成部分：          

|组成|释义|
|---|---|
|Engine|框架的引擎|
|Connection Pooling|数据库连接池|
|Dialect|选择连接数据库的DB API种类|
|Schema/Types|架构和类型|
|SQL Exprression Language|SQL表达式语言|

&emsp;&emsp;SQLAlchemy 本身无法操作数据库，其必须以来 pymsql 等第三方插件，Dialect 用于和数据 API 进行交流，根据配置文件的不同调用不同的数据库 API，从而实现对数据库的操作，如：             
```text
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
    
pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
    
MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
    
cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
    
更多：http://docs.sqlalchemy.org/en/latest/dialects/index.html
```

<br>
<br>

### 二、SQLAlchemy使用
#### 1、执行原生sql语句
通过 SQLAlchemy 执行原生的 sql 语句           

