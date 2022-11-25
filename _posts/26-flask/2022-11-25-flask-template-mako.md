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
&emsp;&emsp;作为模板语言的 Mako，下面演示一下模板渲染和子模板文件渲染的基本用法。         

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

（1）第一步：定义模板文件 templates/mako/hello.mako 并写入以下内容       
```
Hello ${name}
```

<br>

（2）第二步：打开 Python 控制台，渲染此模板文件        
```
In [5]: from mako.template import Template
In [6]: Template(filename='templates/mako/hello.mako').render(name='Lily')
Out[6]: 
u'Hello Lily\n'
```   

<br>
<br>

#### 3、生成和使用缓存
&emsp;&emsp;Mako 自带了缓存系统，所以可以优化一下性能，保存编译后的模板，待下次有参数相同的调用就能直接使用缓存结果。        

（1）第一步：定义模板文件 templates/mako/hello.mako 并写入以下内容       
```
Hello ${name}
```

<br>

（2）第二步：在项目主路径下设置缓存文件夹 tmp/mako_cache      
```
In [13]: from mako.template import Template
In [14]: Template(filename='templates/mako/hello.mako', module_directory='tmp/mako_cache').render(name='Micky')
Out[14]: 
u'Hello Micky\n'
```

&emsp;&emsp;执行完成后将会在当前项目主路径下生成一个 tmp/mako_cache 的缓存目录，而生成的缓存文件则按照模板路径的结构进行保存。例如模板路径是 templates/mako/hello.mako，而设置的缓存目录是 tmp/mako_cache，那么最终生成的缓存文件路径是 tmp/mako_cache/templates/mako/hello.pyc，如下所示。      
```
haauleon@LAPTOP-EA7BF21I:/mnt/d/gitee/web_develop$ ls -al tmp/mako_cache
total 0
drwxrwxrwx 1 haauleon haauleon 4096 Nov 25 10:59 .
drwxrwxrwx 1 haauleon haauleon 4096 Nov 25 10:59 ..
drwxrwxrwx 1 haauleon haauleon 4096 Nov 25 10:59 templates
haauleon@LAPTOP-EA7BF21I:/mnt/d/gitee/web_develop$ tree tmp/mako_cache
tmp/mako_cache
└── templates
        └── mako
            ├── hello.mako.py
            └── hello.mako.pyc

2 directories, 2 files
```

<br>
<br>

#### 4、子模板文件渲染
&emsp;&emsp;除了单个模板文件的渲染之外，倘若存在模板继承或者模板引用了其他模板的情况时，就需要渲染子模板文件，这里使用类 TemplateLookup 告诉 Mako 要搜索的基类模板的路径。                   

**方式一：通过 Template.render() 进行渲染**       
```
In [13]: from mako.lookup import TemplateLookup  # 导入搜索模板类
In [14]: from mako.template import Template      # 导入模板类
In [15]: mylookup = TemplateLookup(directories=['templates/mako'])          # 设置要搜索的模板的目录路径   
In [16]: temp = Template('<%include file="hello.mako"/>', lookup=mylookup)  # include 标签包含 hello.mako 的模板内容，lookup= 的参数是基类模板所在的目录路径
In [17]: temp.render(name='Corilin')             # 模板渲染
Out[17]: 
u'Hello Corilin\n'
```

<br>

**方式二：通过 TemplateLookup.get_template.render() 进行渲染**      
```
In [3]: from mako.lookup import TemplateLookup
In [4]: mylookup = TemplateLookup(directories=['templates/mako'])
In [5]: mylookup.get_template('hello.mako').render(name='Cindy')
Out[5]: 
u'Hello Cindy\n'
```

<br>

**方式三：TemplateLookup 同样支持 module_directory 参数**                 
```
In [9]:  from mako.lookup import TemplateLookup
In [10]: mylookup = TemplateLookup(directories=['templates/mako'], module_directory='tmp/mako2_cache')
In [11]: mylookup.get_template('hello.mako').render(name='Dibby')
Out[11]: 
u'Hello Dibby\n'
```

<br>

**方式四：使用相对路径渲染模板文件**          
&emsp;&emsp;模板名称 /hello.mako 以 `/` 开头，是因为搜索目录 directories 已经被包含在内了，使用 `/` 仅表示相对路径。      
```
In [12]: from mako.lookup import TemplateLookup
In [13]: mylookup = TemplateLookup(directories=['templates/mako'])
In [14]: mylookup.get_template('/hello.mako').render(name='Vivian')
Out[14]: 
u'Hello Vivian\n'
```

<br>
<br>

### 三、Mako 的基本语法
![](\img\in-post\post-flask\2022-11-25-flask-template-mako-1.jpg)   

<br>

#### 1、<%page>
&emsp;&emsp;上图的 `<%include...>` 并没有带参数，nav.html 里面只要用 `<%page/>` 即可，当需要传参的时候这样使用：      
```
<%page args="x, y, z='default'"/>
``` 

&emsp;&emsp;插入模板的语法如下：     
```
<%namespace name="utils" file="/utils.html" args="1, 2, z='z'"/>
```

&emsp;&emsp;还可以指定缓存方式：      
```
<%page cached="True" cache_type="memory"/>
```

<br>
<br>

#### 2、<%block>



<br>
<br>

#### 3、<%namespace>





<br>
<br>

### 四、Mako 的高级用法
#### 1、过滤器


<br>
<br>

#### 2、模板继承


<br>
<br>


#### 3、Mako 排错