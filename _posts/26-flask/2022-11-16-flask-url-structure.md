---
layout:        post
title:         "Flask Web | 构造 URL"
subtitle:      "选择构建 URL 而不是直接在代码中拼接 URL 的场景"
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

### 一、构造 URL 的方法
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
werkzeug==0.11.10       

&emsp;&emsp;用 url_for 构建 URL，它接受函数名作为第一个参数，也接受对应 URL 规则的变量部分的命名参数，未知的变量部分会添加到 URL 末尾作为查询参数。 

<br>

#### 1、url_for 基本用法
&emsp;&emsp;test_request_context 可以帮助我们在交互模式下产生请求上下文。     
```python
# -*- coding: utf-8 -*-#
from flask import Flask, url_for

app = Flask(__name__)
app.config.from_object('settings')


@app.route('/item/888/')
def item1(id):
    pass


@app.route('/item/<id>/')
def item2(id):
    pass


with app.test_request_context():
    """
    url_for() 第一个参数是视图函数名，后面的参数作为查询参数被添加在URL末尾
    """
    print url_for('item1')
    print url_for('item1', id='1')
    print url_for('item1', id=2, next='/')
    print url_for('item1', id=3, page=1, size=10)
    # print url_for('item2')  # 会报错是因为 item2 需要传入id
    print url_for('item2', id='4')
    print url_for('item2', id=5, next='/')
```

执行结果如下：    
```
/item/888/
/item/888/?id=1
/item/888/?id=2&next=%2F
/item/888/?id=3&page=1&size=10
/item/4/
/item/5/?next=%2F
```

<br>
<br>

#### 2、实现页面重定向
&emsp;&emsp;构造 URL 也叫 URL 反转。一般在页面重定向/模板中会使用 URL 反转，`url_for('hello')` 可以找到视图函数 hello 对应的路由。         
```python
# -*- coding: utf-8 -*-#
from flask import Flask, url_for
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/hello/cheng/')
def hello():
    return 'Hello World'


@app.route('/index/1')
def index():
    return 'Index Page'


@app.route('/item/')
def item():
    return redirect(url_for('hello'))


@app.route('/home/')
def home():
    # 构造带参url,这样不管index的路由怎么变,都可以重定向至该页面
    return redirect(url_for('index', kw='flask'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

```

<br>

执行结果如下：     
1. 访问 `http://127.0.0.1:9000/item` 时，页面会被重定向至 `http://127.0.0.1:9000/hello/cheng/`     
    ![](\img\in-post\post-flask\2022-11-16-flask-structure-url-1.jpg)      
2. 访问 `http://127.0.0.1:9000/home` 时，页面会被重定向至 `http://127.0.0.1:9000/index/1?kw=flask`         
    ![](\img\in-post\post-flask\2022-11-16-flask-structure-url-2.jpg) 

<br>
<br>

### 二、构造 URL 的原因
构建 URL 而不选择直接在代码中拼 URL 的原因有两点：       
1. 在未来有更改的时候只需要一次性修改 URL，而不用到处去替换；       
2. URL 构建回你转义特殊字符和 Unicode 数据，这些工作不需要我们自己处理。    