---
layout:        post
title:         "数据库 | DROP TABLE 报错"
subtitle:      "ERROR 1217 (23000): Cannot delete or update a parent row: a foreign key constraint fails"
author:        "Haauleon"
header-img:    "img/in-post/post-flask/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - 数据库
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、报错描述
```
mysql> DROP TABLE users;
ERROR 1217 (23000): Cannot delete or update a parent row: a foreign key constraint fails
```

<br>
<br>

### 二、报错处理
&emsp;&emsp;原因是 Foreign Key 的约束，通过关闭 Foreign Key 检查后，删除 SQL 表成功：     
```
mysql> Set FOREIGN_KEY_CHECKS = 0;    # 关闭Foreign Key检查
Query OK, 0 rows affected (0.00 sec)

mysql> DROP TABLE users;
Query OK, 0 rows affected (0.01 sec)

mysql> Set FOREIGN_KEY_CHECKS = 1;    # 恢复Foreign Key检查​
Query OK, 0 rows affected (0.00 sec)

mysql> quit;
Bye
```