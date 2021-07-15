---
layout:        post
title:         "Android | adb 命令行工具的安装"
subtitle:      "通过 SDK Platform Tools 进行安装"
date:          2021-07-02
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - APP 测试
---

## adb 简介
&emsp;&emsp;Android Debug Bridge (adb) 即安卓调试桥。是一种功能多样的命令行工具，可让开发者与设备进行通信。adb 命令可用于执行各种设备操作（例如安装和调试应用），并提供对 Unix shell（可用来在设备上运行各种命令）的访问权限。它是一种客户端-服务器程序，包括以下三个组件：                    
* 客户端：用于发送命令。客户端在开发计算机上运行。开发者可以通过发出 adb 命令从命令行终端调用客户端。   
* 守护程序 (adbd)：用于在设备上运行命令。守护程序在每个设备上作为后台进程运行。   
* 服务器：用于管理客户端与守护程序之间的通信。服务器在开发机器上作为后台进程运行。          

<br><br>

## 下载安装
###### 下载 zip 安装包
&emsp;&emsp;独立的 Android SDK 平台工具软件包下载地址：[SDK Platform Tools 下载地址（需翻墙）](https://developer.android.com/studio/releases/platform-tools)。已下载好的基于 windows 平台软件包（adb 版本为 1.0.41）链接：https://pan.baidu.com/s/11_9M2FzlFzxugbD1u9AMVQ 提取码：w6x4          

&emsp;&emsp;解压完成后需要配置系统变量。      

<br><br>

###### 配置系统变量
&emsp;&emsp;解压之后找到 adb.exe 所在的目录，然后将此目录所在的绝对路径添加至系统变量中。             

![](\img\in-post\post-app-test\2021-07-02-android-adb-install-1.png)     

<br>

![](\img\in-post\post-app-test\2021-07-02-android-adb-install-2.png)

<br>

![](\img\in-post\post-app-test\2021-07-02-android-adb-install-3.png)

<br>

![](\img\in-post\post-app-test\2021-07-02-android-adb-install-4.png)

<br><br>

## adb 命令行工具
![](\img\in-post\post-app-test\2021-07-02-android-adb-install-5.png)

<br><br>

###### 检查工具安装
```
C:\Users\Haauleon>adb version
Android Debug Bridge version 1.0.41
Version 31.0.2-7242960
Installed as D:\software\platform-tools\adb.exe
```
