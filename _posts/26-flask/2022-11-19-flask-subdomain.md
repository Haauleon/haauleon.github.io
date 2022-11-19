---
layout:        post
title:         "Flask Web | 子域名"
subtitle:      "借助 subdomain 实现 SaaS 应用为用户提供一个子域名来访问"
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

### 一、子域名
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

&emsp;&emsp;现在许多 SaaS 应用为用户提供一个子域名来访问，可以借助 subdomain 来实现同样的功能。代码如下：      
```python
# coding=utf-8
from flask import Flask, g

app = Flask(__name__)
app.config['SERVER_NAME'] = 'example.com:9000'  # 配置文件 app.config['SERVER_NAME'] 可以自定义


@app.url_value_preprocessor
def get_site(endpoint, values):
    g.site = values.pop('subdomain')


@app.route('/', subdomain='<subdomain>')
def index():
    return g.site


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```

&emsp;&emsp;然后在虚拟机上绑定一下域名，也就是配置 host 文件。host 文件路径在 /etc/hosts，在文件的最后添加上一行：       
```
127.0.0.1 a.example.com b.example.com
```

&emsp;&emsp;配置保存后 a.example.com 和 b.example.com 这两个子域名都可以映射到 127.0.0.1 上，都可以进行访问。需要注意的是，子域名不能在 127.0.0.1 上出现，也不能在 localhost 上出现。执行该程序后，现在打开一个新的终端来验证一下：        
```
(venv) ❯ http http://b.example.com:4000
HTTP/1.0 200 OK
Content-Length: 1
Content-Type: text/html; charset=utf-8
Date: Sat, 19 Nov 2022 16:06:10 GMT
Server: Werkzeug/0.11.10 Python/2.7.11+

b
```

<br>
<br>

相关链接：     
[flask —— windows 系统下实现子域名](https://blog.csdn.net/yuaicsdn/article/details/109465084)