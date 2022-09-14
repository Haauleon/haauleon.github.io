---
layout:        post
title:         "Jmeter | 调试使用Badboy录制的脚本"
subtitle:      ""
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
---

### 一、背景
&emsp;&emsp;不推荐 Jmeter 原生录制方式，而是使用 Badboy 工具进行录制或者手工编写脚本，这里介绍一下使用 Badboy 工具录制完成的脚本如何进行调试。一般情况下，如果网站不需要登录状态就可以访问的话，基本脚本都可以回放成功。但是，如果网站需要登录状态才能访问，就会出现回放失败的问题，需要后期进行人工调试。       

<br>
<br>

### 二、脚本调试
1. 登录接口设置`自动重定向`     
2. 后面需要登录状态的接口设置`跟随重定向`       
3. 字符编码格式设置为`UTF-8`    
     
![](\img\in-post\post-jmeter\2022-09-14-jmeter-debug-1.jpg)       