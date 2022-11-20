---
layout:        post
title:         "Jmeter | 集合点"
subtitle:      "通过同步定时器模拟大量用户在同一时刻发送请求"
author:        "Haauleon"
header-img:    "img/in-post/post-jmeter/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Jmeter
---


### 同步定时器
&emsp;&emsp;性能测试需要模拟大量用户并发，集合点能够尽量让虚拟用户同一时刻发送请求，在 Jmeter 中集合点是通过`定时器`来完成的。定时器可以用来控制取样器的执行时机，这里选择`同步定时器`来保证我们的取样器在同一时刻向服务器发起负载。     

###### 1、添加同步定时器
&emsp;&emsp;在事务控制器下添加`同步定时器`实现将取样器集合在同一时刻执行。                  

![](\img\in-post\post-jmeter\2022-09-19-jmeter-timer-1.jpg) 

<br>

###### 2、配置同步定时器
`模拟用户组的数量`: 设置同步的线程数量。在运行测试时，每一个线程的运行时间可能不一致（有的快有的慢），想要让所有线程都集合在一起可能会等待较长时间，这种情况下可以先让一部分集合完毕的线程运行起来。另外，有些场景不一定要等待所有的线程集合完毕，只需要部分线程保证同步就可以了，基于这些要求设置这个选项即可。       

![](\img\in-post\post-jmeter\2022-09-19-jmeter-timer-2.jpg) 