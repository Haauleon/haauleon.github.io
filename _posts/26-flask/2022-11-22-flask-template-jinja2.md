---
layout:        post
title:         "Flask Web | Jinja2"
subtitle:      "仿 Django 模板的一个模板引擎，速度快、提供沙箱模板"
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

### 一、Jinja2
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

&emsp;&emsp;Jinja2 是日本寺庙的意思，并且寺庙的英文 temple 和 template 的发音类似。       

&emsp;&emsp;Jinja2 是 Flask 默认的仿 Django 模板的一个模板引擎，由 Flask 的作者开发。它速度快，被广泛使用，并且提供了可选的沙箱模板来保证执行环境的安全。有以下优点：    
（1）让 HTML 设计者和后端 Python 开发工作分离。    
（2）减少使用 Python 的复杂程度，**页面逻辑应该独立于业务逻辑**，这样才能开发出易于维护的程序。    
（3）模板非常灵活、快速和安全，对设计者和开发者会更友好。    
（4）提供了控制语句、继承等高级功能，减少开发的复杂度。     

&emsp;&emsp;Jinja2 是 Flask 的一个依赖，安装 Flask 的同时 Flask 也随之安装。而 Jinja2 从 2.7 开始就已经依赖 MarkupSafe 了，MarkupSafe 的 C 实现要快得多。           
```
> pip install flask==0.11.1
> ...
> pip show flask
Name: Flask
Version: 0.11.1
Summary: A microframework based on Werkzeug, Jinja2 and good intentions
Home-page: http://github.com/pallets/flask/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD
Location: d:\python27\lib\site-packages
Requires: itsdangerous, click, Werkzeug, Jinja2
> ...
> pip show jinja2
Name: Jinja2
Version: 2.11.3
Summary: A very fast and expressive template engine.
Home-page: https://palletsprojects.com/p/jinja/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD-3-Clause
Location: d:\python27\lib\site-packages
Requires: MarkupSafe
Location: d:\python27\lib\site-packages 
> ...
> pip show MarkupSafe
Name: MarkupSafe
Version: 1.1.1
Summary: Safely add untrusted strings to HTML/XML markup.
Home-page: https://palletsprojects.com/p/markupsafe/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD-3-Clause
Location: d:\python27\lib\site-packages
Requires: 
```

<br>
<br>

### 二、API 的基本使用方式
#### 1、创建并渲染模板
（1）Jinja2 通过 Template 类创建并渲染模板       
&emsp;&emsp;以下代码片段可知，Jinja2.Template 和 [string.Template](https://haauleon.gitee.io/2022/11/22/flask-template/) 做的事情很像，都是使用 Template 类创建一个对象然后实例化。      
```
In[1]: from jinja2 import Template
In[2]: temp = Template('Hello {{ name }}')
In[3]: temp.render(name='haauleon')
Out[3]: 
u'Hello haauleon'
```

<br>

（2）使用 Environment 的实例来存储配置和全局对象   
&emsp;&emsp;以下代码片段可以解释上述使用 Jinja2.Template 代码片段的背后逻辑，这里使用了 jinja2.Environment 的实例 env 来存储配置和全局对象 temp，最后使用真实值进行替换。           
```
In[4]: from jinja2 import Environment
In[5]: env = Environment()
In[6]: temp = env.from_string('Hello {{ name }}')
In[7]: temp.render(name='Lily')
Out[7]: 
u'Hello Lily'
```

<br>
<br>

