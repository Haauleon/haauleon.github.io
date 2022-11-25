---
layout:        post
title:         "Flask Web | Mako 模板语言"
subtitle:      "支持在模板中写几乎原生的 Python 语法的代码，对 Python 工程师非常友好"
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

### 一、Mako
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

> How fast is it?      
>  
> &emsp;&emsp;We really hate benchmarks especially since they don’t reflect much. The performance of a template depends on many factors and you would have to benchmark different engines in different situations. The benchmarks from the testsuite show that Jinja2 has a similar performance to Mako and is between 10 and 20 times faster than Django’s template engine or Genshi. These numbers should be taken with tons of salt as the benchmarks that took these numbers only test a few performance related situations such as looping. Generally speaking the performance of a template engine doesn’t matter much as the usual bottleneck in a web application is either the database or the application code.    

<br>

&emsp;&emsp;Mako 是除 Jinja2 外另一个知名的模板语言，[性能和 Jinja2 相近](https://jinja.palletsprojects.com/en/2.10.x/faq/#how-fast-is-it)，这点 Jinja2 也承认了。豆瓣几乎全部用户产品都是用 Mako 模板，它还是 Pylons 和 Pyramid 这两个 Web 框架内置的模板模板。Mako 支持在模板中写几乎原生的 Python 语法的代码，还自带了完整的缓存系统。      

&emsp;&emsp;跟 Jinja2 的设计不同之处在于：Jinja2 认为应该尽可能把逻辑从模板中移除，界面清晰，不允许在模板内写 Python 代码，也不支持全部的 Python 内置函数（只提供了很有限、最常用的一部分）；而 Mako 正好相反，它最后会编译成 Python 代码以达到性能最优，在模板里面可以自由写后端逻辑，不需要传递就可以使用 Python 自带的数据结构和内置类。       

&emsp;&emsp;Jinja2 带来的好处是模板引擎易于维护，并且模板有更好的可持续性；而 Mako 是一个对 Python 工程师非常友好的语言，限制很少，完成模板开发工作时更有效率，整个项目的代码可维护性更好。       

<br>

#### 1、安装 Mako
&emsp;&emsp;在 Flask 中使用 Mako 需要额外进行第三方包的安装。     
```
> pip install Mako==1.1.6
Collecting Mako==1.1.6
  Downloading https://files.pythonhosted.org/packages/b4/4d/e03d08f16ee10e688bde9016bc80af8b78c7f36a8b37c7194da48f72207e/Mako-1.1.6-py2.py3-none-any.whl (75kB)
    100% |████████████████████████████████| 81kB 751kB/s
Requirement already satisfied: MarkupSafe>=0.9.2 in d:\python27\lib\site-packages (from Mako==1.1.6)
Installing collected packages: Mako
Successfully installed Mako-1.1.6
```

<br>
<br>

### 二、基本 API 的使用
&emsp;&emsp;作为模板语言的 Mako，下面演示一下模板渲染和子模板渲染的基本用法。         

<br>

#### 1、模板渲染
&emsp;&emsp;Mako 的变量使用了 `${...}` 的风格，可以通过 Template 类创建一个模板实例并渲染它。       
```
In [1]: from mako.template import Template
In [2]: temp = Template('Hello ${name}!')
In [3]: temp.render(name='Haauleon')
Out[3]: 
u'Hello Haauleon!'
```

<br>
<br>

#### 2、单个模板文件渲染
&emsp;&emsp;模板文件后缀不强制以 `.mako` 结尾，使用 `.html` 甚至 `.txt` 都是可以接受的。      
```

```

<br>
<br>

#### 3、使用缓存


<br>
<br>

#### 4、继承(子)模板文件渲染


<br>
<br>