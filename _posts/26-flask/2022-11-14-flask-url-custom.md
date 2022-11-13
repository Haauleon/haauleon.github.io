---
layout:        post
title:         "Flask Web | 自定义 URL 转换器"
subtitle:      "自定义一个转换器实现设置使用的分隔符"
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

### 自定义 URL 转换器
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.12.1           

```
❯ python --version
Python 2.7.11+

~/web_develop master* ⇣ ubuntu@WEB
❯ pip --version
pip 9.0.3 from /usr/local/lib/python2.7/dist-packages (python 2.7)

~/web_develop master* ⇣ ubuntu@WEB
❯ pip show Flask
Name: Flask
Version: 0.12.1
Summary: A microframework based on Werkzeug, Jinja2 and good intentions
Home-page: http://github.com/pallets/flask/
Author: Armin Ronacher
Author-email: armin.ronacher@active-4.com
License: BSD
Location: /usr/local/lib/python2.7/dist-packages
Requires: itsdangerous, click, Werkzeug, Jinja2
```

<br>

#### 1、