---
layout:        post
title:         "Jmeter | 原生、Badboy 录制 jmx 脚本"
subtitle:      "Jmeter 中 HTTP 脚本录制的两种方式详解"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
---


### 一、Jmeter 原生录制
###### 1、添加Jmeter代理服务器
添加HTTP代理服务器        
![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-1.jpg)       

<br>

###### 2、添加脚本存放的目录   
添加`线程组 > 简单控制器`用来放置录制的脚本         
![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-2.jpg)     

<br>

###### 3、配置代理服务器
配置代理服务器的端口、目标控制器和分组     
![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-3.jpg)     

<br>

###### 4、设置系统代理    
（1）打开 chrome 浏览器的设置页面，点击 `系统 > 打开您计算机的代理设置`          
![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-4.jpg)     

<br>

（2）在手动设置代理栏位点击`编辑`按钮        
![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-5.jpg)     

<br>

（3）代理IP地址为 localhost，端口为 jmeter 代理服务器设置的端口           
![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-6.jpg)      

<br>

###### 5、导入Jmeter证书     
在 chrome 浏览器中导入 jmeter 证书（证书在 bin 目录下）        
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

<br>

###### 6、启动Jmeter代理服务器        
![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-19.jpg)       

<br>

###### 7、在浏览器中操作   
在 chrome 浏览器中访问页面并进行操作         

<br>

###### 8、查看Jmeter抓到的接口    
![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-20.jpg) 

<br>
<br>


### 二、Badboy 工具录制
###### 1、下载安装
链接：https://pan.baidu.com/s/16MyKDp5S2uv4jBVrT2MhWA?pwd=yg8v       
提取码：yg8v     

下载完成后双击 exe 文件进行安装即可。    

<br>

###### 2、运行Badboy
在地址栏内输入要访问的页面地址，然后直接进行页面操作即可进行脚本录制。      
![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-21.jpg) 

<br>

###### 3、导出为Jmeter脚本
![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-22.jpg)

<br>

###### 4、在Jmeter中打开脚本
![](\img\in-post\post-jmeter\2022-09-13-jmeter-badboy-23.jpg)   