---
layout:        post
title:         "HTTP | 状态码 502 和 504 的区别"
subtitle:      "接口响应状态码 502 的紧急判断方法"
date:          2021-07-22
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - API 测试
---

## 基本知识
&emsp;&emsp;`502 bad gateway` 即网关错误，后端服务器 tomcat 没有起来，应用服务的问题（前提是接入层7层正常的情况下）。       
&emsp;&emsp;应用服务问题一般有两种。一种是应用本身问题。另一种是因为依赖服务问题比如依赖服务 RT 高，依赖的服务有大的读取（mysql 慢查，http 等），以至于调用方超过超时 read 时间；另外服务集群压力大时，也会出现 502 超时（502 理解为不可响应或响应不过来，其实还是不可响应）。        

&emsp;&emsp;`504 gateway time-out` 即网关超时，一般计算机中的超时就是配置错了，此处一般指 nginx 做反向代理服务器时，所连接的服务器 tomcat 无响应导致的。   
&emsp;&emsp;从网络角度，502已经与后端建立了连接，但超时；504与后端连接未建立，超时。

<br><br>

## 502 检查思路

**1、必现 502，应用“挂了”**                
（1）后端机器上检查：              
```
$ ps -ef |grep java #检查进程是否在

$ sudo netstat -lntp |grep PORT #检查端口有没有起来

$curl -I 127.0.0.1:PORT/health #应用健康检查测试下,Your health check path
```

<br>

（2）上面都正常，看下接入层 access.log 有没有进来。        
```
$ tail -300f access.log |grep xxxx | #grep下你的关键字

$ curl -I 10.10.10.10:80/java_hc #上面都正常情况下，去接入层检查下
```

<br><br>

**2、偶现 502**       
（1）CPU使用率高，QPS增加         
&emsp;&emsp;考虑有大流量，后端压力导致短暂不可用，考虑临时扩容。          

<br>

（2）检查应用本身 nginx read 超时时间配置        
```
    proxy_read_timeout              2s; # vim /opt/nginx/nginx.conf
```

&emsp;&emsp;如果某些正常请求耗时在 2s 左右，那么会有少量大于 2s 的请求是 502 的。可以试着把上面耗时时间调大，看问题是否缓解。优化本身链路请求耗时是根本上的解决办法。    

<br>

（3）检查接入层 nginx read 的配置       
&emsp;&emsp;同（2）。