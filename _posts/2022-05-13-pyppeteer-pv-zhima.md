---
layout:        post
title:         "爬虫 | pyppeteer 框架实现刷浏览量 pv"
subtitle:      "增加芝麻代理池的多用户自动登录并领取 ip 刷数据"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 爬虫
    - Python
---

### 项目背景
项目实现：  
1. 多用户切换领取芝麻代理池每日免费 ip (大概 20 个)     
2. 信宜出海易前台使用 pyppeteer 异步框架实现刷网页浏览量

<br><br>

### 代码设计
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   pyppeteer_process.py
@Date    :   2022-05-12 9:22
@Function:   芝麻代理池的多用户自动登录并领取ip刷数据
1、芝麻免费代理池的使用
2、信宜出海易前台刷网页浏览量
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
import pprint

print = pprint.pprint

_logger = logging.getLogger('xinyi')  # 获取日志记录器
_logger.setLevel(logging.DEBUG)  # 设置日志等级
_handler = logging.StreamHandler(sys.stdout)  # 输入到控制台的 handler
_logger.addHandler(_handler)

# 获取芝麻代理ip
getip_base = "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=0&city=0&yys=0&port=1&pack=%s&ts=0&ys=0&cs=0" \
             "&lb=1&sb=0&pb=4&mr=1&regions=350000,420000,430000,440000 "

# 芝麻账号配置 (账号、密码、套餐pack->从官网获取)
user_data = [
    (
        "xxx",
        "xxx",
        "218550",
    ),
    (
        "xxx",
        "xxx",
        "171569",
    ),
]


def info(msg):
    """日志函数"""
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
    芝麻代理池获取免费代理 ip
    """

    def __init__(self):
        self.user = requests.Session()
        self.zhima_base = 'https://wapi.http.linkudp.com/index'

    def union_get_free_ip(self, username: str, password: str):
        self.zhima_login(username, password)
        self.get_ip()

    def zhima_login(self, username, password):
        """用户登录
        @param username: 芝麻代理账号
        @param password: 芝麻代理密码
        """
        payload = "phone={username}&password={password}&remember=1".format(username=username, password=password)
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
        }
        login_url = "{base_url}/users/login_do".format(base_url=self.zhima_base)
        res = self.user.post(login_url, data=payload, headers=headers)
        r = res.json()
        if r["msg"] == "登录成功":
            info("{username}登录成功".format(username=username))
        else:
            error("{username}登录失败, 提示: {msg}".format(username=username, msg=r["msg"]))

    def get_ip(self):
        """领取终身免费VIP套餐的每日20个免费 ip"""
        get_ip_url = "{base_url}/users/get_day_free_pack".format(base_url=self.zhima_base)
        res = self.user.post(get_ip_url)
        r = res.json()
        if r["msg"] in ["今日已经领取过免费ip", "领取成功"]:
            info(r["msg"])
        else:
            error("每日领取免费ip失败, 提示: {msg}".format(msg=r["msg"]))

    def add_whiteip(self, ip):
        """添加 ip 白名单
        @param ip: 执行脚本的机器所在的本地ip
        """
        payload = "ip=%s" % ip
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
        }
        add_whiteip_url = "{}/users/save_wirteip".format(self.zhima_base)
        res = self.user.post(add_whiteip_url, data=payload, headers=headers)
        r = res.json()
        if r["msg"] in ["保存成功", "该ip已经在您的白名单中！"]:
            info("{ip}添加白名单成功".format(ip=ip))
        else:
            error("{ip}添加白名单失败, 提示: {msg}".format(ip=ip, msg=r["msg"]))

    def get_package_link(self, pack_id):
        """返回获取芝麻代理套餐余额的链接
        @param pack_id: 芝麻代理的套餐余量
        @return: 获取芝麻代理套餐余额的链接
        """
        get_link_url = '{base_url}/index/get_my_package_link/id/{pack}'.format(base_url=self.zhima_base, pack=pack_id)
        return self.user.get(get_link_url).text

    def get_package_balance(self, pack_id):
        """获取套餐余量
        @param pack_id: 芝麻代理的套餐余量
        @return: 套餐余量是否为0
        """
        res = self.user.get(self.get_package_link(pack_id))
        r = res.json()
        if r['data']['package_balance']:
            return True
        else:
            return False


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
            'dumpio': True,    # 不添加会卡顿,
            'autoClose': True  # 在自动关闭浏览器的时候删除tmp文件
        }
    )
    # 在浏览器创建新页面
    page = await browser.newPage()
    # 设置浏览器头部
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ')
    # 设置浏览器大小(如果设置了无头浏览器就把这里屏蔽掉)
    await page.setViewport({'width': 1000, 'height': 1000})
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 注入js，本页刷新后值不变

    for url in urls:
        await page.goto(url, timeout=0)
        time.sleep(15)
    await page.click()
    await page.close()
    await browser.close()


urls = [
    'http://u.shop.bringbuys.com/chiaogoo-amish-design-wooden-yarn-swift-p0110-p0110.html',
    'http://u.shop.bringbuys.com/woodcessories-ecoguard-wooden-ipad-case-p0105-p0105.html',
    'http://u.shop.bringbuys.com/wooden-reading-rest-adjustable-cookbook-holder-p0102-p0102.html',
    'http://u.shop.bringbuys.com/mitre-box-wooden-230x95mm-1-pack-s-56429-p0106.html',
    'http://u.shop.bringbuys.com/kitchencraft-wooden-pancake-crpe-spreader-p0099-p0099.html',
    'http://u.shop.bringbuys.com/wooden-storage-box-95x105x51cm-203x191x152cm-p0095-p0097.html',
    'http://u.shop.bringbuys.com/traditional-unfinished-wooden-double-toggle-light-switch-cover-p0116-p0116.html',
    'http://u.shop.bringbuys.com/baldr-wooden-alarm-clock-digital-bamboo-wood-red-light-p0103-p0103.html',
    'http://u.shop.bringbuys.com/buitenspeel-wooden-build-your-own-birdhouse-p0104-p0104.html',
    'http://u.shop.bringbuys.com/thunder-group-wdsp014-wooden-spoon-14-inch-p0107-p0107.html',
    'http://u.shop.bringbuys.com/browne-744570-10quot-deluxe-wooden-spoon-p0109-p0109.html'
]
# urls = [
#     'http://u.shop.bringbuys.com/chiaogoo-amish-design-wooden-yarn-swift-p0110-p0110.html',
# ]


def run():
    """代理执行"""
    for user in user_data:
        username, password, pack_id = user
        zhima = ZhimaGetIp()
        zhima.union_get_free_ip(username, password)
        # i = 0
        while zhima.get_package_balance(pack_id):
            # 套餐余量不为0
            # while i <= 20:  # （芝麻）官网说每日最多可使用20个免费ip，不过我前几天试过可以领21个
            # start = time.time()
            resp = requests.get(getip_base % pack_id)  # 获取芝麻代理ip, 响应格式是 text
            if 'success' not in resp.text:
                _print("获取ip成功 >>> %s" % resp.text)
                start = time.time()
                while True:
                    loop = asyncio.get_event_loop()  # 创建一个事件循环对象loop
                    task = asyncio.ensure_future(main(resp.text))
                    try:
                        _print("开始刷流量......")
                        loop.run_until_complete(task)  # 完成事件循环，直到最后一个任务结束
                    except:
                        error("此ip请求异常，5秒后重跑......")
                        time.sleep(5)
                        # error("此ip请求异常!5秒后自动切换新ip......")
                        # break
                    finally:
                        if time.time() - start >= 1.0:  # 免费ip最多可使用25分钟即1500.0
                            error("此ip已失效！5秒后自动切换新ip......")
                            break

            else:
                error("获取ip失败 >>> %s" % resp.text)
                if "请添加白名单" in resp.json()["msg"]:
                    ip = resp.json()["msg"][6:]
                    zhima.add_whiteip(ip)
                elif "是否已添加白名单" in resp.json()["msg"]:
                    ip = resp.json()["msg"][20:]
                    zhima.add_whiteip(ip)
                else:
                    error("登录芝麻官网 https://zhimahttp.com/ 检查")
                    break
            time.sleep(5)
            # i += 1

        _print("套餐余量已用完, 10 秒后切换用户")
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
            'dumpio': True,  # 不添加会卡顿,
            'autoClose': True  # 在自动关闭浏览器的时候删除tmp文件
        }
    )
    # 在浏览器创建新页面
    page = await browser.newPage()
    # 设置浏览器头部
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ')
    # 设置浏览器大小(如果设置了无头浏览器就把这里屏蔽掉)
    await page.setViewport({'width': 1000, 'height': 1000})
    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 注入js，本页刷新后值不变

    for _ in range(1):
        for url in urls:
            await page.goto(url, timeout=0)
            time.sleep(15)
    await page.close()
    await browser.close()


def run():
    '''本地执行'''
    _print("开始刷流量......")
    for _ in range(430):
        '''增加2150个pv'''
        loop = asyncio.get_event_loop()  # 创建一个事件循环对象loop
        task = asyncio.ensure_future(main())
        loop.run_until_complete(task)  # 完成事件循环，直到最后一个任务结束
    _print("任务执行完成")
"""


if __name__ == '__main__':
    start = time.time()
    run()
    print('总耗时： %f 秒' % (time.time() - start))
```