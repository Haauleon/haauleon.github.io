---
layout:        post
title:         "Python3 | cron 表达式验证和解析"
subtitle:      "使用 croniter 实现 cron 表达式验证和解析执行计划"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 安装
```
pip install croniter
```

<br>
<br>

### 示例
```python
# -*- coding: utf-8 -*-

from croniter import croniter
from datetime import datetime

# every 5 minutes
cron = '*/5 * * * *'

# 验证cron表达式
is_valid = croniter.is_valid(cron)
print(is_valid)
# True

# 执行计划
base = datetime(2010, 1, 25, 4, 46)

iter = croniter(cron, base)

print(iter.get_next(datetime))  # 2010-01-25 04:50:00
print(iter.get_next(datetime))  # 2010-01-25 04:55:00
print(iter.get_next(datetime))  # 2010-01-25 05:00:00
```