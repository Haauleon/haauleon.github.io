---
layout:        post
title:         "Flask Web | 使用 SQLAlchemy"
subtitle:      "配置并连接数据库、使用原生 SQL 语句和表达式语言"
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
#### 1、create_engine 配置数据库
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

（1）dialect 是数据库的实现，比如 MySQL、PostgreSQL、SQLite      
（2）driver 是 Python 对应的驱动，如果不指定就会选择默认的驱动，比如 MySQL 的默认驱动是 MySQLdb        
```python
engine = create_engine('mysql+mysqldb://haauleon:123456@localhost:8000/mydb')
```

&emsp;&emsp;所以如果连接的是 MySQL 数据库，由于已有默认驱动 MySQLdb，就可以不用指定驱动。如以下语句来配置 MySQL 数据库：         
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

<br>
<br>

#### 2、使用原生 SQL
&emsp;&emsp;之前写的一文 [curd-数据库操作](https://haauleon.gitee.io/2022/11/26/flask-mysql/#3crud-%E6%95%B0%E6%8D%AE%E5%BA%93%E6%93%8D%E4%BD%9C) 中 curd.py 代码如下：     
```python
# coding=utf-8
import MySQLdb
from consts import HOSTNAME, DATABASE, USERNAME, PASSWORD


con = MySQLdb.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)

with con as cur:
    cur.execute('drop table if exists users')
    cur.execute('create table users(Id INT PRIMARY KEY AUTO_INCREMENT, '
                'Name VARCHAR(25))')
    cur.execute("insert into users(Name) values('xiaoming')")
    cur.execute("insert into users(Name) values('wanglang')")
    cur.execute('select * from users')

    rows = cur.fetchall()
    for row in rows:
        print row
    cur.execute('update users set Name=%s where Id=%s', ('ming', 1))
    print 'Number of rows updated:',  cur.rowcount

    cur = con.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('select * from users')

    rows = cur.fetchall()
    for row in rows:
        print row['Id'], row['Name']
```

&emsp;&emsp;现在将以上的代码改写成使用 SQLAlchemy 的 CRUD 代码：      
```python
# coding=utf-8
from sqlalchemy import create_engine
from consts import DB_URI  # 从配置文件 consts.py 中导入 DB_URI = 'mysql://{}:{}@{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, DATABASE)

eng = create_engine(DB_URI)
with eng.connect() as con:
    # con.execute() 执行 SQL 语句
    con.execute('drop table if exists users')
    con.execute('create table users(Id INT PRIMARY KEY AUTO_INCREMENT, '
                'Name VARCHAR(25))')
    con.execute("insert into users(name) values('xiaoming')")
    con.execute("insert into users(name) values('wanglang')")
    rs = con.execute('select * from users')
    # rs 结果通过返回值获取，不再需要执行 rs.fetchone() 或者 rs.fetchall() 也能获取到
    for row in rs:
        print row
```

执行结果如下：    
```
(1L, 'xiaoming')
(2L, 'wanglang')
```


<br>
<br>

#### 3、使用表达式
```python
# coding=utf-8
from sqlalchemy import (create_engine, Table, MetaData, Column, Integer,
                        String, tuple_)
from sqlalchemy.sql import select, asc, and_
from consts import DB_URI

eng = create_engine(DB_URI)

meta = MetaData(eng)
# 定义数据库中的表的模型
users = Table(
    'Users', meta,
    Column('Id', Integer, primary_key=True, autoincrement=True),
    Column('Name', String(50), nullable=False),
)

# 在创建表的时候判断该表是否已存在，已存在则不删除表后再创建表
if users.exists():
    users.drop()
users.create()  # 创建表 users
"""
# 如果要创建的表比较多，比如定义了表 users、balance、account...可使用以下语句：  
meta.create_all(eng)
"""


def execute(s):
    print '-' * 20
    rs = con.execute(s)
    for row in rs:
        print row['Id'], row['Name']


with eng.connect() as con:
    for username in ('xiaoming', 'wanglang', 'lilei'):
        user = users.insert().values(Name=username)
        con.execute(user)

    # stm 变量就是一个生成好的 SQL 语句
    stm = select([users]).limit(1)
    execute(stm)

    k = [(2,)]
    stm = select([users]).where(tuple_(users.c.Id).in_(k))
    execute(stm)

    stm = select([users]).where(and_(users.c.Id > 2,
                                     users.c.Id < 4))
    execute(stm)

    """
    此处的 select([users]).order_by(asc(users.c.Name)) 生成的 SQL 语句即 stm 的返回值是如下：   
    SELECT `Users`.`Id`, `Users`.`Name` FROM `Users` ORDER BY `Users`.`Name` ASC
    """
    stm = select([users]).order_by(asc(users.c.Name))
    execute(stm)

    stm = select([users]).where(users.c.Name.like('%min%'))
    execute(stm)
```

执行结果如下：    
```
--------------------
1 xiaoming
--------------------
2 wanglang
--------------------
3 lilei
--------------------
3 lilei
2 wanglang
1 xiaoming
--------------------
1 xiaoming
```