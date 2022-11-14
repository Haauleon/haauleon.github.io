---
layout:        post
title:         "Flask Web | Flask 配置管理"
subtitle:      "使用文件集中管理 app.config 的设置项，可通过三种方式加载配置文件"
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

### 一、Flask 内置的配置变量
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.12.1           

&emsp;&emsp;复杂的项目需要配置各种环境，app.config 内置的全部配置变量可以参考：[官方文档](https://flask.palletsprojects.com/en/0.12.x/config/)，先打印看看 flask 的 0.12.1 版本提供的内置配置变量有哪些：        
```python
# coding=utf-8
from flask import Flask

app = Flask(__name__)
print app.config
```

执行结果：     
```
<Config {
    'JSON_AS_ASCII': True, 
    'USE_X_SENDFILE': False, 
    'SESSION_COOKIE_PATH': None, 
    'SESSION_COOKIE_DOMAIN': None, 
    'SESSION_COOKIE_NAME': 'session', 
    'SESSION_REFRESH_EACH_REQUEST': True, 
    'LOGGER_HANDLER_POLICY': 'always', 
    'LOGGER_NAME': '__main__', 
    'DEBUG': False, 
    'SECRET_KEY': None, 
    'EXPLAIN_TEMPLATE_LOADING': False, 
    'MAX_CONTENT_LENGTH': None, 
    'APPLICATION_ROOT': None, 
    'SERVER_NAME': None, 
    'PREFERRED_URL_SCHEME': 'http', 
    'JSONIFY_PRETTYPRINT_REGULAR': True, 
    'TESTING': False, 
    'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 
    'PROPAGATE_EXCEPTIONS': None, 
    'TEMPLATES_AUTO_RELOAD': None, 
    'TRAP_BAD_REQUEST_ERRORS': False, 
    'JSON_SORT_KEYS': True, 
    'JSONIFY_MIMETYPE': 'application/json', 
    'SESSION_COOKIE_HTTPONLY': True, 
    'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 
    'PRESERVE_CONTEXT_ON_EXCEPTION': None, 
    'SESSION_COOKIE_SECURE': False, 
    'TRAP_HTTP_EXCEPTIONS': False
}>
```

<br>
<br>

### 二、管理 app.config 设置项
&emsp;&emsp;一般会根据项目需要，自由添加设置项，包括但不限于 app.config 内置的配置变量，这里提供了三种方式进行设置项的管理。    

<br>

#### 1、硬编码
如果设置项很少，可以直接硬编码进来，比如下面的方式：     
```python
# coding=utf-8
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

print app.config
```

执行可知设置项 `DEBUG` 已成功设置为 `True`：           
```
<Config {
    'JSON_AS_ASCII': True, 
    'USE_X_SENDFILE': False, 
    'SESSION_COOKIE_PATH': None, 
    'SESSION_COOKIE_DOMAIN': None, 
    'SESSION_COOKIE_NAME': 'session', 
    'SESSION_REFRESH_EACH_REQUEST': True, 
    'LOGGER_HANDLER_POLICY': 'always', 
    'LOGGER_NAME': '__main__', 
    'DEBUG': True, 
    'SECRET_KEY': None, 
    'EXPLAIN_TEMPLATE_LOADING': False, 
    'MAX_CONTENT_LENGTH': None, 
    'APPLICATION_ROOT': None, 
    'SERVER_NAME': None, 
    'PREFERRED_URL_SCHEME': 'http', 
    'JSONIFY_PRETTYPRINT_REGULAR': True, 
    'TESTING': False, 
    'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 
    'PROPAGATE_EXCEPTIONS': None, 
    'TEMPLATES_AUTO_RELOAD': None, 
    'TRAP_BAD_REQUEST_ERRORS': False, 
    'JSON_SORT_KEYS': True, 
    'JSONIFY_MIMETYPE': 'application/json', 
    'SESSION_COOKIE_HTTPONLY': True, 
    'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 
    'PRESERVE_CONTEXT_ON_EXCEPTION': None, 
    'SESSION_COOKIE_SECURE': False, 
    'TRAP_HTTP_EXCEPTIONS': False
}>
```

<br>
<br>

#### 2、更新数据结构 dict
app.config 是 flask.config.Config 类的实例，继承自 Python 内置数据结构 dict，所以可以使用 update 方法更新设置项：      
```python
# coding=utf-8
from flask import Flask

app = Flask(__name__)

app.config.update(
    DEBUG=True,
    SECRET_KEY='abcdefg123456789'
)

print app.config
```

执行可知设置项 `DEBUG` 已成功设置为 `True`，`SECRET_KEY` 已成功设置为 `abcdefg123456789`：             
```
<Config {
    'JSON_AS_ASCII': True, 
    'USE_X_SENDFILE': False, 
    'SESSION_COOKIE_PATH': None, 
    'SESSION_COOKIE_DOMAIN': None, 
    'SESSION_COOKIE_NAME': 'session', 
    'SESSION_REFRESH_EACH_REQUEST': True, 
    'LOGGER_HANDLER_POLICY': 'always', 
    'LOGGER_NAME': '__main__', 
    'DEBUG': True, 
    'SECRET_KEY': 'abcdefg123456789', 
    'EXPLAIN_TEMPLATE_LOADING': False, 
    'MAX_CONTENT_LENGTH': None, 
    'APPLICATION_ROOT': None, 
    'SERVER_NAME': None, 
    'PREFERRED_URL_SCHEME': 'http', 
    'JSONIFY_PRETTYPRINT_REGULAR': True, 
    'TESTING': False, 
    'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 
    'PROPAGATE_EXCEPTIONS': None, 
    'TEMPLATES_AUTO_RELOAD': None, 
    'TRAP_BAD_REQUEST_ERRORS': False, 
    'JSON_SORT_KEYS': True, 
    'JSONIFY_MIMETYPE': 'application/json', 
    'SESSION_COOKIE_HTTPONLY': True, 
    'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 
    'PRESERVE_CONTEXT_ON_EXCEPTION': None, 
    'SESSION_COOKIE_SECURE': False, 
    'TRAP_HTTP_EXCEPTIONS': False
}>
```

<br>
<br>

#### 3、使用配置文件
如果设置项很多，想要集中管理设置项，应该把它们存放到一个文件里。例如起个叫 settings.py 的配置文件：     
```python
A = 1
B = 2
C = 3
D = 4
```

<br>
<br>

### 三、加载配置文件
上述添加了 settings.py 配置文件后，需要在执行文件的 app.config 配置中加载该配置文件的内容，app.config 支持以下三种方式加载配置文件。  

<br>

#### 1、通过配置文件加载
**方式一：以字符串的名字传入模块名字**    
```python
# coding=utf-8
from flask import Flask

app = Flask(__name__)
app.config.from_object('settings')

print app.config
```

执行可知 settings.py 配置文件的内容已全部添加进 app.config 中：     
```
<Config {
    'JSON_AS_ASCII': True, 
    'USE_X_SENDFILE': False, 
    'C': 3, 
    'B': 2, 
    'D': 4, 
    'SESSION_COOKIE_PATH': None, 
    'SESSION_COOKIE_DOMAIN': None, 
    'SESSION_COOKIE_NAME': 'session', 
    'SESSION_REFRESH_EACH_REQUEST': True, 
    'LOGGER_HANDLER_POLICY': 'always', 
    'A': 1, 
    'LOGGER_NAME': '__main__', 
    'DEBUG': False, 
    'SECRET_KEY': None, 
    'EXPLAIN_TEMPLATE_LOADING': False, 
    'MAX_CONTENT_LENGTH': None, 
    'APPLICATION_ROOT': None, 
    'SERVER_NAME': None, 
    'PREFERRED_URL_SCHEME': 'http', 
    'JSONIFY_PRETTYPRINT_REGULAR': True, 
    'TESTING': False, 
    'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 
    'PROPAGATE_EXCEPTIONS': None, 
    'TEMPLATES_AUTO_RELOAD': None, 
    'TRAP_BAD_REQUEST_ERRORS': False, 
    'JSON_SORT_KEYS': True, 
    'JSONIFY_MIMETYPE': 'application/json', 
    'SESSION_COOKIE_HTTPONLY': True, 
    'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 
    'PRESERVE_CONTEXT_ON_EXCEPTION': None, 
    'SESSION_COOKIE_SECURE': False, 
    'TRAP_HTTP_EXCEPTIONS': False
}>
```

<br>

**方式二：引用文件后直接传入模块对象**     
```python
# coding=utf-8
from flask import Flask
import settings

app = Flask(__name__)
app.config.from_object(settings)

print app.config
```

执行结果跟方式一是一致的。   

<br>
<br>

#### 2、通过文件名字加载
直接传入文件名字，但是不限于只使用 .py 后缀的文件名：     
```python
# coding=utf-8
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('settings.py', silent=True)  # 默认当配置文件不存在时会抛出异常，使用 silent=True 的时候只是返回 False 不会抛出异常

print app.config
```

<br>
<br>

#### 3、通过环境变量加载
这种方式依然支持 silent 参数，获得路径后其实还是使用 from_pyfile 的方式加载：   
```
❯ export MYAPPLICATION_SETTINGS='settings.py'
app.config.from_envvar('MYAPPLICATION_SETTINGS')
```