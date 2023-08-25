---
layout:        post
title:         "Python3 | jinja2 相关模块导入异常"
subtitle:      "ImportError: cannot import name evalcontextfilter, Markup, escape from 'jinja2'"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 问题描述
将 python3.6 升级到 python3.8，各种包安装完成后，运行脚本，报错：`ImportError: cannot import name evalcontextfilter, Markup, escape from 'jinja2'`                   

<br>
<br>

### 解决办法
查看 jinja2 的版本：    
```bash
> pip show jinja2
```

查看了之前 python3.6 时的 jinja2 版本为 3.0.3。升级到 python3.8 后，jinja2 版本为 3.1.x。             

<br>
<br>

### 操作步骤
（1）先卸载已经安装的 jinja2     
```bash
pip uninstall jinja2
```

（2）安装 3.0.3 版本            
```bash
pip install jinja2==3.0.3
```

<br>
<br>

--- 

相关链接：    
[python 报错 ImportError: cannot import name evalcontextfilter, Markup, escape from ‘jinja2‘ 解决方法](https://blog.csdn.net/whatday/article/details/125344577)