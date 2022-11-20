---
layout:        post
title:         "Android | adb 命令行工具的安装"
subtitle:      "通过 Android SDK 进行安装"
author:        "Haauleon"
header-img:    "img/in-post/post-app-test/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Android
---

## 一、背景
&emsp;&emsp;安装 adb 命令行工具目前就我所知，有两种方式。一种是直接下载 `SDK Platform Tools` 安装包，解压后的 `platform-tools` 文件夹下包含有 `adb.exe` ，在配置该文件夹所在路径的环境变量后即可在 cmd 中使用 adb 命令行。另一种是在下载 `Android SDK` 安装包后，通过使用 `SDK Manager.exe` 工具安装不同版本的 SDK 后自动生成一个 `platform-tools` 文件夹，该文件夹下就包含 `adb.exe` ，在配置该文件夹所在路径的环境变量后即可在 cmd 中使用 adb 命令行工具。      

&emsp;&emsp;第一种的安装方法之前就写了，现在来写写第二种安装方法的实现过程。         

<br><br>

## 二、实操部分
###### 1.环境准备
&emsp;&emsp;已成功下载 jdk 并成功配置环境变量。检查是否配置成功：      
```
$ java -version
```

<br><br>

###### 2.下载 Android SDK 安装包
链接：https://pan.baidu.com/s/12qz2QbF3EIcNAqovTBpq2Q       
提取码：afos    

&emsp;&emsp;下载后解压即可，我这里是解压到 `D:\software\android-sdk-windows`，其目录结构如下。      

![](\img\in-post\post-app-test\2021-07-15-android-sdk-install-1.png)    

<br><br>


###### 3.安装各版本的 SDK
&emsp;&emsp;可以直接使用自带的 `SDK Manager.exe` 工具进行安装，不过要翻墙，我因为买了 vpn 所以不存在这个问题。安装步骤如下：       

（1）启用 vpn 连上国外 ip          

（2）双击打开 `SDK Manager.exe` 工具        

（3）选择 SDK 版本进行下载安装          
![](\img\in-post\post-app-test\2021-07-15-android-sdk-install-2.png)     

<br>

![](\img\in-post\post-app-test\2021-07-15-android-sdk-install-3.png)    

<br>

![](\img\in-post\post-app-test\2021-07-15-android-sdk-install-4.png)  

<br>

![](\img\in-post\post-app-test\2021-07-15-android-sdk-install-5.png)    

<br>

（4）系统自动生成一个 `platform-tools` 文件夹，其目录下包含 `adb.exe`         
![](\img\in-post\post-app-test\2021-07-15-android-sdk-install-6.png)     

<br>

![](\img\in-post\post-app-test\2021-07-15-android-sdk-install-7.png)


<br><br>


###### 4.配置环境变量
（1）右键点击打开 `此电脑 > 属性 > 高级系统设置 > 环境变量`。       

（2）新增一个系统变量 ANDROID_HOME，变量配置如下：      
```
变量名    ANDROID_HOME
变量值    D:\software\android-sdk-windows
```

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-9.png)    

<br>

（3）编辑 Path 变量值后点击保存即可：         
```
新增变量值：
%ANDROID_HOME%\platform-tools
%ANDROID_HOME%\tools
%ANDROID_HOME%\build-tools\29.0.3
```

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-10.png)    

<br>

（4）新增一个系统变量 CLASSPATH，变量配置如下：      
```
变量名    CLASSPATH
变量值    %JAVA_HOME%\bin;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar
```

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-11.png) 


<br><br>

###### 5.检查 adb 是否可用
&emsp;&emsp;进入 cmd 命令行工具，输入如下命令进行检查：     

```
$ adb help
```