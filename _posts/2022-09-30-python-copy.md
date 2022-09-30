---
layout:        post
title:         "Python3 | 深拷贝与浅拷贝"
subtitle:      "简单回顾一下两者的区别"
author:        "Haauleon"
header-style:  text
tags:
    - Python
    - Pythoneer
---

### 比较两者
&emsp;&emsp;改变原列表中的可变对象（列表、字典、集合）元素，则浅拷贝中对应可变对象会随之变化而变化，而深拷贝不会受影响。     

```python
# 比较浅拷贝与深拷贝
import copy

list_a = [2018, 10, '2018-10-1', ['hi', 1, 2], (33, 44)]
list_b = ['hi', 1, 2]
list_c = list_a.copy()  # list_c == [2018, 10, '2018-10-1', ['hi', 1, 2], (33, 44)]
list_d = copy.deepcopy(list_a)  # list_d == [2018, 10, '2018-10-1', ['hi', 1, 2], (33, 44)]
# 改变原列表中的可变对象元素
list_a[3].clear()  # list_a == [2018, 10, '2018-10-1', [], (33, 44)]
print("list_a = ", list_a)
# 浅拷贝中的可变对象会随原列表变化而变化
print(bool(list_c == list_a))
print("list_c = ", list_c)
# 深拷贝中的可变对象不会随原列表变化而变化
print(bool(list_d == list_a))
print("list_d = ", list_d)
```