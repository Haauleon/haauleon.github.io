---
layout:        post
title:         "Flask Web | ORM 介绍"
subtitle:      "ORM 在执行对象操作的时候会把对应的操作转换为数据库原生语句"
author:        "Haauleon"
header-img:    "img/in-post/post-flask/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Flask
    - Python
    - Web开发
    - 数据库
    - ORM
    - SQLAlchemy
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、ORM 概览
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     
werkzeug==0.11.10       

<br>

#### 1、ORM 出现的背景 
&emsp;&emsp;随着项目越来越大，采用写原生 SQL 的方式在代码中会出现大量的 SQL 语句，那么问题就出现了：    
1. SQL 语句 **重复利用率不高**，越复杂的 SQL 语句条件越多，代码越长。会看到很多很相近的 SQL 语句。     
2. 很多 SQL 语句是在业务逻辑中拼出来的，如果有数据库需要更改，就要求开发人员非常了解这些逻辑，否则就很 **容易漏掉对某些 SQL 语句的修改**。     
3. 写 SQL 时 **容易忽略 Web 安全问题**，给未来造成隐患。      

<br>
<br>

#### 2、ORM 的相关简介
&emsp;&emsp;ORM，全称 Object Relational Mapping，中文叫作对象关系映射。通过它我们可以直接使用 Python 的类的方式做数据库开发，而不再直接写原生的 SQL 语句（甚至不需要 SQL 的基础）。通过把表映射成类，把行作为实例，把字段作为属性，ORM 在执行对象操作的时候会把对应的操作转换为数据库原生语句的方式来完成数据库开发工作。     

ORM 有如下优点：     
- 易用性。使用这种 ORM 数据库抽象封装方式做开发，可以有效减少出现重复 SQL 语句的概率，**写出来的模型也更直观、清晰**。     
- 性能损耗小。ORM 转换成底层数据库操作指令确实会有一些开销，但其实性能损耗很少（不足 5%），只要不是对性能有严苛的要求，综合考虑开发效率的提升、代码重复利用率等因素，**带来的好处要远大于性能损耗**，而且项目越大其作用越明显。     
- 设计灵活。可以 **很轻松地写复杂的查询**。    
- 可移植。比如 SQLAlchemy，它支持多个关系数据库引擎，包括流行的 MySQL、PostgreSQL 和 SQLite。可以近乎无痛地换数据库，**只需要改很少的配置项即可**。