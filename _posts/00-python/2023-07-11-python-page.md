---
layout:        post
title:         "Python3 | 计算总页数"
subtitle:      "传入记录总数和每页显示的记录条数，计算总共要翻多少页"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 计算总页数
开发 Web 应用程序中，经常需要进行分页操作。我们可以使用 Python 计算出需要分页的总数，方便我们进行页面的切换。       

```python
def get_page_count(total, per_page):
    """
    计算分页总数
    :param total: 记录总数
    :param per_page: 每页记录数
    :return: 分页总数
    """
    page_count = total // per_page
    if total % per_page != 0:
        page_count += 1
        return page_count

# 测试代码
total = 23
per_page = 5
page_count = get_page_count(total, per_page)
print("总数为{}，每页{}条，共分{}页".format(total, per_page, page_count))
```

<br>
<br>

---

相关链接：    
[python 计算总页数](https://www.yzktw.com.cn/post/1238018.html)