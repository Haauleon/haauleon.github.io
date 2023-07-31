---
layout:        post
title:         "影刀RPA | 连接 sql server 数据库"
subtitle:      "下载安装驱动、添加数据源等操作"
author:        "Haauleon"
header-img:    "img/in-post/post-rpa/bg.jpg"
header-mask:   0.4
catalog:       true
tags:
    - 影刀RPA
---


### 一、下载驱动
下载地址：[https://learn.microsoft.com/zh-cn/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16](https://learn.microsoft.com/zh-cn/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16)                
下载 Microsoft ODBC Driver 17 for SQL Server  x64版本的 msi                                
![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-1.png)        

网盘下载地址：           
链接：https://pan.baidu.com/s/1EzyXjjv9dqPhlUdfR-ggFA?pwd=l7ht             
提取码：l7ht                     

<br>
<br>

### 二、安装驱动
傻瓜式安装即可，不需要变更        
![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-2.png)          

![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-3.png)        

![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-4.png)        

![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-5.png)        

![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-6.png)        

<br>
<br>

### 三、添加数据源
#### 1、ODBC Data Sources (32-bit) 添加数据源
![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-7.png)        

![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-8.png)        

<br>

#### 2、配置数据库信息
![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-9.png)        

![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-10.png)        

![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-11.png)        

![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-12.png)        

![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-13.png)        

![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-14.png)        

<br>
<br>

### 四、影刀设置数据库
#### 1、选择驱动
![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-15.png)        

<br>

#### 2、选择已添加的数据源
![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-16.png)        

<br>

#### 3、编辑数据库连接字符串
SQL Server 的数据源配置无法保存密码和无法设置默认数据库，因此需要手动编辑数据库连接字符串。             
**模板**：Provider=MSDASQL.1;Persist Security Info=False;User ID=<用户名>;Password=<密码>;Initial Catalog=<数据库>;Data Source=<已添加的数据源名称>             

**示例**：Provider=MSDASQL.1;Persist Security Info=False;User ID=sa;Password=Ejet@xL3#lM3?oM;Initial Catalog=SalesOrderRecord;Data Source=192.168.1.200             
![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-17.png)        

<br>

#### 4、执行SQL语句
![](\img\in-post\post-rpa\2023-07-31-yingdao-sqlserver-18.png)        
