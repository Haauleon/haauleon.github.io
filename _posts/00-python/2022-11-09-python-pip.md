---
layout:        post
title:         "环境搭建 | Python 包管理和虚拟环境"
subtitle:      ""
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
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

#### 3、构建和分发包的工具

<br>
<br>