---
layout:        post
title:         "Python3 | urllib3 运行报错连接错误443问题"
subtitle:      "HTTPSConnectionPool(host='nominatim.openstreetmap.org', port=443)"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 错误日志
```text
HTTPSConnectionPool(host='nominatim.openstreetmap.org', port=443): Max retries exceeded with

url: /search?postalcode=33101&country=USA&format=json&limit=1 (Caused by ProxyError('Cannot connect to proxy.', FileNotFoundError(2, 'No such file or directory')))
```

<br>
<br>

### 解决方法
卸载现有的 urllib3 库，然后安装低版本：     
```
> pip uninstall urllib3
> pip install urllib3==1.25.11
```
