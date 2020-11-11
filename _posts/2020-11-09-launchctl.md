---
layout: post
title: "Mac | launchctl 定时任务"
subtitle: "我就围观一下顺带实地操作一番，看看效果"
author: "Haauleon"
header-style: text
tags:
  - Mac 小玩意
---

## 背景 
&emsp;&emsp;最近换了个 mac mini 来玩玩，之前试过 windows 自带的任务管理，其实对于执行周期性的任务而言，在本地添加定时任务的方法也是可取的，成本也比较低，不用重新跑在别的系统上免得还要重新搭建环境。这次在 MacOS 上使用 launchctl 来添加定时任务，不同于 linux 的 crontab，**它可以通过 plist 文件来指定执行周期性任务**，且任务重复执行间隔的最小单位是 1 秒，而 crontab 最小单位只能到 1 分。而且 plist 对于 mac 系统交互的操作更支持。              

<br><br>

## plist 文件存在的目录  
```
1.由用户自己定义的任务项（用户登录后启动的服务）
$ ~/Library/LaunchAgents  

2.由管理员为用户定义的任务项（用户登录后启动的服务）
$ /Library/LaunchAgents

3.由管理员定义的守护进程任务项（用户未登陆前就启动的服务）
$ /Library/LaunchDaemons

4.由Mac OS X为用户定义的任务项（用户登录后启动的服务）
$ /System/Library/LaunchAgents

5.由Mac OS X定义的守护进程任务项（用户未登陆前就启动的服务）
$ /System/Library/LaunchDaemons
```

&emsp;&emsp;一般都会将 plist 放置在 /Library/LaunchDaemons 下，可在终端使用输入命令行 `$ open /Library/LaunchDaemons` 查看此目录下的 plist 文件。     

![](\img\in-post\2020-11-09-launchctl\1.jpg)     


&emsp;&emsp;点开其中一个 plist 文件查看任务配置。            

![](\img\in-post\2020-11-09-launchctl\2.jpg)  

<br><br>

## 实操部分 
&emsp;&emsp;实现每隔 30 秒执行一次钉钉报警脚本，执行结果向钉钉群聊发送消息。发送成功即配置成功，发送失败即配置失败。    

<br>

**编写任务配置文件**     
编写文件`com.dingding.notice.task`存放于`/Library/LaunchDaemons`下。       
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<!-- 名称不可重复-->
	<key>Label</key>
	<string>com.dingding.notice.task</string>
	<!-- 脚本存放的绝对路径 -->
	<key>Program</key>
	<string>xxxx/xxxxx/xxxxxxx/xxxxx.py</string>
	<!-- 运行间隔，与StartCalenderInterval使用其一，单位为秒 -->
	<key>StartInterval</key>
    <integer>30</integer>
    <!-- 错误输出 -->
	<key>StandardErrorPath</key>
	<string>/Users/luoliang/Desktop/errorlog</string>
</dict>
</plist>
```

<br><br>
。。。。。。这篇博文烂尾了，遇到了好多问题，等解决完了再更新一版