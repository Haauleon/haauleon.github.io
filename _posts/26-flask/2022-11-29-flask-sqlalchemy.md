---
layout:        post
title:         "Flask Web | Flask-SQLAlchemy"
subtitle:      "在 Flask 实际项目中使用 SQLAlchemy"
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

### 一、Flask-SQLAlchemy
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

&emsp;&emsp;第三方包 Flask-SQLAlchemy 可以帮助我们在 Flask 中很方便地使用 SQLAlchemy。     

<br>

#### 1、安装 Flask-SQLAlchemy
```
❯ pip install Flask-SQLAlchemy
❯ pip show Flask-SQLAlchemy
---
Metadata-Version: 2.0
Name: Flask-SQLAlchemy
Version: 2.1
Summary: Adds SQLAlchemy support to your Flask application
Home-page: http://github.com/mitsuhiko/flask-sqlalchemy
Author: Phil Howell
Author-email: phil@quae.co.uk
Installer: pip
License: BSD
Location: /home/ubuntu/.virtualenvs/venv/lib/python2.7/site-packages
Requires: SQLAlchemy, Flask
```

<br>
<br>

### 二、db.Model 模型设计
&emsp;&emsp;一个大型项目，模型应该对应地存放在不同的模型文件中，如下将 users 这个表的模型存放到 users.py 中：      
```python
from ext import db


"""
db.Model 其实还是基于 declarative_base 实现的，Flask-SQLAlchemy 提供了一个和 Django 风格很像的基类
"""
class User(db.Model):
    __tablename__ = 'users2'

    # id 是自增长的字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        """
        重新定义了 User 的 __init__ 方法，默认需要传入所有字段，而 id 是自增长的字段不需要传入
        """
        self.name = name
```

<br>
<br>

#### 1