---
layout:        post
title:         "Flask Web | 静态文件管理"
subtitle:      "为了给用户更好的访问体验，Web 应用大多会提供静态文件服务"
author:        "Haauleon"
header-img:    "img/in-post/post-flask/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Flask
    - Python
    - Web开发
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、静态文件管理
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   

&emsp;&emsp;Web 应用大多会提供静态文件服务以便给用户更好的访问体验。         
&emsp;&emsp;静态文件主要包含 CSS 样式文件(style.css)、JavaScript 脚本文件、图片文件和字体文件等静态资源。Flask 也支持静态文件访问，默认只需要在项目根目录下创建名字为 static 的目录，在应用中使用 `/static` 开头的路径就可以进行访问。        
&emsp;&emsp;但是为了获得更好的处理能力，推荐使用 Nginx 或者其他 Web 服务器管理静态文件。      

<br>

### 二、静态文件路径
run.py 为执行文件，static 目录为静态文件目录，目录设计如下：        
```
app
├── static
│   └── hello.html
├── templates
│   └── error.html
├── tmp
│   └── hello2.html
├── run.py
```

<br>

#### 1、使用 url_for 生成路径
&emsp;&emsp;不要在模板中写死静态文件路径，应该使用 url_for 生成路径。      
```python
# -*- coding: utf-8 -*-#
from flask import Flask, url_for

app = Flask(__name__)

with app.test_request_context():
    print url_for('static', filename='hello.html')
```

执行可知生成的路径如下：            
```
/static/hello.html
```

<br>
<br>

#### 2、定制静态文件的真实目录
&emsp;&emsp;除了生成路径的方法之外，还可以定制静态文件的真实目录。     
```python
# -*- coding: utf-8 -*-#
from flask import Flask, url_for

app = Flask(__name__, static_folder='/tmp')

with app.test_request_context():
    print url_for('static', filename='hello2.html')
```

执行可知生成的路径不是 /static/hello2.html，而是：      
```
/tmp/hello2.html
```