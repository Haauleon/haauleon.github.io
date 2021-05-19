---
layout:        post
title:         "Python3 | pipreqs 的使用"
subtitle:      "pip 生成和安装 requirements.txt 文件"
date:          2021-05-19
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - Pythoneer
---

## 生成 requirements.txt
```
# 安装 pipreqs
$ pip install pipreqs


# 检查安装
$ pip show pipreqs
Name: pipreqs
Version: 0.4.10
Summary: Pip requirements.txt generator based on imports in project
Home-page: https://github.com/bndr/pipreqs
Author: Vadim Kravcenko
Author-email: vadim.kravcenko@gmail.com
License: Apache License
Location: /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages
Requires: yarg, docopt
Required-by: 


# 在当前工程目录下生成文件
$ pipreqs . --encoding=utf8 --force
INFO: Successfully saved requirements file in ./requirements.txt
```

<br><br>


## 安装 requirements.txt
```
# 使用 requirements.txt 安装依赖
$ pip install -r requirements.txt
```