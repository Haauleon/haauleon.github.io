---
layout:        post
title:         "Flask Web | 信号机制"
subtitle:      "使用信号在触发动作时发送通知，对应用业务进行解耦"
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

### 一、Flask 的信号机制
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     
werkzeug==0.11.10       

&emsp;&emsp;项目功能越复杂，代码量越大，就越需要做 **业务解耦**，否则在其之上做开发和维护是很痛苦的，尤其是对团队的新人。Flask 从 0.6 开始，通过 [Blinker](https://github.com/pallets-eco/blinker) 提供了信号支持。       

&emsp;&emsp;信号就是在框架核心功能或者一些 Flask 扩展发生动作时所发送的通知，用于帮助程序员解耦应用。    

<br>

#### 1、Blinker 的使用
&emsp;&emsp;Blinker 不像 werkzeug 一样是 Flask 的默认依赖，所以如果不安装 Blinker 就无法使用信号。使用以下命令进行安装：    
```
> pip2 install blinker
```

&emsp;&emsp;以下代码简单使用了 blinker.signal 信号对象，设置一个信号接收器 started，而 connect（用于订阅信号）和 send（用于发送信号）则通过 started 作为桥梁达到解耦的作用，因此实现不用将 connect 和 send 放在一个文件中。      
```python
# coding=utf-8
from blinker import signal

# 设置一个信号接收器
started = signal('test-started')


@started.connect
def each(round):
    print 'Round {}!'.format(round)


def round_two(round):
    print 'Only {}'.format(round)


# 将信号接收器连接到信号发送端
started.connect(round_two, sender=2)  # 值为2的时候才会接收

for round in range(1, 4):
    # 信号接收器开始发送信号
    started.send(round)
```

执行结果如下：    
```
Round 1!
Round 2!
Only 2
Round 3!
```

&emsp;&emsp;信号和钩子做的事情其实很像，如 [Flask 的钩子 before_request 和 after_request](https://haauleon.gitee.io/2022/12/01/flask-ctx/#2%E6%B7%BB%E5%8A%A0%E4%B8%8A%E4%B8%8B%E6%96%87%E7%9A%84%E9%92%A9%E5%AD%90)，这些钩子不需要 Blinker 库且允许你改变请求对象（request）或者响应对象（response），而信号并不会对请求对象和响应对象做改变，仅承担记录和通知的工作。       

<br>
<br>

#### 2、Flask 中内置的信号
&emsp;&emsp;Flask 可以发送 9 种信号，第三方的扩展中也可能会有额外的信号。而我们需要做的是 **添加对应的信号订阅**。以下展示常见的 6 种信号的用法：         

（1）flask.template_rendered   
&emsp;&emsp;模板渲染成功的时候发送，这个信号与模板实例 template 上下文的字典一起调用。      
```python
def log_template_renders(sender, template, context, **extra):
    sender.logger.debug('Rendering template "%s" with context %s',
                        template.name or 'string template',
                        context)

from flask import template_rendered
template_rendered.connect(log_template_renders, app)
```

<br>

（2）flask.request_started      
&emsp;&emsp;建立请求上下文后，在请求处理开始前发送，订阅者可以用 request 之类的标准全局代理访问请求。      
```python
def log_request(sender, **extra):
    sender.logger.debug('Request context is set up')

from flask import request_started
request_started.connect(log_request, app)
```

<br>

（3）flask.request_finished     
&emsp;&emsp;在响应发送给客户端之前发送，可以传递 response。     
```python
def log_response(sender, response, **extra):
    sender.logger.debug('Request context is about to close down.'
                        'Response: %s', response)

from flask import request_finished
request_finished.connect(log_response, app)
```

<br>

（4）flask.got_request_exception    
&emsp;&emsp;在请求处理中抛出异常时发送，异常本身会通过 exception 传递到订阅函数。    
```python
def log_exception(sender, exception, **extra):
    sender.logger.debug('Got exception during processing: %s', exception)

from flask import got_request_exception
got_request_exception.connect(log_exception, app)
```

<br>

（5）flask.request_tearing_down    
&emsp;&emsp;在请求销毁时发送，它总是被调用，即使发生异常。     
```python
def close_db_connection(sender, **extra):
    session.close()

from flask import request_tearing_down
request_tearing_down.connect(close_db_connection, app)
```

<br>

（6）flask.appcontext_tearing_down   
&emsp;&emsp;在应用上下文销毁时发送，它总是被调用，即使发生异常。     
```python
def close_db_connection(sender, **extra):
    session.close()

from flask import appcontext_tearing_down
appcontext_tearing_down.connect(close_db_connection, app)
```

<br>
<br>

#### 3、自定义信号
&emsp;&emsp;可以在自己的应用中直接使用 Blinker 创建信号，如下创建一个信号对象 large_file_saved，当上传文件大于一个阈值的时候就可以发送这个信号。当编写一个 Flask 扩展并且想优雅地在未安装 Blinker 时退出，可以使用 flask.signal.Namespace —— 在订阅信号的时候，如果发现未安装 Blinker 则抛出异常 RuntimeError。      
```python
from blinker import Namespace

web_signals = Namespace()
large_file_saved = web_signals.signal('large-file-saved')


def custom(count):
    print '信号自定义测试: {}'.format(count)


large_file_saved.connect(custom)
for count in range(3):
    large_file_saved.send(count)
```

执行结果如下：    
```
信号自定义测试: 0
信号自定义测试: 1
信号自定义测试: 2
```

<br>
<br>

#### 4、信号订阅的高级用法
&emsp;&emsp;从 Blinker 1.1 开始可以用新的 connect_via() 装饰器订阅信号。如下：    
```python
@appcontext_tearing_down.connect_via(app)
def close_db_connection(sender, **extra):
    session.close()
```

&emsp;&emsp;还可以通过装饰器来使用信号订阅的方法 connect，如下：     
```python
def each(round):
    print 'Round {}!'.format(round)


started.connect(each)
```

&emsp;&emsp;以上装饰器还可以简写，如下：    
```python
@started.connect
def each(round):
    print 'Round {}!'.format(round)
```

<br>
<br>

#### 5、Flask-Login 中的信号
&emsp;&emsp;Flask-Login 插件中带了 6 种信号，可以基于其中的信号做一些额外工作，比如基于 user_logged_in 来记录用户的登录次数和登录 IP 等。使用以下命令安装 Flask-Login 插件：    
```
> pip2 install flask-login
```

&emsp;&emsp;在 Flask-Login 中实现的发送信号代码如下，然后使用 connect_via() 装饰器订阅这个信号就可以了。         
```python
user_logged_in.send(current_app._get_current_object(), user=_get_user())
```

<br>
<br>

### 二、实现登录信号代码
```python
# coding=utf-8
from flask import Flask, request, redirect, url_for
import flask_login
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'super secret string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://web:web@localhost:3306/r'

db = SQLAlchemy(app)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

password = '123'


class User(flask_login.UserMixin, db.Model):
    """
    flask-login 提供了 UserMixin，其有一些用户相关的属性：
    - is_authenticated: 是否被验证
    - is_active: 是否被激活
    - is_anonymous: 是否是匿名用户
    - get_id(): 获得用户的 id，并转换为 Unicode 类型

    可以在创建数据库表模型的时候继承 UserMixin
    """
    __tablename__ = 'login_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    login_count = db.Column(db.Integer, default=0)
    last_login_ip = db.Column(db.String(128), default='unknown')


db.create_all()


"""
使用 connect_vat() 订阅信号后，已登录就会触发 user_logged_in 信号，增加登录次数，并添加最近登录 IP
"""
@flask_login.user_logged_in.connect_via(app)
def _track_logins(sender, user, **extra):
    user.login_count += 1
    user.last_login_ip = request.remote_addr
    db.session.add(user)
    db.session.commit()


"""
使用 user_loader 装饰器的回调函数非常重要，它将决定 user 对象是否在登录状态
"""
@login_manager.user_loader
def user_loader(id):
    """
    回调函数
    @param id: 参数值是在 flask_login.login_user(user) 中传入的 user 的 id 属性
    @return:
    """
    user = User.query.filter_by(id=id).first()
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    登录视图函数
    @return:
    """
    if request.method == 'GET':
        """
        如果是 GET 方法则只返回一个简单的表单
        """
        return '''
<form action='login' method='POST'>
    <input type='text' name='name' id='name' placeholder='name'></input>
    <input type='password' name='pw' id='pw' placeholder='password'></input>
    <input type='submit' name='submit'></input>
</form>
               '''

    name = request.form.get('name')
    if request.form.get('pw') == password:
        """
        如果传入参数 name 和 pw 且 pw 的值等于 123，则跳转至视图函数 protected 上
        """
        user = User.query.filter_by(name=name).first()
        if not user:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()
        flask_login.login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    """
    显示登录信息的视图函数
    @return:
    """
    user = flask_login.current_user
    return 'Logged in as: {}| Login_count: {}|IP: {}'.format(
        user.name, user.login_count, user.last_login_ip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
```

请求结果如下：    
1. GET 请求 /login，不传参则返回一个登录表单     
    ```
    (venv) ❯ http GET http://127.0.0.1:9000/login
    HTTP/1.0 200 OK
    Content-Length: 258
    Content-Type: text/html; charset=utf-8
    Date: Tue, 20 Dec 2022 14:44:37 GMT
    Server: Werkzeug/0.11.10 Python/2.7.11+

    <form action='login' method='POST'>
        <input type='text' name='name' id='name' placeholder='name'></input>
        <input type='password' name='pw' id='pw' placeholder='password'></input>
        <input type='submit' name='submit'></input>
    </form>
    ```
    ![](\img\in-post\post-flask\2022-12-19-flask-signal-1.jpg)    
2. POST 请求 /login 且通过 --form 传入表单，则跳转至 http://127.0.0.1:9000/protected 并显示登录信息           
    ```
    (venv) ❯ http --form POST http://127.0.0.1:9000/login name=XiaoMing pw=123
    HTTP/1.0 302 FOUND
    Content-Length: 227
    Content-Type: text/html; charset=utf-8
    Date: Tue, 20 Dec 2022 14:47:58 GMT
    Location: http://127.0.0.1:9000/protected
    Server: Werkzeug/0.11.10 Python/2.7.11+
    Set-Cookie: session=.eJwdzsGKwjAQANBfWebsodvWS2EPQpqgkAlKapi5CKvdjWl6qUpjxH9X_IL3HnD4m_qLh-Y63foFHM4naB7w9QsNGNdWRuwH7bYzuf1oRLdkoQt2u6DDMVFY1exwZBtHtBuPaheN7WoOeqaxLSjLgcquoqArzOtEdj0bIQfjqDDCe7aniAoj2WNipTOWMpCT3tj_zEJ6crpm0c460xKtTpR9ZNXe6W2SXSUsNwMqSqi2P_BcwO3ST58_fMPzBWacR7A.FoNcng.uSJ-t1C3ux32O02w9gkxme21zkM; HttpOnly; Path=/

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>Redirecting...</title>
    <h1>Redirecting...</h1>
    <p>You should be redirected automatically to target URL: <a href="/protected">/protected</a>.  If not click the link.
    ```
    ![](\img\in-post\post-flask\2022-12-19-flask-signal-2.jpg)     

    ![](\img\in-post\post-flask\2022-12-19-flask-signal-3.jpg)    
3. GET 请求 /protected，则提示接口没有访问权限 401 UNAUTHORIZED      
    ```
    (venv) ❯ http GET http://127.0.0.1:9000/protected
    HTTP/1.0 401 UNAUTHORIZED
    Content-Length: 339
    Content-Type: text/html
    Date: Tue, 20 Dec 2022 14:48:29 GMT
    Server: Werkzeug/0.11.10 Python/2.7.11+

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>401 Unauthorized</title>
    <h1>Unauthorized</h1>
    <p>The server could not verify that you are authorized to access the URL requested.  You either supplied the wrong credentials (e.g. a bad password), or your browser doesn't understand how to supply the credentials required.</p>
    ```