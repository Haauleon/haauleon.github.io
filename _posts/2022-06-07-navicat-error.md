---
layout:        post
title:         "数据库 | Navicat 连接 mysql8.0 版本报错"
subtitle:      "MySql错误 1251 - Client does not support authentication protocol requested by server 解决方案"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Windows
    - 数据库
---

### 背景
&emsp;&emsp;本地刚装完 mysql8.0 版本，已经启动 mysql 服务成功了，然后我用 navicat 连接本地 mysql 数据库，输入 root 密码后点击连接测试，提示 `1251 - Client does not support authentication protocol requested by server;` 。      

<br><br>

### 解决方案
1. 确认已经启动了 mysql 服务      
    ```
    $ net start mysql
    ```
2. 使用 root 账号登录数据库     
    ```
    $ mysql -u root -p
    ```
3. 依次输入以下两条命令行      
    ```
    mysql> alter user 'root'@'localhost' identified with mysql_native_password by 'root用户密码';
    Query OK, 0 rows affected (0.00 sec)

    mysql> flush privileges;
    Query OK, 0 rows affected (0.00 sec)
    ```
4. 重新使用 navicat 进行连接，即可解决     