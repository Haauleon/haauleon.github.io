---
layout:        post
title:         "爬虫 | driver.get() 方法加载页面缓慢"
subtitle:      "如何解决 Python selenium get 页面很慢时的问题"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### driver.get()
`driver.get("url")` 方法需等到页面全部加载渲染完成后才会执行后续的脚本。在执行脚本时，如果当前的url页面内容较多加载特别慢，很费时间，但是我们需要操作的元素已经加载出来，可以将页面加载停掉，不影响后面的脚本执行。       

解决办法：        
设置页面加载 timeout，get 操作：          
```python
try:
    driver.get(url) 
except:
    window.stop()
```

在 GeckoDriver 上使用有效果，但是在 ChromeDriver上 还是会有问题，抛出异常 timeout 后续脚本不会继续执行。             
```python
from selenium import webdriver
import re
 
driver = webdriver.Firefox()

# 设定页面加载timeout时长，需要的元素能加载出来就行
driver.set_page_load_timeout(20)
driver.set_script_timeout(20)

# try去get
try:
  driver.get("http://tieba.baidu.com/p/5659969529?red_tag=w0852861182")
except:
  print("加载页面太慢，停止加载，继续下一步操作")
  driver.execute_script("window.stop()")

# 定位到元素尾页元素
last_page_element = driver.find_element_by_css_selector("li.l_pager.pager_theme_4.pb_list_pager >a:nth-child(12)")

# 获取尾页页码链接文本
text = last_page_element.get_attribute("href")

# 正则匹配到页码
all_page_num = re.search("\d+$",text).group()
print("当前贴吧贴子总页数为:%s"%all_page_num)
```

<br>
<br>

---

相关链接：    
[如何解决Python selenium get页面很慢时的问题](https://www.fengnayun.com/news/content/239521.html)             
[WebDriverWait等设置等待时间和超时时间](https://www.cnblogs.com/BigFishFly/p/6337153.html)               
[webdriver 的三种等待方式（强制等待、隐式等待、显示等待）](https://blog.csdn.net/qdPython/article/details/131492086)                 
[What is the correct syntax checking the .readyState of a website in Selenium Python?](https://stackoverflow.com/questions/56728656/what-is-the-correct-syntax-checking-the-readystate-of-a-website-in-selenium-pyt)