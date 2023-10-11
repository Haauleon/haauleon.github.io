---
layout:        post
title:         "爬虫 | Docker环境selenium项目异常处理"
subtitle:      "selenium.common.exceptions.WebDriverException: Message: unknown error: session deleted because of page crash"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 异常描述
&emsp;&emsp;在部署的 Docker 项目上用到了 selenium 去访问亚马逊网页链接，最近出现下面的问题频率较高。             
```bash
...
selenium.common.exceptions.WebDriverException: Message: unknown error: session deleted because of page crash
from tab crashed
(Session info: headless chrome=102.0.5005.182)
```

<br>
<br>

### 异常原因
&emsp;&emsp;通过 Google 搜索问题，发现是 `/dev/shm` 空间不够的原因。             
```bash
Solution
There are diverse solution to this issue. However as per UnknownError: session deleted because of page crash from tab crashed this issue can be solved by either of the following solutions:

Add the following chrome_options:

chrome_options.add_argument('--no-sandbox')         
Chrome seem to crash in Docker containers on certain pages due to too small /dev/shm. So you may have to fix the small /dev/shm size.

An example:

sudo mount -t tmpfs -o rw,nosuid,nodev,noexec,relatime,size=512M tmpfs /dev/shm
It also works if you use -v /dev/shm:/dev/shm option to share host /dev/shm

Another way to make it work would be to add the chrome_options as --disable-dev-shm-usage. This will force Chrome to use the /tmp directory instead. This may slow down the execution though since disk will be used instead of memory.

chrome_options.add_argument('--disable-dev-shm-usage')  
```

<br>
<br>

### 异常处理
&emsp;&emsp;可以通过添加了两个启动参数来解决这个问题。                    
```python
# 设置无头浏览器隐式访问
chrome_options.add_argument('--headless')
# 这将强制 Chrome 改为使用该/tmp目录。这可能会减慢执行速度，因为将使用磁盘而不是内存
chrome_options.add_argument('--disable-dev-shm-usage')
```

<br>
<br>

---

相关链接：     
[common.exceptions.WebDriverException_ Message_ unknown error_ session deleted because of page crash](https://blog.csdn.net/xiaokai1999/article/details/129182755)    