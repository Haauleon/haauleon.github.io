---
layout:        post
title:         "Jenkins | Newman 持续集成"
subtitle:      "基于 Newman + Jenkins 实现定时构建接口自动化测试任务"
date:          2021-04-16
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - API 测试
    - Python
    - Newman
    - Jenkins
---

## 背景
&emsp;&emsp;接口自动化测试可以有很多种实现方法，当我发现 postman 的接口测试集合可以用命令行执行时，就在想为什么不集成到 Jenkins 呢？于是，临时想了一个快速实现接口自动化测试兼预警的方法。即，创建一个 Jenkins 定时构建项目，构建的流程是：先用 newman 执行接口测试集合，执行完成后输出测试报告，然后写一个 python3 脚本去读测试报告，解析 html 元素并定位失败用例的数量，如果数量不为 0，就使用钉钉 outgoing 向我的钉钉群组发送文本消息作为警示。       

&emsp;&emsp;使用本文教程需预先成功运行 jenkins。         

<br><br>

## 使用技巧
###### 一、新建 item  
![](\haauleon\img\in-post\post-jenkins\2021-04-16-newman-jenkins-1.jpg)       

<br><br>

###### 二、新建自由风格的项目
![](\haauleon\img\in-post\post-jenkins\2021-04-16-newman-jenkins-2.jpg)       

<br><br>

###### 三、配置定时构建
&emsp;&emsp;当前为每10分钟构建。       

![](\haauleon\img\in-post\post-jenkins\2021-04-16-newman-jenkins-3.jpg)        

<br><br>

###### 四、配置构建命令 
&emsp;&emsp;配置构建命令行后点击保存配置信息。       

![](\haauleon\img\in-post\post-jenkins\2021-04-16-newman-jenkins-4.jpg)      

<br><br>

###### 五、调试配置信息        
&emsp;&emsp;点击立即构建，调试配置信息是否正确。        

![](\haauleon\img\in-post\post-jenkins\2021-04-16-newman-jenkins-5.jpg)     

<br><br>

###### 六、检查构建结果    
![](\haauleon\img\in-post\post-jenkins\2021-04-16-newman-jenkins-6.jpg)       

<br>

![](\haauleon\img\in-post\post-jenkins\2021-04-16-newman-jenkins-7.jpg)       

<br>

&emsp;&emsp;检查本地的测试报告执行日期有无更新，若更新成功则构建成功。       

![](\haauleon\img\in-post\post-jenkins\2021-04-16-newman-jenkins-8.jpg)       

<br>

&emsp;&emsp;检查是否往钉钉发送消息则仅需修改python脚本即可。      

<br><br>

## 结论
&emsp;&emsp;这套自动化流程里面，除了写 python3 脚本解析 html 并向钉钉发消息外，其他都是使用的工具。这种自动化流程适合于不擅于写代码进行接口测试的人，当然也适合于项目紧张的团队。优势就是快速、简单、方便。