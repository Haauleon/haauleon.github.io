---
layout:        post
title:         "Charles | 保姆级实操总结"
subtitle:      "总结工作中常用的功能、脚本和工具等"
author:        "Haauleon"
header-img:    "img/in-post/post-charles/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Charles
---

### Charles 功能概览
1. 下载安装     
2. 获取IP地址        
3. 手机端代理设置         
4. 断点调试设置（请求、响应数据的篡改）              
5. 单接口重复多次请求           
6. 请求过滤               
7. PC、手机端弱网模拟测试 
8. 小程序抓包

<br><br>

### 一、下载安装 
mac 端：链接: https://pan.baidu.com/s/1RPL0ox8PC1Mw0mywu6yZzw 提取码: fdrw 

<br><br>

### 二、获取IP地址 
Charles 路径：Help > Local IP Addresses          

![](\img\in-post\post-charles\2022-04-28-charles-review-1.png)

<br><br>

### 三、手机端代理设置
详见 [https://haauleon.gitee.io/2020/09/20/charles-set/](https://haauleon.gitee.io/2020/09/20/charles-set/)

<br><br>

### 四、断点调试设置（请求、响应数据的篡改）
1. 步骤一：从任务列表将请求设置断点
    在任务列表选择一条请求点击右键后选择`Breakpoints`，即可将请求加入断点列表，可以在`Proxy > Breakpoints Settings`进行查看和双击进行修改。默认是`Requests & Response`均设置断点。 
    ![](\img\in-post\post-charles\2022-04-28-charles-review-2.png)
2. 步骤二：在断点设置窗口中修改设置
    Charles 路径：Proxy > Breakpoints Settings 
    ![](\img\in-post\post-charles\2022-04-28-charles-review-3.png)
    ![](\img\in-post\post-charles\2022-04-28-charles-review-4.png)

<br><br>

### 五、单接口重复多次请求   
Charles 路径：选择一个请求并右键点击选择`Advanced Repeat`       

![](\img\in-post\post-charles\2022-04-28-charles-review-5.png)

<br><br>

### 六、请求过滤
![](\img\in-post\post-charles\2022-04-28-charles-review-6.png)

<br><br>

### 七、PC、手机端弱网模拟测试
[https://www.jianshu.com/p/b7c56df6f7d0](https://www.jianshu.com/p/b7c56df6f7d0)         

![](\img\in-post\post-charles\2022-04-28-charles-review-7.png)

<br><br>

### 八、小程序抓包
需要在手机端安装证书           
详见 [https://haauleon.gitee.io/2020/09/20/charles-set/](https://haauleon.gitee.io/2020/09/20/charles-set/)