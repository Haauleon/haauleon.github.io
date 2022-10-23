---
layout:        post
title:         "python3 | 获取广东新冠数据"
subtitle:      ""
date:          2021-09-01
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
  - Python
---

&emsp;&emsp;我本人是没办法接种新冠疫苗的，因为过敏体质担心烂脸烂全身，所以很需要有珠海地区疫情的获取的需求。下面放一下自己写的 demo，可以根据实际需求进行优化改造。     

<br>


```python
# -*- coding:utf-8 -*-
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   get_ons_info.py
@Date    :   2021-08-24 16:00:00
@Function:   城市新冠疫情监控器
"""
import requests
import json

# 腾讯新冠疫情 API
ons_url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"


class ONS:
    '''新冠疫情监控'''

    @staticmethod
    def get_ons(provinces, cities):
        '''获取指定城市的疫情'''
    
        city_ons = dict()
        res = requests.get(ons_url).json()
        ons_data = json.loads(res["data"])
        areas = ons_data["areaTree"][0]["children"]
        for area in range(len(areas)):
            if areas[area]["name"] in provinces:
                province = areas[area]["children"]
                for i in range(len(province)):
                    if province[i]["name"] in cities:
                        city_ons[province[i]["name"]] = province[i]["today"]["confirm"]
        return city_ons


if __name__ == '__main__':

    print(ONS.get_ons(['广东', '湖南', '福建'], ['珠海', '深圳', '中山', '广州', '长沙', '福州']))  
    # {'长沙': 0, '中山': 0, '深圳': 0, '广州': 0, '珠海': 0, '福州': 0}
```