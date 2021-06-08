---
layout: post
title: "WSL | Running node error"
subtitle: "在 windows 的子系统上安装 node 的问题解决"
author: "Haauleon"
header-style: text
tags:
  - 异常库
  - Nodejs
---

**问题背景：**       
&emsp;&emsp;WSL，也就是 Windows 上的 Ubuntu 子系统，在使用命令 `$ sudo apt install nodejs` 安装完成后，想检查是否成功安装。在输入命令行 `$ npm -v` 回车后，提示以下错误：        
```
: not foundram Files/nodejs/npm: 3: /mnt/c/Program Files/nodejs/npm:
: not foundram Files/nodejs/npm: 5: /mnt/c/Program Files/nodejs/npm:
/mnt/c/Program Files/nodejs/npm: 6: /mnt/c/Program Files/nodejs/npm: Syntax error: word unexpected (expecting "in")
```     
<br><br>

**解决方法：**
&emsp;&emsp;查了一下解决方案。[https://www.reddit.com/r/node/duplicates/650g4i/running_node_on_wsl/](https://www.reddit.com/r/node/duplicates/650g4i/running_node_on_wsl/)        

![](\img\in-post\others\2021-03-26-wsl-node-error-1.png)