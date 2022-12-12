---
layout:        post
title:         "环境搭建 | Ubuntu20.04 安装 Python3.6"
subtitle:      "Linux Ubuntu 20.04 LTS 安装 Python3.6.9 和 对应的 pip3"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 操作系统
    - Ubuntu
---

> 本篇所有操作均在 Linux Ubuntu 20.04 LTS 系统下执行

<br>
<br>

### 一、安装 Python3.6
#### 1、安装依赖工具
```
> sudo apt-get install -y gcc make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev
```

<br>

#### 2、下载源码文件压缩包
```
> wget https://www.python.org/ftp/python/3.6.9/Python-3.6.9.tgz
```

<br>

#### 3、解压源码文件压缩包
```
> tar -xzf Python-3.6.9.tgz
```

<br>

#### 4、配置
```
> cd Python-3.6.9
> sudo ./configure --prefix=/usr/local/python36
#--prefix=/usr/local/python36：编译的时候用来指定程序存放路径。
#--enable-optimizations安装中就行检测
```

<br>

#### 5、编译
```
> sudo make
```

<br>

#### 6、安装
```
> sudo make install
```

<br>

#### 7、设置软链接
python3 软链接：     
```
> which python3
/usr/bin/python3
> sudo rm /usr/bin/python3  # 删除原有链接
> sudo ln -s -f /usr/local/python36/bin/python3.6 /usr/bin/python3
```

pip3 软链接：     
```
> which pip3
/usr/bin/pip3
> sudo rm /usr/bin/pip3  # 删除原有链接
> sudo ln -s -f /usr/local/python36/bin/pip3.6 /usr/bin/pip3
```

<br>
<br>

### 二、检查安装
```
> python3 --version
> pip3 --version
```

<br>
<br>

相关链接：    
[ubuntu 20.04 安装python 3.6.8](https://www.cnblogs.com/netflix/p/15026768.html)    
[Linux Ubuntu 20.04 LTS 一键安装 Python3 不同版本的方法](https://www.cnblogs.com/mxnote/p/16741568.html)
