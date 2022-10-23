---
layout:        post
title:         "Python3 | 13 位 unix 时间戳的方法"
subtitle:      ""
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
---

### 代码设计
###### 10 位时间戳
```python
>>> import time
>>> t = time.time()
>>> print t
1436428326.76
>>> print int(t)
1436428326
>>> 
```

<br>

###### 13 位时间戳
```python
import time
millis = int(round(time.time() * 1000))
print millis
```

```python
import time

current_milli_time = lambda: int(round(time.time() * 1000))
Then:
>>> current_milli_time()
1378761833768
```