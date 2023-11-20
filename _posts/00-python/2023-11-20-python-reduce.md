---
layout:        post
title:         "Python3 | 使用reduce()函数累加列表中所有元素数值"
subtitle:      "reduce(lambda x, y: x + y, numbers)"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### reduce()函数
```python
from functools import reduce


numbers = [1, 2, 3, 4, 5]
# 累积操作使用 lambda 函数来实现，lambda 函数接受两个参数 x 和 y，返回它们的和
sum = reduce(lambda x, y: x + y, numbers)
print(sum)
```

输出结果为 15，即列表中的所有元素累加起来的结果。            
 

<br>
<br>

---

相关链接：    
[Python 中如何使用 reduce() 函数将一个列表中的所有元素累加起来？](https://www.6qe.net/amg-article-96520-SJVIBLu9bU.html)