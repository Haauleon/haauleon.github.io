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
    - Vagrant
    - Ubuntu
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

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

**pip 使用介绍**         
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

（2）使用 virtualenv 创建一个 Python 环境，环境名为 venv    
```
❯ virtualenv venv
New python executable in /home/ubuntu/venv/bin/python
Installing setuptools, pip, wheel...done.

~ ubuntu@WEB 10s
❯
```

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
**效果实现：在生成虚拟环境 venv 的同时安装 requests 的自定义脚本**     

（1）让 ubuntu 这个用户对 virtualenv 文件可见，方便直接替换     
```
~ ubuntu@WEB
❯ which virtualenv
/usr/local/bin/virtualenv

~ ubuntu@WEB
❯ sudo chown ubuntu:ubuntu /usr/local/bin/virtualenv

~ ubuntu@WEB
❯
```

**如果不改变文件的权限而直接进行定制化脚本的替换，则抛出以下异常：**         
```
❯ python web_develop/chapter2/section2/create-venv-script.py
Updating /usr/local/bin/virtualenv
Traceback (most recent call last):
  File "web_develop/chapter2/section2/create-venv-script.py", line 22, in <module>
    main()
  File "web_develop/chapter2/section2/create-venv-script.py", line 17, in main
    with open(virtualenv_path, 'w') as f:
IOError: [Errno 13] Permission denied: '/usr/local/bin/virtualenv'
```

<br>

（2）编写定制化的脚本    
原版本的 virtualenv 内容如下：    
```
❯ which virtualenv
/usr/local/bin/virtualenv

~ ubuntu@WEB
❯ cat /usr/local/bin/virtualenv
#!/usr/bin/python

# -*- coding: utf-8 -*-
import re
import sys

from virtualenv import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
```

定制化的脚本可以全局替换到原版本，实现在默认的虚拟环境安装完成后去执行其他的工作，脚本如下：      
```python
# coding=utf-8
import subprocess

import virtualenv

virtualenv_path = subprocess.check_output(['which', 'virtualenv']).strip()

EXTRA_TEXT = '''
def after_install(options, home_dir):
    subprocess.call(['{}/bin/pip'.format(home_dir), 'install', 'requests'])
'''


def main():
    text = virtualenv.create_bootstrap_script(EXTRA_TEXT, python_version='2.7')
    print 'Updating %s' % virtualenv_path
    with open(virtualenv_path, 'w') as f:
        f.write(text)


if __name__ == '__main__':
    main()
```

<br>

（3）执行定制化脚本，替换原有的版本 /usr/local/bin/virtualenv      
```
~ ubuntu@WEB
❯ python web_develop/chapter2/section2/create-venv-script.py
Updating /usr/local/bin/virtualenv

~ ubuntu@WEB
❯
```

<br>

（4）生成虚拟环境 tmp 并检查有无自动安装 requests 包     
```
❯ virtualenv venv
New python executable in /home/ubuntu/venv/bin/python2.7
Also creating executable in /home/ubuntu/venv/bin/python
Installing setuptools, pip, wheel...done.
Collecting flake8
```

**如果在这过程有任何一环节出现异常，初始化方法如下：**     
（1）使用 `> vagrant halt` 关闭虚拟机     
（2）进入 VirtualBox 中删除该虚拟机的所有文件    
（3）重新启动虚拟机 `> vagrant up`     
（4）重新进行初始化 `> vagrant provision`     
（5）重新连接虚拟机 `> vagrant ssh`，登录成功后再进行重新操作     

<br>
<br>