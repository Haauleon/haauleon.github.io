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

### 一、使用 MySQL
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



<br>
<br>

#### 2、安装驱动