---
layout:        post
title:         "Python3 | 终端运行时找不到自定义模块"
subtitle:      "报错 ModuleNotFoundError: No module named ‘XXX‘，找不到自定义模块"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - macOs
    - Python
---


### 一、python运行报错
```python3
ModuleNotFoundError： ModuleNotFoundError: No module named 'step_defss’
```

<br><br>

### 二、报错原因
&emsp;&emsp;在 python 中，一个 `.py` 文件就是一个模块，导入模块等于导入文件。是文件，就有文件路径，所以这个情况，本质上就是找不到文件，原因有二。      

1、很多时候在 pycharm 运行一切正常，但是到命令行中运行 `.py` 文件，就会报错                    
原因：  
pycharm 在每次运行时，都会检索整个工程目录，把目录都添加到 `sys.path` 中，运行的时候，就能够找到对应的模块 `.py` 文件        

2、命令行找不到模块         
原因：           
命令行执行时，往往都是直接运行某个 `.py` 文件，缺少路径检索的步骤（需要我们自己代码加上自动检索）      

<br><br>

### 三、解决方法
&emsp;&emsp;在需要执行的 `.py` 文件中，加上以下这段代码，就是在 import 模块文件前，先将模块路径，添加到 `sys.path`，就能够正常引入模块。      
```python
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from step_defss.scenario_steps import *
# 接后续代码
```