---
layout:        post
title:         "Flask Web | 唯一 URL"
subtitle:      "Flask 的 URL 规则基于 Werkzeug 路由模块背后的思想即希望保证优雅且唯一的 URL"
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

### 一、验证 URL 的唯一性
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   

&emsp;&emsp;Flask 的 URL 规则基于 Werkzeug 的路由模块，这个模块背后的思想是基于 Apache 以及更早的 HTTP 服务器的主张，希望保证优雅且唯一的 URL。    

<br>

#### 1、文件夹路径 URL     
```python
# -*- coding: utf-8 -*-#
from flask import Flask

app = Flask(__name__)


@app.route('/index/')
def index():
    return 'Index Page'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
```

<br>

执行结果如下：     
&emsp;&emsp;上述 URL 路径很像一个文件系统中的文件夹路径。在浏览器窗口输入 `http://127.0.0.1:9000/index` 后会被重定向到带 `/` 的规范的 URL ``http://127.0.0.1:9000/index/` 上，这样有助于避免搜索引擎索引同一个页面两次。     

![](\img\in-post\post-flask\2022-11-16-flask-only-url-1.jpg)     

<br>
<br>

#### 2、文件路径 URL  
```python
# -*- coding: utf-8 -*-#
from flask import Flask

app = Flask(__name__)


@app.route('/home')
def home():
    return 'Home Page'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
```

<br>

执行结果如下：     
&emsp;&emsp;上述 URL 路径很像一个文件的路径。在浏览器窗口输入 `http://127.0.0.1:9000/home/` 后会产生一个 404（Not Found）错误。      

![](\img\in-post\post-flask\2022-11-16-flask-only-url-2.jpg) 