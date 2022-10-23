---
layout:        post
title:         "selenium | iframe 元素获取"
subtitle:      "webdriver API 实现获取嵌套网页的元素"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
---


### 背景
&emsp;&emsp;在一个页面中可以嵌套另外一个页面，如 frame/iframe 技术，这是现在很多 web 应用中使用的一种方式，webdriver 对象只能在一个页面(外层是默认的)中定位元素，需要一种方式将 driver 对象从外层切换给内层使用才能对内层的对象进行处理。      

&emsp;&emsp;下图是 qq 邮箱登录页面，其中的登录框就是一个内嵌的 frame 页面，下面我们就以他为案例。        


### 使用方法
webdriver中提供的对 iframe/frame 操作 API 常用到有：          
- driver.switch_to.frame()   
- driver.switch_to.default_content()
- driver.switch_to.parent_frame()

<br>

### 一、driver.switch_to.frame()
###### 1、从外部页面切入 frame 框架中
方法：`driver.switch_to.frame()`    

说明：从外部页面切入 frame 框架中，参数可以为 id/name/index 及页面元素对象，默认是可以给 ID、name 的。       

例如：`driver.switch_to.frame(“login_frame”)`

<br>

###### 2、根据同层 frame 的顺序定位
方法：`driver.switch_to.frame()`         

说明：给出页面的 iframe 的索引 index，根据同层 frame 的顺序定位。      

例如：`driver.switch_to.frame(1)`

<br>
 
###### 3、传参 iframe 的元素对象
方法：`driver.switch_to.frame(iframeObj)`     

说明：传参 iframe 的元素对象。    

例如：   
```python
iframeObj = driver.find_element_by_xpath(’//*[@id=“login_frame”]’)
driver.switch_to.frame(iframeObj)
```

<br><br>

###### 示例
```python
from selenium import webdriver
import time

driver = webdriver.Chrome()

# 1. 创建浏览器对象, 打开腾讯首页；http://www.qq.com
driver.get("https://www.qq.com")

# 2. 点击邮箱图标；
driver.find_element_by_link_text("Qmail").click()

# 3. 跳转到邮箱登录界面
# 跳转到邮箱登录界面(窗口)，涉及到多窗口的处理
handles = driver.window_handles
driver.switch_to.window(handles[1])

# 现在先验证窗口跳转是否成功
# driver.find_element_by_link_text("基本版").click()

# 3.输入用户名
# webdriver中提供API：driver.switch_to.frame()实现frame的切换

# 第一种方式,默认是可以给ID或者name的
# driver.switch_to.frame("login_frame")

# 第二种方式,可以传参iframe的元素对象
# iframeObj = driver.find_element_by_xpath('//*[@id="login_frame"]')
# driver.switch_to.frame(iframeObj)

# 第三种方式,可以给索引号
driver.switch_to.frame(1)
driver.find_element_by_link_text('帐号密码登录').click()
driver.find_element_by_xpath('//*[@id="u"]').send_keys("2572612580")
time.sleep(2)

# 4、输入密码
driver.find_element_by_xpath('//*[@id="p"]').send_keys("123456789")
time.sleep(2)

# 5、点击登录
driver.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(2)

# 6、关闭浏览器
driver.quit()
```

<br><br>

### 二、driver.switch_to.default_content()
&emsp;&emsp;切到 frame 中之后，我们便不能继续操作主文档的元素，这时如果想操作主文档内容，则需切回主文档。        

```python
driver.switch_to.default_content() # 直接从内层 frame 页面切换回到主文档中。
```

<br><br>

### 三、driver.switch_to.parent_frame()
&emsp;&emsp;如果 frame/iframe 有多层，我们可以通过 driver.switch_to.frame() 一层层切入到内层，并可以通过 driver.switch_to.parent_frame() 一层层再退出来，相当于前进、后退。
&emsp;&emsp;相对 driver.switch_to.default_content() 方法，是一层层退回，而不是直接退回主页面。     

```python
driver.switch_to.frame(“frame1”)   # 从主页面切入到 frame1，相当于前进
driver.switch_to.frame(“frame2”)   # 从 frame1 再切入到 frame2，相当于前进
driver.switch_to.parent_frame()    # 返回到上级 frame1，相当于后退
driver.switch_to.parent_frame()    # 返回到主页面
```