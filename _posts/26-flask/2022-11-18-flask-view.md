---
layout:        post
title:         "Flask Web | 即插视图"
subtitle:      "使用基于类而不是绑定函数与URL关系(app.route)的通用视图方式来实现继承"
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

### 一、即插视图
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   

&emsp;&emsp;之前一直使用装饰器 app.route() 来绑定 URL 和视图函数的关系，将请求 URL 映射到对应的视图函数上来执行相应的代码。要知道函数是没有继承这一特性的，想要其他函数的功能基本只能复制粘贴，所以使用起来始终没那么方便。     

&emsp;&emsp;即插视图是使用视图功能的另一种方式，不同于函数的通用视图方式，它的灵感来自于 Django 的基于类，而这样的视图方式就可以支持类的继承这一特性，也便于代码后期维护。它有两种视图类型，分别是 `标准视图` 和 `基于调度方法的视图`。     

<br>

#### 1、标准视图
&emsp;&emsp;标准视图需要继承 flask.views.View，将类 UserView 使用 as_view 作为视图函数，设置一个视图函数名 userview 之后与 /users 的 URL 规则绑定在一起。基础类 BaseView 继承即插视图类 View 并实现自己的 dispatch_request 方法，在执行这个视图的时候会执行 dispatch_request 方法，这样就可以灵活运用这个特性。所以，使用标准视图时必须要自己实现 dispatch_request。       
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
&emsp;&emsp;app.add_url_rule 的作用跟 app.route 是一样的，都是用来绑定 URL 和视图函数的路由关系。