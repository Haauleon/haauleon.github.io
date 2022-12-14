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
werkzeug==0.11.10       

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

#### 4、flask.cli 实现子命令
&emsp;&emsp;实现一个叫做 new_shell 的子命令。使用 app.cli.command 来指定子命令的名字和帮助信息，使用 click.option 给子命令添加参数。由于子命令 new_shell 需要使用 app 这个上下文，所以需要添加 with_appcontext 这个装饰器。     
```python
# coding=utf-8
import sys
import code

import click
from flask import Flask
from flask.cli import with_appcontext  # 导入上下文装饰器

try:
    import IPython  # noqa
    has_ipython = True
except ImportError:
    has_ipython = False

app = Flask(__name__)


def plain_shell(user_ns, banner):
    sys.exit(code.interact(banner=banner, local=user_ns))


def ipython_shell(user_ns, banner):
    IPython.embed(banner1=banner, user_ns=user_ns)


@app.cli.command('new_shell', short_help='Runs a shell in the app context.')
@click.option('--plain', help='Use Plain Shell', is_flag=True)
@with_appcontext
def shell_command(plain):
    from flask.globals import _app_ctx_stack
    app = _app_ctx_stack.top.app
    banner = 'Python %s on %s\nApp: %s%s\nInstance: %s' % (
        sys.version,
        sys.platform,
        app.import_name,
        app.debug and ' [debug]' or '',
        app.instance_path,
    )
    user_ns = app.make_shell_context()
    use_plain_shell = not has_ipython or plain
    if use_plain_shell:
        plain_shell(user_ns, banner)
    else:
        ipython_shell(user_ns, banner)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```

在使用 new_shell 子命令前，需要先指定 FLASK_APP 变量：      
```
❯ export FLASK_APP=web/app_cli.py
```

<br>

执行结果如下：      
1. 查看子命令的帮助信息     
    ```
    ❯ flask new_shell --help
    Usage: flask new_shell [OPTIONS]

    Options:
      --plain  Use Plain Shell
      --help   Show this message and exit.
    ```
2. 使用 --plain 参数      
    ```
    ❯ flask new_shell --plain
    Python 2.7.11+ (default, Apr 17 2016, 14:00:29)
    [GCC 5.3.1 20160413] on linux2
    App: app_cli
    Instance: /home/ubuntu/web/instance
    >>>
    ```
3. 不使用 --plain 参数      
&emsp;&emsp;直接执行命令行 `> flask new_shell` 时，由于使用了 @with_appcontext 装饰器，因此 new_shell 会使用 app 这个上下文。当执行 `import IPython` 这条语句时，由于 pip 已安装第三方包 ipython==5.0.0，所以 has_ipython 标志位设置为 True，进而执行到 `use_plain_shell = not has_ipython or plain` 这条语句时，明显得知 use_plain_shell 的值为 False，所以最终选择执行的语句是 `ipython_shell(user_ns, banner)` ，也就是使用 IPython 交互环境，如下所示。             
    ```
    ❯ flask new_shell
    Python 2.7.11+ (default, Apr 17 2016, 14:00:29)
    [GCC 5.3.1 20160413] on linux2
    App: app_cli
    Instance: /home/ubuntu/web/instance
    In [1]:
    ```

<br>
<br>

相关链接：    
[Flask内置命令行工具—CLI](https://segmentfault.com/a/1190000017436977)        
[Flask内置命令行工具—CLI 官方文档](https://flask.palletsprojects.com/en/1.0.x/cli/)