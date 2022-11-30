---
layout:        post
title:         "Flask Web | 记录慢查询"
subtitle:      "添加钩子将慢查询及相关上下文信息记录到日志中"
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

### 一、记录慢查询
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

&emsp;&emsp;数据库性能是开发者必须关注的重点之一，在复杂的业务代码逻辑前提下，如果只是通过 **MySQL 的日志** 去看慢查询的日志是很难定位问题的。可以借用 SQLALCHEMY_RECORD_QUERIES 和 DATABASE_QUERY_TIMEOUT 将慢查询及相关上下文信息记录到日志中。     

<br>

#### 1、启用查询记录功能
&emsp;&emsp;设置配置项 DATABASE_QUERY_TIMEOUT 和 SQLALCHEMY_RECORD_QUERIES 的阈值，然后使用 logging.Formatter 格式化被记录到日志文件 slow_query.log 中的字符串，最后添加 app.after_request 钩子用于每次请求结束后获取执行的查询语句并判断阈值，超过就记录到日志中。如执行以下代码：                
```python
# coding=utf-8
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, request, jsonify
from flask_sqlalchemy import get_debug_queries

from ext import db
from users import User

app = Flask(__name__)
app.config.from_object('config')
# 设置数据库查询超时时间为 0.0001s
app.config['DATABASE_QUERY_TIMEOUT'] = 0.0001
# 启用查询记录功能
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
db.init_app(app)

# 格式化程序实例用于将 LogRecord 转换为用户定制的格式化文本
formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

"""
RotatingFileHandler() 用于记录到一组文件的处理程序，当当前文件达到一定大小时，该处理程序将从一个文件切换到下一个文件。
例如：
handler = RotatingFileHandler('slow_query.log', maxBytes=10000, backupCount=10)
给 app.logger 添加一个记录日志到名为 slow_query.log 的文件的处理器，这个日志会按大小切分
"""
handler = RotatingFileHandler('slow_query.log', maxBytes=10000, backupCount=10)
handler.setLevel(logging.WARN)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

with app.app_context():
    db.drop_all()
    db.create_all()


@app.route('/users', methods=['POST'])
def users():
    username = request.form.get('name')

    user = User(username)
    print 'User ID: {}'.format(user.id)
    db.session.add(user)
    db.session.commit()

    return jsonify({'id': user.id})


"""
此处添加 app.after_request 钩子，每次请求结束后获取执行的查询语句，例如超过阈值则记录日志
"""


@app.after_request
def after_request(response):
    for query in get_debug_queries():
        if query.duration >= app.config['DATABASE_QUERY_TIMEOUT']:
            app.logger.warn(
                ('\nContext:{}\nSLOW QUERY: {}\nParameters: {}\n'
                 'Duration: {}\n').format(query.context, query.statement,
                                          query.parameters, query.duration))
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```

<br>
<br>

#### 2、客户端发送请求
&emsp;&emsp;应用启动成功后，在客户端发送 post 请求，请求结果如下：     
```
❯ http -f post http://localhost:9000/users name=Wanghuifeng
HTTP/1.0 200 OK
Content-Length: 14
Content-Type: application/json
Date: Wed, 30 Nov 2022 03:10:39 GMT
Server: Werkzeug/0.11.10 Python/2.7.11+

{
    "id": 1
}
```

<br>
<br>

#### 3、终端显示的内容
&emsp;&emsp;客户端发送请求后，应用终端显示的内容如下：     
```
❯ python web/logger_slow_query.py
 * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 203-908-357
User ID: None
--------------------------------------------------------------------------------
WARNING in logger_slow_query [web/logger_slow_query.py:48]:

Context:web/logger_slow_query.py:36 (users)
SLOW QUERY: INSERT INTO users (name) VALUES (%s)
Parameters: ('Wanghuifeng',)
Duration: 0.000552892684937

--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
WARNING in logger_slow_query [web/logger_slow_query.py:48]:

Context:web/logger_slow_query.py:38 (users)
SLOW QUERY: SELECT users.id AS users_id, users.name AS users_name
FROM users
WHERE users.id = %s
Parameters: (1L,)
Duration: 0.000504970550537

--------------------------------------------------------------------------------
127.0.0.1 - - [30/Nov/2022 03:10:39] "POST /users HTTP/1.1" 200 -
```


<br>
<br>

#### 4、日志文件的内容
&emsp;&emsp;从终端显示的结果可知，由于 `app.config['DATABASE_QUERY_TIMEOUT'] = 0.0001`，而 `Duration: 0.000504970550537`，因此 `query.duration > app.config['DATABASE_QUERY_TIMEOUT']`，所以超过设定阈值后就会被记录到日志文件 slow_query.log 中。日志文件的内容如下：     
```
(venv) ❯ cat -n chapter3/section3/slow_query.log
     1  [2016-08-14 17:22:09,859] {logger_slow_query.py:48} WARNING -
     2  Context:logger_slow_query.py:36 (users)
     3  SLOW QUERY: INSERT INTO users (name) VALUES (%s)
     4  Parameters: ('lihang',)
     5  Duration: 0.000456809997559
     6
     7  [2016-08-14 17:22:09,860] {logger_slow_query.py:48} WARNING -
     8  Context:logger_slow_query.py:38 (users)
     9  SLOW QUERY: SELECT users.id AS users_id, users.name AS users_name
    10  FROM users
    11  WHERE users.id = %s
    12  Parameters: (1L,)
    13  Duration: 0.000252962112427
    14
    15  [2016-08-14 17:22:50,244] {logger_slow_query.py:48} WARNING -
    16  Context:logger_slow_query.py:36 (users)
    17  SLOW QUERY: INSERT INTO users (name) VALUES (%s)
    18  Parameters: ('lihang',)
    19  Duration: 0.000751972198486
    20
    21  [2016-08-14 17:22:50,245] {logger_slow_query.py:48} WARNING -
    22  Context:logger_slow_query.py:38 (users)
    23  SLOW QUERY: SELECT users.id AS users_id, users.name AS users_name
    24  FROM users
    25  WHERE users.id = %s
    26  Parameters: (1L,)
    27  Duration: 0.000526905059814
    28
    29  [2016-08-14 17:23:04,196] {logger_slow_query.py:48} WARNING -
    30  Context:logger_slow_query.py:36 (users)
    31  SLOW QUERY: INSERT INTO users (name) VALUES (%s)
    32  Parameters: ('lihang',)
    33  Duration: 0.00152277946472
    34
    35  [2016-08-14 17:23:04,197] {logger_slow_query.py:48} WARNING -
    36  Context:logger_slow_query.py:38 (users)
    37  SLOW QUERY: SELECT users.id AS users_id, users.name AS users_name
    38  FROM users
    39  WHERE users.id = %s
    40  Parameters: (2L,)
    41  Duration: 0.000243902206421
    42
```

&emsp;&emsp;日志中包含了 **出现问题的代码位置** 以及 **对应的 SQL 语句**，就可以直接知道问题的根源了。       

<br>
<br>

注意：变量 DATABASE_QUERY_TIMEOUT 的值为 0.0001 只是为了演示，生产环境需要按需调大这个阈值。    