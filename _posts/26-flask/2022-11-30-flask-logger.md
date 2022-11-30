---
layout:        post
title:         "Flask Web | 记录慢查询"
subtitle:      "添加钩子将慢查询及相关上下文信息记录到日志中"
author:        "Haauleon"
header-img:    "img/in-post/post-flask/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Flask
    - Python
    - Web开发
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、记录慢查询
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

&emsp;&emsp;数据库性能是开发者必须关注的重点之一，在复杂的业务代码逻辑前提下，如果只是通过 **MySQL 的日志** 去看慢查询的日志是很难定位问题的。可以借用 SQLALCHEMY_RECORD_QUERIES 和 DATABASE_QUERY_TIMEOUT 将慢查询及相关上下文信息记录到日志中。     

<br>

#### 1、启用查询记录功能
&emsp;&emsp;设置配置项 DATABASE_QUERY_TIMEOUT 和 SQLALCHEMY_RECORD_QUERIES 的阈值，然后使用 logging.Formatter 格式化被记录到日志文件 slow_query.log 中的字符串，最后添加 app.after_request 钩子用于每次请求结束后获取执行的查询语句并判断阈值，超过就记录到日志中。如执行以下代码：                
