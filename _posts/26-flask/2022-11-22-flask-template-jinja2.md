---
layout:        post
title:         "Flask Web | Jinja2 模板语言"
subtitle:      "Flask 默认的仿 Django 模板的一个模板引擎，速度快、提供沙箱模板"
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
werkzeug==0.11.10       

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

### 二、基本 API 的使用
#### 1、创建并渲染模板
（1）Jinja2 通过 Template 类创建并渲染模板       
&emsp;&emsp;以下代码片段可知，Jinja2.Template 和 [string.Template](https://haauleon.gitee.io/2022/11/22/flask-template/) 做的事情很像，都是使用 Template 类创建一个对象然后实例化。      
```
In [1]: from jinja2 import Template
In [2]: temp = Template('Hello {{ name }}')
In [3]: temp.render(name='haauleon')
Out[3]: 
u'Hello haauleon'
```

<br>

（2）使用 Environment 的实例来存储配置和全局对象   
&emsp;&emsp;以下代码片段可以解释上述使用 Jinja2.Template 代码片段的背后逻辑，这里使用了 jinja2.Environment 的实例 env 来存储配置和全局对象 temp，最后使用真实值进行替换。           
```
In [4]: from jinja2 import Environment
In [5]: env = Environment()
In [6]: temp = env.from_string('Hello {{ name }}')
In [7]: temp.render(name='Lily')
Out[7]: 
u'Hello Lily'
```

<br>
<br>

#### 2、使用模板加载器
1. 先创建一个模板，并写入内容     
    ```
    > echo 'Hello {{ name }}' > templates/jinja2/hello.html
    ```
2. 再创建一个文件，用于加载模板文件     
    ```
    > touch app.py
    ```
3. 在 app.py 文件中加载指定位置的模板文件 hello.html     
    &emsp;&emsp;以下代码中 Environment 的实例用于存储配置和全局对象，然后从文件系统或其他指定位置加载模板。
    ```
    In [8]: from jinja2 import Environment, PackageLoader
    In [9]: env = Environment(loader=PackageLoader('app', 'templates/jinja2'))
    In [10]: temp = env.get_template('hello.html')
    In [11]: temp.render(name='haauleon')
    Out[11]: 
    u'Hello haauleon'
    ```
    &emsp;&emsp;通过 Environment 创建了一个模板环境，模板加载器（loader）会在 templates 文件夹中寻找对应的模板文件。由于模板文件在模板目录的子目录 jinja2/ 下，所以代码也可以这么写：    
    ```
    In [12]: from jinja2 import Environment, PackageLoader
    In [13]: env = Environment(loader=PackageLoader('app', 'templates'))
    In [14]: temp = env.get_template('jinja2/hello.html')
    In [15]: temp.render(name='haauleon')
    Out[15]: 
    u'Hello haauleon'
    ```

<br>

&emsp;&emsp;使用模板加载器的另一个明显的好处就是可以支持 **模板继承**。     

<br>
<br>

### 三、Jinja2 的基本语法
&emsp;&emsp;模板仅仅是文本文件，它可以使用任何基于文本的格式（HTML、XML、CSV、LaTex 等），它没有特定的扩展名，通常使用 `.html` 作为后缀名。     

&emsp;&emsp;模板包含 “变量” 或 “表达式”，这两者在模板求值的时候会被替换为真实值。除此之外，模板中还有标签和控制语句。      
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-1.jpg)       
<br>

在 ipython 控制台输入以下语句执行：     
```
In [38]: from jinja2 import Environment, PackageLoader
In [39]: env = Environment(loader=PackageLoader('app', 'templates'))
In [40]: temp = env.get_template('/jinja2/simple.html')
In [41]: print(temp.render(items=[{'href': 'http://happy123.com', 'caption': 'happy123'}], title=' happy 123 456 ', content='This is a test template'))
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Simple Page</title>
</head>
<body>
    <ul id="navigation">
            <li>
                <a href="http://happy123.com">happy123</a>
            </li>
    </ul>
    <h1>happy 123 456</h1>
    <p>This is a test template</p>
</body>
</html>
```

<br>
<br>

以上模板的解析如下：   
（1）`<!DOCTYPE html>`        
&emsp;&emsp;声明文档类型是 HTML5。      

（2）      
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-2.jpg)        
&emsp;&emsp;上面是三种分隔符，每种分隔符都包含开始标记和结束标记。一对 `{}` 和一对 `#` 的组合是模板注释，不会出现在渲染的页面里，是给程序员看的。一对 `{}` 和一对 `%` 的组合用于执行诸如 for 循环或者赋值的语句。两对 `{}` 用于把表达式的结果输出到模板上，即最终将使用真实值进行替换。      

（3）       
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-3.jpg)    
&emsp;&emsp;此处的 for 循环，这种控制结构的代码块都需要以 `{endxxx}` 作为结束标志。      

（4）      
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-4.jpg)           
&emsp;&emsp;应用把变量传递到模板，可以使用点（`.`）来访问变量的属性，也可以使用中括号语法（`[]`）。下面两行的效果几乎是一样的：        
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-6.jpg)      

（5）     
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-5.jpg)         
&emsp;&emsp;trim 是一个过滤器，在模板中通过管道符（`|`）把变量和过滤器分开。也可以连续使用多个过滤器，多个过滤器之间也通过管道符隔开。       

<br>
<br>

### 四、Jinja2 的高级用法      
#### 1、使用过滤器
&emsp;&emsp;Jinja2 内置了很多非常多的[过滤器](https://jinja.palletsprojects.com/en/2.11.x/templates/#builtin-filters)，需要熟悉这些过滤器，大多在工作中都很常用。

<br>
<br>

#### 2、模板继承
&emsp;&emsp;使用模板继承，能使得模板重用，提高工作效率和代码质量。如果无法重用，那么编写的模板只是一次性的死模板，用完即弃，造成资源浪费。模板继承的前提是先定义一个基础的 “骨架” 模板，让后面的子模板去继承这个基础模板。        

（1）第一步：先定义一个基础的 “骨架” 模板 base.html          
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-7.jpg)        

&emsp;&emsp;如上图，在以上这能被重载的三个代码块 head、content 和 footer 中，head 代码块是有默认内容的，所以该基类模板在被子模板继承时，如果子模板没有重载该 head 代码块的内容，那么就会显示该基类模板的 head 代码块的默认内容。

<br>

（2）第二步：接着定义一个子模板 index.html       
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-8.jpg)         

&emsp;&emsp;如果想多次使用同一个块，可以使用特殊的 `self` 变量并调用与块同名的函数：       
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-9.jpg)       

<br>

打开 Python 控制台，看看 index.html 模板渲染后的最终效果：       
```
In[12]: from jinja2 import Environment, PackageLoader
In[13]: env = Environment(loader=PackageLoader('app', 'templates/jinja2'))
In[14]: template = env.get_template('index.html')
In[15]: print(template.render())
<!DOCTYPE html>
<html lang="en">
    <head>
        <link rel="stylesheet" href="style.css" />
        <title>Index - My Webpage</title>
        <style type="text/css">
            .important { color: #336699; }
        </style>
    </head>
    <body>
        <div id="content">
        <h1>Index</h1>
        <p class="important">
            Welcome on my awesome homepage.
        </p>
        </div>
        <div id="footer">
        </div>
    </body>
</html>
```

<br>
<br>

#### 3、宏
&emsp;&emsp;宏类似于常规编程中的函数，它用于把常用行为抽象为可重用的函数，可以被多次调用。     
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-10.jpg)       

<br>
<br>

#### 4、赋值
&emsp;&emsp;在代码块中，可以为变量赋值。赋值使用 set 标签，并且可以为多个变量赋值。      
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-11.jpg)     

<br>
<br>

#### 5、include 语句
&emsp;&emsp;include 语句用于包含一个模板，渲染时会在 include 语句的对应位置添加被包含的模板内容。可以使用 `ignore missiong` 标记，如果模板不存在，Jinja 就会忽略这条语句。       
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-12.jpg)     

<br>
<br>

#### 6、import 语句
&emsp;&emsp;Jinja2 支持在不同的模板中导入宏并使用，与 Python 中的 import 语句类似。有两种方式来导入模板：       
1. 可以把整个模板导入到一个变量中      
    ```
    import xxx.html
    ```
2. 从已导入模板中导入特定的宏     
    ```
    from xxx.html import macro1, macro2
    ```

<br>

（1）第一步：先定义一个宏模板 macro.html      
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-13.jpg)     


<br>

（2）第二步：再定义一个模板来引用并调用宏模板中的宏 hello_macro.html     
![](\img\in-post\post-flask\2022-11-22-flask-template-jinja2-14.jpg)     

<br>

打开 Python 控制台，看看 hello_macro.html 模板渲染后的最终效果：       
```
In[19]: from jinja2 import FileSystemLoader, Environment
In[20]: from datetime import datetime
In[21]: loader = FileSystemLoader('templates/jinja2')
In[22]: template = Environment(loader=loader).get_template('hello_macro.html')
In[23]: print(template.render(time=datetime.now()))
<p>
    Hello world
</p>
<p>
    2022-11-24 11:48:52
</p>
```