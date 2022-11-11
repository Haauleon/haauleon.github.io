---
layout:        post
title:         "环境搭建 | pip 高级用法"
subtitle:      "命令自动补全，使用 devapi 作为缓存代理服务器，PYPI 的完全镜像"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - Web开发
    - Vagrant
    - Ubuntu
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、命令自动补全
**zsh 用户**      
&emsp;&emsp;pip 支持自动补全功能，zsh 用户可以使用以下命令实现 pip 命令自动补全，如下输入 i + Tab键后自动补全 install：        
```
❯ zsh
❯ pip completion --zsh >> ~/.zprofile    
❯ source ~/.zprofile
❯ pip i<Tab键>
```

<br>

**bash 用户**      
```
❯ bash
ubuntu@WEB:~$ pip completion --bash >> ~/.profile
ubuntu@WEB:~$ source ~/.profile
ubuntu@WEB:~$ pip i<Tab键>
```

<br>

&emsp;&emsp;如上所述，zsh 的环境变量是 ~/.zprofile 文件，而 bash 的环境变量是 ~/.profile 文件。每次使用 zsh/bash 切换环境时，都要执行 `source <环境变量文件>` 命令来保存对应的环境变量文件从而使其生效，后续才可以使用 pip 的命令自动补全功能。    

<br>
<br>

### 二、