---
layout:        post
title:         "macOs | 使用 tree 命令"
subtitle:      "如何安装和使用 tree 命令查看目录结构？"
date:          2021-04-30
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - macOs
---

## 背景
&emsp;&emsp;很多时候看别人的项目代码，都需要使用 tree 命令来查看目录结构。macOs 系统虽然是类 Unix 系统，但是安装和使用却跟 Linux 还是有些差别的，它是使用 brew 来管理 tree 扩展。      

<br><br>

## 使用技巧
```
$ brew search tree
$ brew install tree
$ tree
```

<br>

安装成功后，使用效果如下：        
```
192:utx haauleon$ tree
.
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-37.pyc
│   ├── core.cpython-37.pyc
│   ├── log.cpython-37.pyc
│   ├── runner.cpython-37.pyc
│   ├── setting.cpython-37.pyc
│   └── tag.cpython-37.pyc
├── core.py
├── log.py
├── report
│   ├── __init__.py
│   ├── style_1.py
│   └── style_2.py
├── runner.py
├── setting.py
└── tag.py

2 directories, 15 files
192:utx haauleon$ 
```