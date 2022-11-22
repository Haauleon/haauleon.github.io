---
layout:        post
title:         "Flask Web | Flask 安装和入门"
subtitle:      "安装和入门使用，hello world 代码逐行解释"
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

### Hello World
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1           

```
❯ python --version
Python 2.7.11+

~/web_develop master* ⇣ ubuntu@WEB
❯ pip --version
pip 9.0.3 from /usr/local/lib/python2.7/dist-packages (python 2.7)

~/web_develop master* ⇣ ubuntu@WEB
❯ pip show Flask
Name: Flask
Version: 0.11.1
Summary: A microframework based on Werkzeug, Jinja2 and good intentions
Home-page: http://github.com/pallets/flask/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD
Location: d:\python27\lib\site-packages
Requires: itsdangerous, click, Werkzeug, Jinja2
```

<br>

#### 1、Flask 入门代码    
```python
# coding=utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```

启动：     
```
❯ python hello.py
 * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)
```

启动后打开浏览器访问 http://127.0.0.1:9000 就可以看到熟悉的 `Hello World!` 了，按 `Ctrl + c` 可以停止服务。     

<br>
<br>

#### 2、代码解析
（1）            
```python
# coding=utf-8
```
&emsp;&emsp;声明 python 源文件编码的语法。该编码信息后续会被 python 解析器解析源文件。如果没有特殊原因都应统一使用 utf-8，而不要使用 gb18030、gb2312 等类型。     

（2）      
```python
from flask import Flask
```
&emsp;&emsp;引入 Flask 类，Flask 类实现了一个 WSGI 应用。       

（3）       
```python
app = Flask(__name__)
```
&emsp;&emsp;app 是 Flask 的实例，它接收包或者模块的名字作为参数，但一般都是传递 __name__。是为了让 flask.helpers.get__root_path 函数通过传入这个名字确定程序的根目录，以便获得静态文件和模板文件的目录。       

（4）          
```python
@app.route('/')
def hello_world():
    return 'Hello World!'
```
&emsp;&emsp;使用 app.route 装饰器会将 URL 和执行的视图函数的关系保存到 app.url_map 属性上。而处理 URL 和视图函数的关系的程序就是路由，这里的视图函数就是 hello_world。        

（5）         
```python
if __name__ == '__main__':
```
&emsp;&emsp;使用这个判断可以保证其他文件引用这个文件的时候（例如 from hello import app）不会执行这个判断内的代码，也就是不会执行 app.run 函数。       

（6）    
```python
app.run(host='0.0.0.0', port=9000)
```
&emsp;&emsp;执行 app.run 就可以启动服务了。默认 Flask 只监听虚拟机的本地 127.0.0.1 这个地址，端口为 5000。而这里对虚拟机做的端口转发是 9000，所以需要指定 host 和 port 参数。 0.0.0.0 表示监听所有地址，这样就可以在本机进行访问了。      
&emsp;&emsp;服务器启动后，会调用 werkzeug.serving.run_simple 进入轮询，默认使用单进程单线程的 werkzeug.serving.BaseWSGIServer 处理请求，实际上还是使用标准库 BaseHTTPServer.HTTPServer，通过 select.select 做 0.5 秒的 `while True` 的时间轮询。         
&emsp;&emsp;当我们访问 http://127.0.0.1:9000 ，通过 app.url_map 找到注册的 `/` 这个 URL 模式，就找到了对应的 hello_world 函数并执行，返回 `Hello World!`，状态码为 200。如果访问一个不存在的路径，如 http://127.0.0.1:9000/a ，此时 Flask 找不到对应的模式，就会向浏览器返回 `Not Found`，状态码是 404。     

<br>
<br>

#### 3、app.run
&emsp;&emsp;默认的 app.run 的启动方式只合适调试，不要在生产环境中使用，生产环境应该使用 Gunicorn 或者uWSGI。       

参考：    
[gunicorn部署flask项目简单示例](https://blog.csdn.net/feng_1_ying/article/details/107469379)