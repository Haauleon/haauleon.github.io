---
layout:        post
title:         "认证机制 | session 与 token 的区别"
subtitle:      "token 的优势是什么？session 的劣势是什么？"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 面试
---

## session
###### session 的状态保持原理   
&emsp;&emsp;当用户第一次通过浏览器使用用户名和密码访问服务器时，服务器会验证用户数据，验证成功后在服务器端写入 session 数据，向客户端浏览器返回 sessionid，浏览器将 sessionid 保存在 cookie 中，当用户再次访问服务器时，会携带 sessionid，服务器会拿着 sessionid 从服务器获取 session 数据，然后进行用户信息查询，查询到，就会将查询到的用户信息返回，从而实现状态保持。         

![](\img\in-post\post-http\2021-07-22-session-token-1.png)      

<br><br>

###### session 的弊端     
1、服务器压力增大        
&emsp;&emsp;通常 session 是存储在内存中的，每个用户通过认证之后都会将 session 数据保存在服务器的内存中，而当用户量增大时，服务器的压力增大。        

2、CSRF跨站伪造请求攻击       
&emsp;&emsp;session 是基于 cookie 进行用户识别的, cookie 如果被截获，用户就会很容易受到跨站请求伪造的攻击。        

3、扩展性不强        
&emsp;&emsp;如果将来搭建了多个服务器，虽然每个服务器都执行的是同样的业务逻辑，但是 session 数据是保存在内存中的（不是共享的），用户第一次访问的是服务器 1，当用户再次请求时可能访问的是另外一台服务器 2，服务器 2 获取不到 session 信息，就判定用户没有登录过。      

<br><br>

## token
###### token 的认证机制
token 与 session 的不同主要有以下几点：     
① 认证成功后，会对当前用户数据进行加密，生成一个加密字符串 token，返还给客户端（服务器端并不进行保存）。      
② 浏览器会将接收到的 token 值存储在 Local Storage 中，（通过 js 代码写入 Local Storage，通过 js 获取，并不会像 cookie 一样自动携带）。       
③ 再次访问时服务器端对 token 值的处理：服务器对浏览器传来的 token 值进行解密，解密完成后进行用户数据的查询，如果查询成功，则通过认证，实现状态保持，所以，即时有了多台服务器，服务器也只是做了 token 的解密和用户数据的查询，它不需要在服务端去保留用户的认证信息或者会话信息，这就意味着基于 token 认证机制的应用不需要去考虑用户在哪一台服务器登录了，这就为应用的扩展提供了便利，解决了 session 扩展性的弊端。     

![](\img\in-post\post-http\2021-07-22-session-token-2.png)