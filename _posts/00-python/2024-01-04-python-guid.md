---
layout:        post
title:         "Python3 | 使用uuid模块生成GUID"
subtitle:      "GUID（全局唯一标识符）"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### GUID（全局唯一标识符）
在 Python3 中可以使用 uuid 模块来生成 GUID（全局唯一标识符）。             

下面是一段示例代码：              
```python
import uuid

guid = str(uuid.uuid4())
print("Generated GUID:", guid)
```

运行上述代码将会输出类似于 "Generated GUID: cf7e5a2d-8b3c-4961-ae0d-5bfefdbffebe" 的结果，其中 cf7e5a2d-8b3c-4961-ae0d-5bfefdbffebe 就是生成的 GUID 值。