---
layout:        post
title:         "Flask Web | 子域名"
subtitle:      "借助 subdomain 实现 Saas 应用为用户提供一个子域名来访问"
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

#### 1、背景