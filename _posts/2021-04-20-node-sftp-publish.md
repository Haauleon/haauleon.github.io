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
&emsp;&emsp;我的想法是在 jenkins 上自动构建自动化测试后，生成的 html 测试报告文件自动上传至我的阿里云服务器（服务器已使用 Nginx 部署完成）进行访问，解决读取邮件、发送邮件效率的问题。看网上很多人集成到 jenkins 后第一反应就是发邮件，但是我觉得发邮件是一种很古老的技术了，加上我真的很不喜欢看邮件，有什么比直接看钉钉消息、微信微信更方便的吗？     

&emsp;&emsp;使用本教程需安装 Nodejs 。

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
&emsp;&emsp;进入要传输的文件所在的当前目录，创建一个配置文件 `sftp.json`，并写入以下配置内容：       

```
$ cd 要传输的文件所在的目录
$ touch sftp.json # 创建文件
$ vim sftp.json # 编辑文件
$ cat sftp.json # 显示文件内容
```
<br>

```json
{
    "localPath": "./",                           # 本地要传输的文件所在的相对路径
    "remotePath": "/usr/test-haauleon",          # 远程绝对路径
    "protectedRemotePath": "/usr/test-haauleon", # 远程绝对路径
    "connect": {
        "host": "112.74.205.108",                # 远程服务器 ip
        "port": 22,
        "username": "root",
        "password": "服务器root密码"
    }
}
```    

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