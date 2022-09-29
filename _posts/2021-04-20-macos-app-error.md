---
layout:        post
title:         "macOs | 无法打开软件"
subtitle:      "无法打开xxx.app，因为Apple无法检查其是否包含恶意软件"
date:          2021-04-19
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - macOs
    - 异常库
---

## 问题描述
&emsp;&emsp;从网站上下载了一下 `xxx.dmg` 文件，安装完成后点击启用此 app，启动失败，提示 `无法打开xxx.app，因为Apple无法检查其是否包含恶意软件`。现在附上解决办法。     

<br><br>

## 解决方法
###### 方法一：命令行工具
1.打开 terminal 命令行工具          
输入命令：`$ sudo spctl --master-disable`          
输入密码          

2.再次启动软件，即可解决

<br><br>

###### 方法二：修改安全设置
进入系统偏好设置 —— 安全性与隐私 —— 通用          

![](\haauleon\img\in-post\post-error\2021-04-20-macos-app-error-1.jpg)
