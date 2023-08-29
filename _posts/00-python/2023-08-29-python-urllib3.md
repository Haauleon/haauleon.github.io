---
layout:        post
title:         "爬虫 | 检查字符串是否为 URL"
subtitle:      "给定一个字符串，判断该字符串是否为 URL"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 如何检查字符串是否为URL
#### 方法一：使用Python自带的re库进行URL正则匹配
正则表达式可以识别并匹配形如 URL 的字符，将 URL 从文本中提取出来。        
```python
import re

def is_url_regex(string):
    """
    判断字符串是否为URL的正则表达式匹配方法
    """
    regex = (
        r'^https?:\/\/(?:www\.)?'
        r'(?:(?:[A-Z\d][A-Z\d-]{0,61}[A-Z\d]\.)|[A-Z\d]\.)'
        r'+[A-Z]{2,6}(?::\d+)?'
        r'(?:\/[-a-zA-Z\d%_.~+]*)*'
        r'(?:\?[;&a-zA-Z\d%_.~+=-]*)?'
        r'(?:#[-a-zA-Z\d_]*)?$')
    return re.match(regex, string, re.IGNORECASE)

```

&emsp;&emsp;上述方法使用了正则表达式，对字符串中可能出现的 URL 进行了匹配。其缺点在于代码可读性较差，且在实际代码中可能需要根据实际情况进行相应的修改，适用性较为有限。           


<br>
<br>

#### 方法二：使用Python的urllib库进行URL处理
urllib 是 Python 的一个标准库，提供了一系列操作 URL 的函数，包括 URL 编解码、URL 解析、发送 HTTP 请求等功能。使用此库，可以便捷的对字符串中的 URL 进行处理。                
```python
from urllib.parse import urlparse

def is_url_urllib(string):
    """
    判断字符串是否为URL的urllib库方法
    """
    try:
        result = urlparse(string)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

```

&emsp;&emsp;上述方法使用 urllib 库的 urlparse 函数，将输入的字符串解析成 URL 元组，再判断是否有协议和网络位置字段，以判断该字符串是否为 URL。相较于正则表达式，此种方法可读性更高，适用性更广。               

<br>
<br>

#### 如何对字符串中的URL进行提取和解析
当在程序中识别了字符串中的 URL 后，就需要对这些URL进行相应的处理。例如，可以获取其域名、协议、路径等信息，以便后续的操作。此时，可以通过 Python 标准库中的 urllib 库，灵活的对 URL 进行提取和解析。             
```python
from urllib.parse import urlparse

url = "https://stackoverflow.com/questions/123456/test-url-extract"
parsed_url = urlparse(url)

print(parsed_url.scheme)  # 打印URL协议，输出https
print(parsed_url.netloc)  # 打印网络位置，输出stackoverflow.com
print(parsed_url.path)  # 打印URL路径，输出/questions/123456/test-url-extract

```

&emsp;&emsp;上述代码中，我们利用 Python 中的 urllib 库中的 urlparse 函数，对 URL 进行了解析，将其各个部分提取出来，并进行了打印输出。            
&emsp;&emsp;通过对解析结果的分析，可以发现 urlparse 函数将 URL 解析成了一个元组对象，包含了其协议、网络地址、路径、参数、查询字符串和锚点等各个部分。利用此元组对象，可以灵活的对 URL 进行处理和操作。             


<br>
<br>

---

相关链接：    
[Python程序检查字符串中的URL](https://deepinout.com/python/python-programs/t_python-program-to-check-for-url-in-a-string.html)