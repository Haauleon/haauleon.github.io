---
layout:        post
title:         "Tomcat | 安装和运行"
subtitle:      "windows 环境下的安装和运行"
date:          2021-07-27
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
  - Java
---

## 一、背景
&emsp;&emsp;这几天要重新学习网络协议，需要搭一下服务器环境，后端语言用到了 java，所以自然而然就想到了 tomcat。现在放一下 tomcat 的安装教程。      

<br><br>

## 二、环境准备
（1）已成功安装 jdk1.8 版本    
（2）已成功配置 java 环境变量

<br><br>

## 三、第一种安装方法（无脑安装）
###### 1.下载安装包     
&emsp;&emsp;版本 10 支持 java 版本 8 及以上，符合条件就开始进入[下载页面](https://tomcat.apache.org/download-10.cgi)。      

![](\img\in-post\post-java\2021-07-30-tomcat-install-1.png)       

![](\img\in-post\post-java\2021-07-30-tomcat-install-2.png)       

![](\img\in-post\post-java\2021-07-30-tomcat-install-3.png)       

![](\img\in-post\post-java\2021-07-30-tomcat-install-4.png)       
 
![](\img\in-post\post-java\2021-07-30-tomcat-install-5.png)       

![](\img\in-post\post-java\2021-07-30-tomcat-install-6.png)       

![](\img\in-post\post-java\2021-07-30-tomcat-install-7.png)       

![](\img\in-post\post-java\2021-07-30-tomcat-install-8.png)       

![](\img\in-post\post-java\2021-07-30-tomcat-install-9.png)       
 
<br><br>

###### 2.运行检验       
&emsp;&emsp;在 tomcat 安装界面的最后自动勾选了 `Run Apache Tomcat`，因此系统状态栏将显示 tomcat 后台运行的小图标。在任意浏览器打开并访问 [localhost:8080](localhost:8080) 即可检验是否运行成功。       


![](\img\in-post\post-java\2021-07-30-tomcat-install-10.png)       

![](\img\in-post\post-java\2021-07-30-tomcat-install-11.png)       

<br><br>

## 四、第二种安装方法
###### 1.下载安装包       
&emsp;&emsp;版本 10 支持 java 版本 8 及以上，符合条件就开始进入[下载页面](https://tomcat.apache.org/download-10.cgi)。         

![](\img\in-post\post-java\2021-07-30-tomcat-install-12.png)       

<br><br>

###### 2.运行检验
&emsp;&emsp;将 zip 安装包进行解压，解压后进入 bin 目录，找到 `startup.bat` 程序，双击运行。运行成功后，在任意浏览器打开并访问 [localhost:8080](localhost:8080) 即可检验是否运行成功。           

![](\img\in-post\post-java\2021-07-30-tomcat-install-13.png)       

![](\img\in-post\post-java\2021-07-30-tomcat-install-14.png)     

![](\img\in-post\post-java\2021-07-30-tomcat-install-15.png)     

<br><br>

###### 3.配置环境变量      
&emsp;&emsp;若不配置环境变量，就意味着每一次启动 tomcat，都要去到其所在的 bin 目录下双击运行 `startup.bat` 程序，很麻烦。所以，现在需要配置 tomcat 的环境变量，配置成功后在 cmd 窗口输入 startup 即可启动程序，岂不美哉。    

（1）配置 CATALINA_BASE     
```
变量名：CATALINA_BASE
变量值：D:\software\apache-tomcat-10.0.8（tomcat 安装位置）
```

![](\img\in-post\post-java\2021-07-30-tomcat-install-16.png)       

<br>

（2）配置 CATALINA_HOME     
```
变量名：CATALINA_HOME
变量值：D:\software\apache-tomcat-10.0.8（tomcat 安装位置）
```

![](\img\in-post\post-java\2021-07-30-tomcat-install-17.png)      

<br>

（3）编辑 Path 变量     
```
添加变量值：%CATALINA_HOME%\bin
```

![](\img\in-post\post-java\2021-07-30-tomcat-install-18.png)      

<br>

（4）验证是否配置成功     
&emsp;&emsp;打开 cmd 窗口，输入命令 `startup` 检验是否可以启动，启动后在任意浏览器打开并访问 [localhost:8080](localhost:8080) 即可检验是否运行成功。      

![](\img\in-post\post-java\2021-07-30-tomcat-install-19.png)        

![](\img\in-post\post-java\2021-07-30-tomcat-install-20.png)        

![](\img\in-post\post-java\2021-07-30-tomcat-install-21.png)       

<br><br>

###### 4.解决启动乱码问题      
&emsp;&emsp;输入 `startup` 命令后，发现 tomcat 日志中出现乱码的情况，如下图，现在来解决一下这个编码的问题。     

![](\img\in-post\post-java\2021-07-30-tomcat-install-22.png)              

（1）进入 conf 目录，编辑 `logging.properties` 文件      
![](\img\in-post\post-java\2021-07-30-tomcat-install-23.png)     

（2）编辑 `java.util.logging.ConsoleHandler.encoding = UTF-8` 的值为 `GBK`     
![](\img\in-post\post-java\2021-07-30-tomcat-install-24.png)      

（3）重启 tomcat      
![](\img\in-post\post-java\2021-07-30-tomcat-install-25.png)  