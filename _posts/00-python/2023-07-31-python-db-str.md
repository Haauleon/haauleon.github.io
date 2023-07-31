---
layout:        post
title:         "Python3 | 数据库连接字符串"
subtitle:      "ODBC 数据库驱动的连接字符串标准写法"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 一、SQL Server

<br>

#### ODBC
1、标准连接           
```
Driver={SQL Server};Server=<服务器地址>;Database=<数据库>;Uid=<用户名>;Pwd=<密码>;
```

<br>

2、受信的连接             
```
Driver={SQL Server};Server=<服务器地址>;Database=<数据库>;Trusted_Connection=Yes;
```

<br>

3、指定帐号和密码               
```
oConn.Properties("Prompt") = adPromptAlways
Driver={SQL Server};Server=<服务器地址>;Database=<数据库>;
```

<br>
<br>

#### OLE DB, OleDbConnection (.NET)
1、标准连接      
```
Provider=sqloledb;Data Source=<服务器地址>;Initial Catalog=<数据库>;User Id=<用户名>;Password=<密码>;
```

<br>

2、受信的连接           
```
Provider=sqloledb;Data Source=<服务器地址>;Initial Catalog=<数据库>;Integrated Security=SSPI;
```

<br>

3、使用 serverName\instanceName 作为数据源可以指定 SQL Server 实例        
连接到一个 SQL Server 的实例指定服务器实例的表达式和其他 SQL Server 的连接字符串相同。        
```
Provider=sqloledb;Data Source=<服务器地址/数据源名称>;Initial Catalog=<数据库>;Integrated Security=SSPI;
```

<br>

4、指定帐户和密码       
```
oConn.Provider = "sqloledb"
oConn.Properties("Prompt") = adPromptAlways
Data Source=myServerAddress;Initial Catalog=myDataBase;
```

<br>

5、使用IP地址的连接      
```
Provider=sqloledb;Data Source=190.190.200.100,1433;Network Library=DBMSSOCN;Initial Catalog=<数据库>;User ID=<用户名>;Password=<密码>;
```

<br>
<br>

#### SqlConnection (.NET) 
1、标准连接      
```
Data Source=<服务器地址>;Initial Catalog=<数据库>;User Id=<用户名>;Password=<密码>;
```

<br>

2、 Standard Security alternative syntax       
```
Server=<服务器地址>;Database=<数据库>;User ID=<用户名>;Password=<密码>;Trusted_Connection=False;
```

<br>

3、受信任的连接    
```
Data Source=<服务器地址>;Initial Catalog=<数据库>;Integrated Security=SSPI;
```

<br>

4、 Trusted Connection alternative syntax      
```
Server=<服务器地址>;Database=<数据库>;Trusted_Connection=True;
```

5、连接到SQL Server实例指定服务器实例的表达式和其他SQL Server的连接字符串相同      
```
Server=myServerName\theInstanceName;Database=myDataBase;Trusted_Connection=True;
```

<br>

6、仅能用于CE设备     
```
Data Source=myServerAddress;Initial Catalog=myDataBase;Integrated Security=SSPI;User ID=myDomain\myUsername;Password=myPassword;
```

<br>

7、带有IP地址的连接           
```
Data Source=190.190.200.100,1433;Network Library=DBMSSOCN;Initial Catalog=myDataBase;User ID=myUsername;Password=myPassword;
```

<br>

8、指定包的大小             
默认的包大小为8192字节。
```
Server=myServerAddress;Database=myDataBase;User ID=myUsername;Password=myPassword;Trusted_Connection=False;Packet Size=4096;
```

<br>

9、Data Shape MS Data Shape          
```
Provider=MSDataShape;Data Provider=SQLOLEDB;Data Source=myServerAddress;Initial Catalog=myDataBase;User ID=myUsername;Password=myPassword;
```

<br>
<br>

### 二、MYSQL
#### MyODBC
1、MyODBC 2.50 本地数据库     
```
Driver={mySQL};Server=localhost;Option=16834;Database=myDataBase;
```

<br>

2、MyODBC 2.50 远程数据库     
```
Driver={mySQL};Server=myServerAddress;Port=3306;Option=131072;Stmt=; Database=myDataBase;Uid=myUsername;Pwd=myPassword;
```

<br>

3、MyODBC 3.51 本地数据库      
```
Driver={MySQL ODBC 3.51 Driver};Server=localhost;Database=myDataBase; User=myUsername;Password=myPassword;Option=3;
```

<br>

4、MyODBC 3.51 远程数据库      
```
Driver={MySQL ODBC 3.51 Driver};Server=data.domain.com;Port=3306;Database=myDataBase;User=myUsername; Password=myPassword;Option=3;
```

<br>
<br>

#### OLE DB, OleDbConnection (.NET)
1、标准         
```
Provider=MySQLProv;Data Source=mydb;User Id=myUsername;Password=myPassword;
```

<br>
<br>

#### Connector/Net 1.0 (.NET)
1、标准        
默认端口号是3306。     
```
Server=myServerAddress;Database=myDataBase;Uid=myUsername;Pwd=myPassword;
```

<br>

2、指定端口号     
```
Server=myServerAddress;Port=1234;Database=myDataBase;Uid=myUsername;Pwd=myPassword;
```

<br>

3、命名管道        
如果端口是-1，意思是告诉驱动程序使用命名管道网络协议来连接数据库。        
```
Server=myServerAddress;Port=-1;Database=myDataBase;Uid=myUsername;Pwd=myPassword;
```

<br>
<br>

#### MySqlConnection (.NET)
1、eInfoDesigns.dbProvider      
```
Data Source=myServerAddress;Database=myDataBase;User ID=myUsername;Password=myPassword;Command Logging=false;
```

<br>
<br>

#### SevenObjects MySqlClient (.NET)
1、标准     
```
Host=myServerAddress;UserName=myUsername;Password=myPassword;Database=myDataBase;
```

<br>
<br>

#### Core Labs MySQLDirect (.NET) 
1、标准     
```
User ID=root;Password=myPassword;Host=localhost;Port=3306;Database=myDataBase; Direct=true;Protocol=TCP;Compress=false;Pooling=true;Min Pool Size=0;Max Pool Size=100;Connection Lifetime=0;
```

<br>
<br>

#### MySQLDriverCS (.NET)
1、标准      
```
Location=myServerAddress;Data Source=myDataBase;UserID=myUsername;Password=myPassword;Port=3306;Extended Properties="""";
```

<br>
<br>

---

相关链接：    
[数据库连接字符串](https://www.cnblogs.com/weixing/p/2141416.html)