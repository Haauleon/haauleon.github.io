---
layout: post
title: "完美跳过登录页面的Bug进行登录"
subtitle: '登录页面有Bug导致登录失败？毛使惊！'
author: "Haauleon"
header-style: text
tags:
  - Postman
---

&emsp;&emsp;经常会遇到一些页面上的Bug，如果是登录页面的Bug则导致我不能登录。其实在了解系统并且想要跳过登录这一环节的前提下，还是有解决的办法的。        
![](\img\in-post\2019-02-12-PostmanLogin\1.jpg)                         




## Postman Interceptor
&emsp;&emsp;我们可以使用Postman来发送请求，并同步至Chrome中，最后刷新页面，用这样的办法来跳过页面登录Bug的问题，但是前提是你得知道登录的接口才能发送登录请求。         

### 步骤一：开启相关Interceptor选项
&emsp;&emsp;在Postman客户端的设置选项里面把相关interceptor选项均开启，确保数据能够正确从浏览器同步至客户端中。          
![](\img\in-post\2019-02-12-PostmanLogin\2.jpg)


### 步骤二：打开Interceptor
&emsp;&emsp;在Postman客户端界面上方打开interceptor，右侧的按钮表示正在同步中，可手动触发信息同步。          
![](\img\in-post\2019-02-12-PostmanLogin\3.jpg)


### 步骤三：Postman发送请求同步至Chrome
&emsp;&emsp;设置好之后就可以发送登录请求了，返回登录成功后，切换到Chrome浏览器中刷新需要身份认证的页面，就会发现页面不再跳转至登录页面了，也就是登录成功了。