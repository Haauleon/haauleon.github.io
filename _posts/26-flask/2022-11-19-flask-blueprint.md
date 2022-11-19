---
layout:        post
title:         "Flask Web | 蓝图"
subtitle:      "蓝图可以实现应用的模块化，让应用层次更清晰，让开发者更容易开发和维护项目"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Flask
    - Python
    - Web开发
    - Vagrant
    - Ubuntu
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、蓝图
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

#### 1、背景
&emsp;&emsp;由于项目开发是一个非常耗时间和精力的工程，如果我们将所有的路由都写在同一个文件下的话，非常不便于代码管理和后期功能代码的添加。如下代码示例（manage_v1.py）：     
```python
# -*- coding: utf-8 -*-#
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/admin/hello')
def hello():
    return '/admin/hello'


@app.route('/admin/new')
def new():
    return '/admin/new'


@app.route('/admin/edit')
def edit():
    return '/admin/edit'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
```

<br>
<br>

#### 2、使用蓝图示例
&emsp;&emsp;蓝图（BluePrint）实现了应用的模块化，使用蓝图让应用层次清晰，开发者可以更容易的开发和维护项目。       

&emsp;&emsp;蓝图通常作用于相同的 URL 前缀，比如 /user/:id、/user/profile 这样的地址，这些地址都是以 /user 开头，那么它们就可以放在一个模块中。如以下的模块示例：     
```python
# coding=utf-8
from flask import Blueprint

bp = Blueprint('user', __name__, url_prefix='/user')  # 使用 url_prefix 来设置前缀


@bp.route('/')
def index():
    return '/user/'


@bp.route('/profile')
def index():
    return '/user/profile'
```

&emsp;&emsp;每个模块都会暴露一个全局变量 bp，之后在主程序中使用 register_blueprint 注册模块即可（如果想去掉模块只需要去掉对应的注册语句即可）。在主程序中注册模块的代码示例：       
```python
# coding=utf-8
from flask import Flask
import user

app = Flask(__name__)
app.register_blueprint(user.bp)


if __name__ == '__main__':
    print app.url_map
    app.run(host='0.0.0.0', port=9000)
```

<br>

执行主程序，访问结果如下：     
1. 访问 GET http://127.0.0.1:9000/user/          
    ```
    HTTP/1.0 200 OK
    Content-Length: 6
    Content-Type: text/html; charset=utf-8
    Date: Sat, 19 Nov 2022 14:58:23 GMT
    Server: Werkzeug/0.11.10 Python/2.7.11

    /user/
    ```
2. 访问 http://127.0.0.1:9000/user/profile     
    ```
    HTTP/1.0 200 OK
    Content-Length: 13
    Content-Type: text/html; charset=utf-8
    Date: Sat, 19 Nov 2022 14:58:30 GMT
    Server: Werkzeug/0.11.10 Python/2.7.11

    /user/profile
    ```