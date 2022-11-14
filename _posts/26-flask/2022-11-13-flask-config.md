---
layout:        post
title:         "Flask Web | Flask 配置管理"
subtitle:      "适合设置选项很多且需要集中管理设置项的项目，通过三种方式加载配置文件"
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

### 配置变量
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

#### 1、Flask 内置配置变量
app.config 内置的全部配置变量可以参考：[官方文档](https://flask.palletsprojects.com/en/2.2.x/config/)