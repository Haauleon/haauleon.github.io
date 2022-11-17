---
layout:        post
title:         "Flask Web | 跳转和重定向"
subtitle:      "跳转（301）为页面被永久性移走，重定向（302）为页面暂时性转移"
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

### 一、跳转和重定向
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   

&emsp;&emsp;在 Flask，跳转和重定向是通过 flask.redirect 实现的。      

<br>

#### 1、跳转
&emsp;&emsp;跳转（状态码 301）多用于旧网址在废弃前转向新网址以保证用户的访问，有页面被永久性移走的概念。      
```python
# -*- coding: utf-8 -*-#
from flask import Flask, redirect
app = Flask(__name__)


@app.route('/help2')
def help2():
    return 'Help2 Page'


@app.route('/help')
def help():
    """跳转"""
    return redirect('help2', code=301)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

```

执行结果如下：    
&emsp;&emsp;访问 `GET http://127.0.0.1:9000/help` 后页面会自动跳转至新的页面 `GET http://127.0.0.1:9000/help2`。        

![](\img\in-post\post-flask\2022-11-17-flask-1-url-redirect-1.jpg)

<br>
<br>

#### 2、重定向
&emsp;&emsp;重定向（状态码 302）表示页面是暂时性的转移，但是也不建议经常性使用重定向。     
```python
# -*- coding: utf-8 -*-#
from flask import Flask, url_for, redirect
app = Flask(__name__)


@app.route('/index2/')
def index2():
    return 'Index2 Page'


@app.route('/index/')
def index():
    """重定向"""
    return redirect(url_for('index2', id=2))  # redirect 的状态码 code 默认是 302，即重定向


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

```

执行结果如下：    
&emsp;&emsp;访问 `GET http://127.0.0.1:9000/index` 后页面会自动跳转至新的页面 `GET http://127.0.0.1:9000/index2/?id=2`。        

![](\img\in-post\post-flask\2022-11-17-flask-1-url-redirect-2.jpg)    

<br>

相关链接:     
1. [Flask 的 URL 规则希望保证唯一 URL](https://haauleon.gitee.io/2022/11/16/flask-only-url/)       
2. [使用 url_for 构建 URL 的原因](https://haauleon.gitee.io/2022/11/16/flask-structure-url/)

<br>
<br>

### 二、301 302 308 状态码
&emsp;&emsp;重定向还是有需要深入探讨的地方，返回码不仅有经常使用的 301、303 还有 302、307、308。它们之间有什么区别呢？可以按照 **是否缓存** 和 **重定向方法** 这两个维度去拆分。     

||**缓存（永久重定向）**|**不缓存（临时重定向）**|
|----|----|----|
|转GET|301|302、303|
|方法保持|308|307|

<br>

&emsp;&emsp;如果是永久重定向那么浏览器客户端就会缓存此次重定向结果，下次如果有请求则直接从缓存读取（除非清除浏览器缓存）。譬如我们切换域名，将所有老域名的流量转入新域名，可以使用永久重定向。        

&emsp;&emsp;如果只是临时重定向那么浏览器则不会缓存。譬如我们的服务临时升级，会使用临时重定向。       

&emsp;&emsp;方法保持的意思是原请求和重定向的请求是否使用相同的方法。譬如原请求是 POST 提交一个表单，如果是 301 重定向的话，重定向的请求会转为 GET 重新提交，如果是 308 则会保持原来 POST 请求不变。      

<br>

相关链接：      
[浅析 http 状态码 301、302、303、307、308 区别及对 SEO 优化网址 URL 劫持的影响](http://t.zoukankan.com/goloving-p-14087235.html)

<br>
<br>

### 三、应用代码分析
#### 1、配置文件
`config.py` 配置文件内容：     
```python 
# coding=utf-8
# file: config.py 
DEBUG = False

try:
    from local_settings import *
except ImportError:
    pass
```

代码分析：      
（1）         
```python
from local_settings import *
```       
&emsp;&emsp;local_settings.py 文件时可选存在的，它不进入版本库。若在 local_settings.py 文件中添加了设置项，则这些设置项会全部被添加进配置文件 config.py 中。注意：这是常用的通过本地配置文件重载版本库配置的方法！

<br>
<br>

#### 2、应用文件
`simple.py` 文件内容：     
```python
# coding=utf-8
# file: simple.py 
from flask import Flask, request, abort, redirect, url_for

app = Flask(__name__)
app.config.from_object('config')


@app.route('/people/')
def people():
    name = request.args.get('name')
    if not name:
        return redirect(url_for('login'))
    user_agent = request.headers.get('User-Agent')
    return 'Name: {0}; UA: {1}'.format(name, user_agent)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.headers.get('user_id')
        return 'User: {} login'.format(user_id)
    else:
        return 'Open Login page'


@app.route('/secret/')
def secret():
    abort(401)
    print 'This is never executed'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=app.debug)
```

代码分析：     
（1）       
```python
app.config.from_object('config')
```
&emsp;&emsp;向 app.config 加载配置文件 config.py 中的全部内容。     

（2）     
```python
@app.route('/people/')
```
&emsp;&emsp;访问 `http://127.0.0.1/people` 的请求会被 308 跳转至 `http://127.0.0.1/people/`，保证了 URL 的唯一性。     

（3）      
```python
user_agent = request.headers.get('User-Agent')
```
&emsp;&emsp;request.headers 存放了请求头的头部信息，通过它可以获取 UA 值。     

（4）      
```python
@app.route('/login/', methods=['GET', 'POST'])
```
&emsp;&emsp;request.methods 的值是请求的类型，表示可以使用 POST 请求。      

（5）      
```python
abort(401)
```
&emsp;&emsp;执行 abort(401) 会放弃请求并返回错误代码 401，表示禁止访问。之后的语句永远不会被执行。如下图所示：      
![](\img\in-post\post-flask\2022-11-17-flask-1-url-redirect-3.jpg)        

（6）       
```python
app.run(host='0.0.0.0', port=9000, debug=app.debug)
```
&emsp;&emsp;能使用 `debug=app.debug` 是因为 flask.config.ConfigAttribute 在 app 中做了配置的代理，app.debug 其实就是 `app.config['DEBUG']` 且默认值是 False（可以通过打印 `print app.debug` 进行验证）。目前的配置代理项有：     
```
app.debug -> DEBUG
app.testing -> TESTING
app.secret_key -> SECRET_KEY
app.session_cookie_name -> SESSION_COOKIE_NAME
app.permanent_session_lifetime -> PERMANENT_SESSION_LIFETIME
app.use_x_sendfile -> USE_X_SENDFILE
app.logger_name -> LOGGER_NAME
```

<br>
<br>

#### 3、flask.config.ConfigAttribute
&emsp;&emsp;安装了 flask 之后，进入 flask\app.py 文件中可看到以下配置键且均设置了默认值（在 default_config 中设置默认值）：      
```python
class Flask(_PackageBoundObject):
    ......
    config_class = Config
    debug = ConfigAttribute('DEBUG')
    testing = ConfigAttribute('TESTING')
    secret_key = ConfigAttribute('SECRET_KEY')
    session_cookie_name = ConfigAttribute('SESSION_COOKIE_NAME')
    permanent_session_lifetime = ConfigAttribute('PERMANENT_SESSION_LIFETIME',
        get_converter=_make_timedelta)
    send_file_max_age_default = ConfigAttribute('SEND_FILE_MAX_AGE_DEFAULT',
        get_converter=_make_timedelta)
    use_x_sendfile = ConfigAttribute('USE_X_SENDFILE')
    logger_name = ConfigAttribute('LOGGER_NAME')
    ......
    default_config = ImmutableDict({
        'DEBUG':                                get_debug_flag(default=False),
        'TESTING':                              False,
        'PROPAGATE_EXCEPTIONS':                 None,
        'PRESERVE_CONTEXT_ON_EXCEPTION':        None,
        'SECRET_KEY':                           None,
        'PERMANENT_SESSION_LIFETIME':           timedelta(days=31),
        'USE_X_SENDFILE':                       False,
        'LOGGER_NAME':                          None,
        'LOGGER_HANDLER_POLICY':               'always',
        'SERVER_NAME':                          None,
        'APPLICATION_ROOT':                     None,
        'SESSION_COOKIE_NAME':                  'session',
        'SESSION_COOKIE_DOMAIN':                None,
        'SESSION_COOKIE_PATH':                  None,
        'SESSION_COOKIE_HTTPONLY':              True,
        'SESSION_COOKIE_SECURE':                False,
        'SESSION_REFRESH_EACH_REQUEST':         True,
        'MAX_CONTENT_LENGTH':                   None,
        'SEND_FILE_MAX_AGE_DEFAULT':            timedelta(hours=12),
        'TRAP_BAD_REQUEST_ERRORS':              False,
        'TRAP_HTTP_EXCEPTIONS':                 False,
        'EXPLAIN_TEMPLATE_LOADING':             False,
        'PREFERRED_URL_SCHEME':                 'http',
        'JSON_AS_ASCII':                        True,
        'JSON_SORT_KEYS':                       True,
        'JSONIFY_PRETTYPRINT_REGULAR':          True,
        'JSONIFY_MIMETYPE':                     'application/json',
        'TEMPLATES_AUTO_RELOAD':                None,
    })
```

<br>

&emsp;&emsp;再转到 flask\config.py 文件中可看到 ConfigAttribute 类的作用其实就是将属性转发到配置。所以上述 `app.run(host='0.0.0.0', port=9000, debug=app.debug)` 中的 `debug=app.debug` 也就等同于 `debug=app.config['DEBUG']`，由于 `app.config['DEBUG']` 默认值是 False ，所以 `debug=app.debug` 最终等于 `debug=False`：      
```python
class ConfigAttribute(object):
    """Makes an attribute forward to the config"""

    def __init__(self, name, get_converter=None):
        self.__name__ = name
        self.get_converter = get_converter

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        rv = obj.config[self.__name__]
        if self.get_converter is not None:
            rv = self.get_converter(rv)
        return rv

    def __set__(self, obj, value):
        obj.config[self.__name__] = value
```