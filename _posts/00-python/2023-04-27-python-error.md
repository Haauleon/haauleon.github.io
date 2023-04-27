---
layout:        post
title:         "Python3 | SyntaxError: Non-ASCII character"
subtitle:      "SyntaxError: Non-ASCII character '\xe8' in file test.py on line 5, but no encoding declared; "
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### SyntaxError
```
SyntaxError: Non-ASCII character '\xe8' in file test.py on line 5, but no encoding declared; 
see http://python.org/dev/peps/pep-0263/ for details
```
原因：注释里面出现了中文，而 Python 支持的 ASCII 码无中文。      

<br>
<br>

### 解决方法     
在头文件中添加如下代码：     
```python
# -*- coding: utf-8 -*-

# 这样也行
# coding:utf-8 
```

注意：本行要添加在源代码的第一行。    