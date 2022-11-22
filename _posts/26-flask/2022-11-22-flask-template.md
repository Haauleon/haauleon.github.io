---
layout:        post
title:         "Flask Web | 模板"
subtitle:      "使用 Python 自带的模板 string.Template"
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

### 模板
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

&emsp;&emsp;视图函数可以直接返回文本，而在实际生产环境中其实很少这样用，因为实际的页面（大众看到的页面）大多是带有样式和复杂逻辑的 HTML 代码，这可以让浏览器渲染出非常漂亮和复杂的效果，而不仅仅是简单的文本。     

&emsp;&emsp;页面内容应该是可重用的，因为这对于一个视觉效果还不错的网站而言拥有统一的页头和页尾会显得整齐和统一，除此之外还需要执行更高级的功能。      

&emsp;&emsp;Python 自带的模板 string.Template 提供的功能如下：        
1. 模板求值      
    使用 $ 表示可赋值变量，使用 string.Template 类进行实例化，在调用 substitute() 时可使用关键字传参进行真实值的替换。      
    ```
    Out[1]: from string import Template
    Out[2]: x = Template('$name, $age years old')
    Out[3]: x.substitute(name='haauleon', age=18)
    Out[3]: 
    'haauleon, 18 years old'
    ```
2. 