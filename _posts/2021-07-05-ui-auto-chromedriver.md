---
layout:        post
title:         "selenium | 自动下载浏览器驱动"
subtitle:      "使用 webdriver-manager 自动配置 chromedriver"
date:          2021-07-05
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - UI 测试
---

## 一、背景
&emsp;&emsp;目前市面仍需要结合 chromedriver 浏览器驱动来完成 UI 自动化测试，但是不同的 chrome 浏览器版本对应不同版本的 chromedriver.exe 二进制文件。以往都需要翻墙然后手动去到 [https://sites.google.com/chromium.org/driver/downloads](https://sites.google.com/chromium.org/driver/downloads) 此页面找到对应 chrome 版本的驱动进行下载，然后加入环境变量（windows 系统）。现在可通过 `webdriver-manager` 进行自动下载并自动加入环境变量，整个过程不需要人工参与。同样可用于设置 Firefox、Edge 和 ie 二进制文件。             

<br><br>

## 二、使用
###### 1.安装模块
```
$ pip install webdriver-manager
```

<br><br>

###### 2.使用模块
```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
```

<br><br>

###### 3.使用实例
```python
"""
@File   driver.py
"""

import sys
import io
import os
from selenium.webdriver import Remote
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# 改变标准输出的默认编码，cmd对utf-8不是很好支持会导致中文乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


def browser():
	'''启动浏览器驱动'''
	# 消除“Chrome正受到自动测试软件的控制”提示
	options = webdriver.ChromeOptions() 
	options.add_argument("disable-infobars")
	
	# driver = webdriver.Chrome(chrome_options = options)
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.maximize_window()
	return driver


if __name__ == '__main__':
	drv = browser()
```

<br>

实现效果：            
```
====== WebDriver manager ======
Current google-chrome version is 91.0.4472
Get LATEST driver version for 91.0.4472
Driver [C:\Users\Haauleon\.wdm\drivers\chromedriver\win32\91.0.4472.101\chromedriver.exe] found in cache
```