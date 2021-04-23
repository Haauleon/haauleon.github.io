---
layout:        post
title:         "Fiddler | 拦截请求"
subtitle:      "如何使用 Fiddler 拦截请求并篡改数据？"
date:          2018-02-02
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Fiddler
---



## 背景
&emsp;&emsp;Fiddler 其实就是代理服务器。代理是什么呢？代理其实是一种有**转发功能**的应用程序，它扮演了位于服务器和客户端“中间人”的角色，接收由客户端发送的请求并转发给服务器，同时也接收服务器返回的响应并转发给客户端。

![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-1.png)     

<br><br>

## 拦截 HTTP 请求               
**问题场景：**          
&emsp;&emsp;如何通过 fiddler 的菜单栏设置断点拦截请求？          
&emsp;&emsp;如何通过 fiddler 的界面设置断点快速拦截请求？            
&emsp;&emsp;如何输入命令行设置断点拦截指定的请求？          
&emsp;&emsp;设置了断点后如何退出？
 
<br>

&emsp;&emsp;“拦截”可理解成在播放视频的时候点击的“暂停”按钮，使其画面停留；而当点击“播放”按钮时视频又可继续播放，即“取消断点”。

<br><br>

###### 方式一 通过菜单栏设置断点拦截请求   
&emsp;&emsp;使用菜单栏设置的断点方式将会拦截客户端/服务器发送的所有请求/响应，包括当前发送的请求/响应及后面耦合的所有请求/响应。设置方式如下：
`菜单栏：Rules --> Automatic Breakpoints --> Before Requests/After Responses/Disabled`                   
  
<br>

![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-2.png)    

<br><br>

**使用场景一**       
&emsp;&emsp;在请求未被 fiddler 转发至服务器之前进行拦截。                               
![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-3.png)        

<br>

&emsp;&emsp;使用以上的方法设置好断点后，接下来客户端发送的请求在 fiddler 转发给服务器之前就被拦截下来了。如下图，可以看到被拦截的请求会带上暂停的标识，表示请求还未转发至服务器。
![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-4.png)       

<br><br>   

**使用场景二**
&emsp;&emsp;在响应未被 fiddler 转发至客户端之前进行拦截。    
![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-5.png) 

<br>

&emsp;&emsp;使用以上的方法设置好断点后，接下来服务器发送的响应在 fiddler 转发给客户端之前就被拦截下来了。如下图，可以看到被拦截的响应会带上暂停的标识，表示请求还未转发至客户端。   
![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-6.png) 

<br><br>

**使用场景三**       
&emsp;&emsp;不需要进行拦截，关闭断点的设置，让客户端正常请求及让服务器正常响应。                          
![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-7.png)         

<br><br>

&emsp;&emsp;关闭拦截后，场景二中被 fiddler 拦截的服务器响应可被放开，使其响应正常到达客户端。                       
![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-8.png)            

<br><br>

###### 方式二 快速设置断点拦截请求    
&emsp;&emsp;此种设置的方法最终呈现的效果和方式一是一样的，只是不需要通过菜单栏进行点点点设置，仅适用于方便和快速。      

<br>

**使用场景一**       
&emsp;&emsp;在请求未被 fiddler 转发至服务器之前进行拦截。   
![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-9.png) 

<br><br>

**使用场景二**
&emsp;&emsp;在响应未被 fiddler 转发至客户端之前进行拦截。    
![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-10.png) 

<br><br>

**使用场景三**       
&emsp;&emsp;不需要进行拦截，关闭断点的设置，让客户端正常请求及让服务器正常响应。                     
![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-11.png) 

<br><br>

###### 方式三 输入命令行设置断点拦截
![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-12.png) 
&emsp;&emsp;使用命令行方式（输入命令 + 回车按钮）可以拦截指定的请求或者响应，而其他的请求和响应均可以正常到达。     


<br><br>

![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-13.png) 
<br><br>

**使用场景一**       
&emsp;&emsp;在指定的请求未被 fiddler 转发至服务器之前进行拦截。      
```
# 指定拦截此主机下的所有请求
bpu http://haauleon.com 

# 指定拦截此路径下的所有请求  
bpu http://haauleon.com/index   

# 指定拦截此参数下的所有请求
bpu http://haauleon.com/index?name=haauleon   

# 退出指定请求的断点拦截，使其正常到达服务器
bpu    
```
   

<br><br>

**使用场景二**
&emsp;&emsp;在指定的响应未被 fiddler 转发至客户端之前进行拦截。    
```
# 指定拦截此主机下的所有响应
bpafter http://haauleon.com 

# 指定拦截此路径下的所有响应 
bpafter http://haauleon.com/index   

# 指定拦截此参数下的所有响应
bpafter http://haauleon.com/index?name=haauleon   

# 退出指定响应的断点拦截，使其正常到达客户端
bpafter    
```

<br><br>

&emsp;&emsp;一般情况下，需要验证前端界面对某个接口的请求/响应（500、502、400、404等状态码）结果是否做出反应的情况，就用此方式即可。

<br><br>

## 修改被拦截的请求/响应数据
&emsp;&emsp;修改`Inspectors`下的数据，然后点击`Run to Completion`，修改即可生效。                                
![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-14.png)  

<br>

![](\img\in-post\post-fiddler\2018-02-02-fiddler-breakpoint-15.png) 