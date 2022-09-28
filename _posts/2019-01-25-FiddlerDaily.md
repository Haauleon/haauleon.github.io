---
layout:        post
title:         "Fiddler 日常使用小技巧"
subtitle:      'Fiddler 实用技巧 2'
author:        "Haauleon"
header-style:  text
tags:
  - Fiddler
---

### 一、Fiddler工作原理
> 浏览器 > WinNet > Fiddler > Web Server，打开 Fiddler 后它会自动修改注册表，所有请求、相应都经过 Fiddler，关闭后会自动从注册表中移除，减少资源浪费。

<br>
<br>

### 二、常用功能
###### 1、请求和响应头
![](\img\in-post\post-fiddler\2019-01-25-FiddlerDaily-1.jpg)      

<br>

###### 2、模拟请求
![](\img\in-post\post-fiddler\2019-01-24-FiddlerDaily-2.jpg)    

<br>

###### 3、多次执行同一个请求
![](\img\in-post\post-fiddler\2019-01-24-FiddlerDaily-3.jpg)         

![](\img\in-post\post-fiddler\2019-01-24-FiddlerDaily-4.jpg)

<br>

###### 4、AutoResponder      
&emsp;&emsp;AutoResponder 用于拦截某一请求，并重定向到本地的资源，或者使用 Fiddler 的内置响应。可用于调试服务器端代码而无需修改服务器端的代码和配置，因为拦截和重定向后，实际上访问的是本地的文件或者得到的是 Fiddler 的内置响应。因此，如果要调试服务器的某个脚本文件，可以将该脚本拦截到本地，在本地修改完脚本之后，再修改服务器端的内容，这可以保证，尽量在真实的环境下去调试，从而最大限度的减少bug发生的可能性。         


![](\img\in-post\post-fiddler\2019-01-24-FiddlerDaily-5.jpg)         

![](\img\in-post\post-fiddler\2019-01-24-FiddlerDaily-6.jpg)