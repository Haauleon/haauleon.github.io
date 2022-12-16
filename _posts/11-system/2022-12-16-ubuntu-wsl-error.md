---
layout:        post
title:         "Windows11 | 启动 WSL 报错"
subtitle:      "请启用虚拟机平台 Windows 功能并确保在 BIOS 中启用虚拟化"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 操作系统
    - Ubuntu
    - Windows
---

> 本篇所有操作均在 64 位的 Windows 11 系统下执行

<br>
<br>

### 报错原因
&emsp;&emsp;早前启动蓝叠模拟器的时候会自动关闭了 Hyper-V 这个功能，导致了我的 WSL 运行报错，提示 “请启用虚拟机平台 Windows 功能并确保在 BIOS 中启用虚拟化”，在网上找了很多答案，终于搞定了。    

<br>
<br>

### 解决方法
1. 点击 `开始` 菜单搜索 `计算机管理` 并进入，将所有 Hyper-V 有关的服务全部设置为自动启动。      
    ![](https://img-blog.csdnimg.cn/8bc53cc210d94b2196d575a1c7f34348.png)
2. 确认BIOS中已经开启虚拟化。按 `ctrl+alt+del` 打开任务管理器，点击 `性能 > CPU` 会显示是否开启 `虚拟化`      
3. 必须安装Windows自带的虚拟机软件hyper-v、虚拟机平台。进入 `设置 > 应用 > 可选功能 > 更多Windows功能` 找到并安装 `适用于Linux的Windows系统`、`Windows虚拟机监控程序平台` 和 `虚拟机平台` 完成后必须重启电脑          
4. 上述功能都正常，就有可能是关闭了 `虚拟化的安全` 功能导致。按 `Win+X` 快捷键，选择 `Window 终端（管理员）`，输入命令 `> bcdedit /set hypervisorlaunchtype auto` 回车，重启电脑即可解决。注意：开启 `虚拟化的安全` 功能会导致雷电、MUMU、蓝叠等安卓模拟器无法启动。


<br>
<br>

相关链接：    
[请启用虚拟机平台 Windows 功能并确保在 BIOS 中启用虚拟化](https://blog.csdn.net/weixin_45112649/article/details/126715321)    
[wsl set default version: 请启用虚拟机平台 windows 功能并确保在 bios 中启用虚拟化](https://blog.csdn.net/Antarctic_Bear/article/details/123489609)    
[windows 11 Android子系统启用虚拟机平台解决方法](http://www.manongjc.com/detail/27-kzrkvohhtaadtey.html)     
[这就是修复 Windows 11 的 WSL 错误的方法](https://www.yundongfang.com/Yun144781.html)