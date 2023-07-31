---
layout:        post
title:         "影刀RPA | 连接 mariadb/mysql 数据库"
subtitle:      "下载安装驱动、添加数据源等操作"
author:        "Haauleon"
header-img:    "img/in-post/post-rpa/bg.jpg"
header-mask:   0.4
catalog:       true
tags:
    - 影刀RPA
---


### 一、下载驱动
mariadb 和 mysql 使用的驱动是一样的，所以只需要下载一种就够了。       

下载地址：[https://downloads.mysql.com/archives/c-odbc/](https://downloads.mysql.com/archives/c-odbc/)          
下载32位驱动：Windows (x86, 32-bit), MSI Installer       
![](\img\in-post\post-rpa\2023-07-31-yingdao-mariadb-1.png)       

网盘下载地址：           
链接：https://pan.baidu.com/s/1khg_CI0IptE4gjweZDsEQw?pwd=q4fl                  
提取码：q4fl          

<br>
<br>

### 二、安装驱动
双击已下载的 msi 文件进行安装即可，安装过程傻瓜式安装就好。      

<br>
<br>

### 三、添加数据源
#### 1、搜索并打开 ODBC Data Sources (32-bit) 
![](\img\in-post\post-rpa\2023-07-31-yingdao-mariadb-2.png)      

<br>

#### 2、添加mariadb数据源
![](\img\in-post\post-rpa\2023-07-31-yingdao-mariadb-3.png)      

![](\img\in-post\post-rpa\2023-07-31-yingdao-mariadb-4.png)      

<br>

#### 3、配置数据库信息
![](\img\in-post\post-rpa\2023-07-31-yingdao-mariadb-5.png)      

<br>
<br>

### 四、影刀连接数据库配置
#### 1、使用配置向导
![](\img\in-post\post-rpa\2023-07-31-yingdao-mariadb-6.png)          

<br>

#### 2、选择驱动
![](\img\in-post\post-rpa\2023-07-31-yingdao-mariadb-7.png)          

<br>

#### 3、选择已添加的数据源
![](\img\in-post\post-rpa\2023-07-31-yingdao-mariadb-8.png)          

<br>

#### 4、执行SQL语句
![](\img\in-post\post-rpa\2023-07-31-yingdao-mariadb-9.png)          