---
layout:        post
title:         "Python3 | pip 版本不符"
subtitle:      "解决项目部署过程中 pip 版本不符的问题"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### pip版本问题
目前部署经常会遇到以下几个问题：    
1、无法在当前版本的 python 解释器下安装指定版本的 pip 包，如：pip install mariadb==1.1.6      
有两种解决方法：     
（1）如果是 mariadb==1.1.6 的包需要更高的解释器版本，那就升级 python 解释器版本      
（2）如果是不想升级 python 解释器版本，可以采取安装更低版本的 pip 包，如：pip install mariadb==1.1.5，以此类推         

2、pip 版本太高导致部分包安装失败，可以采用安装更低版本的 pip 来解决    
```
> pip install --upgrade pip==21.1.1
```