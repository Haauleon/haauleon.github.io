---
layout:        post
title:         "Jmeter | 原生、Badboy 录制 jmx 脚本"
subtitle:      "Jmeter 中 HTTP 脚本录制及脚本调试"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
---

### 一、脚本录制
###### Jmeter 原生录制
1. 添加HTTP代理服务器     
    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-1.jpg)     
2. 添加`线程组 > 简单控制器`用来放置录制的脚本      
    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-2.jpg)     
3. 配置代理服务器的端口、目标控制器和分组     
    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-3.jpg) 
4. 设置系统代理    
    （1）打开 chrome 浏览器的设置页面，点击 `系统 > 打开您计算机的代理设置`        
    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-4.jpg)     

    （2）在手动设置代理栏位点击`编辑`按钮
    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-5.jpg)     

    （3）代理IP地址为 localhost，端口为 jmeter 代理服务器设置的端口        
    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-6.jpg) 
5. 在 chrome 浏览器中导入 jmeter 证书（证书在 bin 目录下）        
    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-7.jpg)     

    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-8.jpg)    

    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-9.jpg)         

    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-10.jpg)     

    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-11.jpg)      

    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-12.jpg)      

    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-13.jpg)      

    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-14.jpg)      

    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-15.jpg)      

    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-16.jpg)      

    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-17.jpg)     

    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-18.jpg)              
6. 启动 Jmeter 代理服务器        
    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-19.jpg) 
7. 在 chrome 浏览器中访问页面并进行操作      
8. 查看 Jmeter 抓到的 HTTP 接口    
    ![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-20.jpg) 


<br>

###### Badboy 工具录制


<br>
<br>


### 二、脚本调试
###### 1、测试计划

<br>

###### 2、线程组

<br>

###### 3、HTTP Cookie 管理器

<br>

###### 4、用户定义的变量


###### 5、HTTP信息头管理器

###### 6、循环控制器

###### 7、HTTP请求   
