---
layout:        post
title:         "爬虫 | webdriver 三种等待方式"
subtitle:      "强制等待、隐式等待、显示等待"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 三种等待
&emsp;&emsp;selenium 中，经常会出现元素还没有加载出来，浏览器找不到元素而报错的问题，设置等待是保证脚本运行的一个重要手段，常用的等待有三种--强制等待、隐式等待、显示等待。      

<br>

#### 1、强制等待
强制等待也可以叫做固定等待，就是我们常用的 `sleep()`。     
强制等待多用于调试、观察效果等。     
实际项目中不建议用，不可靠。（网络的好坏会导致等待的时间不确定）     

用法：     
```python
from time import sleep,ctime

print('好好学习')
print(ctime())
sleep(2)  # 固定等待2秒
print('天天向上')
print(ctime())


>>> # 运行结果
好好学习
Sun Dec 26 22:10:08 2021
天天向上
Sun Dec 26 22:10:10 2021
```

<br>

#### 2、隐式等待
语法：    
```python
driver.implicitly_wait(最大等待时间X秒)
```
参数是最大等待时间，只要在此规定时间内整个页面加载完成即可操作元素。     
设置一次，则全局（对应浏览器的整个生命周期内）生效，所以一般在打开浏览器后立即设置。     
缺点：实际操作中你需要定位的元素已经加载完成，但其他元素未加载完成，也只能继续等待，相对（显式等待）来说会浪费时间。     
举个栗子：你的工作完成了，但别人没完成，你也要陪着他加班。这样并不好。     

用法：      
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.baidu.com')
try:
    driver.find_element_by_id('kw')  # 百度输入框
except:
    print('都5秒了，搜索框还没找到，什么破网？')
finally:
    driver.quit()  # 退出
```

<br>

#### 3、显示等待（WebDriverWait）
针对隐式等待的浪费时间问题，显式等待就更加有针对性。它是针对某个（或某组）具体的元素，看它是否具备了一定的特征，就开始有所动作了。     
显示等待也有最大等待时间，并提供了轮询间隔，等待条件成立。     
默认轮询间隔是0.5秒，即每隔0.5秒程序就看一眼条件成立没。    

语法：    
（1）直接用         
```python
WebDriverWait(driver,20,0.5).until(可执行方法,超时后返回的信息)
```
（2）结合 `EC（expected_conditions）` 模块     
```python
WebDriverWait(driver,20,0.5).until(EC.方法)
```

```python
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://cn.bing.com/')  # 打开必应
# 找到id为'est_en1'的元素，每1秒检查一次，五秒后未找到返回信息--'没找到'
WebDriverWait(driver,5,1).until(lambda x:x.find_element_by_id('est_en1'),'没找到').click()
# 如果没有找到则报如下错误：
# selenium.common.exceptions.TimeoutException: Message: 没找到
--------------------------------------------------
# 判断网页的title是否为’必应‘，是则返回True，否则返回False
try:
    WebDriverWait(driver,5,1).until(EC.title_is('必应11'))
except:
    print('网页title错误')
finally:
    driver.quit()
```

EC 用法汇总：       
```python
'''判断title是否是一致,返回布尔值'''
WebDriverWait(driver,10,0.1).until(EC.title_is("title_text"))

'''判断title是否与包含预期值,返回布尔值'''
WebDriverWait(driver,10,0.1).until(EC.title_contains("title_text"))

'''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回元素'''
WebDriverWait(driver,10,0.1).until(EC.presence_of_element_located((locator)))

'''判断某个元素是否被添加到了dom里并且可见，可见代表元素可显示且宽和高都大于0'''
WebDriverWait(driver,10,0.1).until(EC.visibility_of_element_located((locator)))

'''判断元素是否可见，如果可见就返回这个元素'''
WebDriverWait(driver,10,0.1).until(EC.visibility_of(driver.find_element(locator)))

'''判断是否至少有1个元素存在于dom树中，如果定位到就返回列表'''
WebDriverWait(driver,10,0.1).until(EC.presence_of_all_elements_located((locator)))

'''判断是否至少有一个元素在页面中可见，如果定位到就返回列表'''
WebDriverWait(driver,10,0.1).until(EC.visibility_of_any_elements_located((locator)))

'''判断指定的元素中是否包含了预期的字符串，返回布尔值'''
WebDriverWait(driver,10,0.1).until(EC.text_to_be_present_in_element((locator),'预期的text'))

'''判断指定元素的value属性值中是否包含了预期的字符串，返回布尔值(注意：只是value属性)'''
WebDriverWait(driver,10,0.1).until(EC.text_to_be_present_in_element_value((locator),'预期的text'))

'''判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False'''
WebDriverWait(driver,10,0.1).until(EC.frame_to_be_available_and_switch_to_it(locator))

'''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素'''
WebDriverWait(driver,10,0.1).until(EC.invisibility_of_element_located((locator)))

'''判断某个元素是否可见并且是可点击的，如果是的就返回这个元素，否则返回False'''
WebDriverWait(driver,10,0.1).until(EC.element_to_be_clickable((locator)))

'''等待某个元素从dom树中移除'''
WebDriverWait(driver,10,0.1).until(EC.staleness_of(driver.find_element(locator)))

'''判断某个元素是否被选中了,一般用在下拉列表'''
WebDriverWait(driver,10,0.1).until(EC.element_to_be_selected(driver.find_element(locator)))

'''判断某个元素的选中状态是否符合预期'''
WebDriverWait(driver,10,0.1).until(EC.element_selection_state_to_be(driver.find_element(locator),True))

'''判断某个元素的选中状态是否符合预期'''
WebDriverWait(driver,10,0.1).until(EC.element_located_selection_state_to_be((locator),True))

'''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''
accept = WebDriverWait(driver,10,0.1).until(EC.alert_is_present())
```

<br>
<br>

---

相关链接：    
[Selenium10--webdriver的高级操作（四）三种等待&文件上传](https://zhuanlan.zhihu.com/p/450647425)