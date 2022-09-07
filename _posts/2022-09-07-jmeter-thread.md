---
layout:        post
title:         "Jmeter | 使用插件设计浪涌、阶梯状递增负载等场景"
subtitle:      "该插件解决 Jmeter 原线程组无法负载递增的问题"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
---

### 一、安装插件
&emsp;&emsp;Jmeter 中原生的线程组无法设计出复杂的测试场景，如浪涌场景，其需要设置多条线程来运行。为了设计出复杂场景来进行性能测试，需要在插件市场安装插件来使用。           

&emsp;&emsp;进入 [https://jmeter-plugins.org/install/Install/](https://jmeter-plugins.org/install/Install/) 插件市场下载此插件放置 `lib/ext` 目录下，然后重启 Jmeter。进入插件管理页面，搜索 `Custom Thread Groups` 然后点击安装。       

![](\img\in-post\post-jmeter\2022-09-07-jmeter-thread-1.jpg) 

<br>
<br>

### 二、使用插件
&emsp;&emsp;插件中的 `Ultimate Thread Group` 和 `Stepping Thread Group` 这两个线程组元件都可以设置多条线程作业计划。      

<br>

###### 1、设计浪涌/稳定性测试场景
1. 在测试计划中添加线程组 **Ultimate Thread Group**       
    ![](\img\in-post\post-jmeter\2022-09-07-jmeter-thread-2.jpg)   
2. 如下图设置 3 条线程作业计划         
    ```
    Start Thread Count: 开始线程数量
    Initial Delay, Sec: 线程延迟多长时间开始运行
    Startup Time,  Sec: 线程加载多长时间
    Hold Load For, Sec: 线程持续运行多长时间
    Shutdown Time     : 线程停止时长，在多长时间内停止下来 
    ```
    第一条，10 个线程立刻在 10 秒内启动，持续运行 600 秒，然后 10 秒内停止。     
    第二条，10 个线程等待 620 秒之后在 10 秒内启动完成，持续运行 600 秒，然后 10 秒内停止。     
    第三条，10 个线程等待 1240 秒之后在 10 秒内启动完成，持续运行 600 秒，然后 10 秒内停止。      
    ![](\img\in-post\post-jmeter\2022-09-07-jmeter-thread-3.jpg)

<br>
<br>

###### 2、设计负载不继增大的场景
1. 在测试计划中添加线程组 **Ultimate Thread Group**       
2. 如下图设置 3 条线程作业计划    
    ```
    Start Thread Count: 开始线程数量
    Initial Delay, Sec: 线程延迟多长时间开始运行
    Startup Time,  Sec: 线程加载多长时间
    Hold Load For, Sec: 线程持续运行多长时间
    Shutdown Time     : 线程停止时长，在多长时间内停止下来 
    ```
    如下图是 3 条线程任务作业的负载不继增大的场景，每一个持续时间是 600 秒，10 个线程运行 600 秒后再加 10 个，共有 30 个线程。            
    ![](\img\in-post\post-jmeter\2022-09-07-jmeter-thread-4.jpg)

<br>
<br>

###### 3、设计阶梯状增加负载场景
1. 在测试计划中添加线程组 **Stepping Thread Group**       
    ![](\img\in-post\post-jmeter\2022-09-07-jmeter-thread-5.jpg)   
2. 如下图设置阶梯状递增负载作业计划        
    ```
    This group will start      : 加载多少线程，如图为 100      
    First,wait for             : 等待多长时间开始加载线程（第一个线程延迟多少秒开始加载）   
    Then start                 : 初次加载多少个线程，如图为 0 个
    Next,add                   : 下一次加载多少个线程，如图为 20 个
    Threads every              : 当前运行多长时间后再次加载线程，如图为 600 秒
    Using ramp-up              : 加载线程时间，如图为 5 秒，即 20 个线程在 5 秒内加载完成
    Then hold load for         : 线程全部加载完成后运行多长时间，如图是 1000 秒
    Finally,stop /threads every: 多长时间停止多少个线程，如图是 1 秒停止 10 个线程
    ```
    如下图是 100 个线程按阶梯状递增运行的场景，每 5 秒内加载 20 个线程直到 100，每个阶梯是 600 秒，最后一个阶梯是 1000 秒（并发 100 线程时运行 1000 秒），最后每秒停止 10 个线程。这是一个典型的负载场景，持续增加负载，检验服务在不同负载下的性能（TPS、RT 等）。           
    ![](\img\in-post\post-jmeter\2022-09-07-jmeter-thread-6.jpg)