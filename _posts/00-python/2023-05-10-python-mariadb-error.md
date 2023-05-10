---
layout:        post
title:         "数据库 | server has gone away 错误"
subtitle:      "python 重现 server has gone away 错误以及解决方案"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
    - 数据库
---

### 一、前言
&emsp;&emsp;本篇主要是通过 python 程序连接数据库的错误，从而引出 mysql 的 wait_timeout 参数和 interactive_timeout 的概念，继而重现程序错误，从根源上解决问题。          

需求：      
python 脚本监听文件，当文件行数增加 10 行则执行一次数据库持久化操作。只是文件有时候可能需要几十分钟才增加 10 行，此时操作数据库会出现：MySQL server has gone away 的错误，并且脚本被停止。       
根据以上错误，首先是要重现 `MySQL server has gone away` 的情况，看看是哪个参数造成的，又该通过哪种方式来捕获这种错误。大家随便一百度就能知道影响数据库连接时间的参数一般是 wait_timeout 和 interactive_timeout 两个参数，下面就着重重现一下错误，并总结下遇到的问题。        

&emsp;&emsp;关于 python 如何捕获 mysql 的各种错误，可以参考我的上篇文章：[python怎么捕获mysql报错](https://blog.csdn.net/LJFPHP/article/details/102733868)      

<br>
<br>

### 二、了解 wait_timeout 和 interactive_timeout 两个参数
&emsp;&emsp;为了重现错误，我们设置两个参数都为 10s，即 10s 后数据库就自动断开连接了，先通过命令行测试下看看。       

<br>

#### 1、命令行操作        
不管是设置wait_timeout 还是设置 interactive_timeout = 10，执行sql命令行都会报错：       

**错误1 ：**     
```
ERROR 2013 (HY000): Lost connection to MySQL server during query
```
重新执行sql，则会重新连接，此时的错误才是我们想要的 gone away     

<br>

**错误2 ：**    
```
mysql> show variables like '%timeout%';
ERROR 2006 (HY000): MySQL server has gone away
No connection. Trying to reconnect...
Connection id:    27
Current database: *** NONE ***
```
本来想着会直接报：MySQL server has gone away 的错误，没想到先报的是数据库失去连接错误，博主怀疑这两个参数是否会影响两种错误的产生。     

<br>

#### 2、wait_time 设置失效问题
&emsp;&emsp;这个刚开始还挺奇怪的，明明设置的 wait_time =10，interactive_timeout =1000，但是实际查看的时候，总是发现 wait_time =1000 了，真是奇了怪了，为何这个参数会自己改变呢？       
&emsp;&emsp;修改wait_timeout不生效的问题：[https://www.cnblogs.com/azhqiang/p/5454000.html](https://www.cnblogs.com/azhqiang/p/5454000.html)，通过这个链接可以发现，实际上wait_timeout是受interactive_timeout 影响，只是为什么会出现这种情况呢？       

<br>

#### 3、参考手册概念，解释两个参数
**interactive_timeout：**     
```
The number of seconds the server waits for activity on an interactive connection before closing it. An interactive client is defined as a client that uses the CLIENT_INTERACTIVE option to mysql_real_connect()
```

<br>

**wait_timeout：**     
```
The number of seconds the server waits for activity on a noninteractive connection before closing it. On thread startup, the session wait_timeout value is initialized from the global wait_timeout value or from the global interactive_timeout value,
 depending on the type of client (as defined by the CLIENT_INTERACTIVE connect option to mysql_real_connect())
```
&emsp;&emsp;他们都是 session/global 级别的，简单的说前者用于描述交互式的客户端的空闲超时，后者用于非交互式的客户端的空闲超时，但是这里也揭示了，如果是交互式客户端连接的 session 那么 wait_timeout 将被 interactive_timeout 覆盖掉，换句话说如果是非交互式的客户端连接的 session 将不会使用 interactive_timeout 覆盖掉 wait_timeout，也就是 interactive_timeout 没有任何作用了。一旦会话登录成功，如果想要会话级别修改超时参数，不管交互式还是非交互式都是修改 wait_timeout 参数才会生效。

<br>

参考：[http://blog.itpub.net/7728585/viewspace-2637237/](http://blog.itpub.net/7728585/viewspace-2637237/)       

&emsp;&emsp;这篇文章解析的相当清楚，例子也很生动，总结来说就是：如果是交互式客户端连接的 session 那么 wait_timeout 将被 interactive_timeout 覆盖掉，换句话说如果是非交互式的客户端连接的 session 将不会使用 interactive_timeout 覆盖掉 wait_timeout，也就是 interactive_timeout 没有任何作用了。      

<br>

#### 4、那么什么算是交互式，什么算是非交互式呢
**交互式操作：**     
&emsp;&emsp;通俗的说，就是你在你的本机上打开 mysql 的客户端，就是那个黑窗口，在黑窗口下进行各种 sql 操作，当然走的肯定是 tcp 协议。（小黑框方式）        

**非交互式操作：**   
&emsp;&emsp;就是你在你的项目中进行程序调用。比如一边是 tomcat web 服务器，一边是数据库服务器，两者怎么通信？在 java web 里，我们通常会选择 hibernate 或者是 jdbc 来连接。那么这时候就是非交互式操作。 （代码连接方式）    

根据上面所述的，之前命令行测试属于交互式操作，那咱们程序连接的应该就是非交互式连接，如果想要程序重现这个问题，那么需要设置非交互式的 wait_time 的值。    

<br>
<br>

### 三、python 重现 mysql server has gone away
&emsp;&emsp;到底哪个参数会造成`错误1`，哪些参数会造成`错误2`呢。在命令行测试的时候，发现总是先出现`错误1`，再出现`错误2`，那么这两个错误是否是分开受到两个参数的影响呢？如何重现出来我们想要的：`mysql server has gone away` 错误。     

通过代码测试，不继续在命令行测试了。代码为非交互式操作。           

1、通过代码测试两个参数影响      
（1）当两个参数都设置为 10s 的时候：     
```python
try:
    conn.ping()
except MySQLdb.Error, e:
    print 'error'
    # sqlError = "Error %d:%s" % (e.args[0], e.args[1])
    print e.args[0]
    print e.args[1]
    try:
        conn.ping()
    except MySQLdb.OperationalError,e:
        print 'error1'
        print e
    pass
```

这段代码打印如下：
```
error
2013
Lost connection to MySQL server during query
error1
(2006, 'MySQL server has gone away')
```
经过试验，还是没直接获得 MySQL server has gone away 的错误，都是先报数据库失去连接，然后再进行重连，此时才报出：MySQL server has gone away      

<br>

（2）当 wait_timeout = 10，而i nteractive_timeout = 1000       
```
error
2013
Lost connection to MySQL server during query
2013
error1
(2006, 'MySQL server has gone away')
2222_2
```
结果和上面一致，并没有单独报 MySQL server has gone away 的错误。     

<br>

（3）当 interactive_timeout = 10，而 wait_timeout = 1000      
没有报错，程序正常执行。当代码连接 mysql 的时候，相当于是非交互式，那么此时的 interactive_timeout 相当于没用了，用的是 wait_timeout 的值，所以程序没报错。      

<br>

（4）设置两个参数都为10s，程序 `sleep(15)` 看看效果       
```
import time

time.sleep(15)
```

```
error
2013
Lost connection to MySQL server during query
2013
error1
(2006, 'MySQL server has gone away')
```

通过频繁的测试发现，出现`错误1`和`错误2`似乎并不是这两个参数来操纵的，因为这两个错误总是一起出现的，这就和原来的猜想不一样了。不过仔细想想也是，你想要操作 Mysql，肯定是要先检查是否存在子线程的，发现不存在就报个错，重新连接失败再报个错，比较符合逻辑。       

<br>
<br>

2、不设置重连，直接执行相应的 sql 看看        
```python
try:
    cursor.execute(insert_sql)  # 直接执行sql
except MySQLdb.Error, e:
    print 'error'
    # sqlError = "Error %d:%s" % (e.args[0], e.args[1])
    print e.args[0]
    print e.args[1]
    print e[0]
    try:
        cursor.execute(insert_sql)
    except MySQLdb.OperationalError, e:
        print 'error1'
        print e
        pass
```

打印结果如下：
```
error
2006
MySQL server has gone away
2006
error1
(2006, 'MySQL server has gone away')
```
这里发现，在直接执行 sql 的时候，会直接报 MySQL server has gone away 的错误。OK，报错已经重现。       

<br>
<br>

3、总结       
&emsp;&emsp;这个报错并不是 interactive_timeout 和 wait_timeout 这两个参数影响的。估计是，mysql 在直接执行 sql 的时候，会主动去线程池寻找子进程，找不到的时候，先抛出 `Lost connection to MySQL server during query` 错误，然后尝试重连的时候抛出 `MySQL server has gone away` 错误。       
&emsp;&emsp;我们上面的代码是一直在尝试重连，所以先抛出`错误1`，再抛出`错误2`。而直接执行 sql 的时候，`错误1`被`错误2`给覆盖了，因此打印出来的 MySQL server has gone away，实际上`错误1`依然存在。       

<br>
<br>

### 四、捕获 mysql 错误并重新连接的完整代码
代码如下：      
```python
try:
    cursor.execute(insert_sql)
except MySQLdb.OperationalError:  # 先检测数据库连接的问题，检测无误则执行sql
    print 'connect error1'
    cursor = MakeDbConnection()	  # 重新连接sql，函数里面的是connect()方法
    try:
        cursor.execute(insert_sql)
        except MySQLdb.ProgrammingError:    # 捕获sql语句执行的错误
            try:
                xxxxxxxxxxxxxxx 		 # 根据各自的需求，重新调整下
                cursor.execute(insert_sql)     	#重新执行sql
            except:
            pass
 except UnicodeDecodeError:     # 捕获编码错误，如捕获代码不是utf-8的错误
        pass
```
如此便可避免数据库丢失连接的错误，捕获到连接失败，则重新连接，然后执行代码即可，妈妈再也不用担心我的脚本会自己停掉了。


<br>
<br>

---

相关链接：    
[python重现 mysql server has gone away错误以及解决方案](https://blog.csdn.net/LJFPHP/article/details/102751743)