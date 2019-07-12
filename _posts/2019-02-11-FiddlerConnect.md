---
layout: post
title: "Fiddler抓包时遇到Tunnel to"
subtitle: 'Tunnel to是什么原因造成的呢？'
author: "Haauleon"
header-style: text
tags:
  - Fiddler
  - Tunnel
---

&emsp;&emsp;好奇宝宝又来了，简直是不能放过任何一个细节有木有。早上在iOS客户端请求淘宝接口时出现了大量的Tunnel&#32;to，且图标是一把锁的形状，请求方式是我没见过的Connect，所以借此机会来补下脑。如下图：          
![](\img\in-post\2019-02-11-FiddlerConnect\1.jpg)




## HTTP协议
原文地址：[HTTP协议基础](https://www.cnblogs.com/phpper/p/9127553.html)              

&emsp;&emsp;HTTP是一个基于TCP&#47;IP通信协议来传递数据，包括html文件、图像、结果等，即是一个客户端和服务器端请求和应答的标准。

### HTTP协议特点
1&#46;http无连接：限制每次连接只处理一个请求，服务端完成客户端的请求后，即断开连接。（传输速度快，减少不必要的连接，但也意味着每一次访问都要建立一次连接，效率降低）                      

2&#46;http无状态：对于事务处理没有记忆能力。每一次请求都是独立的，不记录客户端任何行为。（优点解放服务器，但可能每次请求会传输大量重复的内容信息）                        

3&#46;客户端&#47;服务端模型：客户端支持web浏览器或其他任何客户端，服务器通常是apache或者iis等                         

4&#46;简单快速                            

5&#46;灵活：可以传输任何类型的数据                      

### HTTP请求方法
根据HTTP标准，HTTP请求可以使用多种请求方法。         

HTTP1&#46;0定义了三种请求方法：GET，POST和HEAD方法。                      
HTTP1&#46;1新增了五种请求方法：OPTIONS，PUT，DELETE，TRACE和CONNECT方法。

#### GET
&emsp;&emsp;发送请求来获得服务器上的资源，请求体中不会包含请求数据，请求数据放在协议头中。另外get支持快取、缓存、可保留书签等。幂等

#### POST
&emsp;&emsp;和get一样很常见，向服务器提交资源让服务器处理，比如提交表单、上传文件等，可能导致建立新的资源或者对原有资源的修改。提交的资源放在请求体中。不支持快取。非幂等

#### HEAD
&emsp;&emsp;本质和get一样，但是响应中没有呈现数据，而是http的头信息，主要用来检查资源或超链接的有效性或是否可以可达、检查网页是否被串改或更新，获取头信息等，特别适用在有限的速度和带宽下。

#### PUT
&emsp;&emsp;和post类似，html表单不支持，发送资源与服务器，并存储在服务器指定位置，要求客户端事先知道该位置；比如post是在一个集合上（&#47;province），而put是具体某一个资源上（&#47;province&#47;123）。所以put是安全的，无论请求多少次，都是在123上更改，而post可能请求几次创建了几次资源。幂等

#### DELETE
&emsp;&emsp;请求服务器删除某资源。和put都具有破坏性，可能被防火墙拦截。如果是https协议，则无需担心。幂等

#### CONNECT
&emsp;&emsp;HTTP&#47;1&#46;1协议中预留给能够将连接改为管道方式的代理服务器。就是把服务器作为跳板，去访问其他网页然后把数据返回回来，连接成功后，就可以正常的get、post了。

#### OPTIONS
&emsp;&emsp;获取http服务器支持的http请求方法，允许客户端查看服务器的性能，比如ajax跨域时的预检等。

#### TRACE
&emsp;&emsp;回显服务器收到的请求，主要用于测试或诊断。一般禁用，防止被恶意攻击或盗取信息。


## 理解HTTP CONNECT通道
原文地址：[理解HTTP CONNECT通道](https://www.joji.me/zh-cn/blog/the-http-connect-tunnel)          

&emsp;&emsp;为了确保数据通信的安全，HTTPS已广泛应用于互联网，浏览器与服务器之间的HTTPS通信都是加密的。然而当浏览器需要通过代理服务器发起HTTPS请求时，由于请求的站点地址和端口号都是加密保存于HTTPS请求头中的，代理服务器是如何既确保通信是加密的（代理服务器自身也无法读取通信内容）又知道该往哪里发送请求呢？为了解决这个问题，浏览器需要先通过明文HTTP形式向代理服务器发送一个CONNECT请求告诉它目标站点地址及端口号。当代理服务器收到这个请求后，会在对应的端口上与目标站点建立一个TCP连接，连接建立成功后返回一个HTTP 200状态码告诉浏览器与该站点的加密通道已建成。接下来代理服务器仅仅是来回传输浏览器与该服务器之间的加密数据包，代理服务器并不需要解析这些内容以保证HTTPS的安全性。

### 什么时候会用到CONNECT方法？
只有当浏览器配置为使用代理服务器时才会用到CONNECT方法。

### CONNECT通道建立流程
这里我们以Fiddler作为代理服务器。      

1&#46;首先浏览器向代理服务器发送CONNECT请求            
2&#46;代理服务器返回HTTP 200状态台码表示连接已建立          
![](\img\in-post\2019-02-11-FiddlerConnect\2.jpg)               
3&#46;之后浏览器和服务器开始HTTPS握手并交换加密数据，Fiddler作为代理服务器只负责传输彼此的数据包，并不能读取具体数据内容（除非开启了Fiddler的解密HTTPS的功能并安装Fiddler根证书）。        



## Fiddler抓包时遇到Tunnel to
原文地址：[Fiddler教程：fiddler抓包时，出现的tunnel to](https://blog.csdn.net/qq_15283475/article/details/62227067)          

&emsp;&emsp;connect是为了建立http&#32;tunnel，connect是http众多方法中的其中一种，它跟post、get、put、options方法是并列的。但是它的使用场景很特殊。只有在受限制的网络环境中（防火墙、NAT、代理器）并且是https通信时，客户端使用http&#32;connect请求代理服务器，代理服务器使用connect方法与目标服务器建立http&#32;tunnel，通道建立后，客户端与服务器进行通信，代理服务器就像透明一样，只是接收、转发tcp&#32;stream。

### 为什么要建立http  tunnel？ 
&emsp;&emsp;这是因为，网络环境受限，客户端无法直接访问某些网络，所以只能通过代理服务器访问网络，然后，将内容转发给客户端，从宏观上看，客户端与服务器端就像建立了一条隧道一样。 
但是由于http tunnnel可控性不强，所以，服务器通常会限制”可connect的端口”(一般只开放SSL的443端口)

### 为什么fiddler抓包时，出现大量connect连接？ 
&emsp;&emsp;因为fiddler是代理，访问百度网页（使用了https协议），满足了使用connect条件，所以客户端会使用connect方法与目标服务器建立http tunnel，一旦connection建立完成，后续fiddler会转发、接收所有的tcp stream。        

&emsp;&emsp;当然，并不是所有的受限网络(restricted&#32;network)，https通信时，都会使用connect建立http&#32;tunnel，如果目标服务器限制connect方法，那么就会使用其它方法来建立通道（post&#47;get）；如果服务器不支持http&#32;tunnel,那么就需要安装http&#32;tunnel&#32;server端的程序，客户端不支持http&#32;tunnel，那么客户端就需要安装http&#32;tunnel&#32;client程序；http&#32;tunnel程序包含两部分，server端程序和client端程序。


### 隐藏Tunnel to
![](\img\in-post\2019-02-11-FiddlerConnect\3.jpg)