---
layout:        post
title:         "Python3 | 芝麻城市代理刷网页"
subtitle:      "pyppeteer 实现刷网页浏览量 pv"
date:          2021-06-07
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - 爬虫
---

## 背景
&emsp;&emsp;前几天公司其他项目同事提了个需求过来，要用国内的代理池去刷网页浏览量 pv，我这里用的还是芝麻代理，理由很简单，就是每日可领用 20 个免费 ip。头痛的是每个 ip 的使用时长不能超过 25 分钟，超过就失效了，而且不知道是不是因为是免费的关系，有些 ip 经常出现连接超时的异常，我不得不做异常处理和超时判断。现在放一下代码，依旧在大神的代码基础上进行的修改。                     

<br><br>

## 代码
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   pyppeteer_process_v2.py
@Date    :   2021-06-07 16:22
"""

from os import stat
import random
import time

import asyncio
# from typing_extensions import Final
import pyppeteer
import requests


regions_list = [
    'hk', 'tw', 'china', 'us', 'mo', 'jp', 'pt', 'sg', 'ca', 'my'
]

# 全球代理IP地址
# ip_url = "http://tiqu.linksocket.com:81/abroad?num=1&type=1&lb=1&sb=0&flow=1&regions=%s&port=1&n=0"
# 流量查询接口
# flow_api = 'https://api.ipidea.net/index/index/get_my_balance?neek=210208&appkey=a85c3bcc4a83fdc63b4d0f1a231c95fc'

# 芝麻代理IP地址（国内）
ip_url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=0&city=0&yys=0&port=1&pack=153381&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=440000'
# 芝麻账户
username = "username"
password = "password"


class ZhimaGetIp:
    """
    获取每日免费 ip
    """
    def __init__(self):
        self.user = requests.Session()
        self.login_url = "https://wapi.http.linkudp.com/index/users/login_do"
        self.get_ip_url = "https://wapi.http.linkudp.com/index/users/get_day_free_pack"

    def union_get_free_ip(self):
        '''统一操作'''
        self.zhima_login(username, password)
        self.get_ip()
    
    def zhima_login(self, username, password):
        '''用户登录'''
        payload = "phone=%s&password=%s&remember=1" %(username, password)
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
        }
        self.user.post(self.login_url, data=payload, headers=headers)

    def get_ip(self):
        '''获取每日免费 ip'''
        res = self.user.post(self.get_ip_url)
        print(res.text)
        

class SpiderGoogle(object):
    """
    异步类
    """
    pyppeteer.DEBUG = True
    page = None
    item_list = list()
    proxy = None

    def __init__(self, proxy):
        self.proxy = proxy

    async def _init(self):
        """
        初始化浏览器,获取代理ip
        :return:
        """
        browser = await pyppeteer.launch(
            {
                'headless': False,  # 浏览器是否启用无头模式
                'args': ['--disable-extensions',
                         '--hide-scrollbars',
                         '--disable-bundled-ppapi-flash',
                         '--mute-audio',
                         '--no-sandbox',
                         '--disable-setuid-sandbox',
                         '--disable-gpu',
                         '--disable-infobars',
                         '--proxy-server={}'.format(self.proxy)],
                'dumpio': True,   # 不添加会卡顿,
                'autoClose': True # 在自动关闭浏览器的时候删除tmp文件
            }
        )
        # 在浏览器创建新页面
        self.page = await browser.newPage()
        # 设置浏览器头部
        await self.page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ')
        # 设置浏览器大小(如果设置了无头浏览器就把这里屏蔽掉)
        await self.page.setViewport({'width': 1000, 'height': 1000})

    async def _insert_js(self):
        """
        注入js
        :return:
        """
        await self.page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 本页刷新后值不变

    async def main(self):
        await self._init()
        await self._insert_js()
        i = 0
        while i < 4:    # 一个标签页循环4次，计20个pv
            await self.page.goto('https://macaoideas.ipim.gov.mo/home', timeout=0) # 3.1MB
            time.sleep(30)
            await self.page.goto('https://macaoideas.ipim.gov.mo/category', timeout=0) # 1.8MB
            time.sleep(30)
            await self.page.goto('https://macaoideas.ipim.gov.mo/product/%d' % random.randint(1400, 1453), timeout=0) # 1.6MB
            time.sleep(30)
            await self.page.goto('https://macaoideas.ipim.gov.mo/company/view/%d' % random.randint(1, 34), timeout=0) # 1.5MB
            time.sleep(30)
            await self.page.goto('https://macaoideas.ipim.gov.mo/news', timeout=0) # 2.1MB
            time.sleep(15)
            i += 1
        await self.page.close()


def run():
    zhima = ZhimaGetIp()
    zhima.union_get_free_ip()
    i = 0
    while i <= 20:   # （芝麻）官网说每日最多可使用20个免费ip，不过我前几天试过可以领21个
        start = time.time()
        resp = requests.get(ip_url)    # 响应格式是 text
        if 'success' not in resp.text:
            print(resp.text)
            while True:
                google = SpiderGoogle(resp.text)
                loop = asyncio.get_event_loop()
                task = asyncio.ensure_future(google.main())
                try:
                    loop.run_until_complete(task)
                except:
                    print("此ip请求异常，10秒后重跑......")
                    time.sleep(10)
                finally:
                    if time.time()-start >= 1500.0:        # 免费ip最多可使用25分钟
                        print("此ip已失效！5秒后自动切换新ip......")
                        break
        else:
            print(resp.text)
            break
        time.sleep(5)
        i += 1
    print("每日免费ip已用完......")


if __name__ == '__main__':

    start = time.time()
    run()
    print('总耗时：', time.time()-start)
```