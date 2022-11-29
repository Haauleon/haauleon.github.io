---
layout:        post
title:         "Flask Web | Flask-SQLAlchemy"
subtitle:      "Flask 中使用 SQLAlchemy 实现在 Web 上实现创建用户"
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

### 二、Web 创建用户实践
&emsp;&emsp;实现一个能在 Web 上实现创建用户的应用，项目文件结构如下：     
```
web
├── __init__.py
├── app_with_sqlalchemy.py   # 应用创建文件
├── config.py                # 应用配置文件
├── consts.py                # 数据库配置文件
├── ext.py                   # 第三方扩展集合文件
└── users.py                 # 模型文件
```     

<br>

#### 1、db.Model 模型设计
&emsp;&emsp;一个大型项目，模型应该对应地存放在不同的模型文件中，如下将 users 这个表的模型存放到 users.py 中：      
```python
# coding=utf-8
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

#### 2、使用 ext.py 文件
&emsp;&emsp;在 ext.py 文件中存放 Flask 第三方的扩展，文件内容如下：      
```python
# coding=utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

```
&emsp;&emsp;这样的好处是，由于 db 是一个没有依赖的常量， 因此在 app 中就可以使用 `from ext import db`，这样就不会造成 **循环依赖**。

<br>
<br>


#### 3、数据库配置文件
数据库配置文件 consts.py 的内容如下：    
```python
# coding=utf-8
HOSTNAME = 'localhost'
DATABASE = 'r'
USERNAME = 'web'
PASSWORD = 'web'
DB_URI = 'mysql://{}:{}@{}/{}'.format(
    USERNAME, PASSWORD, HOSTNAME, DATABASE)
```

<br>
<br>

#### 4、应用配置文件
&emsp;&emsp;把应用的配置也独立出来，统一放到 config.py 中，如下内容：      
```python
# coding=utf-8
# 导入数据库配置
from consts import DB_URI
# 应用配置项
DEBUG = True
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

<br>
<br>

#### 5、应用创建文件
&emsp;&emsp;所有配置都准备好之后，在创建应用的文件 app_with_sqlalchemy.py 中加载配置并启动应用。     
```python
# coding=utf-8
from flask import Flask, request, jsonify

from ext import db
from users import User  # 导入模型类

app = Flask(__name__)
# 使用 from_object 加载 config.py 中的配置，生产环境中推荐这样管理配置
app.config.from_object('config')
# 将第三方扩展放在 ext.py 之后，这里只需要使用 xx.init_app(app) 的方式初始化，这也是推荐的用法
db.init_app(app)

"""
Flask-SQLAlchemy 要求执行的时候有应用上下文，但是在这里还没有，所以需要使用 with app.app_context() 创建应用上下文
"""
with app.app_context():
    """
    drop_all() 和 create_all() 要在定义 model 之后再执行
    """
    db.drop_all()
    db.create_all()


@app.route('/users', methods=['POST'])
def users():
    username = request.form.get('name')

    user = User(username)
    """
    print 的 user.id 永远是 None，因为在没有 commit 之前还没有创建它；commit 之后 user.id 会自动改成在表中创建的条目 id
    """
    print 'User ID: {}'.format(user.id)
    db.session.add(user)
    db.session.commit()

    return jsonify({'id': user.id})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```

启动应用，发送以下请求查看响应结果：     
```
POST http://127.0.0.1:9000/users?name=wujun
POST /users?name=wujun HTTP/1.1
User-Agent: PostmanRuntime/7.29.2
Accept: */*
Cache-Control: no-cache
Postman-Token: f53491f1-b97e-4d70-ab34-26e7c0ec4cdb
Host: 127.0.0.1:9000
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 0
 
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 14
Server: Werkzeug/0.11.10 Python/2.7.11+
Date: Tue, 29 Nov 2022 14:31:09 GMT
 
{
"id": 4
}
```

应用文件显示的内容如下：     
```
 ❯ python web/app_with_sqlalchemy.py
 * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 203-908-357
User ID: None
10.0.2.2 - - [29/Nov/2022 14:31:09] "POST /users?name=wujun HTTP/1.1" 200 -
```