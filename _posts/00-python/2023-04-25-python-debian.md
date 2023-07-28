---
layout:        post
title:         "Python3 | 在 Debian 上安装 Python 3.8"
subtitle:      "在 Debian 上安装 Python 3.8"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 安装步骤
在 Debian 上构建 Python 3.8 是一个相对简单的过程，只需几分钟。      

（1）首先安装构建Python源所需的包：     
```
sudo apt update 
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
```

<br>

（2）使用以下curl命令从Python下载页面下载最新版本的源代码：       
```
curl -O https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz
```

如果因网络问题无法从官网下载，可以从以下网盘链接中进行下载，然后使用工具 FileZilla 传到服务器即可：    
链接：https://pan.baidu.com/s/1HTxY6viOEBm15-8z3YhV3w?pwd=p5dm        
提取码：p5dm            


<br>

在撰写本文时，最新版本是3.9.3。    

<br>

（3）下载完成后解压tgz压缩包      
```
tar -xf Python-3.8.10.tgz
```

<br>

（4）导航到Python源目录并运行configure脚本，该脚本将执行大量检查以确保系统上存在所有依赖项：     
```
cd Python-3.8.10 
./configure --enable-optimizations
```
--enable-optimizations选项将通过运行多个测试来优化Python二进制文件，这将使构建过程变慢。

<br>

（5）运行make以启动构建过程：    
```
make -j 2
```
为了缩短构建时间，请根据处理器修改-j标志。 如果你不知道处理器的核心数，可以通过键入nproc来找到它。 我的系统有2个内核，所以我使用-j2标志。

<br>

（6）构建完成后，通过以具有sudo访问权限的用户身份运行以下命令来安装Python二进制文件：       
```
sudo make altinstall
```
不要使用标准的make install，因为它会覆盖默认的系统python3二进制文件。

<br>

（7）此时，Python 3.8已安装在你的Debian系统上并可以使用。 你可以输入以下命令进行验证：      
```
python3.8 --version
```

输出版本信息     
```
Python 3.8.10
```

再补点：     
查了下，python3.8,这个命令是在 /usr/local/bin/python3.8，直接输入 python3.8 也是可以执行的。但这个格式不方便，我想改成 python        
```
> which python3.8
/usr/local/bin/python3.8
> which python3
/usr/bin/python3
> which python
> which pip
```

使用以下命令可以替换默认的解释器版本和 pip 版本：      
```
sudo rm /usr/bin/python

sudo rm /usr/bin/python2

sudo rm /usr/bin/python2.7

ln -s /usr/local/bin/python3.8 /usr/bin/python
```

以后直接输： python就可以了。pip3.8，也改成pip了       
```
sudo rm /usr/bin/pip
sudo ln -s /usr/local/bin/pip3.8 /usr/bin/pip
```

<br>
<br>

---

相关链接：    
[在 Debian 上安装 Python 3.8](http://e.betheme.net/zz/553103.html?action=onClick)