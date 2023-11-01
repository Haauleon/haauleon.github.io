---
layout:        post
title:         "爬虫 | 使用html.xpath、driver.xpath两种方式实现查找相似节点的元素"
subtitle:      "Selenium Webdriver 使用 xpath 查找所有 class 节点具有相似名称的元素"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---


### html.xpath
&emsp;&emsp;使用这种 xpath 查询方式的前提是要先通过 webdriver 拿到页面的字符串类型的 html 源代码，然后使用 `lxml.tree()` 方法将源代码转成可通过 DOM 树的形式进行层级遍历。代码如下：    
```python
from lxml import etree


text = driver.page_source
html = etree.HTML(text)

review_ids = html.xpath('//*[@class="a-section review aok-relative"]/@id')
print(review_ids)
if review_ids:
    for review_id in review_ids:
        print(review_id)

```
 
<br>
<br>

### driver.xpath
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


elements = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="a-section review aok-relative"]')))
for element in elements:
    print(element.get_attribute('id'))

```

<br>
<br>

---

相关链接：   
[Python Selenium Webdriver查找所有div节点具有相似名称的元素](https://www.cnpython.com/qa/1554453)