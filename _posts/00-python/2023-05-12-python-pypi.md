---
layout:        post
title:         "环境搭建 | 解决 pypi 访问超时"
subtitle:      "使用国内的镜像源替换 pypi 官方的镜像"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 
---


### 一、使用国内镜像方案（推荐）

经常在使用 python 的时候需要安装各种模块，而pip是很强大的模块安装工具，但是由于国外官方pypi经常被墙，导致不可用，所以我们最好是将自己使用的 pip 源更换一下，这样就能解决被墙导致的装不上库的烦恼。       

网上有很多可用的源，例如：    
豆瓣 http://pypi.douban.com/simple/          
清华 https://pypi.tuna.tsinghua.edu.cn/simple       
阿里云 http://mirrors.aliyun.com/pypi/simple      
中科大 http://pypi.mirrors.ustc.edu.cn/simple     
网易云 https://mirrors.163.com/pypi/simple       

清华大学的 pip 源是官网 pypi 的镜像，每隔 5 分钟同步一次。          

可以在使用 pip 的时候加参数 `-i https://pypi.tuna.tsinghua.edu.cn/simple`       

例如：    
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple gevent
```
这样就会从清华这边的镜像去安装 gevent 库。

<br>
<br>

### 二、增加连接时延

设置超时时间：`pip --default-timeout=100 install XXX`        

除了上述两种方案外，还有使用代理，修改配置文件等方式。条条大路通罗马，我认为第一种方案已经很方便了。但是如果想用 pycharm 对虚拟环境安装相应的，就需要修改配置文件了，具体方法如下：      

<br>
<br>

### 三、永久修改 pip 下载网址（本人暂未测试）

永久修改pip镜像：       
linux 下，修改 ~/.pip/pip.conf (没有就创建一个)， 修改 index-url 至 tuna       
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

windows下，直接在user目录中创建一个 pip 目录，如：C:\Users\xx\pip，新建文件 pip.ini，内容如下：        
```
​​​​​​​[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

或者直接在cmd中     
```
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

<br>
<br>

### 四、在配置文件中修改pip的连接时延
```
python -m pip install --upgrade pip --timeout 6000
```

<br>

本文参考：     
https://www.cnblogs.com/maxiaodoubao/p/9866482.html    
https://blog.csdn.net/weixin_41357300/article/details/97318913   

<br>
<br>

### 五、pycharm安装第三方包时出现错误

之前考虑用方法三改了地址后，再调用 pycharm 指令，后来发现根本没必要这么麻烦，在 pycharm 中搜索库时，在安装按钮的右侧，有一个下面的按钮，点进去把镜像网址加入即可。              
![](https://img-blog.csdnimg.cn/20200301153956394.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0pvaG5XZWlp,size_16,color_FFFFFF,t_70)     

<br>
<br>

---

相关链接：       
[Pypi 超时或安装第三方库失败的解决办法](https://www.cnblogs.com/bushLing/p/16953002.html)          
[解决ERROR: Cannot determine archive format of ...pip-req-build-t35bzb_f](https://blog.csdn.net/m0_50140251/article/details/115211970)