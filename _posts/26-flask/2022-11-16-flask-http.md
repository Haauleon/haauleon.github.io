---
layout:        post
title:         "Flask Web | HTTP 方法"
subtitle:      "使用装饰器传参可以改变路由只回应 GET 请求的行为"
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

### 一、HTTP 方法
&emsp;&emsp;HTTP 有多个访问 URL 方法，默认情况下，路由只回应 GET 请求，但是通过 app.route 装饰器传递 methods 参数可以改变这个行为。如下使用 `methods=['GET', 'POST']` 可以实现既支持 GET 请求也支持 POST 请求：           
```python
# -*- coding: utf-8 -*-#
from flask import Flask

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return 'Login Index Page!'


@app.route('/j/item/<id>', methods=['DELETE', 'POST'])
def item(id):
    return 'Update: {}'.format(id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
```

<br>

执行结果如下：     
1. 访问 `GET http://127.0.0.1:9000/login`    
    ![](\img\in-post\post-flask\2022-11-16-flask-http-1.jpg)       
2. 访问 `POST http://127.0.0.1:9000/login`       
    ![](\img\in-post\post-flask\2022-11-16-flask-http-2.jpg)     
3. 访问 `POST http://127.0.0.1:9000/j/item/9999999`     
    ![](\img\in-post\post-flask\2022-11-16-flask-http-3.jpg)     
4. 访问 `DELETE http://127.0.0.1:9000/j/item/9999999`    
    ![](\img\in-post\post-flask\2022-11-16-flask-http-4.jpg) 