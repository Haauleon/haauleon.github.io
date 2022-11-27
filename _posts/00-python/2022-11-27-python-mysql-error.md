---
layout:        post
title:         "Python2 | windows11 安装 mysql-python 报错"
subtitle:      "building '_mysql' extension error: Microsoft Visual C++ 9.0 is required."
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

> 本篇所有操作均在基于 Python==2.7.11 且 pip==9.0.3 的环境下完成 

<br>
<br>

### 一、异常处理
#### 1、mysql-python 安装异常
&emsp;&emsp;windows11 在执行第三方包安装命令 `pip install mysql-python==1.2.5` 时报了如下错误：      
```
> pip install MySQL-python==1.2.5
Collecting MySQL-python==1.2.5
  Using cached https://files.pythonhosted.org/packages/a5/e9/51b544da85a36a68debe7a7091f068d802fc515a3a202652828c73453cad/MySQL-python-1.2.5.zip
Installing collected packages: MySQL-python
  Running setup.py install for MySQL-python ... error
    Complete output from command d:\python27\python2.exe -u -c "import setuptools, tokenize;__file__='c:\\users\\haauleon\\appdata\\local\\temp\\pip-build-ie34id\\MySQL-python\\setup.p
y';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record c:\users\haauleon\appdata\local\temp\pip-heat2g-record\install-record.txt --single-version-externally-managed --compile:
    running install
    running build
    running build_py
    creating build
    creating build\lib.win-amd64-2.7
    copying _mysql_exceptions.py -> build\lib.win-amd64-2.7
    creating build\lib.win-amd64-2.7\MySQLdb
    copying MySQLdb\__init__.py -> build\lib.win-amd64-2.7\MySQLdb
    copying MySQLdb\converters.py -> build\lib.win-amd64-2.7\MySQLdb
    copying MySQLdb\connections.py -> build\lib.win-amd64-2.7\MySQLdb
    copying MySQLdb\cursors.py -> build\lib.win-amd64-2.7\MySQLdb
    copying MySQLdb\release.py -> build\lib.win-amd64-2.7\MySQLdb
    copying MySQLdb\times.py -> build\lib.win-amd64-2.7\MySQLdb
    creating build\lib.win-amd64-2.7\MySQLdb\constants
    copying MySQLdb\constants\__init__.py -> build\lib.win-amd64-2.7\MySQLdb\constants
    copying MySQLdb\constants\CR.py -> build\lib.win-amd64-2.7\MySQLdb\constants
    copying MySQLdb\constants\FIELD_TYPE.py -> build\lib.win-amd64-2.7\MySQLdb\constants
    copying MySQLdb\constants\ER.py -> build\lib.win-amd64-2.7\MySQLdb\constants
    copying MySQLdb\constants\FLAG.py -> build\lib.win-amd64-2.7\MySQLdb\constants
    copying MySQLdb\constants\REFRESH.py -> build\lib.win-amd64-2.7\MySQLdb\constants
    copying MySQLdb\constants\CLIENT.py -> build\lib.win-amd64-2.7\MySQLdb\constants
    running build_ext
    building '_mysql' extension
    error: Microsoft Visual C++ 9.0 is required. Get it from http://aka.ms/vcpython27

    ----------------------------------------
Command "d:\python27\python2.exe -u -c "import setuptools, tokenize;__file__='c:\\users\\haauleon\\appdata\\local\\temp\\pip-build-ie34id\\MySQL-python\\setup.py';f=getattr(tokenize, '
open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record c:\users\haauleon\appdata\local\temp\pip-heat2g-record\install-record.txt --single-version-externally-managed --compile" failed with error code 1 in c:\users\haauleon\appdata\local\temp\pip-build-ie34id\MySQL-python\
```

<br>
<br>

#### 2、报错处理
1. 到 [https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysql-python) 下载对应的 mysql-python 的 `.whl` 第三方包      
2. 进入 cmd 窗口，重新安装，安装成功          
    ```
    > pip install MySQL_python‑1.2.5‑cp27‑none‑win_amd64.whl
    Installing collected packages: MySQL-python
    Successfully installed MySQL-python-1.2.5

    > pip show mysql-python
    Name: MySQL-python
    Version: 1.2.5
    Summary: Python interface to MySQL
    Home-page: https://github.com/farcepest/MySQLdb1
    Author: Andy Dustman
    Author-email: farcepest@gmail.com
    License: GPL
    Location: d:\python27\lib\site-packages
    Requires:
    ```