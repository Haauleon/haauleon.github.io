---
layout:        post
title:         "数据库 | Windows 安装 MySQL"
subtitle:      "下载、安装和使用命令"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Windows
    - 数据库
---

### 下载
进入官网下载：[https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)       

百度网盘资源：        
链接：https://pan.baidu.com/s/1dNFDFmuJ5P--5GVMcjFMNw?pwd=t66y     
提取码：t66y      

<br><br>


### 安装、配置
1. 解压已经下载好的 .zip 安装包到 c 盘，我是放到 `C:\Program Files\` 下       
2. 在左下角中输入 cmd 后点击 `以管理员身份运行`       
3. 在 cmd 窗口中使用命令行 `$ cd C:\Program Files\mysql-8.0.29-winx64\bin` 进行 bin 目录      
4. 使用以下命令行初始化数据库，然后记录随机生成的 root 用户密码 bJvW,tgO9n6M               
    ```
    $ mysqld --initialize --console
    initializing of server in progress as process 22388
    2022-06-07T12:21:53.160001Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
    2022-06-07T12:21:53.681532Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
    2022-06-07T12:21:55.229123Z 6 [Note] [MY-010454] [Server] A temporary password is generated for root@localhost: bJvW,tgO9n6M
    ```
5. 使用以下命令行将 mysql 安装为 windows 的服务          
    ```
    $ mysqld -install
    Service successfully installed.
    ```
6. 输入 `$ net start mysql` 或 `$ sc start mysql` 启动 mysql 服务       
    ```
    $ net start mysql
    ```