---
layout:        post
title:         "Flask Web | 命令行接口使用"
subtitle:      "在命令行窗口执行 flask 命令启动应用、flask shell 交互以及使用 flask.cli 模块"
author:        "Haauleon"
header-img:    "img/in-post/post-flask/bg.jpeg"
header-mask:   0.4
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

### 一、命令行接口
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

&emsp;&emsp;在 Flask 0.11 之前，启动的应用的端口（port）、主机地址（host）以及是否开启 DEBUG 模式，都需要在代码中明确指定，如下：       
```python
...
...


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
```

<br>
<br>

### 二、使用 Flask 命令行
#### 1、Flask-Script 启动应用   
&emsp;&emsp;一个比较好的方式是使用第三方扩展 Flask-Script 管理，需要安装以下版本的 Flask-Script 包：     
```
 ❯ pip install Flask-Script==2.0.5
 ❯ pip show Flask-Script
---
Metadata-Version: 2.0
Name: Flask-Script
Version: 2.0.5
Summary: Scripting support for Flask
Home-page: http://github.com/smurfix/flask-script
Author: Matthias Urlichs
Author-email: matthias@urlichs.de
Installer: pip
License: BSD
Location: /home/ubuntu/.virtualenvs/venv/lib/python2.7/site-packages
Requires: Flask
Classifiers:
  Development Status :: 5 - Production/Stable
  Environment :: Web Environment
  Intended Audience :: Developers
  License :: OSI Approved :: BSD License
  Operating System :: OS Independent
  Programming Language :: Python
  Programming Language :: Python :: 2
  Programming Language :: Python :: 2.7
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3.3
  Topic :: Internet :: WWW/HTTP :: Dynamic Content
  Topic :: Software Development :: Libraries :: Python Modules
```

<br>

&emsp;&emsp;现在可以直接在命令行窗口执行 Flask 命令启动应用：     
```
 ❯ export FLASK_APP=web/run.py      # 主程序文件路径
 ❯ export FLASK_DEBUG=1             # 设置调试模式 0/1
 ❯ flask run -h 0.0.0.0 -p 9000 
 * Serving Flask app "run"
 * Forcing debug mode on
 * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 145-709-830
127.0.0.1 - - [20/Nov/2022 04:25:46] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [20/Nov/2022 04:26:03] "GET / HTTP/1.1" 200 - 
```

<br>
<br>

#### 2、使用 shell 交互模式   
&emsp;&emsp;flask 命令还支持 shell 子命令，可以在交互模式中进行打印输出：         
```
 ❯ export FLASK_APP=chapter3/section1/run.py
 ❯ export FLASK_DEBUG=1
 ❯ flask shell
Python 2.7.11+ (default, Apr 17 2016, 14:00:29)
[GCC 5.3.1 20160413] on linux2
App: hello [debug]
Instance: /home/ubuntu/web/instance
>>> app
<Flask 'run'>
>>> app.url_map
Map([<Rule '/' (HEAD, OPTIONS, GET) -> hello_world>,
 <Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>])
>>> app.config
<Config {'JSON_AS_ASCII': True, 'USE_X_SENDFILE': False, 'SESSION_COOKIE_PATH': None, 'SESSION_COOKIE_DOMAIN': None, 'SESSION_COOKIE_NAME': 'session', 'SESSION_REFRESH_EACH_REQUEST': True, 'LOGGER_HANDLER_POLICY': 'always', 'LOGGER_NAME': 'hello', 'DEBUG': True, 'SECRET_KEY': None, 'EXPLAIN_TEMPLATE_LOADING': False, 'MAX_CONTENT_LENGTH': None, 'APPLICATION_ROOT': None, 'SERVER_NAME': None, 'PREFERRED_URL_SCHEME': 'http', 'JSONIFY_PRETTYPRINT_REGULAR': True, 'TESTING': False, 'PERMANENT_SESSION_LIFETIME': datetime.timedelta(31), 'PROPAGATE_EXCEPTIONS': None, 'TEMPLATES_AUTO_RELOAD': None, 'TRAP_BAD_REQUEST_ERRORS': False, 'JSON_SORT_KEYS': True, 'JSONIFY_MIMETYPE': 'application/json', 'SESSION_COOKIE_HTTPONLY': True, 'SEND_FILE_MAX_AGE_DEFAULT': datetime.timedelta(0, 43200), 'PRESERVE_CONTEXT_ON_EXCEPTION': None, 'SESSION_COOKIE_SECURE': False, 'TRAP_HTTP_EXCEPTIONS': False}>
>>> app.debug
True
```

<br>
<br>

#### 3、集成 Click
&emsp;&emsp;从 Flask 0.11 开始，Flask 集成了 Click，如下 Requires：     
```
 ❯ pip show flask
---
Metadata-Version: 2.0
Name: Flask
Version: 0.11.1
Summary: A microframework based on Werkzeug, Jinja2 and good intentions
Home-page: http://github.com/pallets/flask/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
Installer: pip
License: BSD
Location: /home/ubuntu/.virtualenvs/venv/lib/python2.7/site-packages
Requires: itsdangerous, click, Werkzeug, Jinja2
Classifiers:
  Development Status :: 4 - Beta
  Environment :: Web Environment
  Intended Audience :: Developers
  License :: OSI Approved :: BSD License
  Operating System :: OS Independent
  Programming Language :: Python
  Programming Language :: Python :: 2
  Programming Language :: Python :: 2.6
  Programming Language :: Python :: 2.7
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3.3
  Programming Language :: Python :: 3.4
  Programming Language :: Python :: 3.5
  Topic :: Internet :: WWW/HTTP :: Dynamic Content
  Topic :: Software Development :: Libraries :: Python Modules
Entry-points:
  [console_scripts]
  flask=flask.cli:main
```

&emsp;&emsp;使用 Click 甚至还能替换 Flask-Script。现在基于 flask.cli 模块添加子命令 initdb，该子命令用来初始化数据库，代码没有实际逻辑只做演示。            
```python
# coding=utf-8
import click
from flask import Flask

app = Flask(__name__)


@app.cli.command()
def initdb():
    click.echo('Init the db')
```

&emsp;&emsp;指定上述执行文件位置后就可以使用 initdb 了。     
```
 ❯ export FLASK_APP=web/app_cli.py
 ❯ flask initdb
Init the db
```


<br>
<br>

相关链接：    
[Flask内置命令行工具—CLI](https://segmentfault.com/a/1190000017436977)        
[Flask内置命令行工具—CLI 官方文档](https://flask.palletsprojects.com/en/1.0.x/cli/)