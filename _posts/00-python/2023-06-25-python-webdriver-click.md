---
layout:        post
title:         "爬虫 | webdriver 点击元素失败"
subtitle:      "元素被遮挡或覆盖导致无法点击 element click intercepted"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 异常
python 自动化测试，遇到 `selenium.common.exceptions.ElementClickInterceptedException: Message: Element` 错误。    

<br>
<br>

### 解决
这个错误表示在尝试单击一个元素时，该元素被其他元素遮挡或覆盖。具体来说，错误消息中显示的是无法单击的元素和阻挡它的元素。      
要解决这个问题，通常有以下两种方法。     

<br>

#### 1、使用ActionChains类
使用 ActionChains 类来模拟鼠标操作，将鼠标移动到可单击的元素上，然后单击它。例如：      
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

# 访问页面
driver.get('http://example.com')

# 查找元素
element = driver.find_element(By.XPATH, "//a[@class='ui-pager-next']")

# 使用 ActionChains 模拟鼠标操作
actions = ActionChains(driver)
actions.move_to_element(element).click().perform()

# 关闭浏览器
driver.quit()
```

在这个示例代码中，我们使用 ActionChains 类来模拟鼠标操作。首先，我们使用 `driver.find_element(By.XPATH, "//a[@class='ui-pager-next']")` 查找可单击的元素(`a`标签)。接下来，我们创建了一个 actions 对象，并使用 `actions.move_to_element(element)` 将鼠标移动到该元素上，再使用 `click()` 方法单击它。最后，使用 `perform()` 方法来执行操作。      

<br>

#### 2、使用execute_script方法
尝试使用 `execute_script()` 方法通过 JavaScript 执行单击事件。例如：    
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 访问页面
driver.get('http://example.com')

# 查找元素
element = driver.find_element(By.XPATH, "//a[@class='ui-pager-next']")

# 使用 JavaScript 执行单击事件
driver.execute_script("arguments[0].click();", element)

# 关闭浏览器
driver.quit()
```

在这个示例代码中，我们使用 `driver.execute_script()` 方法通过 JavaScript 执行了单击事件。我们将可单击的元素(`a`标签)和事件传递给 `execute_script()` 方法，直接模拟单击事件。       
无论哪种方法，都可以通过模拟鼠标操作或 JavaScript 来成功地单击元素，从而解决这个异常。     

<br>
<br>

---

相关链接：   
[selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted](https://www.zhihu.com/tardis/bd/art/626704447?source_id=1001)     
[python自动化测试，遇到selenium.common.exceptions.ElementClickInterceptedException: Message: Element错的解决方法](https://www.cnblogs.com/zz-1021/p/14476155.html)