---
layout:        post
title:         "Python3 | requests 访问 https 网站"
subtitle:      "有些网站 https 需要证书才可以访问, 两种解决方法"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 爬虫
    - Python
---


### 一、指定证书
&emsp;&emsp;指定一个本地证书用作客户端证书，可以是单个文件（包含秘钥和证书）或一个包含两个文件路径的元组。     

```python
import ssl

requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))
```

<br><br>

### 二、忽略证书（不安全）
&emsp;&emsp;如果将 `verify` 设置为 `False`, `requests` 也能忽略对 ssl 证书的验证。    

```python
import requests
from requests.packages import urllib3

urllib3.disable_warinings()
req = requests.get('https://frwsyw.bjgjj.gov.cn/ish', verify=False)
```

<br>

###### 解决 warning 的方式
```python
InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.

警告：正在发出未经验证的 HTTPS 请求。强烈建议添加证书验证。
```


解决 warning 的方式：忽略验证警告信息，有两种方式。     
**新版本解决方式：**       
```python
import urllib3
urllib3.disable_warinings(urllib3.exceptions.InsecureRequestWarning)
```

<br>

**旧版本解决方式：**      
```python
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warinings(InsecureRequestWarning)
```