---
layout:        post
title:         "Flask Web | 文件托管服务"
subtitle:      "实现一个文件托管服务"
author:        "Haauleon"
header-img:    "img/in-post/post-flask/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Flask
    - Python
    - Web开发
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、需求列表
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

文件托管服务的需求说明如下：     
1. 上传后的文件可以被永久存放。    
2. 上传后的文件有一个功能完备的预览页。预览页显示文件大小、文件类型、上传时间、下载地址和短链接等信息。     
3. 可以通过传参数对图片进行缩放和剪切。    
4. 不错的页面展示效果。    
5. 为节省空间，相同文件不重复上传，如果文件已经上传过，则直接返回之前上传的文件。    

<br>
<br>

### 二、项目准备
#### 1、环境准备
先安装一些依赖：    
```
> sudo apt-get install libjpeg8-dev -yq
> sudo pip install -r requirements.txt
```

requirements.txt 的 pip 第三方包列表如下：    
```python
python-magic==0.4.10  # libmagic 的 Python 绑定，用于确定文件类型 
Pillow==3.2.0         # PIL(Python Imaging Library) 的分支，用来替代 PIL 
cropresize2==0.1.9    # 用来剪切和调整图片大小
short-url==1.2.1      # 创建短链接
```

<br>

#### 2、建表语句
文件托管服务的建表语句如下:          
```sql
CREATE TABLE `PasteFile` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `filename` varchar(5000) NOT NULL,
    `filehash` varchar(128) NOT NULL,
    `filemd5` varchar(128) NOT NULL,
    `uploadtime` datetime NOT NULL,
    `mimetype` varchar(256) NOT NULL,
    `size` int(11) unsigned NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `filehash` (`filehash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

&emsp;&emsp;建表时指定了 `ENGINE=InnoDB`，意味着这个表会使用 InnoDB 引擎，这是 MySQL 的默认存储引擎。现在创建一个文件 databases/schema.sql，写入以上建表 SQL 语句，然后使用命令行将该文件导入到数据库中：            
```
❯ vim databases/schema.sql
> (echo "use r"; cat databases/schema.sql) | mysql --user='web' --password='web'
```

&emsp;&emsp;将表导入到数据库后，可以通过以下命令检查是否导入成功：    
```
> sudo mysql -u root
mysql> use r;
mysql> DESC PasteFile;
+------------+------------------+------+-----+---------+----------------+
| Field      | Type             | Null | Key | Default | Extra          |
+------------+------------------+------+-----+---------+----------------+
| id         | int(11)          | NO   | PRI | NULL    | auto_increment |
| filename   | varchar(5000)    | NO   |     | NULL    |                |
| filehash   | varchar(128)     | NO   |     | NULL    |                |
| filemd5    | varchar(128)     | NO   |     | NULL    |                |
| uploadtime | datetime         | NO   |     | NULL    |                |
| mimetype   | varchar(256)     | NO   |     | NULL    |                |
| size       | int(11) unsigned | NO   |     | NULL    |                |
+------------+------------------+------+-----+---------+----------------+
7 rows in set (0.00 sec)
```

<br>
<br>

#### 3、项目结构
```
 ❯ tree web
web
├── __init__.py
├── config.py
├── utils.py
├── mimes.py
├── ext.py
├── models.py
├── app.txt
└── requirements.py

0 directories, 8 files
```