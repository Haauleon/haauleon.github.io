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

> 虚拟机安装在主机上，必须在主机上才能运行，主机就是一个宿主，则相对于虚拟机而言，正在使用的计算机就是宿主机。

<br>

###### 1、安装 VirtualBox
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
&emsp;&emsp;Vagrant 用来操作 VirtualBox、VMWar、AWS 这些虚拟机系统，可以很快地完成一套开发环境的部署。直接启动就好，不需要了解所有相关环境的知识和细节。可以通过 `vagrant provision` ，使用 Shell 脚本或者主流的配置管理工具（如 Puppet、Ansible等）对软件进行自动安装、更新和配置管理。  

<br>

###### 1、安装 Vagrant
（1）进入[官网](https://www.vagrantup.com/)下载        
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-10.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-11.jpg) 

<br>
<br>

（2）双击进行安装      
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-12.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-13.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-14.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-15.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-16.jpg)    