---
layout:        post
title:         "selenium | 自动下载 chromedriver"
subtitle:      "使用 webdriver-manager 自动配置 chromedriver"
date:          2021-07-06
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - UI 测试
    - Python
---

## 一、背景       
[官网介绍](https://chromedriver.chromium.org/)        

> WebDriver 是一个开源工具，用于跨多种浏览器自动测试 web 应用程序。它提供导航到网页、用户输入、JavaScript 执行等功能。ChromeDriver 是一个独立的服务器，它实现了W3C WebDriver 标准。ChromeDriver 适用于 Android 上的 Chrome 和桌面上的 Chrome（Mac、Linux、Windows 和 ChromeOS）。        

&emsp;&emsp;目前市面仍需要结合浏览器驱动来完成 UI 自动化测试，但是不同的 chrome 浏览器版本对应不同版本的 chromedriver.exe 二进制文件。以往都需要翻墙然后手动去到 [https://sites.google.com/chromium.org/driver/downloads](https://sites.google.com/chromium.org/driver/downloads) 此页面找到对应 chrome 版本的驱动进行下载，然后加入环境变量（windows 系统）。现在可通过 `webdriver-manager` 进行自动下载并自动加入环境变量，整个过程不需要人工参与。同样可用于设置 Firefox、Edge 和 ie 二进制文件。           

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
# -*- coding:utf-8 -*-
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   driver.py
@Function:   配置浏览器驱动
"""

import io
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver import Remote

# 改变标准输出的默认编码，cmd对utf-8不是很好支持会导致中文乱码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


def browser():
	'''启动浏览器驱动'''
	# 消除 Chrome正受到自动测试软件的控制 提示
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

    # 启动浏览器驱动
	driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
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