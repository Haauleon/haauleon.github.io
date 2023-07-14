---
layout:        post
title:         "Python3 | 解析数据库的 cron 表达式"
subtitle:      "网上没有类似的实现方法，那就来自己实现一个cron表达式解析类"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 代码实现
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   cron_parser.py 
@Date    :   2023-07-14 17:32
@Function:   cron表达式解析

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2023-07-14 17:32         haauleon         1.0           None
"""


class CronParser:

    def __init__(self):
        self.cron = None  # cron表达式，如 0 43 17 ? * MON-FRI

    @property
    def seconds(self):
        return tuple(self.cron.split(' '))[0]

    @property
    def minutes(self):
        return tuple(self.cron.split(' '))[1]

    @property
    def hours(self):
        return tuple(self.cron.split(' '))[2]

    @property
    def day_of_month(self):
        day_of_month = tuple(self.cron.split(' '))[3]
        day_of_month = day_of_month if not day_of_month == '?' else None
        return day_of_month

    @property
    def month(self):
        return tuple(self.cron.split(' '))[4]

    @property
    def day_of_week(self):
        day_of_week = tuple(self.cron.split(' '))[5]
        day_of_week = day_of_week if not day_of_week == '?' else None
        return day_of_week
```
