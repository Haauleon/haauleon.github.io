---
layout:        post
title:         "Android | adb 基本使用"
subtitle:      "adb 命令的简单使用"
author:        "Haauleon"
header-img:    "img/in-post/post-app-test/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Android
---

## 一、adb 命令
###### 1.工作原理
&emsp;&emsp;安卓设备连接成功后，使用命令 `$ adb devices` 启动某个 adb 客户端时，该客户端会先检查是否有 adb 服务器进程正在运行。如果没有，它会启动服务器进程。服务器在启动后会与本地 TCP 端口 5037 绑定，并监听 adb 客户端发出的命令。**所有 adb 客户端均通过端口 5037 与 adb 服务器通信**。      

&emsp;&emsp;然后，服务器会与所有正在运行的设备建立连接。它通过扫描 5555 到 5585 之间（该范围供前 16 个模拟器使用）的奇数号端口查找模拟器。服务器一旦发现 adb 守护程序 (adbd)，便会与相应的端口建立连接。请注意，每个模拟器都使用一对按顺序排列的端口 - 用于控制台连接的偶数号端口和用于 adb 连接的奇数号端口。例如：      

```
模拟器 1，控制台：5554
模拟器 1，adb：5555
模拟器 2，控制台：5556
模拟器 2，adb：5557
依此类推
```

&emsp;&emsp;如上所示，在端口 5555 处与 adb 连接的模拟器与控制台监听端口为 5554 的模拟器是同一个。        

&emsp;&emsp;服务器与所有设备均建立连接后，就可以使用 adb 命令访问这些设备。由于服务器管理与设备的连接，并处理来自多个 adb 客户端的命令，因此可以从任意客户端（或从某个脚本）控制任意设备。      

<br><br>

## 二、实操部分
###### 1.使用 usb 连接安卓机
&emsp;&emsp;目前是使用 usb 数据线连接安卓机和一台 windows 笔记本。这就是我全部的资源了。     

<br><br>

###### 2.配置安卓机开发者选项    
![](\img\in-post\post-app-test\2021-07-13-adb-base-use-1.png)    

<br>

![](\img\in-post\post-app-test\2021-07-13-adb-base-use-2.png)   

<br>

![](\img\in-post\post-app-test\2021-07-13-adb-base-use-3.png)   

<br>

![](\img\in-post\post-app-test\2021-07-13-adb-base-use-4.png)  

<br><br>

###### 3.adb 命令启动服务器    
&emsp;&emsp;一般习惯先 `$ adb kill-server` 干掉服务器再 `$ adb start-server` 启动服务器，这样可以保证一个干净的环境。在使用 `$ adb start-server` 命令的时候会要求在安卓机允许 USB 调试。       

```
C:\Users\Haauleon>adb kill-server

C:\Users\Haauleon>adb start-server
* daemon not running; starting now at tcp:5037
* daemon started successfully
```

<br>

![](\img\in-post\post-app-test\2021-07-13-adb-base-use-5.png)    


<br><br>

###### 4.基本 adb 命令使用
```
C:\Users\Haauleon>adb devices -l
List of devices attached
dd926a61               device product:R9sk model:OPPO_R9sk device:R9sk transport_id:1


C:\Users\Haauleon>adb shell pm list package
package:com.coloros.backuprestore
package:com.oppo.logkitsdservice
package:com.oppo.ctautoregist
package:com.coloros.phonenoareainquire
package:com.oppo.oppopowermonitor
package:com.android.providers.telephony
package:com.coloros.wirelesssettings
package:com.gnss.power
```