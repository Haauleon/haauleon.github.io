---
layout:        post
title:         "爬虫 | 指定selenium配置取消加载图片"
subtitle:      "指定selenium配置以增加取消加载图片和使用代理可以解决页面加载过慢的问题"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 一、selenium基本配置
1、取消自动测试        
```python
from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = Chrome(options=options)
driver.get('https://www.baidu.com/')
driver.implicitly_wait(5)
```

2、取消图片加载              
```python
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

print(driver.page_source)
driver.close()
```

<br>
<br>

### 二、selenium使用代理
1、第一步：创建配置对象            
```python
from selenium.webdriver import Chrome, ChromeOption


options = ChromeOptions()
```

2、第二步：添加配置         
```python
options.add_argument('--proxy-server=http://代理服务器:端口')
```

3、第三步：通过指定配置创建浏览器对象       
```python
driver = Chrome(options = options)  #options：选择、选项、选择权，相当于做了一个配置，借助这个配置创建浏览器对象
driver.get('https://www.baidu.com/')
print(driver.page_source)
```

<br>
<br>

### 三、selenuim等待
#### 1、设置加载超时
```python
driver.set_page_load_timeout(5)
driver.set_script_timeout(5)
try:
    driver.get(url)
except:
    print("加载页面太慢，停止加载，继续下一步操作")
    driver.execute_script("window.stop()")
```

<br>
<br>

#### 2、隐式等待
&emsp;&emsp;如果没有设置隐式等待：在通过浏览器获取标签的时候，如果标签不存在会直接报错。           
&emsp;&emsp;如果设置了隐式等待：在通过浏览器获取标签的时候，如果标签不存在不会直接报错，而是在指定时间范围内，不断尝试重新获取标签，直到获取到标签或者超时为值（如果超时会报错）。         
&emsp;&emsp;一个浏览器只需设置一次隐式等待时间，它会作用于这个浏览器每次获取标签的时候。             
```python
#sleep设置等待时间，如果给出的时间不够，有可能没有加载完，会报错，隐式等待比较灵活。
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 取消图片加载
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

driver = Chrome()
driver.get('https://www.jd.com')
# 1.设置隐式等待
# 1）. 设置隐式等待时间,这个隐式等待是在获取标签的时候有效。
driver.implicitly_wait(5) #
print('============')
# 2）. 获取标签的时候，隐式等待时间才会生效

input_tag = driver.find_element_by_id('key')
input_tag.send_keys('钱包')
```

<br>
<br>

---

相关链接：    
[python 23 selenium高级和使用代理](https://blog.csdn.net/woaixuexi6666/article/details/126394558)             