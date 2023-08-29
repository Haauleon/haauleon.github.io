---
layout:        post
title:         "爬虫 | selenium 定位图片后获取 src 属性"
subtitle:      "webdriver 定位到 img 标签元素，再使用方法 get_attribute 获取 src 的属性值"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 获取 src 属性值
```python
# 直接导入selenium
from selenium import webdriver

# 打开网页后通过以下两种方式来识别ID 获取需要的对象
driver.find_element_by_id("user_account")
driver.find_element_by_xpath("//*[@id='imgObj']")

# 获取对象后通过 get_attribute 方法来拿取该对象的其它属性
driver.find_element_by_xpath("//*[@id='imgObj']").get_attribute("src")
```

此方法也可以同来批量拿取图片，对比正则表达式来拿取图片然后识别src肯定是更加便捷方便的。那个 selenium 的文档只说了如何定位，但是定位后拿取其它元素没有讲解。      

<br>
<br>

---

相关链接：    
[python 通过selenium 定位图片后获取src属性](https://www.ngui.cc/zz/2202129.html?action=onClick)