---
layout:        post
title:         "Python3 | 安装 MariaDB 报错"
subtitle:      "Python MariaDB pip 安装失败，缺少 MariaDB 配置"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 安装mariadb
尝试安装：      
```
pip install mariadb==1.1.6
```

报错信息如下：       
```
Collecting mariadb
  Using cached mariadb-1.0.0.tar.gz (78 kB)

    ERROR: Command errored out with exit status 1:
     command: /home/niklas/Desktop/Stuff/venv/bin/python -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pycharm-packaging/mariadb/setup.py'"'"'; __file__='"'"'/tmp/pycharm-packaging/mariadb/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /tmp/pip-pip-egg-info-wfnscxnz
         cwd: /tmp/pycharm-packaging/mariadb/
    Complete output (12 lines):
    /bin/sh: 1: mariadb_config: not found
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pycharm-packaging/mariadb/setup.py", line 26, in <module>
        cfg = get_config(options)
      File "/tmp/pycharm-packaging/mariadb/mariadb_posix.py", line 49, in get_config
        cc_version = mariadb_config(config_prg, "cc_version")
      File "/tmp/pycharm-packaging/mariadb/mariadb_posix.py", line 27, in mariadb_config
        "mariadb_config not found.\nPlease make sure, that MariaDB Connector/C is installed on your system, edit the configuration file 'site.cfg' and set the 'mariadb_config'\noption, which should point to the mariadb_config utility.")
    OSError: mariadb_config not found.
    Please make sure, that MariaDB Connector/C is installed on your system, edit the configuration file 'site.cfg' and set the 'mariadb_config'
    option, which should point to the mariadb_config utility.
    ----------------------------------------
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
```

解决步骤：     
```
sudo apt install mariadb-server
sudo apt-get install libmariadb3 libmariadb-dev
```

再次安装 pip install mariadb==1.1.6 时如果还会提示 Connector/C 的版本不符的问题，可以尝试安装低版本的 mariadb：          
```
pip install mariadb==1.0.11
```

最后安装成功：      
```
> pip show mariadb
Name: mariadb
Version: 1.0.11
Summary: Python MariaDB extension
Home-page: https://www.github.com/mariadb-corporation/mariadb-connector-python
Author: Georg Richter
Author-email: None
License: LGPL 2.1
Location: /usr/local/lib/python3.8/site-packages
Requires:
Required-by:
```