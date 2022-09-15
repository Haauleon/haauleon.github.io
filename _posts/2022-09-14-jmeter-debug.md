---
layout:        post
title:         "Jmeter | 脚本调试总结"
subtitle:      "调试手工编写的需要登录状态的Jmeter脚本"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
---

### 一、背景
&emsp;&emsp;不推荐 Jmeter 原生录制方式，而是使用 Badboy 工具进行录制或者手工编写脚本，这里介绍一下需要登录状态的脚本如何进行调试。一般情况下，如果网站不需要登录状态就可以访问的话，基本脚本都可以回放成功。但是，如果网站需要登录状态才能访问，就会出现回放失败的问题，需要后期进行人工调试。       

<br>
<br>

### 二、脚本调试
1. 关于重定向    
    - 自动重定向（状态码一般是200、20X）：只针对GET和Head请求，自动重定向可以自动跳转到最终目标页面，jmeter不记录重定向过程内容,在查看结果树中只能看到重定向后的响应内容。             
    - 跟随重定向（状态码一般是302、30X）：自动重定向可以自动跳转到最终目标页面，jmeter记录重定向过程内容,在查看结果树中既能看到重定向后的响应内容，也能看到重定向前的响应内容。     
2. 添加`HTTP Cookie管理器`保持登录状态         
    在线程组添加`HTTP Cookie管理器`可以让 Jmeter 自动记录 Cookie 信息用来保持连接。        
    ![](\img\in-post\post-jmeter\2022-09-14-jmeter-debug-3.jpg)      
3. 字符编码格式设置为`UTF-8`        
    [Jmeter | 响应数据中文乱码](https://haauleon.gitee.io/2022/07/21/jmeter-utf8/)      
4. 添加信息头      
    根据实际情况在线程组中添加统一请求头，或者在单个请求中添加请求头。例如常见的`User-Agent`、`Accept`等等信息，这里统一添加。      
    ![](\img\in-post\post-jmeter\2022-09-14-jmeter-debug-1.jpg)         
5. 添加请求默认值     
    用于统一添加协议（HTTP/HTTPS）、HOST、IP，然后在后续的接口中只需要填写接口路径名即可。     
    ![](\img\in-post\post-jmeter\2022-09-14-jmeter-debug-2.jpg)      
6. 测试计划设置    
    ![](\img\in-post\post-jmeter\2022-09-14-jmeter-debug-4.jpg)     