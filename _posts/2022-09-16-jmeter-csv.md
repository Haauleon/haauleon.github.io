---
layout:        post
title:         "Jmeter | CSV Data Set Config 参数化"
subtitle:      "使用多个不用账号真实模拟用户行为，实现性能测试并发多个用户"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
---


### CSV Data Set Config
&emsp;&emsp;做性能测试需要并发多个用户，为了真实模拟用户行为，我们需要模拟多个不同的账号，这时需要做参数化。参数化的方式之一是通过 `CSV Data Set Config` 来实现，它可以从执行的文件中逐行去提取文本中的内容，然后根据分隔符去拆解这一行内容并把内容与变量名对应上，之后这些变量名就可以在 HTTP 登录请求中被引用了。     

&emsp;&emsp;有一种做法是，从数据库中的 user 用户表中拷贝用户名、密码这两列数据，然后存放到 csv 文件中，之后在 jmeter 中引用 csv 文件中的真实用户数据来做并发。但因为这里只是做讲解说明，所以只添加了三条真实用户数据。        

<br>
<br>

###### 1、添加配置元件
&emsp;&emsp;直接在对应的 HTTP 登录请求下添加配置元件 `CSV Data Set Config` 即可。     

![](\img\in-post\post-jmeter\2022-09-16-jmeter-csv-2.jpg) 

<br>

###### 2、创建user.csv文件
&emsp;&emsp;创建一个 `.txt` 文本文件，输入以下数据后保存，然后更改文件扩展名为 `.csv`。      
```
13976062467,123456
13976062440,123456
13976062450,123456
```

![](\img\in-post\post-jmeter\2022-09-16-jmeter-csv-1.jpg) 

<br>

###### 3、编辑配置元件
- 文件名：csv 文件存放的路径，点击`浏览`按钮找到并导入   
- 文件编码：`utf-8`    
- 变量名：与 csv 文件列值对应，分别是用户名 `usr` 和密码 `pwd`    

![](\img\in-post\post-jmeter\2022-09-16-jmeter-csv-3.jpg) 

<br>

###### 4、编辑线程组
&emsp;&emsp;csv 文件中目前有三条用户记录，线程组编辑页面的线程数可以设置 `>=3` ，如果设置为 4，那么第四个用户又会从头开始循环也就是读取文件中第一行的用户数据。    

![](\img\in-post\post-jmeter\2022-09-16-jmeter-csv-4.jpg) 

<br>

###### 5、编辑取样器
&emsp;&emsp;使用配置文件中的变量名，分别是用户名 `${usr}` 和密码 `${pwd}`。     

![](\img\in-post\post-jmeter\2022-09-16-jmeter-csv-5.jpg) 

<br>

###### 6、执行并发
&emsp;&emsp;在查看结果树中查看运行结果，结果显示用户登录的账号密码分别是 csv 文件中的数据，说明 Jmeter 逐行读取 csv 文件数据成功。         

![](\img\in-post\post-jmeter\2022-09-16-jmeter-csv-6.jpg)     

![](\img\in-post\post-jmeter\2022-09-16-jmeter-csv-7.jpg)      

![](\img\in-post\post-jmeter\2022-09-16-jmeter-csv-8.jpg) 