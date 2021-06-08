---
layout: post
title: "Fiddler日常使用小技巧"
subtitle: 'Fiddler实用技巧2'
author: "Haauleon"
header-style: text
tags:
  - Fiddler
---


&emsp;&emsp;今天看到了一篇关于Fiddler常用文档的文章，讲的很详细，介绍了一些平时百分百可以用得上的一些技巧，很实用。




## Fiddler工作原理
&emsp;&emsp;浏览器&#32;&#45;&#62;&#32;WinNet&#32;&#45;&#62;&#32;Fiddler&#32;&#45;&#62;&#32;Web Server，打开Fiddler后它会自动修改注册表，所有请求、相应都经过Fiddler，关闭后会自动从注册表中移除，减少资源浪费，是不是很优雅。


## 常用功能
### 请求和响应头
![](\img\in-post\post-fiddler\2019-01-25-FiddlerDaily-1.jpg)

### 模拟请求
![](\img\in-post\post-fiddler\2019-01-24-FiddlerDaily-2.jpg)

### 多次执行同一个请求
![](\img\in-post\post-fiddler\2019-01-24-FiddlerDaily-3.jpg)        

![](\img\in-post\post-fiddler\2019-01-24-FiddlerDaily-4.jpg)

### AutoResponder      
&emsp;&emsp;Fiddler比较重要且比较强大的功能之一。用于拦截某一请求，并重定向到本地的资源，或者使用Fiddler的内置响应。可用于调试服务器端代码而无需修改服务器端的代码和配置，因为拦截和重定向后，实际上访问的是本地的文件或者得到的是Fiddler的内置响应。因此，如果要调试服务器的某个脚本文件，可以将该脚本拦截到本地，在本地修改完脚本之后，再修改服务器端的内容，这可以保证，尽量在真实的环境下去调试，从而最大限度的减少bug发生的可能性。        

&emsp;&emsp;调试生产环境js&#58;大概思路就是用Fiddler把生产环境的js替换为本地的js，修改本地js来验证程序或者查找问题。这个场景多发生在紧急修复生产环境的bug后需要先在本地进行测试，此时测试人员只需要连上开发人员的代理，便可以测试和调试了，本地测试通过之后再更新到生产环境。
![](\img\in-post\post-fiddler\2019-01-24-FiddlerDaily-5.jpg)         

![](\img\in-post\post-fiddler\2019-01-24-FiddlerDaily-6.jpg)