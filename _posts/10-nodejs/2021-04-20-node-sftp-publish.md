---
layout:        post
title:         "Nodejs | 本地文件自动上传"
subtitle:      "使用 sftp-publish 工具自动上传本地文件至服务器"
date:          2021-04-19
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Nodejs
---

## 背景
![](\haauleon\img\in-post\post-other\2021-04-20-node-sftp-publish-5.jpg)

<br><br>

## 使用技巧
###### 一、安装 nodejs      
&emsp;&emsp;直接去官网下载 nodejs 安装包，解压安装即可。        

<br><br>

###### 二、安装 nodejs 工具
&emsp;&emsp;使用 npm 软件包管理工具安装 `sftp-publish`。      

```
$ sudo npm i sftp-publish -g
$ sudo npm link publish-sftp
```
<br>

![](\haauleon\img\in-post\post-node\2021-04-20-node-sftp-publish-1.jpg)

<br><br>

###### 三、新建配置文件
![](\haauleon\img\in-post\post-other\2021-04-20-node-sftp-publish-6.jpg)  

<br>

&emsp;&emsp;本地要传输的文件如下：     

![](\haauleon\img\in-post\post-node\2021-04-20-node-sftp-publish-2.jpg)

<br><br>

###### 四、使用命令行传输
&emsp;&emsp;配置完成后进入终端，使用命令行进行传输。      

```
$ publish-sftp -c
```
&emsp;&emsp;此命令默认将本地 sftp.json 文件所在的相对路径 `"localPath": "./"` 下的所有文件上传至远程 `"remotePath": "/usr/test-haauleon"` 目录。也可使用 `$ publish-sftp -c haauleon(自定义目标目录名)`，即可将文件上传至远程 `"remotePath": "/usr/test-haauleon/haauleon"` 目录。       

&emsp;&emsp;本地要传输的文件如下：

![](\haauleon\img\in-post\post-node\2021-04-20-node-sftp-publish-2.jpg)

<br><br>

###### 五、传输完成
![](\haauleon\img\in-post\post-node\2021-04-20-node-sftp-publish-3.jpg)

<br><br>

## 结论
&emsp;&emsp;跟 ssh 连接、ftp 传输的原理差不多，只不过配置写到 json 文件里面，可以通过命令行去执行和传输。一切通过命令行执行的动作皆可集成到 jenkins。