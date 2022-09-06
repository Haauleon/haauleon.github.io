---
layout:        post
title:         "Jmeter | 如何设计出浪涌（多个波峰）的场景？"
subtitle:      "使用 JMeter Plugins 解决原线程组无法负载递增的问题"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
---

### 负载递增

<br>

###### 一、非GUI运行方式
&emsp;&emsp;非 GUI 运行方式虽然不显示界面，但也会以字符形式周期性显示执行结果，对负载机的资源消耗会小一些。所以，同等条件下非 GUI 方式的 Jmeter 机器产生的负载比 GUI 方式大一些。运行命令如下：（提前设置好环境变量 JMETER_HOME）         
```
$ java -jar %JMETER_HOME%/bin/ApacheJMeter.jar -n -t [测试计划的绝对路径.jmx] -l [测试结果绝对路径.txt] -e -o [web测试报告目录的绝对路径]

$ jmeter -n -t [测试计划的绝对路径.jmx] -l [测试结果绝对路径.txt] -e -o [web测试报告目录的绝对路径]  
```

&emsp;&emsp;可以使用以上两种命令来运行测试计划，其本质是通过运行 ApacheJMeter.jar 来完成的。     
![](\img\in-post\post-jmeter\2022-09-06-jmeter-save-source-1.jpg)   