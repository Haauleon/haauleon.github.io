---
layout:        post
title:         "Python3 | pyppeteer 运行报错"
subtitle:      "urllib3.exceptions.MaxRetryError: HTTPSConnectionPool"
date:          2021-03-19
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - 异常库
---


## 背景
&emsp;&emsp;pyppeteer 安装完成后执行以下 `百度截图脚本` 代码：                                               
```python
#!/usr/bin/env python3

import asyncio
from pyppeteer import launch

async def main():
browser = await launch()
page = await browser.newPage()
await page.goto('https://www.baidu.com')
await page.screenshot({'path': 'homepage.png'})
await browser.close()

asyncio.run(main())
```
<br>

执行结果：                             
```
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='storage.googleapis.com', port=443): Max retries exceeded with url: /chromium-browser-snapshots/Mac/588429/chrome-mac.zip (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1091)')))
```
<br><br>

## 解决方法
###### 一、检查 本地 urllib3 的版本
```
$ pip show urllib3
```
<br>

执行结果：                           
```
Name: urllib3
Version: 1.25.8
Summary: HTTP library with thread-safe connection pooling, file post, and more.
Home-page: https://urllib3.readthedocs.io/
Author: Andrey Petrov
Author-email: andrey.petrov@shazow.net
License: MIT
Location: /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages
Requires: 
Required-by: selenium, requests, pyppeteer, elasticsearch
```
<br>

分析：当前安装的 urllib3 的版本是 `1.25.8` 。

<br><br>

###### 二、安装 1.25 以下的版本
```
$ pip install -U &quot;urllib3<1.25&quot;
$ pip show urllib3
```
<br>

执行结果：                         
```
Name: urllib3
Version: 1.24.3
Summary: HTTP library with thread-safe connection pooling, file post, and more.
Home-page: https://urllib3.readthedocs.io/
Author: Andrey Petrov
Author-email: andrey.petrov@shazow.net
License: MIT
Location: /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages
Requires: 
Required-by: selenium, requests, pyppeteer, elasticsearch
```
<br><br>

###### 三、重新在终端执行程序
程序运行正确，截图成功：                    
![](\img\in-post\post-python\2021-03-19-python-pyppeteer-1.jpg)
