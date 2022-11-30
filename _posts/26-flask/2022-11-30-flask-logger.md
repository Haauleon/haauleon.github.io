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

