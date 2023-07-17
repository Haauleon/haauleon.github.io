---
layout:        post
title:         "Python3 | 把方法变成属性调用"
subtitle:      "Python内置的@property装饰器可以把一个方法变成属性调用"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 示例代码
```python
"""
装饰器（decorator）可以给函数动态加上功能,对于类的方法，装饰器一样起作用。
Python内置的@property装饰器就是负责把一个方法变成属性调用的：
@property:把一个getter方法xxx(无入参)变成属性
@xxx.setter:负责把一个setter方法(有入参)变成属性赋值
"""

class CronParser:

    def __init__(self):
        self.cron = None

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

<br>

1、实例化一个对象后获取属性值     
```python
c = CronParser()
c.cron = '0 41 8 ? * MON-FRI'
print(c.seconds)
print(c.minutes)
print(c.hours)
print(c.day_of_month)
print(c.month)
print(c.day_of_week)
```

```
0
41
8
None
*
MON-FRI
```

2、通过继承实现获取属性值      
```python
class RunTime(CronParser):

    def __init__(self):
        super().__init__()
        self.cron = '30 45 9 ? * MON-FRI'


r = RunTime()
print(r.seconds)
print(r.minutes)
print(r.hours)
print(r.day_of_month)
print(r.month)
print(r.day_of_week)
```

```
30
45
9
None
*
MON-FRI
```

<br>
<br>

---

相关链接：    
[python把方法变成属性调用](https://blog.csdn.net/qq_38091782/article/details/126257904)