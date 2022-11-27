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