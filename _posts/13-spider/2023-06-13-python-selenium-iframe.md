---
layout:        post
title:         "爬虫 | selenium 切换 iframe"
subtitle:      "selenium + python 处理 iframe 切换"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - 爬虫
    - Python
---

### iframe 切换
selenium + python处理 iframe 切换有 3 种方法：       
1、如果 iframe 有 id 或 name，则可根据 iframe 的 id 或 name 切换。       
2、把 iframe 当作页面元素，通过元素定位表达式进行切换。       
3、将 iframe 存储到 list 中，然后根据 ifrane 的索引定位 （适合页面有多个 iframe，且前两种方法无法使用）。      

如果页面有多层 iframe 嵌套，则需要一层一层往内切换，切出 iframe 则只需要一次操作。selenium+python 具体代码示例如下：        
```python
import time
from selenium import webdriver



# 实例化浏览器，访问目标网页，窗口最大化
driver = webdriver.Chrome()
driver.get("http://www.eteams.cn/")
driver.maximize_window()
driver.implicitly_wait(5)

# 切换到iframe中，针对多层嵌套的iframe，需要一层一层往里切换，切出去只需一次
# 方法:1：根据iframe的id或name切换
driver.switch_to.frame("needit")
driver.switch_to.frame("ueditor_0")
driver.switch_to.default_content()

# 方法2：把iframe当作页面元素进行切换
iframe1 = driver.find_element_by_css_selector("iframe.needit")
driver.switch_to.frame(iframe1)
iframe2 = driver.find_element_by_css_selector("iframe[frameborder='0']")
driver.switch_to.frame(iframe2)
driver.switch_to.default_content()

# 方法3：将iframe存储到list中，然后根据ifrane的索引定位
iframeElements = driver.find_elements_by_tag_name("iframe")
print("iframe List的长度是："+str(len(iframeElements)))
driver.switch_to.frame(0)
driver.switch_to.frame(1)
driver.switch_to.default_content()

driver.quit()

```

<br>
<br>

---

相关链接：   
[selenium+python处理iframe切换](https://blog.csdn.net/weixin_44169484/article/details/119744709)