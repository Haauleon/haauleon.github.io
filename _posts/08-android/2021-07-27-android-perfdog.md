---
layout:        post
title:         "Android | PerfDog 采集性能指标"
subtitle:      "使用 PerfDog 采集性能指标并上传至云端分析"
date:          2021-07-27
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 数据分析
    - Android
---

## 一、背景
&emsp;&emsp;PerfDog 作为移动全平台 iOS/Android 性能测试、分析工具平台。能够快速定位分析性能问题，提升 APP 应用及游戏性能和品质。手机无需 ROOT/越狱，手机硬件、游戏及应用 APP 也无需做任何修改，极简化即插即用。               

&emsp;&emsp;PerfDog 支持移动平台所有应用程序（游戏、APP 应用、浏览器、小程序、小游戏、H5、后台系统进程等）、Android 模拟器、云真机等性能测试。支持 APP 多进程测试（如 Android 多子进程及 iOS 扩展进程 APP Extension）。        

&emsp;&emsp;Windows & Mac OS X 平台 PerfDog 桌面应用程序版本都支持对 iOS 和 Android 设备进行测试。PC 上 PerfDog 可多开，单 PC 可同时测试多台手机。     

&emsp;&emsp;安卓系统和苹果系统相比，性能问题出现较多，所以此次来采集一下安卓系统的性能指标。这里使用到了 PerfDog 性能测试工具，主要用于采集 app 的性能指标。[PerfDog 的官网](https://perfdog.qq.com/)。采集结果如下：      
![](\img\in-post\post-app-test\2021-07-27-perfdog-1.png)    

<br>

![](\img\in-post\post-app-test\2021-07-27-perfdog-2.png)

<br><br>

## 二、实操部分
###### 1.环境准备
（1）进入[官网](https://perfdog.qq.com/)根据自己的操作系统下载对应的版本，我用的是 win10 就下载 windows 版本      
（2）解压后找到程序 `PerfDog.exe` 直接发送至桌面快捷方式      
（3）在桌面双击打开客户端，此操作需要在官网注册一个账号       
（4）使用 USB 连接安卓机和电脑，此操作需要在安卓机的开发者选项中点击允许调试          

<br><br>

###### 2.选择待测机型
![](\img\in-post\post-app-test\2021-07-27-perfdog-3.png)

<br><br>

###### 3.选择待测应用
&emsp;&emsp;在选择应用之前需要提前在安卓机上启动对应的应用，否则无法进行指标采集。        
![](\img\in-post\post-app-test\2021-07-27-perfdog-4.png)

<br><br>

###### 4.操作应用
&emsp;&emsp;进入应用的性能测试后，就可以开始在安卓机上操作此应用了。可以按场景来划分测试用例，比如要测试商品加购、商品下单的场景等。       

<br><br>

###### 5.PerfDog 添加场景标记
&emsp;&emsp;PerfDog 支持添加测试场景标记，当进入性能测试指标采集后，它默认创建第一个标记 `Lable1`，可以双击进行重命名。         
![](\img\in-post\post-app-test\2021-07-27-perfdog-5.png)

<br><br>

###### 6.PerfDog 添加操作标注
&emsp;&emsp;一个测试场景可以由几个不同的操作步骤组成，PerfDog 支持添加操作标注，它默认不创建，仅由用户拖动鼠标并双击进行创建。       
![](\img\in-post\post-app-test\2021-07-27-perfdog-6.png)      

<br><br>

###### 7.上传性能指标至云端
![](\img\in-post\post-app-test\2021-07-27-perfdog-7.png)      

<br>

![](\img\in-post\post-app-test\2021-07-27-perfdog-8.png)    

<br>

![](\img\in-post\post-app-test\2021-07-27-perfdog-9.png)  

<br><br>

###### 8.进入云端数据     
&emsp;&emsp;数据上传成功后，就可以在浏览器打开[我的数据](https://perfdog.qq.com/mydata/cases)页面进行查看。       
![](\img\in-post\post-app-test\2021-07-27-perfdog-10.png)  

<br><br>

## 三、性能指标分析
&emsp;&emsp;可以多次采集（不同机型、不同系统版本或者性能优化前后）应用的性能指标，然后上传至云端加入对比，就可以轻而易举地进行分析。       
![](\img\in-post\post-app-test\2021-07-27-perfdog-11.png)    

<br>  

![](\img\in-post\post-app-test\2021-07-27-perfdog-12.png)