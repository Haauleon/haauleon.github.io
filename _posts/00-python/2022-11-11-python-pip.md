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
#### 1、查看当前的 shell
查看当前发行版可以使用的 shell 有哪些：             
参考：[直达链接](https://blog.csdn.net/Michael177/article/details/124369188)         
```
❯ cat /etc/shells
# /etc/shells: valid login shells
/bin/sh
/bin/dash
/bin/bash
/bin/rbash
/usr/bin/tmux
/usr/bin/screen
/bin/zsh
/usr/bin/zsh
```

<br>

使用一条命令即可查看 ubuntu 系统当前正在使用的 shell：     
```
$ ps -ef | grep `echo $$` | grep -v grep | grep -v ps
```  
**① bash**     
```
❯ bash
ubuntu@WEB:~$ ps -ef | grep `echo $$` | grep -v grep | grep -v ps
ubuntu    2217  2150  0 15:04 pts/0    00:00:00 bash
```
**② zsh**     
```
ubuntu@WEB:~$ zsh

~ ubuntu@WEB
❯ ps -ef | grep `echo $$` | grep -v grep | grep -v ps
ubuntu    2240  2217  7 15:05 pts/0    00:00:00 zsh
ubuntu    2273  2240  0 15:05 pts/9    00:00:00 zsh
```


<br>
<br>

#### 2、不同 shell 的配置
**zsh 用户**      
&emsp;&emsp;pip 支持自动补全功能，zsh 用户可以使用以下命令实现 pip 命令自动补全，如下输入 i + Tab键后会自动补全 install：          
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

### 二、devapi 缓存代理服务器
&emsp;&emsp;pip 缓存只针对当前的用户，如果公司使用 Python 的规模很大，尤其是有很多自己分发的包时，使用缓存代理服务器可以很大程度提高下载效率，从而不再依赖网络环境到 PYPI 进行下载包了。      

安装 devapi 缓存代理服务器：    
```

```