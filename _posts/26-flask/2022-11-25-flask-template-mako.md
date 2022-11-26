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
&emsp;&emsp;`%block` 和 `%def` 很像，它受 Jinja2 的 block 启发，在定义的地方被渲染，无须像 `%def` 那样当需要调用时才会被渲染。`%block` 也可以接收缓存、过滤器的参数：         
```
<html>
    <body>
        <%block cached="True" cache_timeout="60">
            This content will be cached for 60 seconds.
        </%block>
    </body>
</html>
```

&emsp;&emsp;还可以给代码块加个名字以便重复调用，以下代码中 pagecontrol 共渲染了两次：       
```
<div name="page">
    <%block name="pagecontrol">
        <a href="">previous page</a> |
        <a href="">next page</a>
    </%block>

    <table>
        ## some content
    </table>

    ${pagecontrol()}
</div>
```

<br>
<br>

#### 3、<%namespace>
&emsp;&emsp;`<%namespace>` 的作用很像 Python 的 import，可以把其他模板当成是 Python 模块一样引用进来。以下代码把模板文件 /utils.html 当作模块并导入 strftime 函数：        
```
<%namespace file="/utils.html" import="strftime"/>
```

&emsp;&emsp;导入 strftime 后就可以直接使用了：      
```
<h2>${strftime(datetime.now())}</h2>
```

&emsp;&emsp;import 支持 `*` 操作符（可能会影响性能，建议采用显示的 import）。     
```
<%namespace file="/utils.html" import="*"/>
```

&emsp;&emsp;file 参数还可以接收表达式，动态地传入文件名：     
```
<%namespace name="dyn" file="${context['namespace_name']}"/>
```

&emsp;&emsp;除了上面通过 `utils.strftime` 的方式调用，还可用以下两种方式调用：      
```
<%utils:strftime args='${datetime.now()}'/>
<%call expr='utils.strftime()' args='${datetime.now()}'></%call>
```

<br>
<br>

### 四、过滤器
&emsp;&emsp;Mako 模板中同样使用管道符号（`|`）把过滤器和变量分隔开，但需要注意的是，多个过滤器是用逗号（`,`）隔开。     
```
${ "this is some text" | u }
${ "<tag>some value</tag>" | h,trim }
```

<br>

#### 1、常用过滤器
&emsp;&emsp;Mako 中的常用过滤器包含以下 4 种：      
1. u: URL 的转换，等价于 `urllib.quote_plus(string.encode('utf-8'))`       
    ```
    In [3]: from mako.template import Template
    In [4]: Template('Hello ${ name | u}!').render(name='Haauleon')
    Out[4]: 
    u'Hello Haauleon!'
    In [5]: Template('Hello ${ name | u}!').render(name=u'小可爱')
    Out[5]: 
    u'Hello %E5%B0%8F%E5%8F%AF%E7%88%B1!'
    ```
2. h: HTML 转换，等价于 `markupsafe.escape(string)`，如果没有安装 markupsafe 模块则等价于 `cgi.escape(string, True)`       
    ```
    In [9]:  from mako.template import Template
    In [10]: Template('Hello ${ name|h }!').render(name='<div>&emsp;&emsp;</div>')
    Out[10]: 
    u'Hello &lt;div&gt;&amp;emsp;&amp;emsp;&lt;/div&gt;!'
    ```
3. trim: 过滤行首和行尾的空格，实际上是 `string.strip()`      
    ```
    In [13]: from mako.template import Template
    In [14]: Template('Hello ${ name|trim }!').render(name='       A B C        ')
    Out[14]: 
    u'Hello A B C!'
    ```
4. n: 禁用默认的过滤器       
    ```
    In [17]: from mako.template import Template
    In [18]: Template('Hello ${ name|n }!').render(name=' a &emsp; ')
    Out[18]: 
    u'Hello  a &emsp; !'
    ```

<br>
<br>

#### 2、定义一个过滤器
&emsp;&emsp;在 Mako 中定义一个过滤器非常简单，首先定义一个 mako 模板文件 my_filters.html 并写入以下内容：     
```
<%!
    def div(text):
        return "<div>" + text + "</div>"
%>

## 传固定值
Here's a div: ${ "ABC" | div }
## 需从外部传入参数 text 的值
Here's a div: ${ text | div }
```  

&emsp;&emsp;由于函数 div 需要传入参数 text，如果不传参则执行到 `Here's a div: ${ text | div }` 这一行的时候会报错。       
```
In [15]: from mako.lookup import TemplateLookup
In [16]: mylookup = TemplateLookup(directories=['templates/mako'])
In [17]: print(mylookup.get_template('my_filters.html').render(text='hello'))

Here's a div: <div>ABC</div>
Here's a div: <div>hello</div>
```

<br>
<br>

#### 3、指定全局的设置
&emsp;&emsp;还可以使用 default_filters 参数指定全局的设置。如果不指定，在 python2 中默认设置是 `['unicode']`，在 python3 中默认设置是 `['str']`。如以下代码已在 default_filters 中指定过滤器 `trim` 了，所以就不需要在模板中指定了。           
```
In [26]: from mako.lookup import TemplateLookup
In [27]: mylookup = TemplateLookup(directories=['templates/mako'], default_filters=['unicode', 'trim', 'decode.utf8'])
In [28]: print(mylookup.get_template('my_filters.html').render(text=u' 小可爱     '))

Here's a div: <div>ABC</div>
Here's a div: <div>小可爱</div>
```

<br>
<br>

#### 4、全局开启自定义过滤器
&emsp;&emsp;如果想要全局开启自定义的过滤器，需要使用以下方式：          
```
mylookup = Template(
    directories=['templates/mako'],
    default_filters=['str', 'myfilter'],
    imports=['from mypackage import myfilter']
)
```

&emsp;&emsp;Mako 模板编译完成后会生成这样的代码，截取片段如下：    
```python
# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1669345191.0
_enable_loop = True
_template_filename = 'templates/mako/hello.mako'
_template_uri = 'templates/mako/hello.mako'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        name = context.get('name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'Hello ')
        __M_writer(unicode(name))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()
```
&emsp;&emsp;render_body 是每个 Mako 模板编译完成之后生成的 Python 代码的主函数，渲染的时候就是通过调用它生成 HTML 代码的。过滤器的执行顺序和当时指定的顺序是一样的。      


<br>
<br>

### 五、模板继承
&emsp;&emsp;可以使用 Mako 的模板继承来生成和 Jinja2 一样的 HTML 页面。      

（1）第一步：定义基础的骨架模板 base.html      
```
<!DOCTYPE HTML>
<html lang="en">
    <head>
        <%block name="head">
            <link rel="stylesheet" href="style.css" />
            ## 此处没有使用 title() 而是使用了 self.title()
            ## 如果没有加 self，子模板继承后即便重写了 title 函数，在调用 parent.title() 时使用的还是原来 title 函数，造成子模板不能覆盖父模板的内容
            <title>${ self.title() } - My Webpage</title>
        </%block>
    </head>
    <body>
        <div id="content">
            <%block name="content"/>
        </div>
        <div id="footer">
            <%block name="footer"/>
        </div>
    </body>
</html>

<%def name="title()">
</%def>
```

<br>

（2）第二步：定义一个子模板 index.html      
```
<%inherit file="base.html"/>

<%def name="title()">Index</%def>

<%block name="head">
    ${ parent.head() }
    <style type="text/css">
        .important { color: #336699; }
    </style>
</%block>

<%block name="content">
    <h1>Index</h1>
    <p class="important">
        Welcome on my awesome homepage.
    </p>
</%block>
```

<br>

&emsp;&emsp;最终执行的子模板渲染效果如下：     
```
In [7]: from mako.lookup import TemplateLookup
In [8]: mylookup = TemplateLookup(directories=['templates/chapter3/section2/mako'])
In [9]: print(mylookup.get_template('index.html').render())

<!DOCTYPE HTML>
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


### 六、Mako 排错
&emsp;&emsp;Mako 有一个让人非常迷惑的地方，即出现 `NameError(NameError: Undefined)`，尤其在使用了模板多继承的情况下。举个例子，不小心在模板中使用了一个没有被定义的变量，渲染页面就会失败。    


<br>

#### 1、在终端打印编译内容
&emsp;&emsp;找到 Mako 源码中的 template.py 文件，在 _compile 这个函数结尾处添加两行打印输出。这样就可以在终端看到编译后的模板的内容，从而定位错误原因了。      
```python
def _compile(template, text, filename, generate_magic_comment):
    ...

    for index, s in enumerate(source.splitlines()):
        print index, s

    return source, lexer
```