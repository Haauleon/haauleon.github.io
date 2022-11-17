---
layout:        post
title:         "Flask Web | 跳转和重定向"
subtitle:      "跳转（301）为页面被永久性移走，重定向（302）为页面暂时性转移"
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

### 一、跳转和重定向
&emsp;&emsp;在 Flask，跳转和重定向是通过 flask.redirect 实现的。      

<br>

#### 1、跳转
&emsp;&emsp;跳转（状态码 301）多用于旧网址在废弃前转向新网址以保证用户的访问，有页面被永久性移走的概念。      
```python
# -*- coding: utf-8 -*-#
from flask import Flask, redirect
app = Flask(__name__)


@app.route('/help2')
def help2():
    return 'Help2 Page'


@app.route('/help')
def help():
    """跳转"""
    return redirect('help2', code=301)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

```

执行结果如下：    
&emsp;&emsp;访问 `GET http://127.0.0.1:9000/help` 后页面会自动跳转至新的页面 `GET http://127.0.0.1:9000/help2`。        

![](\img\in-post\post-flask\2022-11-17-flask-1-url-redirect-1.jpg)

<br>
<br>

#### 2、重定向
&emsp;&emsp;重定向（状态码 302）表示页面是暂时性的转移，但是也不建议经常性使用重定向。     
```python
# -*- coding: utf-8 -*-#
from flask import Flask, url_for, redirect
app = Flask(__name__)


@app.route('/index2/')
def index2():
    return 'Index2 Page'


@app.route('/index/')
def index():
    """重定向"""
    return redirect(url_for('index2', id=2))  # redirect 的状态码 code 默认是 302，即重定向


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

```

执行结果如下：    
&emsp;&emsp;访问 `GET http://127.0.0.1:9000/index` 后页面会自动跳转至新的页面 `GET http://127.0.0.1:9000/index2/?id=2`。        

![](\img\in-post\post-flask\2022-11-17-flask-1-url-redirect-2.jpg)    

<br>

相关链接:     
1. [Flask 的 URL 规则希望保证唯一 URL](https://haauleon.gitee.io/2022/11/16/flask-only-url/)       
2. [使用 url_for 构建 URL 的原因](https://haauleon.gitee.io/2022/11/16/flask-structure-url/)

<br>
<br>

### 二、301 302 308 状态码
&emsp;&emsp;重定向还是有需要深入探讨的地方，返回码不仅有经常使用的 301、303 还有 302、307、308。它们之间有什么区别呢？可以按照 **是否缓存** 和 **重定向方法** 这两个维度去拆分。     

||**缓存（永久重定向）**|**不缓存（临时重定向）**|
|----|----|----|
|转GET|301|302、303|
|方法保持|308|307|

<br>

&emsp;&emsp;如果是永久重定向那么浏览器客户端就会缓存此次重定向结果，下次如果有请求则直接从缓存读取（除非清除浏览器缓存）。譬如我们切换域名，将所有老域名的流量转入新域名，可以使用永久重定向。        

&emsp;&emsp;如果只是临时重定向那么浏览器则不会缓存。譬如我们的服务临时升级，会使用临时重定向。       

&emsp;&emsp;方法保持的意思是原请求和重定向的请求是否使用相同的方法。譬如原请求是 POST 提交一个表单，如果是 301 重定向的话，重定向的请求会转为 GET 重新提交，如果是 308 则会保持原来 POST 请求不变。      

<br>

相关链接：      
[浅析 http 状态码 301、302、303、307、308 区别及对 SEO 优化网址 URL 劫持的影响](http://t.zoukankan.com/goloving-p-14087235.html)