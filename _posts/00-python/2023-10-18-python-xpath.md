---
layout:        post
title:         "爬虫 | xpath 定位方法详解"
subtitle:      "python + selenium + xpath 定位方法详解"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 前言
&emsp;&emsp;selenium 中的 xpath 有八大定位策略，分别是 id、name、class name、tag name、link text、partial link text、xpath、css 。那么我们今天呢主要来讲讲八大定位策略中的 xpath 的定位方法。

<br>
<br>

### 一、xpath基本定位用法
#### 1.1 使用id定位
```python
driver.find_element_by_xpath('//input[@id="kw"]') 
```

[](\img\in-post\post-python\2023-10-18-python-xpath-1.png)

<br>

#### 1.2 使用class定位
```python
driver.find_element_by_xpath('//input[@class="s_ipt"]')
```

[](\img\in-post\post-python\2023-10-18-python-xpath-2.png)

<br>

#### 1.3 其他方式结合xpath定位
通过常用的 8 种方式结合 xpath 均可以定位（name、tag_name、link_text、partial_link_text）以上只列举了 2 种常用方式哦。           

<br>
<br>

### 二、xpath相对路径/绝对路径定位
#### 2.1 相对定位
以 `//` 开头 如：       
```
//form//input[@name="phone"]
```

[](\img\in-post\post-python\2023-10-18-python-xpath-3.png)

<br>

#### ​2.2 绝对定位
以 `/` 开头，但是要从根目录开始，比较繁琐，一般不建议使用 如：       
```
/html/body/div/a
```

[](\img\in-post\post-python\2023-10-18-python-xpath-4.png)


<br>
<br>

### 三、xpath文本、模糊、逻辑定位
#### 3.1 文本定位
使用 `text()` 元素的 text 内容 如：          
```
//button[text()="登录"]
```

[](\img\in-post\post-python\2023-10-18-python-xpath-5.png)          

<br>

#### 3.2 模糊定位contains
使用 `contains()` 包含函数（多用于display属性），如：     
```
//button[contains(text(),"登录")]
//button[contains(@class,"btn")]
``` 

[](\img\in-post\post-python\2023-10-18-python-xpath-6.png)          


<br>

#### 3.3 模糊定位匹配开头/结尾的属性值
使用 `starts-with` 匹配以xx开头的属性值；使用 `ends-with` 匹配以xx结尾的属性值。如：            
```
//button[starts-with(@class,"btn")]
//input[ends-with(@class,"-special")]
```

<br>

#### 3.4 使用逻辑运算符
使用逻辑运算符 `and`、`or`。如：         
```
//input[@name="phone" and @datatype="m"]
```

<br>
<br>

### 四、xpath轴定位
#### 4.1 轴运算
ancestor：祖先节点 包括父 　　 
parent：父节点 　　 
preceding-sibling：当前元素节点标签之前的所有兄弟节点 　　 
preceding：当前元素节点标签之前的所有节点      
following-sibling: 当前元素节点标签之后的所有兄弟节点        
following：当前元素节点标签之后的所有节点         

使用语法： `轴名称 :: 节点名称`          
使用较多场景：页面显示为一个表格样式的数据列             

如：            
[](\img\in-post\post-python\2023-10-18-python-xpath-7.png)          

[](\img\in-post\post-python\2023-10-18-python-xpath-8.png)          

注意：             
（1）定位 找到元素 -- 做到唯一识别            
（2）优先使用id              
（3）舍弃：有下标的出现、有绝对定位的出现、id动态变化时舍弃              

```python
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
 

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.maximize_window()
 
time.sleep(3)
 
# 定位百度搜索框
driver.find_element_by_id("kw").send_keys("python")
time.sleep(3)
driver.find_element_by_id("su").click()
time.sleep(5)
 
# 找到这个元素
ele = driver.find_element_by_xpath('//a[text()="_百度百科"]')
 
# 拖动元素到可见区域--scrollIntoView() 拉到顶部显示，有可能会被导航栏遮挡，定位不到而报错；scrollIntoView(false)可视区域底部对齐
driver.execute_script("arguments[0].scrollIntoView(false);", ele)
time.sleep(5)
driver.quit()
```

<br>
<br>

### 定位后的常见操作

|操作|注释|
|----|----|
|get(url)|打开网页|
|send_keys(str)|输入|
|click()|点击|
|clear()|清空|
|text|获取标签文本内容|
|get_attribute('属性')|获取元素属性值|
|close()|关闭当前标签页|
|quit()|关闭浏览器，释放进程|

<br>
<br>

### FAQ
脚本结束如果没有调用 `quit()` 方法，chromedriver 进程会在后台继续运行。大概占用 4M 空间。如果创建多了不关，会导致电脑卡。            
```python
__import__('os').system("taskkill /f /t /im chromedriver.exe")
```


<br>
<br>

---

相关链接：    
[python—selenium —xpath定位方法详解](https://blog.csdn.net/qishuzdh/article/details/124847147)