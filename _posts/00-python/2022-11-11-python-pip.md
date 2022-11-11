---
layout:        post
title:         "环境搭建 | pip 高级用法"
subtitle:      "命令自动补全，使用 devapi 作为缓存代理服务器，PYPI 的完全镜像"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - Web开发
    - Vagrant
    - Ubuntu
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、命令自动补全
#### 1、查看当前的 shell
查看当前发行版可以使用的 shell 有哪些：             
参考：[直达链接](https://blog.csdn.net/Michael177/article/details/124369188)         
```
❯ cat /etc/shells
# /etc/shells: valid login shells
/bin/sh
/bin/dash
/bin/bash
/bin/rbash
/usr/bin/tmux
/usr/bin/screen
/bin/zsh
/usr/bin/zsh
```

<br>

使用一条命令即可查看 ubuntu 系统当前正在使用的 shell：     
```
$ ps -ef | grep `echo $$` | grep -v grep | grep -v ps
```  
**① bash**     
```
❯ bash
ubuntu@WEB:~$ ps -ef | grep `echo $$` | grep -v grep | grep -v ps
ubuntu    2217  2150  0 15:04 pts/0    00:00:00 bash
```
**② zsh**     
```
ubuntu@WEB:~$ zsh

~ ubuntu@WEB
❯ ps -ef | grep `echo $$` | grep -v grep | grep -v ps
ubuntu    2240  2217  7 15:05 pts/0    00:00:00 zsh
ubuntu    2273  2240  0 15:05 pts/9    00:00:00 zsh
```


<br>
<br>

#### 2、不同 shell 的配置
**zsh 用户**      
&emsp;&emsp;pip 支持自动补全功能，zsh 用户可以使用以下命令实现 pip 命令自动补全，如下输入 i + Tab键后会自动补全 install：          
```
❯ zsh
❯ pip completion --zsh >> ~/.zprofile    
❯ source ~/.zprofile
❯ pip i<Tab键>
```

<br>

**bash 用户**      
```
❯ bash
ubuntu@WEB:~$ pip completion --bash >> ~/.profile
ubuntu@WEB:~$ source ~/.profile
ubuntu@WEB:~$ pip i<Tab键>
```

<br>

&emsp;&emsp;如上所述，zsh 的环境变量是 ~/.zprofile 文件，而 bash 的环境变量是 ~/.profile 文件。每次使用 zsh/bash 切换环境时，都要执行 `source <环境变量文件>` 命令来保存对应的环境变量文件从而使其生效，后续才可以使用 pip 的命令自动补全功能。    

<br>
<br>

### 二、缓存代理服务器
&emsp;&emsp;pip 缓存只针对当前的用户，如果公司使用 Python 的规模很大，尤其是有很多自己分发的包时，使用缓存代理服务器可以很大程度提高下载效率，从而不再依赖网络环境到 PYPI 进行下载包了。      

<br>

#### 1、环境准备
pip 需要升级到 9.0.3，否则安装 devpi-server 会有异常：      
```
    Complete output from command python setup.py egg_info:
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
    IOError: [Errno 2] No such file or directory: '/tmp/pip-build-M32JbN/importlib-metadata/setup.py'

    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-M32JbN/importlib-metadata/
```

解决方法（pip 升级到 0.0.3 版本）：
```
❯ pip --version
pip 8.1.2 from /home/ubuntu/.venvburrito/lib/python2.7/site-packages/pip-8.1.2-py2.7.egg (python 2.7)
❯ sudo pip install --upgrade pip==9.0.3
❯ python --version
Python 2.7.11+
❯ pip --version
pip 9.0.3 from /usr/local/lib/python2.7/dist-packages (python 2.7)
```

<br>
<br>

#### 2、安装 devapi-server
指定版本 4.4.0 安装 devpi-server：    
```
❯ sudo pip install devpi-server==4.4.0
```

<br>
<br>

#### 3、安装 devapi-web
指定版本 3.2.2 安装 devapi-web：     
```
❯ sudo pip install devpi-web==3.2.2
```

<br>
<br>

#### 4、使用缓存代理服务器
（1）启动 devpi-server      
```
❯ devpi-server --host=0.0.0.0 --start
2022-11-11 17:25:23,540 INFO  NOCTX Loading node info from /home/ubuntu/.devpi/server/.nodeinfo
2022-11-11 17:25:23,542 INFO  NOCTX wrote nodeinfo to: /home/ubuntu/.devpi/server/.nodeinfo
2022-11-11 17:25:23,543 WARNI NOCTX Can't open sqlite3 db with uri keyword. Python 3.4 is the first version to support it.
2022-11-11 17:25:23,543 WARNI NOCTX unable to open database file
2022-11-11 17:25:23,544 WARNI NOCTX Can't open sqlite3 db with options in URI. There is a higher possibility of read/write conflicts between threads, causing slowdowns due to retries.
minor version upgrade: setting serverstate to 4.4.0 from 4.0.0
starting background devpi-server at http://0.0.0.0:3141
/home/ubuntu/.devpi/server/.xproc/devpi-server$ /usr/local/bin/devpi-server --host=0.0.0.0
process u'devpi-server' started pid=2028
devpi-server process startup detected
logfile is at /home/ubuntu/.devpi/server/.xproc/devpi-server/xprocess.log
```

（2）指定使用缓存代理下载 Django、Tornado     
```
❯ sudo pip install -i http://localhost:3141/root/pypi/ django==1.9.6 tornado==4.4.1
Collecting django==1.9.6
  Downloading http://localhost:3141/root/pypi/+f/83f/234f52a86eb98/Django-1.9.6-py2.py3-none-any.whl (6.6MB)
    100% |████████████████████████████████| 6.6MB 5.0MB/s
Collecting tornado==4.4.1
  Downloading http://localhost:3141/root/pypi/+f/371/d0cf3d56c47ac/tornado-4.4.1.tar.gz (456kB)
    100% |████████████████████████████████| 460kB 35.1MB/s
Collecting singledispatch (from tornado==4.4.1)
  Downloading http://localhost:3141/root/pypi/+f/bc7/7afa97c8a2259/singledispatch-3.7.0-py2.py3-none-any.whl
Collecting certifi (from tornado==4.4.1)
  Downloading http://localhost:3141/root/pypi/+f/0d9/c601124e5a6ba/certifi-2022.9.24.tar.gz (162kB)
    100% |████████████████████████████████| 163kB 3.1MB/s
Collecting backports_abc>=0.4 (from tornado==4.4.1)
  Downloading http://localhost:3141/root/pypi/+f/520/89f97fe7a9aa0/backports_abc-0.5-py2.py3-none-any.whl
Requirement already satisfied: six in /usr/local/lib/python2.7/dist-packages (from singledispatch->tornado==4.4.1)
Installing collected packages: django, singledispatch, certifi, backports-abc, tornado
  Running setup.py install for certifi ... done
  Running setup.py install for tornado ... done
Successfully installed backports-abc-0.5 certifi-2022.9.24 django-1.9.6 singledispatch-3.7.0 tornado-4.4.1
```    

（3）重启 devpi-server       
```
❯ devpi-server --host=0.0.0.0 --stop
❯ devpi-server --host=0.0.0.0 --start
```

（4）通过 http://127.0.0.1:3141 访问 web       
![](\img\in-post\post-python\2022-11-11-python-pip-1.jpg)   
