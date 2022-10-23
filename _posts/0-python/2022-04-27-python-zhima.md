---
layout:        post
title:         "Python3 | 本地ip刷网页浏览量脚本"
subtitle:      ""
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
---

### 背景
&emsp;&emsp;上一个版本使用的是芝麻免费 ip 代理池，但是普通用户一天只能领取 20 个免费 ip，而且每个 ip 都是有使用时限的，限制了 25 分钟，导致浏览量脚本重重阻碍。现在加了一个使用本地 ip 去驱动 chrome 浏览器，然后进行刷网页浏览量的功能，已调试成功。    
&emsp;&emsp;使用方法就是：打开 vscode 编辑器，然后开启多个 bash/cmd/ubuntu 等可以执行脚本的终端，我是开了 10 个终端，然后执行同一个文件，可以做到一个小时增加 2000 以上个 pv，已成功。

<br><br>

### 代码实现
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   pyppeteer_process_v4.py
@Date    :   2022-04-25 12:22
@Function:   芝麻代理池的多用户自动登录并领取ip刷数据
"""

from os import stat
import re
import sys
import random
import time
import logging
import asyncio
# from typing_extensions import Final
import pyppeteer
import requests
from colorama import Fore, Style

_logger = logging.getLogger('zhima')        # 获取日志记录器
_logger.setLevel(logging.DEBUG)                 # 设置日志等级
_handler = logging.StreamHandler(sys.stdout)    # 输入到控制台的 handler
_logger.addHandler(_handler)    

# 获取芝麻代理ip
getip_base = "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=0&city=0&yys=0&port=1&pack=%s&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=350000,420000,430000,440000"

user_data = [
    (
        "芝麻账号",
        "芝麻密码",
        getip_base %"171569",
    ),
]

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


class ZhimaGetIp:
    """
    获取20个每日免费 ip
    """
    def __init__(self):
        self.user = requests.Session()
        self.login_url = "https://wapi.http.linkudp.com/index/users/login_do"
        self.get_ip_url = "https://wapi.http.linkudp.com/index/users/get_day_free_pack"
        self.add_wirteip_url = "https://wapi.http.linkudp.com/index/users/save_wirteip"

    def union_get_free_ip(self, username, password):
        self.zhima_login(username, password)
        self.get_ip()
    
    def zhima_login(self, username, password):
        '''用户登录'''
        payload = "phone=%s&password=%s&remember=1" %(username, password)
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
        }
        res = self.user.post(self.login_url, data=payload, headers=headers)
        r = res.json()
        if r["msg"] == "登录成功":
            info("用户 %s 登录成功" %username)
        else:
            error("用户 %s 登录失败 >>> %s" %(username,r["msg"]))

    def get_ip(self):
        '''获取每日免费 ip'''
        res = self.user.post(self.get_ip_url)
        r = res.json()
        if r["msg"] == "今日已经领取过免费ip" or r["msg"] == "领取成功":
            info("每日领取20个免费ip成功")
        else:
            error("每日领取20个免费ip失败 >>> %s" %r["msg"])

    def add_wirteip(self, ip):
        '''添加 ip 白名单'''
        payload = "ip=%s" %ip
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
        }
        res = self.user.post(self.add_wirteip_url, data=payload, headers=headers)
        r = res.json()
        if r["msg"] == "保存成功" or r["msg"] == "该ip已经在您的白名单中！":
            info("%s 添加白名单成功" %ip)
        else:
            error("%s 添加白名单失败 >>> %s" %(ip,r["msg"]))


"""        
async def main(proxy):

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
                        '--proxy-server={}'.format(proxy)],
            'dumpio': True,   # 不添加会卡顿,
            'autoClose': True # 在自动关闭浏览器的时候删除tmp文件
        }
    )
    # 在浏览器创建新页面
    page = await browser.newPage()
    # 设置浏览器头部
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ')
    # 设置浏览器大小(如果设置了无头浏览器就把这里屏蔽掉)
    await page.setViewport({'width': 1000, 'height': 1000})
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 注入js，本页刷新后值不变

    i = 0
    while i < 1:            # 一个标签页循环4次，计20个pv
        await page.goto('https://macaoideas.ipim.gov.mo/home', timeout=0) # 3.1MB
        # 只能使用同步语句，若使用asyncio.sleep(3)则导致其他未处于当前标签页的页面浏览量无法增加，谷歌统计无法增加pv值
        time.sleep(15)
        await page.goto('https://macaoideas.ipim.gov.mo/category', timeout=0) # 1.8MB
        time.sleep(15)
        await page.goto('https://macaoideas.ipim.gov.mo/product/%d' % random.randint(1400, 1453), timeout=0) # 1.6MB
        time.sleep(15)
        await page.goto('https://macaoideas.ipim.gov.mo/company/view/%d' % random.randint(1, 34), timeout=0) # 1.5MB
        time.sleep(15)
        await page.goto('https://macaoideas.ipim.gov.mo/news', timeout=0) # 2.1MB
        time.sleep(15)
        i += 1
    await page.close()
    await browser.close()
    
    
def run():
    '''代理执行'''
    for user in user_data:
        username, password, ip_url = user
        zhima = ZhimaGetIp()
        zhima.union_get_free_ip(username, password)
        i = 0
        while i <= 20:   # （芝麻）官网说每日最多可使用20个免费ip，不过我前几天试过可以领21个
            start = time.time()
            resp = requests.get(ip_url)    # 响应格式是 text
            if 'success' not in resp.text:
                _print("获取ip成功 >>> %s" %resp.text)
                while True:
                    loop = asyncio.get_event_loop()           # 创建一个事件循环对象loop
                    task = asyncio.ensure_future(main(resp.text))
                    try:
                        _print("开始刷流量......")
                        loop.run_until_complete(task)         # 完成事件循环，直到最后一个任务结束
                    except:
                        error("此ip请求异常，5秒后重跑......")
                        time.sleep(5)
                    finally:
                        if time.time()-start >= 1200.0:        # 免费ip最多可使用25分钟即1500.0
                            error("此ip已失效！5秒后自动切换新ip......")
                            break

            else:
                error("获取ip失败 >>> %s" %resp.text)
                if "请添加白名单" in resp.json()["msg"]:
                    ip = resp.json()["msg"][6:]
                    zhima.add_wirteip(ip)
                elif "是否已添加白名单" in resp.json()["msg"]:
                    ip = resp.json()["msg"][20:]
                    zhima.add_wirteip(ip)
                else:
                    error("登录芝麻官网 https://zhimahttp.com/ 检查")
                    break
            time.sleep(5)
            i += 1

        _print("10 秒后切换用户")
        time.sleep(10)
    _print("全部用户的免费代理 ip 已用完")
"""


async def main():

    browser = await pyppeteer.launch(
        {
            'headless': True,  # 浏览器是否启用无头模式
            'args': [
                        '--disable-extensions',
                        '--hide-scrollbars',
                        '--disable-bundled-ppapi-flash',
                        '--mute-audio',
                        '--no-sandbox',
                        '--disable-setuid-sandbox',
                        '--disable-gpu',
                        '--disable-infobars',
                     ],
            'dumpio': True,   # 不添加会卡顿,
            'autoClose': True # 在自动关闭浏览器的时候删除tmp文件
        }
    )
    # 在浏览器创建新页面
    page = await browser.newPage()
    # 设置浏览器头部
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ')
    # 设置浏览器大小(如果设置了无头浏览器就把这里屏蔽掉)
    await page.setViewport({'width': 1000, 'height': 1000})
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 注入js，本页刷新后值不变

    i = 0
    while i < 1:            # 一个标签页循环4次，计20个pv
        await page.goto('https://macaoideas.ipim.gov.mo/home', timeout=0) # 3.1MB
        # 只能使用同步语句，若使用asyncio.sleep(3)则导致其他未处于当前标签页的页面浏览量无法增加，谷歌统计无法增加pv值
        time.sleep(15)
        await page.goto('https://macaoideas.ipim.gov.mo/category', timeout=0) # 1.8MB
        time.sleep(15)
        await page.goto('https://macaoideas.ipim.gov.mo/product/%d' % random.randint(1400, 1453), timeout=0) # 1.6MB
        time.sleep(15)
        await page.goto('https://macaoideas.ipim.gov.mo/company/view/%d' % random.randint(1, 34), timeout=0) # 1.5MB
        time.sleep(15)
        await page.goto('https://macaoideas.ipim.gov.mo/news', timeout=0) # 2.1MB
        time.sleep(15)
        i += 1
    await page.close()
    await browser.close()


def run():
    """本地执行"""
    _print("开始刷流量......")
    for _ in range(430):
        '''增加2150个pv'''
        loop = asyncio.get_event_loop()  # 创建一个事件循环对象loop
        task = asyncio.ensure_future(main())
        loop.run_until_complete(task)  # 完成事件循环，直到最后一个任务结束
    _print("任务执行完成")


if __name__ == '__main__':

    start = time.time()
    run()
    print('总耗时：', time.time()-start)

```