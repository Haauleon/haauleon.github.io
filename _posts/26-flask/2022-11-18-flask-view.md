---
layout:        post
title:         "Flask Web | 即插视图"
subtitle:      "使用基于类而不是绑定函数与URL关系(app.route)的通用视图方式来实现继承"
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

### 一、即插视图
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   

&emsp;&emsp;之前一直使用装饰器 app.route() 来绑定 URL 和视图函数的关系，将请求 URL 映射到对应的视图函数上来执行相应的代码。要知道函数是没有继承这一特性的，想要其他函数的功能基本只能复制粘贴，所以使用起来始终没那么方便。     

&emsp;&emsp;即插视图是使用视图功能的另一种方式，不同于函数的通用视图方式，它的灵感来自于 Django 的基于类，而这样的视图方式就可以支持类的继承这一特性，也便于代码后期维护。它有两种视图类型，分别是 `标准视图` 和 `基于调度方法的视图`。     

<br>
<br>

### 二、标准视图
&emsp;&emsp;标准视图需要继承 flask.views.View，将类 UserView 使用 as_view 作为视图函数，设置一个视图函数名 userview 之后与 /users 的 URL 规则绑定在一起。基础类 BaseView 继承即插视图类 View 并实现自己的 dispatch_request 方法，在执行这个视图的时候会执行 dispatch_request 方法，这样就可以灵活运用这个特性。所以，使用标准视图时必须要自己实现 dispatch_request。          

模板文件 chapter3/section1/users.html 的内容如下：    
```
{% for user in users %}
<p>{{ user.username }}</p>
<img src="{{ user.avatar }}"></img>
{% endfor %}
```

执行文件的内容如下：      
```python
# coding=utf-8
from flask import Flask, request, render_template
from flask.views import View

app = Flask(__name__, template_folder='../../templates')


class BaseView(View):
    def get_template_name(self):
        raise NotImplementedError()

    def render_template(self, context):
        return render_template(self.get_template_name(), **context)

    def get_users(self):
        pass

    def dispatch_request(self):
        if request.method != 'GET':
            return 'UNSUPPORTED!'
        context = {'users': self.get_users()}
        return self.render_template(context)


class UserView(BaseView):

    def get_template_name(self):
        return 'chapter3/section1/users.html'

    def get_users(self):
        return [{
            'username': 'fake',
            'avatar': 'https://gfs17.gomein.net.cn/T1ATE5BTJv1RCvBVdK_450.jpg'
        },
            {
                'username': 'niko',
                'avatar': 'https://gfs17.gomein.net.cn/T1ATE5BTJv1RCvBVdK_450.jpg'
            }
        ]


app.add_url_rule('/users', view_func=UserView.as_view('userview'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
```

访问 GET http://127.0.0.1:3000/users 的执行结果如下：          
```
HTTP/1.0 200 OK
Content-Length: 172
Content-Type: text/html; charset=utf-8
Date: Fri, 18 Nov 2022 08:33:57 GMT
Server: Werkzeug/0.11.10 Python/2.7.11

<p>fake</p>
<img src="https://gfs17.gomein.net.cn/T1ATE5BTJv1RCvBVdK_450.jpg"></img>

<p>niko</p>
<img src="https://gfs17.gomein.net.cn/T1ATE5BTJv1RCvBVdK_450.jpg"></img>
```


<br>

代码解析：      
（1）      
```python
from flask import Flask, request, render_template
```
&emsp;&emsp;flask.render_template 用来渲染模板文件夹中的模板，因此需要设置模板文件夹的路径。      

（2）      
```python
from flask.views import View
```
&emsp;&emsp;标准视图需要继承 View 类来实现 dispatch_request 方法，该方法相当于视图函数代码块会被执行。     

（3）     
```python
app = Flask(__name__, template_folder='../../templates')
```
&emsp;&emsp;通过 template_folder 设置模板文件夹的存放路径，此处使用相对于当前文件所在位置的相对路径。     

（4）     
```python
class BaseView(View):
    ......

    def dispatch_request(self):
        if request.method != 'GET':
            return 'UNSUPPORTED!'
        context = {'users': self.get_users()}
        return self.render_template(context)
```
&emsp;&emsp;dispatch_request 方法的代码块，会被 app.add_url_rule 用来与 URL 绑定在一起，访问 URL 就会执行此代码块。       

（5）      
```python
app.add_url_rule('/users', view_func=UserView.as_view('userview'))
```
&emsp;&emsp;app.add_url_rule 的作用跟 app.route 是一样的，都是用来绑定 URL 和视图函数的路由关系，这里就是将 /users （自定义的 URL）和 userview （自定义的函数名）绑定在一起。    

<br>
<br>

### 三、基于调度方法的视图
&emsp;&emsp;flask.views.MethodView 对每个 HTTP 方法执行不同的函数（映射到对应方法的小写的同名方法上），如实现了 get() 方法，则在发送 GET 请求时将会执行 get() 方法的代码块，这对 RESTful API 尤其有用。这里没有重写 dispatch_request 方法，意味着会调用继承自 MethodView 的 dispatch_request 方法，在请求指定的 HTTP 方法时执行对应的函数。            
```python
# coding=utf-8
from flask import Flask, jsonify
from flask.views import MethodView

app = Flask(__name__)


class UserAPI(MethodView):

    def get(self):
        return jsonify({
            'username': 'fake',
            'avatar': 'https://gfs17.gomein.net.cn/T1ATE5BTJv1RCvBVdK_450.jpg'
        })

    def post(self):
        return 'UNSUPPORTED!'


app.add_url_rule('/user', view_func=UserAPI.as_view('userview'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

<br>

执行结果如下：    
1. 访问 GET HTTP://127.0.0.1:5000/user        
    ```
    HTTP/1.0 200 OK
    Content-Length: 172
    Content-Type: text/html; charset=utf-8
    Date: Fri, 18 Nov 2022 08:33:57 GMT
    Server: Werkzeug/0.11.10 Python/2.7.11

    <p>fake</p>
    <img src="https://gfs17.gomein.net.cn/T1ATE5BTJv1RCvBVdK_450.jpg"></img>

    <p>niko</p>
    <img src="https://gfs17.gomein.net.cn/T1ATE5BTJv1RCvBVdK_450.jpg"></img>
    ```
2. 访问 POST HTTP://127.0.0.1:5000/user      
    ```
    HTTP/1.0 200 OK
    Content-Type: text/html; charset=utf-8
    Date: Fri, 18 Nov 2022 09:47:56 GMT
    Server: Werkzeug/0.11.10 Python/2.7.11

    UNSUPPORTED!
    ```

<br>

相关链接：    
[flask 即插视图(Pluggable Views) 和 endpoint](https://www.cnblogs.com/piperck/p/6060505.html)

<br>

#### 1、对视图的装饰
###### （1）装饰 as_view 的返回值
&emsp;&emsp;通过装饰 as_view 的返回值来实现对视图的装饰功能，常用于权限的检查、登录验证等。     
```python
# coding=utf-8
from flask import Flask, jsonify, abort
from flask.views import MethodView

app = Flask(__name__)


def user_required(f):
    """定义一个装饰器用来装饰视图"""

    def decorator(*args, **kwargs):
        if not g.user:
            abort(401)
        return f(*args, **kwargs)

    return decorator


class UserAPI(MethodView):

    def get(self):
        return jsonify({
            'username': 'fake',
            'avatar': 'https://gfs17.gomein.net.cn/T1ATE5BTJv1RCvBVdK_450.jpg'
        })

    def post(self):
        return 'UNSUPPORTED!'


view = user_required(UserAPI.as_view('users'))  # 装饰 as_view 的返回值来实现对视图的装饰功能
app.add_url_rule('/users/', view_func=view)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

<br>
<br>

###### （2）添加 decorator 属性
&emsp;&emsp;从 Flask 0.8 开始，还可以通过在继承 MethodView 的类中添加 decorator 属性来实现对视图的装饰。      
```python
# coding=utf-8
from flask import Flask, jsonify, abort
from flask.views import MethodView

app = Flask(__name__)


def user_required(f):
    """定义一个装饰器用来装饰视图"""

    def decorator(*args, **kwargs):
        if not g.user:
            abort(401)
        return f(*args, **kwargs)

    return decorator


class UserAPI(MethodView):
    decorator = [user_required]  # 在继承 MethodView 的类中添加 decorator 属性来实现对视图的装饰

    def get(self):
        return jsonify({
            'username': 'fake',
            'avatar': 'https://gfs17.gomein.net.cn/T1ATE5BTJv1RCvBVdK_450.jpg'
        })

    def post(self):
        return 'UNSUPPORTED!'


app.add_url_rule('/users/', view_func=UserAPI.as_view('users'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

<br>

相关链接：    
[关于 Flask 高级视图 —— 装饰器修饰视图的方法](https://blog.csdn.net/qq_55961861/article/details/126538113)