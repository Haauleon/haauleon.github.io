---
layout:        post
title:         "Ubuntu | 服务器后台运行程序"
subtitle:      "服务器后台运行程序 screen"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 操作系统
    - Ubuntu
---


<br>
<br>

### 一、背景
&emsp;&emsp;最近在服务器上跑程序，但是超时连接后就自动断开了，程序也停止了。后来用到了 screen，挺好用的。          

<br>
<br>

### 二、screen命令

#### 1、安装
命令行输入下面的命令检查是否安装，没有会提示程序"screen"尚未安装。             
```bash
> screen -ls
```

未安装则输入如下命令安装：     
```bash
> sudo apt install screen
```

<br>
<br>

#### 2、使用
（1）创建新的窗口             
```bash
> screen -S <自定义的窗口名称>
```

（2）查看当前已经创建的全部窗口          
```bash
> screen -ls
```

（3）回到指定的窗口         
```bash
> screen -d -r <自定义的窗口名称>
```

（4）关闭指定的窗口     
```bash
> screen -X -S <自定义的窗口名称> quit
```
或者使用组合键 `ctrl + d`        


<br>
<br>

---

相关链接：   
[服务器后台运行程序（nohup/screen/tmux）](https://blog.csdn.net/zeronose/article/details/122263384)。