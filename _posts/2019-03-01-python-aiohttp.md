---
layout:        post
title:         "Python3 | aiohttp 模块提示 ssl 异常"
subtitle:      "aiohttp.client_exceptions.ClientConnectorCertificateError"
date:          2017-11-01
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - 异常库
---


## 背景
执行以下代码：         
```python
import aiohttp

url = "https://movie.douban.com/top250"

async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()
```

执行结果：提示 `aiohttp.client_exceptions.ClientConnectorCertificateError` 异常            
```
aiohttp.client_exceptions.ClientConnectorCertificateError: Cannot connect to host movie.douban.com:443 ssl:True [SSLCertVerificationError: (1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1091)')]
```
<br><br>

## 解决方法
```python
import aiohttp

url = "https://movie.douban.com/top250"

conn = aiohttp.TCPConnector(verify_ssl=False) # 防止ssl报错
async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(url) as response:
            return await response.text()
```
