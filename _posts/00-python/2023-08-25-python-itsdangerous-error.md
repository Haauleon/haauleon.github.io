---
layout:        post
title:         "Python3 | itsdangerous 相关模块导入异常"
subtitle:      "ImportError: cannot import name 'json' from itsdangerous"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 问题描述
目前使用 python3.8 和 `Flask==1.1.2`，各种包安装完成后，运行脚本，报错：          
```bash
ImportError: cannot import name 'json' from itsdangerous                   
```

<br>
<br>

### 解决办法
查看 itsdangerous 的版本：    
```bash
> pip show itsdangerous
```

更新 itsdangerous 版本为 2.0.1。             

<br>
<br>

### 操作步骤
（1）先卸载已经安装的 itsdangerous     
```bash
pip uninstall itsdangerous
```

（2）安装 2.0.1 版本            
```bash
pip install itsdangerous==2.0.1
```

<br>
<br>

--- 

相关链接：    
[导入错误：无法从 itsdangerous 导入名称“json”](https://segmentfault.com/q/1010000043254452)
