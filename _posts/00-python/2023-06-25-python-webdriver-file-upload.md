---
layout:        post
title:         "爬虫 | webdriver 文件上传"
subtitle:      ""
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 文件上传

#### 1、input标签
如果是 input 标签，直接 send_keys 即可。以百度首页，搜索框的小相机为例：             

```python
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


path = ChromeDriverManager(cache_valid_range=7).install()
option = webdriver.ChromeOptions()
# option.add_argument('--headless')  # 无头模式
# option.add_argument('--window-size=1920,1080')
driver = webdriver.Chrome(executable_path=path, options=option)
driver.maximize_window()
driver.get('https://www.baidu.com/')#打开百度
#点击搜索框的’相机按钮‘
driver.find_element_by_css_selector('span.soutu-btn').click()
sleep(3)
driver.find_element_by_css_selector('input.upload-pic').send_keys(r'D:\111.png')
sleep(10)
driver.close()
```

<br>

#### 2、非input标签
如果是非 input 标签，我们则需要借助第三方库：    
（1）pyautogui      
用法：    
```python
import pyautogui

# 找到上传按钮并点击
driver.find_element('上传按钮').click()
sleep(3)
# 在打开的文件选择窗口输入文件路径
pyautogui.typewrite(文件路径：例如'D:\111.jpg')
# 点击确定
pyautogui.press('enter')
```

（2）pywinauto      
用法：    
```python
from pywinauto.keyboard import send_keys

# 1.通过元素点击，打开windows的选择文件窗口
 driver.find_element('上传按钮').click()
 sleep(3)
# 2.输入要上传的文件路径
 send_keys(文件路径：例如'D:\111.jpg')
# 3.按回车
 send_keys('{ENTER}')
```

<br>

### 注意事项
注意：     
1. 输入文件路径时，要注意输入法切换为英文          
2. 点击`上传`按钮打开的文件选择窗口是 windows 对话框，只能用强制等待 `sleep()`        
3. 多文件上传可以用 pyautogui 实现，用法：`pyautogui.typewrite(r'"文件1" "文件2"')`，两个文件中间有空格    

<br>
<br>

---

相关链接：    
[Selenium10--webdriver的高级操作（四）三种等待&文件上传](https://zhuanlan.zhihu.com/p/450647425)