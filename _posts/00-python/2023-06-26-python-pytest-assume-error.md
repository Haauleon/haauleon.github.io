---
layout:        post
title:         "Pytest | pytest-assume 导入异常"
subtitle:      "解决 ImportError: cannot import name assume from pytest 问题"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - Allure
    - Pytest
    - 单元测试框架
---

### 问题描述
代码如下：     
```python
from pytest import assume
```
报错：    
```shell
ImportError: cannot import name `assume` from `pytest` (C:\Users\EJET\AppData\Local\Programs\Python\Python38\Lib\site-packages\pytest\_init_.py)
```

<br>
<br>

### 解决方法
&emsp;&emsp;根据报错信息，打开 C:\Users\EJET\AppData\Local\Programs\Python\Python38\Lib\site-packages\pytest\_init_.py 文件，发现这个文件里都是一些 import 操作，搜索后发现，确实没有导入 assume。       
![](\img\in-post\post-python\2023-06-26-python-assume-error-1.png)      

&emsp;&emsp;随后，我在 C:\Users\EJET\AppData\Local\Programs\Python\Python38\Lib\site-packages 目录下发现存在 pytest_assume 模块。            
![](\img\in-post\post-python\2023-06-26-python-assume-error-2.png)      

&emsp;&emsp;查找后发现，assume 模块存在于 pytest_assume 中的 plugin.py 中。   
![](\img\in-post\post-python\2023-06-26-python-assume-error-3.png)        
![](\img\in-post\post-python\2023-06-26-python-assume-error-4.png)          


将 `from pytest import assume` 换成以下语句可解决：   
```python
from pytest_assume.plugin import assume
```

<br>
<br>

---

相关链接：   
[pytest assume无法导入：解决ImportError: cannot import name ‘assume‘ from ‘pytest‘问题](https://blog.csdn.net/tianshuiyimo/article/details/116519264)