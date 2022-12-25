---
layout:        post
title:         "Flask Web | 使用 Werkzeug"
subtitle:      "挖掘 Werkzeug 中有用的函数和类，帮助我们进行 Web 开发"
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

### Werkzeug 的使用
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     
werkzeug==0.11.10       

&emsp;&emsp;Werkzeug 是 WSGI 协议层工具集，可以挖掘 Werkzeug 中有用的函数和类，帮助我们进行 Web 开发。由于 Werkzeug 也是 Flask 的依赖包，所以在安装 Flask 的同时也安装了 Werkzeug，没有安装可以独立进行安装。     

```
> pip2 install Werkzeug
```

<br>

#### 1、DebuggedApplication
&emsp;&emsp;在Tornado 框架中集成 DebuggedApplication 的例子如下。    

（1）安装 Tornado     
```
> pip2 install tornado==4.3
```

<br>

（2）自定义请求处理类      
```python
import tornado.web
from werkzeug.debug import DebuggedApplication


class Handler(tornado.web.RequestHandler):
    """自定义请求处理类"""
    
    def initialize(self, debug):
        if debug:
            """
            如果开启 DEBUG 模式，则使用 DebugApplication 的 render_exception 方法生成 HTML
            """
            self.write_error = self.write_debugger_error

    def write_debugger_error(self, status_code, **kwargs):
        assert isinstance(self.application, DebugApplication)
        html = self.application.render_exception()
        self.write(html.encode('utf-8', 'replace'))
```

<br>

（3）创建 BadHandler     
```python
class BadHandler(Handler):
    """基于 Handler 创建一个使用 GET 就会报错的 BadHandler"""
    def get(self):
        raise Exception('This is a test')
        self.write('You will never see this text.')
```

<br>

（4）创建 DebugApplication 类     
```python
import tornado.wsgi
from tornado.web import Application
from werkzeug.debug.tbtools import get_current_traceback


class RequestDispatcher(tornado.web._RequestDispatcher):
    def set_request(self, request):
        super(RequestDispatcher, self).set_request(request)
        if '__debugger__' in request.uri:
            return self.application.debug_container(request)


class DebugApplication(Application):
    def __init__(self, *args, **kwargs):
        super(DebugApplication, self).__init__(*args, **kwargs)
        self.debug_app = DebuggedApplication(self, evalex=True)
        self.debug_container = tornado.wsgi.WSGIContainer(self.debug_app)

    def start_request(self, server_conn, request_conn):
        return RequestDispatcher(self, request_conn)

    def render_exception(self):
        traceback = get_current_traceback()

        for frame in traceback.frames:
            self.debug_app.frames[frame.id] = frame
        self.debug_app.tracebacks[traceback.id] = traceback

        return traceback.render_full(evalex=True,
                                     secret=self.debug_app.secret)
```

<br>

（5）创建路由    
```python
def create_application(debug=False):
    """
    创建的路由统一放在函数中，虽然仅有 /error/ 这一个可用地址，但是更有利于独立管理
    """
    handlers = [
        ('/error/', BadHandler, {'debug': debug}),
    ]
    if debug:
        return DebugApplication(handlers, debug=True)
    return Application(handlers, debug=debug)
```

<br>

（6）创建主函数        
```python
import tornado.ioloop
from tornado.options import define, options, parse_command_line


def main():

    # 使用 define 可以定义命令行参数的名字、类型和默认值
    define('debug', default=False, type=bool, help='Run in debug mode.')
    define('port', default=9000, type=int, help='Port on which to listen.')
    parse_command_line()

    logger = logging.getLogger()
    port = options.port
    application = create_application(debug=options.debug)
    logger.info('Running tornado on port {}.'.format(port))
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
```

&emsp;&emsp;create_application 的逻辑是，当 debug 为 False 时即不指定 debug 参数时，则使用默认的 Application：          
```
> python2 app_tornado.py
```
&emsp;&emsp;如果开启 debug 模式，则使用 DebugApplication，即可以使用更友好的 werkzeug.debug.DebuggedApplication：    
```
> python2 app_tornado.py --debug
```

<br>

演示效果如下：    
1. 未开启 debug 模式     
    ![](\img\in-post\post-flask\2022-12-25-flask-werkzeug-1.jpg)      

    ```
    (venv) ❯ http get http://127.0.0.1:9000/error
    HTTP/1.1 404 Not Found
    Content-Length: 69
    Content-Type: text/html; charset=UTF-8
    Date: Sun, 25 Dec 2022 13:23:38 GMT
    Server: TornadoServer/4.3

    <html><title>404: Not Found</title><body>404: Not Found</body></html>


    (venv) ❯ http get http://127.0.0.1:9000/error/
    HTTP/1.1 500 Internal Server Error
    Content-Length: 93
    Content-Type: text/html; charset=UTF-8
    Date: Sun, 25 Dec 2022 13:23:42 GMT
    Server: TornadoServer/4.3

    <html><title>500: Internal Server Error</title><body>500: Internal Server Error</body></html>
    ```
2. 开启 debug 模式     
    ![](\img\in-post\post-flask\2022-12-25-flask-werkzeug-2.jpg)      

    ```
    (venv) ❯ http get http://127.0.0.1:9000/error
    HTTP/1.1 404 Not Found
    Content-Length: 358
    Content-Type: text/plain
    Date: Sun, 25 Dec 2022 13:25:00 GMT
    Server: TornadoServer/4.3

    Traceback (most recent call last):
    File "/home/ubuntu/.virtualenvs/venv/local/lib/python2.7/site-packages/tornado/web.py", line 1422, in _execute
        result = self.prepare()
    File "/home/ubuntu/.virtualenvs/venv/local/lib/python2.7/site-packages/tornado/web.py", line 2149, in prepare
        raise HTTPError(self._status_code)
    HTTPError: HTTP 404: Not Found


    (venv) ❯ http get http://127.0.0.1:9000/error/
    HTTP/1.1 500 Internal Server Error
    Content-Length: 6027
    Content-Type: text/html; charset=UTF-8
    Date: Sun, 25 Dec 2022 13:26:19 GMT
    Server: TornadoServer/4.3

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">
    <html>
    <head>
        <title>Exception: This is a test // Werkzeug Debugger</title>
        <link rel="stylesheet" href="?__debugger__=yes&amp;cmd=resource&amp;f=style.css"
            type="text/css">
        <!-- We need to make sure this has a favicon so that the debugger does
            not by accident trigger a request to /favicon.ico which might
            change the application state. -->
        <link rel="shortcut icon"
            href="?__debugger__=yes&amp;cmd=resource&amp;f=console.png">
        <script src="?__debugger__=yes&amp;cmd=resource&amp;f=jquery.js"></script>
        <script src="?__debugger__=yes&amp;cmd=resource&amp;f=debugger.js"></script>
        <script type="text/javascript">
        var TRACEBACK = 139673206462160,
            CONSOLE_MODE = false,
            EVALEX = true,
            EVALEX_TRUSTED = true,
            SECRET = "6RQeqh5dQszk1yKv5Fwf";
        </script>
    </head>
    <body>
        <div class="debugger">
    <h1>Exception</h1>
    <div class="detail">
    <p class="errormsg">Exception: This is a test</p>
    </div>
    <h2 class="traceback">Traceback <em>(most recent call last)</em></h2>
    <div class="traceback">

    <ul><li><div class="frame" id="frame-139673206462480">
    <h4>File <cite class="filename">"/home/ubuntu/.virtualenvs/venv/lib/python2.7/site-packages/tornado/web.py"</cite>,
        line <em class="line">1443</em>,
        in <code class="function">_execute</code></h4>
    <div class="source"><pre class="line before"><span class="ws">
            </span>yield self.request.body</pre>
    <pre class="line before"><span class="ws">                </span>except iostream.StreamClosedError:</pre>
    <pre class="line before"><span class="ws">                    </span>return</pre>
    <pre class="line before"><span class="ws"></span> </pre>
    <pre class="line before"><span class="ws">            </span>method = getattr(self, self.request.method.lower())</pre>
    <pre class="line current"><span class="ws">            </span>result = method(*self.path_args, **self.path_kwargs)</pre>
    <pre class="line after"><span class="ws">            </span>if result is not None:</pre>
    <pre class="line after"><span class="ws">                </span>result = yield result</pre>
    <pre class="line after"><span class="ws">            </span>if self._auto_finish and not self._finished:</pre>
    <pre class="line after"><span class="ws">                </span>self.finish()</pre>
    <pre class="line after"><span class="ws">        </span>except Exception as e:</pre></div>
    </div>

    <li><div class="frame" id="frame-139673206463120">
    <h4>File <cite class="filename">"/home/ubuntu/web_develop/chapter4/section3/app_tornado.py"</cite>,
        line <em class="line">26</em>,
        in <code class="function">get</code></h4>
    <div class="source"><pre class="line before"><span class="ws">        </span>self.write(html.encode('utf-8', 'replace'))</pre>
    <pre class="line before"><span class="ws"></span> </pre>
    <pre class="line before"><span class="ws"></span> </pre>
    <pre class="line before"><span class="ws"></span>class BadHandler(Handler):</pre>
    <pre class="line before"><span class="ws">    </span>def get(self):</pre>
    <pre class="line current"><span class="ws">        </span>raise Exception('This is a test')</pre>
    <pre class="line after"><span class="ws">        </span>self.write('You will never see this text.')</pre>
    <pre class="line after"><span class="ws"></span> </pre>
    <pre class="line after"><span class="ws"></span> </pre>
    <pre class="line after"><span class="ws"></span>class RequestDispatcher(tornado.web._RequestDispatcher):</pre>
    <pre class="line after"><span class="ws">    </span>def set_request(self, request):</pre></div>
    </div>
    </ul>
    <blockquote>Exception: This is a test</blockquote>
    </div>

    <div class="plain">
    <form action="/?__debugger__=yes&amp;cmd=paste" method="post">
        <p>
        <input type="hidden" name="language" value="pytb">
        This is the Copy/Paste friendly version of the traceback.  <span
        class="pastemessage">You can also paste this traceback into
        a <a href="https://gist.github.com/">gist</a>:
        <input type="submit" value="create paste"></span>
        </p>
        <textarea cols="50" rows="10" name="code" readonly>Traceback (most recent call last):
    File "/home/ubuntu/.virtualenvs/venv/lib/python2.7/site-packages/tornado/web.py", line 1443, in _execute
        result = method(*self.path_args, **self.path_kwargs)
    File "/home/ubuntu/web_develop/chapter4/section3/app_tornado.py", line 26, in get
        raise Exception('This is a test')
    Exception: This is a test</textarea>
    </form>
    </div>
    <div class="explanation">
    The debugger caught an exception in your WSGI application.  You can now
    look at the traceback which led to the error.  <span class="nojavascript">
    If you enable JavaScript you can also use additional features such as code
    execution (if the evalex feature is enabled), automatic pasting of the
    exceptions and much more.</span>
    </div>
        <div class="footer">
            Brought to you by <strong class="arthur">DON'T PANIC</strong>, your
            friendly Werkzeug powered traceback interpreter.
        </div>
        </div>

        <div class="pin-prompt">
        <div class="inner">
            <h3>Console Locked</h3>
            <p>
            The console is locked and needs to be unlocked by entering the PIN.
            You can find the PIN printed out on the standard output of your
            shell that runs the server.
            <form>
            <p>PIN:
                <input type=text name=pin size=14>
                <input type=submit name=btn value="Confirm Pin">
            </form>
        </div>
        </div>
    </body>
    </html>

    <!--

    Traceback (most recent call last):
    File "/home/ubuntu/.virtualenvs/venv/lib/python2.7/site-packages/tornado/web.py", line 1443, in _execute
        result = method(*self.path_args, **self.path_kwargs)
    File "/home/ubuntu/web_develop/chapter4/section3/app_tornado.py", line 26, in get
        raise Exception('This is a test')
    Exception: This is a test

    -->
    ```

<br>
<br>

#### 2、数据结构
&emsp;&emsp;Werkzeug 中提供了多种定制的数据结构，在工作中有时也会需要这样的数据结构，这里举例说明以下常用的几种数据结构。      
1. TypeConversionDict   
    &emsp;&emsp;它继承于 dict，执行 get 方法时可以指定值的类型。
    ```
    In [1]: from werkzeug.datastructures import TypeConversionDict

    In [2]: d = TypeConversionDict(foo='42', bar='blub')

    In [3]: d.get('foo', type=int)  # 指定值的类型为 int
    Out[3]: 42

    In [4]: d.get('bar', -1, type=int)  # 指定值的类型为 int 并更新值为 -1
    Out[4]: -1
    ```
2. ImmutableTypeConversionDict     
    &emsp;&emsp;不可变的 TypeConversionDict，无法更新键的值。         
    ```
    In [1]: from werkzeug.datastructures import ImmutableTypeConversionDict

    In [2]: d = ImmutableTypeConversionDict(name='Lily', age=19)

    In [3]: d.get('name', 'Jimmy', type=str)
    Out[3]: 'Lily'

    In [4]: d.get('age', 20, type=int)
    Out[4]: 19
    ```
3. MultiDict     
    &emsp;&emsp;它继承于 TypeConversionDict，可以对相同的键传入多个值，会把这些值都保留下来。      
    ```
    In [1]: from werkzeug.datastructures import MultiDict

    In [2]: d = MultiDict([('a', 'b'), ('a', 'c')])

    In [3]: d.getlist('a')
    Out[3]: ['b', 'c']

    In [4]: list(d.iterlists())
    Out[4]: [('a', ['b', 'c'])]

    In [5]: d.setlist('d', ['e', 'f'])

    In [6]: d
    Out[6]: MultiDict([('a', 'b'), ('a', 'c'), ('d', 'e'), ('d', 'f')])

    In [7]: d.poplist('d')
    Out[7]: ['e', 'f']

    In [8]: d
    Out[8]: MultiDict([('a', 'b'), ('a', 'c')])

    In [9]: d.get('a')
    Out[9]: 'b'
    ```
4. ImmutableMultiDict  
    &emsp;&emsp;不可变的 MultiDict。     
    ```
    In [1]: from werkzeug.datastructures import ImmutableMultiDict

    In [2]: d = ImmutableMultiDict([('a', 'b'), ('a', 'c')])

    In [3]: d.getlist('a')
    Out[3]: ['b', 'c']

    In [4]: d.setlist('d', ['e', 'f'])
    TypeError: 'ImmutableMultiDict' objects are immutable
    ```
5. OrderedMultiDict    
    &emsp;&emsp;它继承于 MultiDict，但是保留了字典的顺序。     
    ```
    In [1]: from werkzeug.datastructures import OrderedMultiDict

    In [2]: d = OrderedMultiDict([('a', 'c'), ('a', 'b')])

    In [3]: d.getlist('a')
    Out[3]: ['c', 'b']

    In [4]: d.setlist('d', ['f', 'e'])

    In [5]: d
    Out[5]: OrderedMultiDict([('a', 'c'), ('a', 'b'), ('d', 'f'), ('d', 'e')])
    ```
6. ImmutableOrderedMultiDict      
    &emsp;&emsp;不可变的 OrderedMultiDict。    
    ```
    In [1]: from werkzeug.datastructures import ImmutableOrderedMultiDict

    In [2]: d = ImmutableOrderedMultiDict([('a', 'c'), ('a', 'b')])

    In [3]: d
    Out[3]: ImmutableOrderedMultiDict([('a', 'c'), ('a', 'b')])

    In [4]: d.setlist('d', ['f', 'e'])
    TypeError: 'ImmutableOrderedMultiDict' objects are immutable
    ```


<br>
<br>

#### 3、功能函数
&emsp;&emsp;Werkzeug 中提供了多个有用的函数。      
1. cached_property     
    &emsp;&emsp;非常知名的装饰器，它通过描述符把方法执行的结果作为一个属性（property）缓存下来。     
    ```
    In [2]: from werkzeug import cached_property

    In [3]: class Foo:
    ...:
    ...:     @cached_property
    ...:     def bar(self):
    ...:         print 'calculate something'
    ...:         return 1
    ...:

    In [4]: foo = Foo()

    In [5]: foo.bar  # 方法只执行一次，此后都直接返回结果
    calculate something
    Out[5]: 1

    In [6]: foo.bar
    Out[6]: 1

    In [7]: foo.bar
    Out[7]: 1
    ```
2. import_string    
    &emsp;&emsp;一个帮助我们直接通过字符串找到对应模块的功能函数。     
    ```
    In [1]: from werkzeug import import_string

    In [2]: import_string('os')
    Out[2]: <module 'os' from '/home/ubuntu/.virtualenvs/venv/lib/python2.7/os.pyc'>

    In [3]: import_string('werkzeug.utils')
    Out[3]: <module 'werkzeug.utils' from '/home/ubuntu/.virtualenvs/venv/local/lib/python2.7/site-packages/werkzeug/utils.pyc'>
    ```
3. secure_filename    
    &emsp;&emsp;返回一个安全版本的文件名。    
    ```
    In [1]: from werkzeug import secure_filename

    In [2]: secure_filename('My cool movie.mov')
    Out[2]: 'My_cool_movie.mov'

    In [3]: secure_filename('../../../etc/passwd')
    Out[3]: 'etc_passwd'

    In [4]: secure_filename(u'i contain cool /xfcml/xe4uts.txt')
    Out[4]: 'i_contain_cool_xfcml_xe4uts.txt'
    ```


<br>
<br>

#### 4、密码加密
&emsp;&emsp;数据库中的重要字段（如密码）不能明文存储，需要加密之后存储。Web 开发常用到的方法是加盐哈希加密，也就是在加密时混入一段随机字符串（盐值， salt）再进行哈希加密（如 MD5、SHA1 等），这样即使密码相同，如果混入的盐值不同，那么哈希值也是不一样的。Werkzeug 中提供了密码加盐的哈希函数：     
```
In [1]: from werkzeug.security import generate_password_hash

In [2]: pw_1 = generate_password_hash('haauleon')

In [3]: pw_2 = generate_password_hash('haauleon')

In [4]: pw_1
Out[4]: 'pbkdf2:sha1:1000$AcopqCqB$50014045342e0c4d920104f9f2757b5c1c828c5d'

In [5]: pw_2
Out[5]: 'pbkdf2:sha1:1000$FcmmYxAj$4194d910ec59be2a7388b4729d4da3b154dd4401'
```

&emsp;&emsp;哈希之后的哈希字符串格式是 `method$salt$hash`，其中 1000 表示迭代次数，默认是 1000。由于盐值是随机的，同一个密码生成的哈希值不一样，因为不容易呗暴力破解。      

&emsp;&emsp;经过哈希之后的字符串是不能获取原密码的，只能使用 check_password_hash 来验证：     
```
In [6]: from werkzeug.security import check_password_hash

In [7]: check_password_hash(pw_1, 'haauleon')
Out[7]: True

In [8]: check_password_hash(pw_2, 'haauleon')
Out[8]: True

In [9]: check_password_hash(pw_2[:-1] + 'a', 'haauleon')
Out[9]: False
```

<br>

&emsp;&emsp;SQLAlchemy 记录密码的哈希值的方法如下，其中装饰器 hybrid_property 把 password 变成了一个混合属性，可以通过 user.password 属性来访问哈希的密码，也会在给 user.password 赋值的时候触发 password.setter：          
```python
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    __tablename__ = 'hashed_users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    _password = db.Column(db.String(256), nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        self._password = generate_password_hash(plaintext)

    def verify_password(self, password):
        return check_password_hash(self.password, password)
```

效果如下：    
```
In [1]: user = User(name='xiaoming', password='123')
In [2]: db.session.add(user)
In [3]: db.session.commit()

In [4]: print user.password
Out[4]:
pbkdf2:sha1:1000$HPqbW3Gt$59a167db9d008bdeb9bec1c20e5a0d8d50d01ccf

In [5]: print user.verify_password('223')
Out[5]:
False

In [6]: print user.verify_password('123')
Out[6]:
True
```

<br>
<br>

#### 5、中间件
&emsp;&emsp;中间件（Middleware）会对每次请求添加额外的处理。可以用来记录日志、会话管理、请求验证、性能分析等工作。Werkzeug 中提供了 10 个中间件，之前提到的 werkzeug.debug.DebuggedApplication 也是一个中间件。下面介绍几个常用的中间件。     

（1）SharedDataMiddleware     
&emsp;&emsp;一般而言，静态文件都应该使用 Nginx 来服务，但是在测试环境中或者对资源响应要求不高时，也可以使用 SharedDataMiddleware 来提供这样的服务，之前实现的文件托管服务也使用了它。使用示例如下：    
```python
# coding=utf-8
import os

from flask import Flask
from werkzeug.wsgi import SharedDataMiddleware

app = Flask(__name__)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/static/': os.path.join(os.path.dirname(__file__), 'static')
})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```

&emsp;&emsp;假设程序所在目录的 static 子目录下有一个叫作 main.js 的文件，可以使用 http://localhost:9000/static/main.js 来访问。    
```
(venv) ❯ http get http://127.0.0.1:9000/static/main.js
HTTP/1.0 200 OK
Cache-Control: max-age=43200, public
Content-Length: 0
Content-Type: application/javascript
Date: Sun, 25 Dec 2022 15:32:15 GMT
Etag: "wzsdm-1465692695-0-182321841"
Expires: Mon, 26 Dec 2022 03:32:15 GMT
Last-Modified: Sun, 12 Jun 2016 00:51:35 GMT
Server: Werkzeug/0.11.10 Python/2.7.11+
```

<br>

（2）ProfilerMiddleware    
&emsp;&emsp;可以很方便地使用 ProfilerMiddleware 添加性能分析。当请求页面的时候，就可以获得分析的结果。    

1. 以下代码不指定 profile_dir，则会在终端输出分析结果。     
    ```python
    # coding=utf-8
    from flask import Flask
    from werkzeug.contrib.profiler import ProfilerMiddleware

    app = Flask(__name__)
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app)


    @app.route('/')
    def hello():
        return 'Hello'


    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=9000)
    ```

    访问 http://127.0.0.1:9000/ 后，控制台输出到分析结果部分如下：    
    ```
    PATH: '/'
            322 function calls in 0.001 seconds

    Ordered by: internal time, call count

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            1    0.000    0.000    0.000    0.000 /home/ubuntu/.virtualenvs/venv/local/lib/python2.7/site-packages/werkzeug/routing.py:1243(bind_to_environ)
            1    0.000    0.000    0.000    0.000 /home/ubuntu/.virtualenvs/venv/local/lib/python2.7/site-packages/werkzeug/wrappers.py:756(__init__)
           10    0.000    0.000    0.000    0.000 /home/ubuntu/.virtualenvs/venv/local/lib/python2.7/site-packages/werkzeug/local.py:68(__getattr__)
           10    0.000    0.000    0.000    0.000 {method 'decode' of 'str' objects}
            6    0.000    0.000    0.000    0.000 /home/ubuntu/.virtualenvs/venv/local/lib/python2.7/site-packages/werkzeug/local.py:160(top)
            1    0.000    0.000    0.000    0.000 /home/ubuntu/.virtualenvs/venv/lib/python2.7/encodings/__init__.py:71(search_function)
            2    0.000    0.000    0.000    0.000 /home/ubuntu/.virtualenvs/venv/local/lib/python2.7/site-packages/werkzeug/datastructures.py:1145(set)
            1    0.000    0.000    0.000    0.000 /home/ubuntu/.virtualenvs/venv/local/lib/python2.7/site-packages/werkzeug/routing.py:1425(match)
            1    0.000    0.000    0.000    0.000 /home/ubuntu/.virtualenvs/venv/local/lib/python2.7/site-packages/werkzeug/wrappers.py:1086(get_wsgi_headers)
    ```
2. 指定 profile_dir 后，在访问页面之后，结果会被保存下来。     
    ```python
    # coding=utf-8
    from flask import Flask
    from werkzeug.contrib.profiler import ProfilerMiddleware

    app = Flask(__name__)
    app.wsgi_app = ProfilerMiddleware(app.wsgi_app, profile_dir='tmp')


    @app.route('/')
    def hello():
        return 'Hello'


    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=9000)
    ```
    tmp 目录保存到的文件如下：     
    ```
    (venv) ❯ ls -al tmp
    total 56
    drwxrwxr-x 2 ubuntu ubuntu  4096 Dec 25 15:44 .
    drwxrwxr-x 4 ubuntu ubuntu  4096 Dec 25 15:44 ..
    -rw-rw-r-- 1 ubuntu ubuntu 46729 Dec 25 15:44 GET.root.000000ms.1671983054.prof
    ```

<br>

（3）DispatcherMiddlerware    
&emsp;&emsp;DispatcherMiddlerware 是可以调度多个应用的中间件，现在利用 JSONResponse 实现如下功能：  
- 当访问以 /json 开头的地址时都默认自动用 jsonify 格式化。   
- 访问其他地址不受影响。    

代码实现如下：    
```python
# coding=utf-8
from collections import OrderedDict

from flask import Flask, jsonify
from werkzeug.wrappers import Response
from werkzeug.wsgi import DispatcherMiddleware

app = Flask(__name__)
json_page = Flask(__name__)


class JSONResponse(Response):
    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, dict):
            rv = jsonify(rv)
        return super(JSONResponse, cls).force_type(rv, environ)

json_page.response_class = JSONResponse


@json_page.route('/hello/')
def hello():
    return {'message': 'Hello World!'}


@app.route('/')
def index():
    return 'The index page'


app.wsgi_app = DispatcherMiddleware(app.wsgi_app, OrderedDict((
    ('/json', json_page),
)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```

访问结果如下：     
```
(venv) ❯ http get http://127.0.0.1:9000/hello/
HTTP/1.0 404 NOT FOUND
Content-Length: 233
Content-Type: text/html
Date: Sun, 25 Dec 2022 16:02:40 GMT
Server: Werkzeug/0.11.10 Python/2.7.11+

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>


(venv) ❯ http get http://127.0.0.1:9000/json/hello/
HTTP/1.0 200 OK
Content-Length: 32
Content-Type: application/json
Date: Sun, 25 Dec 2022 16:02:47 GMT
Server: Werkzeug/0.11.10 Python/2.7.11+

{
    "message": "Hello World!"
}
```

&emsp;&emsp;使用这个中间件对访问地址是有副作用的，`@json_page('/')` 等价于 `@app.route('/json/')`，也就是子路径的地址前面是有 /json 前缀的，这一点比较隐晦。