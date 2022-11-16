---
layout:        post
title:         "Flask Web | 构造 URL"
subtitle:      "选择构建 URL 而不是直接在代码中拼接 URL 的场景"
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
&emsp;&emsp;Flask 的 URL 规则基于 Werkzeug 的路由模块，这个模块背后的思想是基于 Apache 以及更早的 HTTP 服务器的主张，希望保证优雅且唯一的 URL。    

<br>

#### 1、文件夹路径 URL   