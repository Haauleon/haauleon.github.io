---
layout:        post
title:         "爬虫 | 新历和旧历日期的转换"
subtitle:      ""
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
  - Python
  - 爬虫
  - 数据监控
---

&emsp;&emsp;最近有新旧历日期转换的需求，就把别人的写的方法进行了封装改造，我写的比较简单，应该还看得过去。代码如下：       

<br>

```python
# -*- coding:utf-8 -*-
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   get_lunar.py
@Date    :   2021-09-01 11:00:00
@Function:   新历和旧历相互转换
"""
import sxtwl

# 日历中文索引
YMC = [
    "十一", "十二", "正", "二", "三", 
    "四", "五", "六", "七", "八", "九", "十"
]

RMC = [
    "初一", "初二", "初三", "初四", "初五", 
    "初六", "初七", "初八", "初九", "初十",
    "十一", "十二", "十三", "十四", "十五", 
    "十六", "十七", "十八", "十九", "二十", 
    "廿一", "廿二", "廿三", "廿四", "廿五", 
    "廿六", "廿七", "廿八", "廿九", "三十", "卅一"
]

lunar = sxtwl.Lunar()  # 实例化日历库


class GetDay:
    '''新旧历的转换'''

    @staticmethod
    def get_day_by_lunar(*solar_date):
        '''旧历转新历'''
        year, month, day = solar_date
        lunar_date = lunar.getDayByLunar(year, month, day, False)
        return "%s年%s月%s日" %(lunar_date.y, lunar_date.m, lunar_date.d)

    @staticmethod
    def get_day_by_solar(*lunar_date):
        '''新历转旧历'''
        year, month, day = lunar_date
        solar_date = lunar.getDayBySolar(year, month, day)
        # bool(solar_date.Lleap) 为True即润年，反之则不是润年
        return "%s月%s日" %(YMC[solar_date.Lmc], RMC[solar_date.Ldi])


if __name__ == '__main__':
    print(GetDay.get_day_by_lunar(2021,8,12))
    print(GetDay.get_day_by_solar(2021,9,18))
```