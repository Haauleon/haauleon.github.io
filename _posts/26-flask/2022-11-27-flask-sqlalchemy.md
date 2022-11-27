---
layout:        post
title:         "Flask Web | 使用 SQLAlchemy"
subtitle:      "SQLAlchemy 是最流行的关系型数据库的 ORM 框架"
author:        "Haauleon"
header-img:    "img/in-post/post-flask/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Flask
    - Python
    - Web开发
    - 数据库
    - ORM
    - SQLAlchemy
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、SQLAlchemy
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     


&emsp;&emsp;SQLAlchemy 是最流行的关系型数据库的 ORM 框架，它由 Mako 的作者 Mike Bayer 创建，[官网直达](https://www.sqlalchemy.org/)。        

<br>

#### 1、安装 SQLAlchemy
```
> pip install SQLAlchemy
> pip show SQLAlchemy
Name: SQLAlchemy
Version: 1.4.44
Summary: Database Abstraction Library
Home-page: https://www.sqlalchemy.org
Author: Mike Bayer
Author-email: mike_mp@zzzcomputing.com
License: MIT
Location: d:\python27\lib\site-packages
Requires: importlib-metadata
```

<br>
<br>

### 二、使用 SQLAlchemy
#### 1、create_engine 连接数据库
&emsp;&emsp;使用 `> vagrant ssh` 连接和操作虚拟机系统，输入 `> ipython` 打开 Ipython 进入交互终端：      
```
In [14]: from sqlalchemy import create_engine
In [15]: engine = create_engine('sqlite://', echo=False)
In [16]: rs = engine.execute('SELECT 1')
In [17]: rs.fetchone()
Out[17]: (1,)
```

&emsp;&emsp;可以使用 with 语句做异常处理，如下：    
```
In [18]: from sqlalchemy import create_engine
In [19]: engine = create_engine('sqlite://', echo=False)
In [20]: with engine.connect() as con:
    ...:     rs = con.execute('SELECT 1')
    ...:     print rs.fetchone()
    ...:
(1,)
```

&emsp;&emsp;create_engine 传入了一个数据库的 URI，`sqlite://` 表示使用了一个 SQLite 的内存型数据库。URI 的格式如下：     
```
dialect+driver://username:password@host:port/database
```
1. dialect 是数据库的实现，比如 MySQL、PostgreSQL、SQLite      
2. driver 是 Python 对应的驱动，如果不指定就会选择默认的驱动，比如 MySQL 的默认驱动是 MySQLdb      
    ```python
    engine = create_engine('mysql+mysqldb://haauleon:123456@localhost:8000/mydb')
    ```

<br>

&emsp;&emsp;所以如果连接的是 MySQL 数据库，由于已有默认驱动 MySQLdb，就可以不用指定驱动。如以下语句来连接 MySQL 数据库：         
```python
engine = create_engine('mysql://haauleon:123456@localhost:8000/mydb')
```

&emsp;&emsp;如果需要详细的输出，可以设置 echo=True：      
```
In [21]: from sqlalchemy import create_engine
In [22]: engine = create_engine('sqlite://', echo=True)
In [23]: with engine.connect() as con:
    ...:     rs = con.execute('SELECT 1')
    ...:     print rs.fetchone()
    ...:
2022-11-27 03:07:37,442 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2022-11-27 03:07:37,442 INFO sqlalchemy.engine.base.Engine ()
2022-11-27 03:07:37,445 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2022-11-27 03:07:37,445 INFO sqlalchemy.engine.base.Engine ()
2022-11-27 03:07:37,448 INFO sqlalchemy.engine.base.Engine SELECT 1
2022-11-27 03:07:37,449 INFO sqlalchemy.engine.base.Engine ()
(1,)
``` 
