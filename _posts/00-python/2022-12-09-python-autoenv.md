---
layout:        post
title:         "环境搭建 | 快速激活虚拟环境"
subtitle:      "virtualenv + autoenv 实现切换工程目录时自动激活虚拟环境"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - Ubuntu
    - Web开发
---

> 本篇所有操作均在基于 ubuntu==20.04，python==2.7.11+ 且 pip==9.0.3 的环境下完成 

<br>
<br>

### 一、背景
&emsp;&emsp;虚拟环境可以达到项目环境隔离的效果，为了免去进入工程项目后还要手动激动虚拟环境，这里使用 autoenv 实现在切换目录的同时自动激活该项目的虚拟环境。  

<br>
<br>

### 二、环境配置
以项目 flask_web 为例。      

<br>

#### 1、安装 autoenv
```
> sudo pip2 install virtualenv
> sudo pip2 install autoenv
> source /usr/local/bin/activate.sh
```

<br>
<br>

#### 2、创建虚拟环境 venv
```
> cd flask_web
> virtualenv venv
```

#### 2、配置 .env 文件
```
> cd flask_web
> touch .env
> echo "source /mnt/d/gitee/flask_web/venv/bin/activate" > .env  # 需要使用 activate 所在的完整路径
```

<br>
<br>

#### 3、效果演示
```
> cd ..
> cd flask_web
You must source this script: $ source /mnt/d/gitee/flask_web/venv/bin/activate
autoenv:
autoenv: WARNING:
autoenv: This is the first time you are about to source /mnt/d/gitee/flask_web/.env:      
autoenv:
autoenv:     --- (begin contents) ---------------------------------------
autoenv:     source /mnt/d/gitee/flask_web/venv/bin/activate
autoenv:
autoenv:     --- (end contents) -----------------------------------------
autoenv:
autoenv: Are you sure you want to allow this? (y/N) y
(venv) haauleon@LAPTOP-EA7BF21I:/mnt/d/flask_web$
```