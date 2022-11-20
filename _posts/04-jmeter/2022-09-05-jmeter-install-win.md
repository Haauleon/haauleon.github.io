---
layout:        post
title:         "Jmeter | Windows 系统下的安装"
subtitle:      "下载、安装和汉化"
author:        "Haauleon"
header-img:    "img/in-post/post-jmeter/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Jmeter
---

### 一、安装 jdk
jmeter 安装需要依赖 jdk，jdk 版本要求 8 以上。                  

<br>
<br>

### 二、安装 jmeter
###### 1、下载
jmeter下载： [https://jmeter.apache.org/download_jmeter.cgi](https://jmeter.apache.org/download_jmeter.cgi)        
![](\img\in-post\post-jmeter\2022-09-05-jmeter-install-win-1.jpg)       

如果无法下载，备用：     
链接：https://pan.baidu.com/s/1xFm2FfTc3FOvY_iudksa9Q?pwd=jk7i         
提取码：jk7i       

<br>

###### 2、解压
我这里下载的 Binaries 的 zip 包，这里对其进行解压得到 apache-jmeter-5.5              
![](\img\in-post\post-jmeter\2022-09-05-jmeter-install-win-2.jpg)     

<br>

###### 3、配置环境变量
1. 记录解压得到的 apache-jmeter-5.5 路径，如下路径为 D:\software\apache-jmeter-5.5               
    ![](\img\in-post\post-jmeter\2022-09-05-jmeter-install-win-2.jpg)   
2. 新建系统变量           
    ```
    变量名：JMETER_HOME   
    变量值：D:\software\apache-jmeter-5.5
    ```
3. 在终端中输入 `$ echo %JMETER_HOME%` 验证是否配置成功        
    ```
    C:\Users\Haauleon>echo %JMETER_HOME%
    D:\software\apache-jmeter-5.5
    ```
4. 编辑系统变量 Path，新增变量值          
    ```
    变量名：Path   
    变量值：%JMETER_HOME%\bin
    ```           
5. 配置保存成功后，在 cmd 中输入 jmeter 检查是否可以成功启动        
    ![](\img\in-post\post-jmeter\2022-09-05-jmeter-install-win-3.jpg)       

    <br>

    ![](\img\in-post\post-jmeter\2022-09-05-jmeter-install-win-4.jpg)

<br>

###### 4、jmeter 汉化
将 apache-jmeter-5.5/bin/jmeter.properties 文件中的 #language=en 更改为 language = zh_CN。      
![](\img\in-post\post-jmeter\2022-09-05-jmeter-install-win-5.jpg)     

![](\img\in-post\post-jmeter\2022-09-05-jmeter-install-win-6.jpg)

<br>

###### 5、打开 jmeter
重启 jmeter 即可打开汉化后的界面      
![](\img\in-post\post-jmeter\2022-09-05-jmeter-install-win-7.jpg)

<br>
<br>

---
以上参考自 [https://blog.csdn.net/qq_30236721/article/details/125373480](https://blog.csdn.net/qq_30236721/article/details/125373480)