---
layout:        post
title:         "Flask Web | 响应"
subtitle:      "视图函数的返回值会被自动转换为响应对象，需要包装 jsonify 使其返回 JSON 格式的响应"
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

### 一、响应
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   

&emsp;&emsp;视图函数的返回值会被自动转换为一个响应对象，其转换的逻辑我在这里使用了如以下代码示例：    
```python
# -*- coding: utf-8 -*-#
from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    """返回一个字符串"""
    return 'Index Page!'


@app.route('/home')
def home():
    """返回一个元组"""
    return 'Home Page!', 201, {'version': 1}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```       

<br>

转换逻辑说明：     
1. 如果返回的是一个合法的响应对象，它会从视图直接返回。     
2. 如果返回的是一个字符串，会用字符串数据和默认参数创建以字符串为主体，状态码为 200，MIME 类型是 text/html 的 werkzeug.wrappers.Response 相应对象。        
    ```
    GET http://127.0.0.1:9000/index
    HTTP/1.0 200 OK
    Content-Length: 11
    Content-Type: text/html; charset=utf-8
    Date: Thu, 17 Nov 2022 14:48:18 GMT
    Server: Werkzeug/0.11.10 Python/2.7.11

    Index Page!
    ```
3. 如果返回的是一个元组，且元组中的元素可以提供额外的信息。这样的元组必须是 (response, status, headers) 的形式，但是需要至少包含一个元素。status 值会覆盖状态码，headers 可以是一个列表或字典用来作额外的消息头。     
    ```
    GET http://127.0.0.1:9000/home 
    HTTP/1.0 201 CREATED
    Content-Length: 10
    Content-Type: text/html; charset=utf-8
    Date: Thu, 17 Nov 2022 14:48:32 GMT
    Server: Werkzeug/0.11.10 Python/2.7.11
    version: 1

    Home Page!
    ```
4. 如果上述条件均不满足，Flask 会假设返回值是一个合法的 WSGI 应用程序，并通过 Response.force_type(rv, request.environ) 转换为一个请求对象。    

<br>
<br>

#### 1、使用 make_response
&emsp;&emsp;需求是要返回的是一个元组，如果不使用 make_response 则响应元组直接 return 返回：     
```python
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
```

<br>

&emsp;&emsp;可以改成显示调用 make_response 的方式，这种方法很灵活也很整洁，可以添加一些额外的工作，比如设置 cookie、头部信息等：      
```python
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    return resp
```

<br>
<br>

#### 2、返回 JSON 格式的响应
&emsp;&emsp;API 都是返回 JSON 格式的响应，所以需要包装 jsonify。可以抽象一下，让 Flask 自动帮我们做这些工作：     
```python
# coding=utf-8
from flask import Flask, jsonify, render_template
from werkzeug.wrappers import Response

app = Flask(__name__)


class JSONResponse(Response):
    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, dict):
            rv = jsonify(rv)
        return super(JSONResponse, cls).force_type(rv, environ)


app.response_class = JSONResponse


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    return resp


@app.route('/')
def hello_world():
    return {'message': 'Hello World!'}


@app.route('/custom_headers')
def headers():
    return {'headers': [1, 2, 3]}, 201, [('X-Request-Id', '100')]


@app.route('/custom_new')
def headers():
    """视图中也可以直接指定状态字符串，使用 201 CREATED 替代数字的 201"""
    return {'headers': [1, 2, 3]}, '201 CREATED', [('X-Request-Id', '100')]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```

<br>

执行结果如下：    
1. 访问 http://127.0.0.1:9000/cheng，由于该页面不存在则向浏览器渲染 error.html 文件（自定义）的内容。             
    ```
    HTTP/1.0 404 NOT FOUND
    Content-Length: 134
    Content-Type: text/plain; charset=utf-8
    Date: Thu, 17 Nov 2022 15:21:39 GMT
    Server: Werkzeug/0.11.10 Python/2.7.11

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>404 Not Found!!!</title>
    </head>
    <body>

    </body>
    </html>
    ```
2. 访问 http://127.0.0.1:9000/，返回 JSON 格式的响应。           
    ```
    HTTP/1.0 200 OK
    Content-Length: 32
    Content-Type: application/json
    Date: Thu, 17 Nov 2022 15:21:47 GMT
    Server: Werkzeug/0.11.10 Python/2.7.11

    {
        "message": "Hello World!"
    }
    ```
3. 访问 http://127.0.0.1:9000/custom_headers，返回 JSON 格式的响应。     
    ```
    HTTP/1.0 201 CREATED
    Content-Length: 45
    Content-Type: application/json
    Date: Thu, 17 Nov 2022 15:21:58 GMT
    Server: Werkzeug/0.11.10 Python/2.7.11
    X-Request-Id: 100

    {
        "headers": [
            1,
            2,
            3
        ]
    }
    ```
4. 访问 http://127.0.0.1:9000/headers2，其响应结果同上。     
    ```      
    HTTP/1.0 201 CREATED
    Content-Length: 45
    Content-Type: application/json
    Date: Thu, 17 Nov 2022 15:22:06 GMT
    Server: Werkzeug/0.11.10 Python/2.7.11
    X-Request-Id: 100

    {
        "headers": [
            1,
            2,
            3
        ]
    }
    ```

<br>
<br>

#### 3、使用 httpie 发送请求
&emsp;&emsp; httpie 是一个使用 Python 编写的，提供了语法高亮、JSON 支持，可以替代 curl 在命令行下请求数据的工具，它也可以很方便地集成到 Python 项目中。      

（1）安装 httpie      
```
pip install httpie==0.9.4
```

（2）使用 httpie     
打开终端，请求 http://127.0.0.1:9000/headers2，结果如下：     
![](\img\in-post\post-flask\2022-11-17-flask-response.jpg)               
