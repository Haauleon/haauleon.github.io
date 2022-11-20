---
layout:        post
title:         "爬虫 | 豆瓣小组-珠海租房监控器"
subtitle:      ""
date:          2021-09-01
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
  - Python
  - 爬虫
  - 数据监控
---

&emsp;&emsp;目前有找银石雅园的房子的需求，特地写了一个脚本放在服务器上去定时爬取，然后推送到钉钉群。可以根据关键字查找，我主要找的是银石雅园。          

<br>


```python
# -*- coding:utf-8 -*-
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   douban_zufang.py
@Date    :   2021-08-26 12:00:00
@Function:   豆瓣小组-珠海租房监控器，目前有找银石雅园的房子的需求
"""
import requests
import re
from functools import wraps
import json

Search_Key = '银石雅园'

def traceback_error(func):
    @wraps(func)
    def wraper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
        except Exception as e:
            import traceback
            ex_msg = '{exception}'.format(exception=traceback.format_exc())
            print(ex_msg)
            result = ex_msg
        return result
    return wraper


class DingDingNotice:
    '''钉钉发送类'''

    def __init__(self, ding_token=None, atMobiles=None, isAtAll=None):
        # 根据电话@用户
        self.atMobiles = ['1397606xxxx',] if atMobiles==None else atMobiles
        # self.token = 'cbb3b771657ef' if ding_token==None else ding_token
        # 是否@所有人
        self.isAtAll = True if isAtAll==None else isAtAll
        self.token = '1bf33b1503399d9610fxxxxxxxxx'
        self.api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(self.token)
        self.headers = {'Content-Type': 'application/json;charset=utf-8'}

    @traceback_error
    def send_msg(self,content):
        msg = {
            'msgtype': 'text',
            'text': {'content': content},
            'at': {'atMobiles': self.atMobiles, 'isAtAll': self.isAtAll}
        }
        data = requests.post(self.api, data=json.dumps(msg), headers=self.headers).json()
        return json.dumps(data)


class DoubanGroup:
    '''豆瓣小组'''

    def __init__(self):
        self.group_url = "https://www.douban.com/group/555279/discussion?start=%s"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'cache-control': "no-cache",
            'Cookie': 'xxxxx',
        }

    def get_group_titles(self, search_key):
        '''获取 3 页豆瓣小组-珠海租房的帖子'''
        zufangs = dict()
        for page in range(0, 51, 25):
            resp = requests.request("GET", self.group_url % page, headers=self.headers)

            titles = re.compile(r'title="(.*?)"',re.S)    
            titles = titles.findall(resp.text)            # 获取单页所有标题

            links = re.compile(r'href="(.*?)"',re.S)      
            links = links.findall(resp.text)              # 获取单页所有链接
            zufang_links = []             
            for j in links:
                if '/group/topic/' in j:
                    '''过滤非豆瓣小组的租房帖子'''
                    zufang_links.append(j)

            zufang = dict(zip(titles, zufang_links))
            zufangs.update(zufang)

        zufang_search = []
        for i,j in zufangs.items():
            if search_key in i:
                '''根据关键字搜索结果'''
                zufang_search.append("%s %s" %(i,j))  
        return zufang_search


def zufang_monitour_run():
    '''抓取豆瓣租房小组帖子脚本执行'''
    douban = DoubanGroup()
    dingding_msg = douban.get_group_titles(Search_Key)
    service = DingDingNotice()
    service.send_msg(
        content='豆瓣租房小组监控提醒！现在{}的租房帖子有{}条，分别是：\n\n'.format(Search_Key, len(dingding_msg)) + 
                '' + 
                '\n'.join(dingding_msg) + 
                '\n\n请及时查看！'
    )


if __name__ == '__main__':
    zufang_monitour_run()
```