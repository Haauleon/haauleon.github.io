---
layout:        post
title:         "Flask Web | 使用 MySQLdb"
subtitle:      "用 MySQL 的 Python 驱动（MySQLdb）写原生语句来进行数据库开发"
author:        "Haauleon"
header-img:    "img/in-post/post-flask/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Flask
    - Python
    - Web开发
    - Vagrant
    - Ubuntu
    - MySQL
    - 数据库
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、环境安装
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

&emsp;&emsp;数据是动态网站的基础，如果把数据放进数据库，就可以通过数据库管理系统对数据进行管理。    

&emsp;&emsp;MySQL 是一个开源的关系型数据库管理系统。它性能高、免费、配置简单、可靠性好，已经成为最流行的开源数据库。     

&emsp;&emsp;在 Flask 应用中可以自由使用 MySQL、PostgreSQL、SQLite、Redis、MongoDB 来写原生的语句实现功能，也可以使用更高级别的数据库抽象方式，如 SQLAlchemy 或 MongoEngine 这样的 OR(D)M。这里使用 MySQL 的 Python 驱动（MySQLdb）写原生语句的方法演示 Web 开发中的数据库开发工作。     

<br>

#### 1、安装 MySQL
&emsp;&emsp;进入 ubuntu 终端页面，使用以下命令完成 mysql 的安装。安装完成之后默认已经启动了 MySQL，安装 mysql-server 的过程中需要指定 root 账户的密码，**生产环境一定要设置强复杂度的密码**。    
```
~ ubuntu@WEB
❯ sudo apt-get install mysql-server libmysqlclient-dev -yq
Reading package lists...
Building dependency tree...
Reading state information...
libmysqlclient-dev is already the newest version (5.7.13-0ubuntu0.16.04.2).
mysql-server is already the newest version (5.7.13-0ubuntu0.16.04.2).
0 upgraded, 0 newly installed, 0 to remove and 112 not upgraded.

~ ubuntu@WEB
❯ sudo /etc/init.d/mysql start
[ ok ] Starting mysql (via systemctl): mysql.service.
```


<br>
<br>

#### 2、安装驱动 MySQLdb
**注意：** 安装的是 mysql-python，而不是 MySQLdb。      
```
❯ sudo pip install mysql-python
Collecting mysql-python
Installing collected packages: mysql-python
Successfully installed mysql-python-1.2.5

~ ubuntu@WEB
❯ pip show mysql-python
Name: MySQL-python
Version: 1.2.5
Summary: Python interface to MySQL
Home-page: https://github.com/farcepest/MySQLdb1
Author: Andy Dustman
Author-email: farcepest@gmail.com
License: GPL
Location: /usr/local/lib/python2.7/dist-packages
Requires:
```

<br>
<br>

### 二、设置应用账号和权限
&emsp;&emsp;root 的权限很大，不应该在 Web 应用中直接使用此用户（root 密码一般都会被写进应用的配置文件中），应该使用一个单独的用户。执行以下三步来创建一个单独的用户并分配权限：     
1. 创建一个数据库 mydb      
    ```
    ~ ubuntu@WEB
    ❯ sudo mysql -u root
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 3
    Server version: 5.7.13-0ubuntu0.16.04.2 (Ubuntu)

    Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    mysql> create database mydb;
    Query OK, 1 row affected (0.00 sec)
    ```    
2. 创建一个用户，名为 web，密码为 web      
    ```
    mysql> create user 'web'@'locallost' identified by 'web';
    Query OK, 0 rows affected (0.00 sec)
    ```
3. 设置用户权限。用户 web 对数据库 mydb 有全部权限     
    ```
    mysql> use mydb;
    Database changed
    mysql> grant all on r.* TO 'web'@'localhost';
    Query OK, 0 rows affected (0.00 sec)

    mysql> quit;
    Bye
    ```

<br>
<br>

### 三、用 MySQLdb 写原生语句
&emsp;&emsp;以下编写一系列数据库开发的例子，为了重复利用，把常量放到独立的 consts.py 文件里，写入以下内容：     
```python
# coding=utf-8
HOSTNAME = 'localhost'
DATABASE = 'r'
USERNAME = 'web'
PASSWORD = 'web'
DB_URI = 'mysql://{}:{}@{}/{}'.format(
    USERNAME, PASSWORD, HOSTNAME, DATABASE)
```