---
layout:        post
title:         "Jmeter | 数据库接口测试"
subtitle:      "使用 Jmeter 进行数据库测试"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
    - API 测试
---

### 一、Jmeter 数据库测试
&emsp;&emsp;Jmeter 支持基于 JDBC 对数据库进行测试，它可以帮助我们建立连接池，同时提供程序来执行我们给出的 SQL 语句，并且可以进行参数化。为了在 Jmeter 中成功设置数据库连接池，首先需要安装数据库支持的 JDBC 驱动，各厂家的数据库都提供了 JDBC 驱动，可以在对应的官网获取。我当前的公司使用的是 MySql 数据库。      

<br>
<br>

### 二、驱动配置
###### 1、下载 JDBC 驱动
&emsp;&emsp;进入 MySql 下载专区 [https://dev.mysql.com/downloads/](https://dev.mysql.com/downloads/)，选择 `Connector/J` 进入驱动下载页面 [https://dev.mysql.com/downloads/connector/j/](https://dev.mysql.com/downloads/connector/j/)。   

![](\img\in-post\post-jmeter\2022-07-18-jmeter-database-1.png)     

如果无法下载，备用：     
链接: https://pan.baidu.com/s/13FI_rMMvrYi_KAyXGgKlWw?pwd=oejr    
提取码: oejr 

<br>

###### 2、解压和配置
&emsp;&emsp;将下载成功的 zip 包进行解压，然后将 mysql-connector-java-8.0.29.jar 文件放在 Jmeter 安装目录的 lib 目录下。重启 Jmeter，即可使用 JDBC 驱动。    

<br>
<br>

### 三、JDBC 连接池设置
###### 1、添加配置元件
&emsp;&emsp;在测试计划下添加配置元件，选择 `JDBC Connection Configuration`，即可将 JDBC Connection Configuration 加入测试计划，整个测试计划中的所有 JDBC 请求都可以使用该 JDBC Connection Configuration 配置的连接池。     
![](\img\in-post\post-jmeter\2022-07-18-jmeter-database-2.png)         

<br>

###### 2、配置数据库
![](\img\in-post\post-jmeter\2022-07-18-jmeter-database-3.png)     

---

**Variable Name for created pool**       
- JDBC Connection Configuration 算是一个数据库连接池配置
- Variable Name ：数据库连接池的名称。自定义参数，在 `JDBC Request` 中会用到
- 一个测试计划可以有多个 JDBC Connection，只要名称不重复就行

---
**Connection pool Configuration**    
连接池参数配置，基本保持默认就行了，可根据需要进行修改。    
- Max Number of Connections：最大连接数；做性能测试时，建议填 0，如果填了10，则最大连接10个线程
- Max Wait(ms)：在连接池中取回连接最大等待时间，单位毫秒
- Time Between Eviction Runs(ms)：线程可空闲时间，单位毫秒。如果当前连接池中某个连接在空闲了 time Between Eviction Runs Millis 时间后任然没有使用，则被物理性的关闭掉
- Auto Commit：自动提交sql语句，如：修改数据库时，自动 commit
- Transaction isolation：事务隔离级别
- Preinit Pool：立即初始化连接池。如果为 False，则第一个 JDBC 请求的响应时间会较长，因为包含了连接池建立的时间

---
**Connection Validation by Pool**     
验证连接池是否可响应。     
- Test While Idle：当连接空闲时是否断开
- Soft Min Evictable Idle Time(ms)：连接在池中处于空闲状态的最短时间
- Validation Query：一个简单的查询，用于确定数据库是否仍在响应。默认为jdbc驱动程序的 isValid() 方法，适用于许多数据库

---
**Database Connection Configuration**      
数据库连接配置。    
- Database URL：数据库连接 URL。通用填写格式如下： 
    ```
    jdbc:mysql://localhost(数据库连接IP):3306(端口)/dbname(数据库名称)?useUnicode=true&characterEncoding=UTF8&autoReconnect=true&allowMultiQueries=true(允许执行多条 sql)
    ```
- JDBC Driver class：数据库驱动
- Username：数据库登录用户名
- Password：数据库登录密码
- Connection Properties：建立连接时要设置的连接属性（可选）

常见数据库的连接 URL和驱动     
|数据库|驱动|URL|
|---|---|---|
|MySQL|com.mysql.jdbc.Driver|jdbc:mysql://host:port/{dbname}|
|PostgreSQL|org.postgresql.Driver|jdbc:postgresql:{dbname}|
|Oracle|oracle.jdbc.driver.OracleDriver|jdbc:oracle:thin:user/pass@//host:port/service|
|sqlServer|com.microsoft.sqlserver.jdbc.SQLServerDriver|jdbc:sqlserver://host:port;databaseName=databaseName|

---
以上参考自 [https://cloud.tencent.com/developer/article/1651225](https://cloud.tencent.com/developer/article/1651225)     

<br>

###### 3、添加线程组
![](\img\in-post\post-jmeter\2022-07-18-jmeter-database-4.png) 

<br>

###### 4、添加 JDBC Request
![](\img\in-post\post-jmeter\2022-07-18-jmeter-database-5.png)        

![](\img\in-post\post-jmeter\2022-07-18-jmeter-database-6.png)     

<br>

###### 5、添加查看结果树
![](\img\in-post\post-jmeter\2022-07-18-jmeter-database-7.png)      

![](\img\in-post\post-jmeter\2022-07-18-jmeter-database-8.png)         

<br>

###### 6、添加聚合报告
![](\img\in-post\post-jmeter\2022-07-18-jmeter-database-9.png)      

![](\img\in-post\post-jmeter\2022-07-18-jmeter-database-10.png) 

---
以上参考自 [https://www.cnblogs.com/YouJeffrey/p/16035526.html](https://www.cnblogs.com/YouJeffrey/p/16035526.html)