---
layout:        post
title:         "Fiddler | 代理设置"
subtitle:      "设置手机代理"
date:          2018-01-12
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Fiddler
---


# 设置手机代理

###### fiddler 的安装
**Step1：下载安装 fiddler**          
&emsp;&emsp;在桌面版应用市场搜索 fiddler 并下载安装。我这里为了方便直接在“软件管理”客户端进行下载安装，快速敏捷又方便。               

![](\img\in-post\post-fiddler\2018-01-12-fiddlder-set-1.png)           

<br><br>

###### fiddler 的设置
**Step1：设置 https 选项**
&emsp;&emsp;设置 fiddler：Tools > Fiddler Options > https 选项。                               
![](\img\in-post\post-fiddler\2018-01-12-fiddlder-set-2.png)         

<br><br>

**Step2：设置 connections 选项**        
&emsp;&emsp;设置 fiddler：`Tools > Fiddler Options > connections` 选项。这里的端口 port 需要记一下，手机设置代理时需要用到。             
![](\img\in-post\post-fiddler\2018-01-12-fiddlder-set-3.png) 

<br><br>

**Step3：重启 fiddler**          
&emsp;&emsp;设置完之后，重启 fiddler 。打开 cmd 控制台，输入 ipconfig 获取 IPV4 地址。这里的 IP 也需要记一下，手机设置代理时需要用到。                             
![](\img\in-post\post-fiddler\2018-01-12-fiddlder-set-4.png)         

<br><br>

###### 抓取 http 接口
**Step1：电脑联网和手机联网在同一个局域网**                
&emsp;&emsp;打开手机 WLAN，连接的 wifi 需要和电脑连接的 wifi 是一样的。  

<br><br>

**Step2：手机代理信息设置**       
&emsp;&emsp;在 wifi 详情页面设置代理信息，分别写入 IP 地址和端口 port。不同的手机系统对应的页面可能不一样，但是需要设置的的信息是相同的。         
![](\img\in-post\post-fiddler\2018-01-12-fiddlder-set-5.png)      

<br><br>

**Step3：对手机应用进行 http 抓包**
&emsp;&emsp;设置完成后打开 fiddler，即可抓取到手机应用的 http 协议下的接口。                             

<br><br>

###### 抓取 https 接口             
**Step1：电脑联网和手机联网在同一个局域网**                
&emsp;&emsp;打开手机 WLAN，连接的 wifi 需要和电脑连接的 wifi 是一样的。            

<br><br>

**Step2：手机代理信息设置**       
&emsp;&emsp;在 wifi 详情页面设置代理信息，分别写入 IP 地址和端口 port。           
    
<br><br>           

**Step3：下载安装 fiddler 证书**           
&emsp;&emsp;下载安装 fiddler 证书即可抓取 https 接口。进入手机浏览器，在地址栏输入 `http://[电脑本机ip]:[fiddler设置的port]`（如：http://192.168.2.2:8866）进行访问，访问成功后在页面上点击下载 fiddler 证书，然后在隐私设置中安装并使用此证书。完成此操作步骤后即可抓取 https 接口。
