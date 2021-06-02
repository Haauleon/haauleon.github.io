---
layout:        post
title:         "Python3 | 芝麻城市代理刷网页"
subtitle:      "xlrd + pyppeteer 实现读取 excel 刷网页"
date:          2021-06-02
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - 爬虫
---

## 背景
&emsp;&emsp;接到个异地代理访问图片的需求，前几天常州市无法访问阿里云 oss 绑定的图片，然后我上网搜了一下全国城市路线最多的代理服务商，找到了芝麻。提供的城市路线相对较多，我这里用得是通过 api 获取 ip 来实现代理浏览器访问图片，抄了一下大神的代码，然后增加了读取 excel 和截图的功能。现在放一下 demo，也是刚新鲜出炉的代码，后面有时间再做异常处理。                             

<br><br>

## 代码
获取芝麻的城市代码接口：http://wapi.http.linkudp.com/index/api/get_city_code?key=&export_type=1                 


```python
# -*- coding: utf-8 -*-#
# Description: 
# Author:       haauleon
# Date:         2020/6/2
import time

import asyncio
import pyppeteer
import requests
import xlrd


ip_url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=%s&city=%s&yys=0&port=1&pack=153378&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='


class ZhimaCity:
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
                'headless': True,  # 浏览器是否启用无头模式
                'args': ['--disable-extensions',
                         '--hide-scrollbars',
                         '--disable-bundled-ppapi-flash',
                         '--mute-audio',
                         '--no-sandbox',
                         '--disable-setuid-sandbox',
                         '--disable-gpu',
                         '--disable-infobars',
                         '--window-size=1366,850',
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
        await self.page.setViewport({'width': 1366, 'height': 768})
    
    async def main(self, url, pic_name):
        await self._init()
        await self.page.goto(url, timeout=0)
        # await asyncio.sleep(6)
        await self.page.screenshot(path='zhima\city_pic\%s.png' %(pic_name))
        
    async def close_page(self):
        await self.page.close()


def run():
    workBook = xlrd.open_workbook('zhima\城市代码_芝麻.xlsx')
    sheet1_content1 = workBook.sheet_by_index(0)  # 第一个 sheet

    for i in range(1, sheet1_content1.nrows):
        rows = sheet1_content1.row_values(i) # 返回值是一行的数据，数据类型是列表
        pro = str(int(rows[1]))
        city = str(int(rows[3]))
        city_name = rows[2]
        resp = requests.get(ip_url %(pro, city))
        # resp = requests.get(ip_url %('130000', '130200'))
        print(resp.text[:resp.text.index(":")])  # 截取 ：之前的字符串，即 ip
        if resp.status_code == 200:
            zhima = ZhimaCity(resp.text)
            loop = asyncio.get_event_loop()
            tasks = [] # 任务列表，放置多个任务对象
            for url in urls:
                print(city_name)
                task = asyncio.ensure_future(zhima.main(url, city_name))
                tasks.append(task)
            # 将多个任务对象对应的列表注册到事件循环中
            loop.run_until_complete(asyncio.wait(tasks))

urls = [
    'https://www.cnblogs.com',
]


if __name__ == '__main__':

    start = time.time()
    run()
    print('总耗时：', time.time()-start)
```