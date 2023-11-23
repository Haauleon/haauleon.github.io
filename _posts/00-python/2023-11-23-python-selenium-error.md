---
layout:        post
title:         "爬虫 | selenium报错ValueError"
subtitle:      "ValueError: Timeout value connect was <...>, but it must be an int, float or None."
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 异常分析
在新机器上安装：          
```
pip install selenium==3.141.0
```

安装完以后显示：        
```
Successfully installed selenium-3.141.0 urllib3-2.0.2（坑出现了）
```

运行以下代码后报错：         
```python
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
```

报错：     
```
ValueError: Timeout value connect was <object object at 0x0000019A00694540>, but it must be an int, float or None.
```

<br>
<br>

### 异常处理
其实是 selenium 版本和 urllib3 版本不兼容问题。更换 urllib3 版本为 1.26.2 即可解决：           
```bash
> pip uninstall urllib3
> pip install urllib3==1.26.2
```

<br>
<br>

---

相关链接：   
[python selenium报错ValueError: Timeout value connect was ＜...＞, but it must be an int, float or None.](https://blog.csdn.net/liu_liu_123/article/details/131146119)