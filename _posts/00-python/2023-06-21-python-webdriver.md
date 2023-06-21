---
layout:        post
title:         "爬虫 | selenium 无头模式下无法定位元素"
subtitle:      "webdriver 无法在 chrome 无头模式下定位元素"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 问题
```
Python 3.8.10
pip 21.1.1
selenium==3.141.0
```

<br>

&emsp;&emsp;本地调试配置 chrome 驱动 driver，使用无头模式运行。运行结果提示元素定位不到，但是不使用无头模式的情况是是可以运行的。以下为配置代码：    
```python
path = ChromeDriverManager(cache_valid_range=7).install()
option = webdriver.ChromeOptions()
option.add_argument('--headless')  # 无头模式
driver = webdriver.Chrome(executable_path=path, options=option)
```

<br>
<br>

### 解决
在驱动配置代码中增加窗口尺寸的设置，用以解决元素定位不到的问题：   
```python 
path = ChromeDriverManager(cache_valid_range=7).install()
option = webdriver.ChromeOptions()
option.add_argument('--headless')  # 无头模式
option.add_argument('--window-size=1920,1080')  # 定义窗口尺寸，解决无头模式下元素定位不到的问题
driver = webdriver.Chrome(executable_path=path, options=option)
```