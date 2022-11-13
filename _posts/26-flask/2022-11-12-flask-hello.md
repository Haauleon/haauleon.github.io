---
layout:        post
title:         "Flask Web | Flask 安装和入门"
subtitle:      "安装和入门使用，hello world 代码逐行解释"
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

### Hello World
环境准备：     
Python 2.7.11+      
pip==9.0.3 
flask==0.12.1           

```
❯ python --version
Python 2.7.11+

~/web_develop master* ⇣ ubuntu@WEB
❯ pip --version
pip 9.0.3 from /usr/local/lib/python2.7/dist-packages (python 2.7)

~/web_develop master* ⇣ ubuntu@WEB
❯ pip show Flask
Name: Flask
Version: 0.12.1
Summary: A microframework based on Werkzeug, Jinja2 and good intentions
Home-page: http://github.com/pallets/flask/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD
Location: /usr/local/lib/python2.7/dist-packages
Requires: itsdangerous, click, Werkzeug, Jinja2
```

<br>

#### 1、Flask 入门代码    
```
# coding=utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/item/<int:nid>')
def item(nid):
    return 'Item: {}'.format(nid)


@app.route('/cname/<cname>')
def cname(cname):
    return 'your name: {}'.format(cname)


@app.route('/word/<any(a,b):word>')
def word(word):
    return 'word: {}'.format(word)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
```

启动：     
```
❯ python hello.py
 * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 206-892-073
10.0.2.2 - - [13/Nov/2022 15:00:22] "GET /word/b HTTP/1.1" 200 -
```