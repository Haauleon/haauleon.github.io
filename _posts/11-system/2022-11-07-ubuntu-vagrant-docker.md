---
layout:        post
title:         "Ubuntu | 使用Docker和Vagrant安装Ubuntu"
subtitle:      "搭建一个能运行的虚拟机环境"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 操作系统
    - Web开发
---

### 一、VirtualBox
&emsp;&emsp;VirtualBox 是 Oracle 开源的虚拟化系统，支持 Linux 、OS X、Windows 等平台，Docker 和 Vagrant 环境都需要它作为宿主机。     

> 虚拟机安装在主机上，必须在主机上才能运行，主机就是一个“宿主”，则相对于虚拟机而言，正在使用的计算机就是宿主机。

<br>

###### 1、安装 VirtualBox
**Windows 11 系统安装 VirtualBox**     

（1）进入[官网](https://www.virtualbox.org/)下载最新版       
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-1.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-2.jpg)    
   
<br>
<br>

（2）双击进行安装      
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-3.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-4.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-5.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-6.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-7.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-8.jpg)    

<br>
<br>

（3）进入 VirtualBox 主页    
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-9.jpg)    

<br>
<br>

### 二、Vagrant

###### 1、安装 Vagrant
