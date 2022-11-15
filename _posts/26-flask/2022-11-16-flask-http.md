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

<br>
<br>

&emsp;&emsp;如果存在 GET 请求方法，那么也会自动添加 HEAD 方法，无需干预无需指定。它会确保遵照 HTTP RFC（描述 HTTP 协议的文档）处理 HEAD 请求，所以完全可以忽略这部分的 HTTP 规范。从 Flask 0.6 起，它也实现了 OPTIONS 的自动处理。以下简要介绍 HTTP 方法和使用场景：        

|HTTP 方法|使用场景|
|----|----|
|GET|获取资源，GET 操作应该是幂等的|
|HEAD|想要获取信息，但是只关心信息头。应用应该像处理 GET 请求一样来处理它，但是不返回实际内容|
|POST|创建一个新的资源|
|PUT|完整地替换资源或者创建资源。PUT 操作虽然有副作用，但应该是幂等的|
|DELETE|删除资源。DELETE 操作有副作用，但也是幂等的|
|OPTIONS|获取资源支持的所有 HTTP 方法|
|PATCH|局部更新，修改某个已有的资源|