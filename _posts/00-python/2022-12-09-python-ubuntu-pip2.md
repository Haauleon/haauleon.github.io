---
layout:        post
title:         "环境搭建 | Ubuntu20.04 安装 pip2"
subtitle:      "Ubuntu20.04 安装 python2.7 对应版本的 pip9.0.3"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 操作系统
    - Ubuntu
    - Web开发
---

> 本篇所有操作均在基于 Ubuntu20.04 的环境下完成 

<br>
<br>

### 一、背景
&emsp;&emsp;Ubuntu 20.04 LTS 已经移除 Python2，默认安装 python3，但是很多时候还是会经常用到 python2.7 版本，这里首先单独安装 python2.7，然后指定版本安装 pip2==9.0.3。   

<br>
<br>

### 二、操作步骤
###### 1、python2.7   
使用命令：    
```
> sudo apt install python2
> python2 --version
Python 2.7.18
```

<br>
<br>

###### 2、安装pip
```
> sudo apt-get update
> sudo apt-get install curl  # 安装curl下载工具
> sudo curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py  # 下载安装脚本
> sudo python get-pip.py  # 运行安装脚本
> sudo pip2 install pip==9.0.3  # 安装需要的pip版本
> pip2 --version
pip 9.0.3 from /usr/local/lib/python2.7/dist-packages (python 2.7)
```