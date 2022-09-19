---
layout:        post
title:         "Jmeter | 事务控制器"
subtitle:      "通过事务控制器将多个操作统计成一个事务从而观察 TPS（每秒事务数）"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
---


### 事务控制器
&emsp;&emsp;性能测试的结果统计时我们一定会关注 TPS（每秒事务数），虽然 Jmeter 能把每个请求都统计成一个事务，但是我们有时希望可以将多个操作统计成一个事务。所以，这里用到`事务控制器`来完成。

###### 1、添加事务控制器
&emsp;&emsp;在循环控制器下添加`事务控制器`用来将多个操作统计成功一个事务。            

![](\img\in-post\post-jmeter\2022-09-19-jmeter-tps-1.jpg) 

<br>

###### 2、配置事务控制器
`Generate parent sample`: 如果事务控制器下有多个取样器（请求）就勾选它，之后可以在**查看结果树**中看到事务控制器下的所有取样器。    

![](\img\in-post\post-jmeter\2022-09-19-jmeter-tps-2.jpg) 

<br>

###### 3、事务执行成功
&emsp;&emsp;事务控制器定义的事务是否成功取决于子事务是否全部成功，任何一个子事务失败则代表整个事务失败。这里展示所有子事务均成功的结果。                

![](\img\in-post\post-jmeter\2022-09-19-jmeter-tps-3.jpg) 
![](\img\in-post\post-jmeter\2022-09-19-jmeter-tps-4.jpg) 

<br>

###### 4、事务执行失败
&emsp;&emsp;事务控制器定义的事务是否成功取决于子事务是否全部成功，任何一个子事务失败则代表整个事务失败。这里展示有一个子任务失败的结果。       

![](\img\in-post\post-jmeter\2022-09-19-jmeter-tps-5.jpg) 
![](\img\in-post\post-jmeter\2022-09-19-jmeter-tps-6.jpg) 