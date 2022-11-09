---
layout:        post
title:         "环境搭建 | Python 包管理和虚拟环境"
subtitle:      "常用的包管理工具 pip 和虚拟环境 virtualenv 定制化"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - Web开发
---

### 一、包管理
&emsp;&emsp;Python 的第三方包很强大，使得我们不需要额外造轮子就可以享用，轮子直达：[https://zhuanlan.zhihu.com/p/511280808](https://zhuanlan.zhihu.com/p/511280808)。    

<br>

#### 1、第三方包的主要分布
**（1）PYPI**     
Python 的官方仓库，[https://pypi.python.org/pypi](https://pypi.python.org/pypi)      

**（2）Github**   
Github 上有很多 Python 工具包，例如：解析、格式化、存储、验证手机号码 [https://github.com/daviddrysdale/python-phonenumbers](https://github.com/daviddrysdale/python-phonenumbers)       

**（3）Bitbucket**     
跟 Github 一样，用于代码托管，官方网址：[https://bitbucket.org](https://bitbucket.org)      

<br>
<br>

#### 2、安装和管理第三方包
**（1）Python 社区开发的工具**     
pip、easy_install 等    

**（2）系统自带的包管理器**     
yum、emerge、apt-get 等      

**（3）源码安装**     
通过命令行 `$ python setup.py install` 进行安装     

<br>

###### pip 使用介绍    
目前安装、管理第三方包的主流工具是 pip 且其已经被内置到 python2.7.9 和 python3.4 及以上版本里面了，主要原因：    
（1）支持第三方包的安装、卸载、升级等等包管理功能     
（2）支持二进制包使用 wheel 格式（后缀是 .whl）     
（3）支持虚拟环境工具 virtualenv     
（4）可以集中管理项目依赖列表文件 requirements.txt   

<br>
<br>

#### 3、构建和分发项目的工具
&emsp;&emsp;如果想要把自己的项目分享出去，放到 PYPI 或者其他托管服务上时，需要使用构建和分发项目工具来实现。除非项目的环境依赖简单到只需要用到 distutils ，否则推荐使用 setuptools 包。

<br>
<br>

### 二、虚拟环境
虚拟环境可以解决以下问题：    
（1）系统自带的 Python 是 2.6，而新项目要用到 Python 2.7 中的某些特性        
（2）不同的项目之间使用了不同版本的某些包，但由于某些原因（如有依赖冲突）而无法直接升级到最新版本     
（3）所有的包若都共用一个目录，很容易出现更新了项目A的依赖，却影响了项目B用到的依赖的情况          

&emsp;&emsp;使用虚拟环境可以让全局的 site-package 目录非常干净，从而实现对环境进行隔离。目前主流的创建和管理虚拟环境的工具有 virtualenv 和 pyvenv。    

<br>

#### 1、安装和使用 virtualenv
（1）安装 virtualenv    
```
> pip install virtualenv
```

<br>
<br>

（2）使用 virtualenv 创建一个 Python 环境，环境名为 venv    
```
❯ virtualenv venv
New python executable in /home/ubuntu/venv/bin/python
Installing setuptools, pip, wheel...done.

~ ubuntu@WEB 10s
❯
```

<br>
<br>

（3）激活虚拟环境 venv        
激活成功后，可以看到已经不再使用系统环境变量中的 Python 了，而是在虚拟环境 /home/ubuntu/venv 下创建了一个单独的 python 环境。原系统环境变量的 Python 是 /usr/bin/python。       
```
❯ source venv/bin/activate

~ ubuntu@WEB
(venv) ❯

(venv) ❯ which python
/home/ubuntu/venv/bin/python

```

<br>
<br>

（4）退出虚拟环境 venv      
```
~ ubuntu@WEB
(venv) ❯ deactivate

~ ubuntu@WEB
❯
```

<br>
<br>

#### 2、virtualenv 定制化
