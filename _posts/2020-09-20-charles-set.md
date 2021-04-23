---
layout:        post
title:         "Charles | 代理设置"
subtitle:      "设置手机代理"
date:          2020-09-20
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Charles
---


## 背景
&emsp;&emsp;换了台 macos 系统的 mac mini，最近抓包工作从 fiddler 转移到了 charles。     

<br><br>

## 使用技巧
###### 一、Charles 代理设置
&emsp;&emsp;首先我们得在 `Proxy--Proxy Setting` 中设置代理端口号，默认 8888，一般用默认的就行，除非和电脑上其他端口有冲突，下面的勾 `√` 也有勾上，这是为了能抓取 HPPTS 数据的。                           

![](\img\in-post\post-charles\2020-09-20-charles-set-1.png)                                 

<br><br>

###### 二、安装证书到电脑
&emsp;&emsp;Charles 证书安装在电脑里，点击 `Help--SSL Proxying--Install Charles Root Certificate` 。                                 

![](\img\in-post\post-charles\2020-09-20-charles-set-2.png)     

<br>

&emsp;&emsp;点击安装后，在证书列表里找到它，设置始终信任它就行，我这是 Mac，windows 好像更简单，全部下一步就行。               

![](\img\in-post\post-charles\2020-09-20-charles-set-3.png)                         

<br>

![](\img\in-post\post-charles\2020-09-20-charles-set-4.png)                                   

<br><br>

###### 三、查看电脑ip
![](\img\in-post\post-charles\2020-09-20-charles-set-5.png)                        

<br>

![](\img\in-post\post-charles\2020-09-20-charles-set-6.png)                          

<br><br>

###### 四、安装证书到手机
&emsp;&emsp;首先，我们让手机和电脑子啊同一局域网下，先查看下电脑的 IP，Windows 电脑 cmd 里输入 ipconfig 命令查看 IP，Mac 电脑在终端输入 ifconfig 查看 IP，手机的无线网里设置代理，填上刚查到的 IP 和端口号 8888。                            

![](\img\in-post\post-charles\2020-09-20-charles-set-7.png)                       

<br>

&emsp;&emsp;如果手机是第一次和电脑连接，Charles 上会有弹窗提示，选择 Allow 同意即可。                        

![](\img\in-post\post-charles\2020-09-20-charles-set-8.png) 

<br>

&emsp;&emsp;连上之后，我们点击 `Help--SSL Proxying--Install Charles Root Certificate on a Mobile Devices or Remote Browser`，这时会弹窗告诉我们怎么做。                                          

![](\img\in-post\post-charles\2020-09-20-charles-set-9.png)                                  

<br>

&emsp;&emsp;弹窗的意思是让我们手机连上代理后，手机浏览器里输入 `chls.pro/ssl` 网址，下载安装证书。                           

![](\img\in-post\post-charles\2020-09-20-charles-set-10.png) 

<br>

&emsp;&emsp;下载后安装就可以了，我这是 Android 手机，苹果手机多一步信任证书的步骤，这点要注意。证书都安装完成后，操作手机上的 APP，就会抓到大量的数据信息了。                                        

![](\img\in-post\post-charles\2020-09-20-charles-set-11.png) 