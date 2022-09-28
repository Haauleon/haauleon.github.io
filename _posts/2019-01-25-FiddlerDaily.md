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
&emsp;&emsp;用于阻拦某一请求，并重定向到本地的资源或者使用 Fiddler 的内置响应。可用于调试 server 端代码而无需修改 server 端的代码和配置，因为阻拦和后，实际上访问的是本地的文件，或者说得到的是 Fiddler 的内置响应。因此，如果要调试 server 的某个脚本文件，可以将该脚本拦到本地，在本地修改完脚本之后，再修改 server 端的内容，这可以保证，尽量在真实的环境下去调试，从而最大限度的减少 bug 发生的可能性。         

&emsp;&emsp;调试生产环境 js，大概思路就是用 Fiddler 把生产环境的 js 替换为本地的 js，修改本地 js 来验证程序或者查找问题。这个场景多发生在紧急修复生产环境的 bug 后需要先在本地进行测试，此时测试人员只需要连上开发人员的代理，便可以测试和调试了，本地测试通过之后再更新到生产环境。
![](\img\in-post\post-fiddler\2019-01-24-FiddlerDaily-5.jpg)         

![](\img\in-post\post-fiddler\2019-01-24-FiddlerDaily-6.jpg)