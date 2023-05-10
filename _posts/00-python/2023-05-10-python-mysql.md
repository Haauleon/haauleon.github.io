---
layout:        post
title:         "数据库 | python 怎么捕获 mysql 报错"
subtitle:      "MySQLdb 到底该如何获取 mysql 错误"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
    - 数据库
    - MySQLdb
    - Mariadb
---

### 一、前言
最近在运行 python 脚本的时候，经常出现：`mysql server has gone away` 的错误，导致脚本停止运行。只是代码里面明明已经使用 `try: except` 这种方式来捕获 mysql 错误了，用的方法是：`MySQLdb.ProgrammingError`，但是毛用没用。很好，很强大，那么咱们就来研究下这到底是怎么回事。       

捕获代码：     
```python
try:
    cursor.execute(sql)
except MySQLdb.ProgrammingError,e:
    print e
```
打印不出来任何东西，直接脚本就停了，报错：mysql server has gone away

<br>
<br>

### 二、MySQLdb 到底该如何获取 mysql 错误
既然 MySQLdb.ProgrammingError 这种方式获取不了 mysql 报错，那么会不会是用错方法了呢？而且这个 MySQLdb.ProgrammingError 到底获取的是什么错误，博主也不是很清楚，只知道要用它来捕获错误。既然如此，咱们百度下还有没有其他的方案。      

<br>

#### 1、网上的方案（亲测可用）
```python
try:
    conn.ping()			        # 尝试数据库重新连接，conn是数据库连接对象，不是cursor对象
except MySQLdb.Error, e:    	# 捕获到错误则打印错误，打印出来的是个数组形式的，可用e[0],e[1]来获取
    print 'error'
    print e
```
参考： [https://blog.csdn.net/zyz511919766/article/details/20546237](https://blog.csdn.net/zyz511919766/article/details/20546237)       

打印结果：    
```
error
(2013, 'Lost connection to MySQL server during query')
```
虽然成功捕获了错误，但是为何 MySQLdb.ProgrammingError 捕获不到呢，为啥代码里用的都是 MySQLdb.ProgrammingError 呢？很好奇区别到底在哪里。       

<br>

#### 2、关于 MySQLdb.ProgrammingError
网上查询到了 Mysqldb 的手册，才知道原来获取 mysql 错误的方法还是挺多的。比如这个 MySQLdb.ProgrammingError，这个捕获的主要是 sql 的错误，一般是编程错误会引发此异常，例如，当您的 SQL 中存在语法错误或未找到表时。   
那就怪不得捕获不到 mysql 的连接上的错误了，这个方法主要捕获 sql 语句的错误，算是 mysql 内部的方法，相当于是在连接无误的基础上，捕获 sql 执行的错误。       

关于 MySQLdb 的相关函数，可以参考手册：[MySQLdb的手册](https://mysqlclient.readthedocs.io/MySQLdb.html)      

<br>

### 3、常用的方法如下     
```
异常 MySQLdb.DataError
基数： _mysql_exceptions.DatabaseError

因处理的数据问题（例如被零除，数值超出范围等）引起的错误引发异常。

异常 MySQLdb.DatabaseError
基数： _mysql_exceptions.Error

与数据库相关的错误引发异常。

异常 MySQLdb.Error
基数： _mysql_exceptions.MySQLError

异常是所有其他错误异常的基类（不是警告）。

异常 MySQLdb.ProgrammingError
基数： _mysql_exceptions.DatabaseError

因编程错误而引发的异常，例如，找不到或已经存在表，SQL语句中的语法错误，指定的参数数量错误等。
```
我们这里使用的是 MySQLdb.Error 来捕获错误，相当于是所有的异常，自然是也能捕获到数据库连接失败的错误了。      

<br>

#### 4、Mysqldb 捕获连接错误方法
回到原来的问题上，我们需要捕获的是 mysql server has gone away 错误，那么需要的方法如下：     
```
异常 MySQLdb.OperationalError
基数： _mysql_exceptions.DatabaseError

因与数据库操作相关且不一定在程序员控制下的错误而引发的异常，例如，发生意外的断开连接，
找不到数据源名称，无法处理事务，在处理期间发生内存分配错误，等等。
```
使用这个方法可以直接捕获到断开连接的错误，不管是 `Lost connection to MySQL server during query` 还是 `mysql server has gone away` 都当做是断开连接错误，只要捕获到该错误，直接重连即可。          

有事没事，多翻手册，果然是有道理的。

<br>
<br>

---

相关链接：   
[python怎么捕获mysql报错](https://blog.csdn.net/LJFPHP/article/details/102733868)