---
layout:        post
title:         "MacOS 安装 MySQL"
subtitle:      ""
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - MacOs
    - 数据库
---

### 下载
&emsp;&emsp;打开 MySQL 官网下载对应操作系统类型 - 对应系统版本 - 对应 mysql 版本：[https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/)。当前系统为 MacOS 10.15 版本，则从 Archives 列表内筛选并下载系统版本为 10.15 的 dmg 文件即可。       

**已成功下载的 mysql-8.0.23-macos10.15-x86_64.dmg 百度网盘资源：**     
链接: https://pan.baidu.com/s/1LmzHOB17LbVC_FUmDzSkdQ?pwd=jl3u     
提取码: jl3u 

<br><br>

### 安装
&emsp;&emsp;双击已下载完成的 .dmg 文件，然后双击安装器中的 .pkg 文件进行安装。安装要点如下：     
1. **安装**: 需要输入本机的管理员密码      
2. **Configuration**: 选择 `Use Strong Password Encryption` ，然后设置 root 用户密码     
    
<br><br>

### 配置
1. 配置系统环境变量           
    `$ vim ~/.zprofile` 
2. 在文件末尾添加以下内容并保存       
    ```
    # mysql
    export PATH=/usr/local/mysql/bin:$PATH
    ```
3. 激活配置   
    `$ source ~/.zprofile`
4. 使用安装过程中设置的 root 用户密码登录本地 mysql 服务端         
    `$ mysql -u root -p`