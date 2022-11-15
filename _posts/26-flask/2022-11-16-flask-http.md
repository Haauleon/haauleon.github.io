---
layout:        post
title:         "Flask Web | HTTP 方法"
subtitle:      "使用装饰器传参可以改变路由只回应 GET 请求的行为"
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

### 一、HTTP 方法
&emsp;&emsp;HTTP 有多个访问 URL 方法，默认情况下，路由只回应 GET 请求，但是通过 app.route 装饰器传递 methods 参数可以改变这个行为：      
```python

```