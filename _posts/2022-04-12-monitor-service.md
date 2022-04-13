---
layout:        post
title:         "Python3 | 爬虫执行策略脚本"
subtitle:      "爬取源: http://www.hengqin.gov.cn/macao_zh_hans/hzqgl/dtyw/xwbb/"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 爬虫
    - Python
    - 小而美脚本
---

### 背景
&emsp;&emsp;已开发上线的 [横琴粤澳深度合作区澳门办事处](https://www.hengqin-cooperation.gov.mo/zh_CN) 网站的最新动态数据需要根据爬取的数据进行更新，源网站是 [横琴粤澳深度合作区](http://www.hengqin.gov.cn/macao_zh_hans/hzqgl/dtyw/xwbb/) 。目前的爬虫策略是运营人员每天需要定时去网站后台手动同步（调取爬虫脚本爬数据入库）并进行数据状态的更新，从而显示在前台。麻烦的是，现在公司没有专门的运营人员，所以我也肩负起了运营的任务。但是，我没有时间去人工处理。


### 需求
```python
# -*- coding:utf-8 -*-
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   run_hengqing_service_v1.py
@Date    :   2022-04-12 14:56:00
@Function:   同步成功的资讯，判断当前日期和横琴官网资讯日期，如果日期一致则更新资讯状态显示至澳门办事处网站前台
澳门办事处网站前台资讯更新添加自动同步脚本且测试通过，目前脚本执行策略：
1、隔5分钟去校验横琴官网资讯，如果有返回资讯则进行同步
2、同步成功的资讯，判断当前日期和横琴官网资讯日期，如果日期一致则更新资讯状态显示至澳门办事处网站前台
3、脚本同样可以具有预防爬虫脚本报错的功能
4、脚本支持周末自动同步资讯
"""

import requests
import time
import json
import logging
import sys
from colorama import Fore, Style

COOKIE = 'xxxxxxxx'


# 日志配置
_logger = logging.getLogger('macau')            # 获取日志记录器
_logger.setLevel(logging.DEBUG)                 # 设置日志等级
_handler = logging.StreamHandler(sys.stdout)    # 输入到控制台的 handler
_logger.addHandler(_handler)                    # 日志记录器增加 handler


def info(msg):
    '''日志函数'''
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.info(Fore.GREEN + now + " [INFO] " + str(msg) + Style.RESET_ALL)

def error(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.error(Fore.RED + now + " [ERROR] " + str(msg) + Style.RESET_ALL)

def _print(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.debug(Fore.BLUE + now + " [PRINT] " + str(msg) + Style.RESET_ALL)



class RestClient:
    '''请求方法封装'''

    def __init__(self):
        self.user = requests.Session()

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def request(self, url, method, data=None, json=None, **kwargs):
        if method == "GET":
            return self.user.get(url, **kwargs)
        if method == "POST":
            return self.user.post(url, data, json, **kwargs)
        if method == "DELETE":
            return self.user.delete(url, **kwargs)


class MacauOfficeInfo(RestClient):
    '''同步横琴官网资讯并更新资讯状态'''

    def __init__(self, **kwargs):
        super(MacauOfficeInfo, self).__init__(**kwargs)
        self.headers = {'Cookie': COOKIE}
        self.base_url = 'http://boss.macau-office.bringbuys.com/api'
        self.cur_time = time.strftime("%Y-%m-%d")

    def pull_info_list(self):
        '''同步官网最新资讯'''
        url = self.base_url + '/information/pullInformation'
        res = self.get(url, headers=self.headers).json()
        info(res['msg'])

    def get_info_list(self):
        '''获取最新资讯列表'''
        url = self.base_url + '/information/list?showIndexType=LATEST_NEWS_TYPE&showIndex=information_news&page=1&limit=50'
        res = self.get(url, headers=self.headers).json()
        r = res['result']['list']
        for info in range(len(r)):
            if self.cur_time == r[info]['informationDate'].split(' ')[0]:
                if r[info]['isShow'] == 0 or r[info]['isTop'] == 0:
                    detail = (r[info]['id'], r[info]['title'])
                    yield detail
        
    def update_info_top_show(self, info_id, info_title):
        '''更新最新资讯状态'''
        url = self.base_url + '/information/updateState'
        payload = json.dumps({
            "id": info_id,
            "sortNo": 1,
            "isShow": 1,
            "isTop": 1,
            "isRecommend": 0,
            "title": info_title,
        })
        headers = {
            'Cookie': COOKIE,
            'Content-Type': 'application/json',
        }
        res = self.post(url, data=payload, headers=headers).json()
        if res['success']:
            info('最新资讯更新成功: %s' %info_title)


def run_info():
    '''同步官网资讯且更新资讯'''
    macau = MacauOfficeInfo()
    macau.pull_info_list()
    time.sleep(100)
    infos = macau.get_info_list()
    # macau.pull_info_list()
    while True:
        try:
            info_id, info_title = next(infos)
            macau.update_info_top_show(info_id, info_title)
        except:
            break


if __name__ == "__main__":
    # 同步官网资讯且更新资讯
    _print("脚本开始执行")
    run_info()
    _print("脚本执行完成")
```