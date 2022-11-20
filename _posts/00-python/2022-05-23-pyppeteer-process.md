---
layout:        post
title:         "爬虫 | 网站增加谷歌分析指标"
subtitle:      "谷歌分析指标如 pv、uv、跳出率，增加 local 和芝麻代理池两种方式"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 代码设计
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   pyppeteer_process_v3.py
@Date    :   2021-08-12 12:22
@Function:   商汇馆网站增加谷歌分析指标, 如 pv、uv、跳出率

更新于 2022-05-23 15:59
1、增加网站跳出率(单页访问: 访问者在访问网站时，只浏览了一个页面就离开)
2、增加本地local方式
3、增加芝麻代理池方式
"""

import sys
from pyppeteer import launch
from pyppeteer_stealth import stealth
import random
import time
import logging
import asyncio
# from typing_extensions import Final
import pyppeteer
import requests
from colorama import Fore, Style

_logger = logging.getLogger('ipim')  # 获取日志记录器
_logger.setLevel(logging.DEBUG)  # 设置日志等级
_handler = logging.StreamHandler(sys.stdout)  # 输入到控制台的 handler
_logger.addHandler(_handler)

# 获取芝麻代理ip
getip_base = "http://webapi.http.zhimacangku.com/getip?num=1&type=1&pro=0&city=0&yys=0&port=1&pack=%s&ts=0&ys=0&cs=0" \
             "&lb=1&sb=0&pb=4&mr=1&regions=350000,420000,430000,440000 "

# 芝麻账号配置 (账号、密码、套餐pack->从官网获取)
user_data = [("xxx", "xxx", "218550",),
             ("xxx", "xxx", "171569",), ]


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
        self.coupon_snapped()
        self.active_num()
        self.get_coupon_pic()
        self.start_captcha_servlet()
        self.bidding_domain_url()
        self.get_regnum_ip()
        self.user_info()
        self.agio_info()
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

    def coupon_snapped(self):
        self.user.post(self.zhima_base + '/coupon/snapped_up')

    def active_num(self):
        self.user.post(self.zhima_base + '/index/activenum')

    def get_coupon_pic(self):
        self.user.post(self.zhima_base + '/coupon/get_coupon_pic')

    def start_captcha_servlet(self):
        current_milli_time = lambda: int(round(time.time() * 1000))
        self.user.post(self.zhima_base + '/users/start_captcha_servlet?t=%s' % current_milli_time)

    def bidding_domain_url(self):
        self.user.post(self.zhima_base + '/index/bidding_domain_url')

    def get_regnum_ip(self):
        self.user.post(self.zhima_base + '/users/get_regnum_ip')

    def user_info(self):
        self.user.post(self.zhima_base + '/users/user_info')

    def agio_info(self):
        self.user.post(self.zhima_base + '/index/agio_info')

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
        _print(res.text)
        if r['data']['package_balance']:
            return True
        else:
            return False

    def get_pack_use_history_list(self):
        """当日使用IP量
        @return: 当日使用IP量是否大于20，每日限20个免费
        """
        res = self.user.post(self.zhima_base + '/users/get_pack_use_history_list')
        r = res.json()
        if r['ret_data']['lastUseNum'] <= 20:
            return True
        else:
            return False


class IPIM:
    """商汇馆刷数据
    网站首页: https://macaoideas.ipim.gov.mo/home
    """

    def __init__(self, proxy=''):
        self.width, self.height = 1366, 768
        self.proxy = proxy

    async def _init(self):
        """初始化浏览器"""
        self.browser = await launch(
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
                'dumpio': True,    # 不添加会卡顿,
                'autoClose': True  # 在自动关闭浏览器的时候删除tmp文件
            }
        )
        # 在浏览器创建新标签页
        self.page = await self.browser.newPage()
        # 消除指纹
        await stealth(self.page)
        # 设置浏览器头部
        await self.page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ')
        # 设置窗口大小(如果设置了无头模式就屏蔽掉这里)
        await self.page.setViewport({'width': self.width, 'height': self.height})

    async def _insert_js(self):
        """注入js"""
        # 本页刷新后值不变
        await self.page.evaluate(
            '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')

    async def goto_page(self, page_url):
        """前往目标网页"""
        await self.page.goto(page_url, timeout=0)
        # 等待页面完全加载
        await asyncio.sleep(15)

    async def ele_click(self, selector):
        """点击操作"""
        await self.page.waitForSelector(selector, {'timeout': 20000})
        await self.page.click(selector)
        await asyncio.sleep(5)

    async def increase_single_pageviews(self):
        """单页访问增加网站跳出率100%
        单页访问: 访问者在访问网站时只浏览了一个页面就离开了
        """
        await self._init()
        await self._insert_js()
        await self.goto_page('https://macaoideas.ipim.gov.mo/home')
        await self.page.close()      # 关闭标签页
        await self.browser.close()   # 关闭浏览器

    async def increase_more_pageviews(self):
        """多页访问增加页面浏览量, 跳出率0%"""
        await self._init()
        await self._insert_js()
        await self.goto_page('https://macaoideas.ipim.gov.mo/home') # 3.1MB
        await self.goto_page('https://macaoideas.ipim.gov.mo/category') # 1.8MB
        await self.goto_page('https://macaoideas.ipim.gov.mo/product/%d' % random.randint(1400, 1453)) # 1.6MB
        await self.goto_page('https://macaoideas.ipim.gov.mo/company/view/%d' % random.randint(1, 34)) # 1.5MB
        await self.goto_page('https://macaoideas.ipim.gov.mo/news') # 2.1MB
        await self.page.close()      # 关闭标签页
        await self.browser.close()   # 关闭浏览器

    async def main(self):
        """主函数"""
        await self.increase_more_pageviews()
        

class Run:
    
    @staticmethod
    def exec_proxy_pool():
        """方式一: 芝麻代理池执行"""
        for user in user_data:
            username, password, pack_id = user
            zhima = ZhimaGetIp()
            zhima.union_get_free_ip(username, password)
            while zhima.get_pack_use_history_list() or zhima.get_package_balance(pack_id):
                resp = requests.get(getip_base % pack_id)  # 获取芝麻代理ip, 响应格式是 text
                if 'success' not in resp.text:
                    _print("获取ip成功 >>> %s" % resp.text)
                    start_time = time.time()
                    while True:
                        ipim = IPIM(resp.text)
                        loop = asyncio.get_event_loop()    # 创建一个事件循环对象loop
                        task = asyncio.ensure_future(ipim.main())
                        try:
                            _print("开始刷流量......")
                            loop.run_until_complete(task)  # 完成事件循环，直到最后一个任务结束
                        except:
                            error("此ip请求异常, 5秒后重跑......")
                            time.sleep(5)
                        finally:
                            if time.time()-start_time >= 1200.0:        # 免费ip最多可使用25分钟即1500.0
                                error("此ip已失效! 5秒后自动切换新ip......")
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
                        error("其他异常, 登录芝麻官网 https://zhimahttp.com/ 进行检查")
                        break
                time.sleep(5)

            _print("套餐余量已用完, 10 秒后切换用户")
            time.sleep(10)
        _print("全部用户的免费代理 ip 已用完")

    @staticmethod
    def exec_local():
        """方式二: 本地执行"""
        _print("开始刷流量......")
        for _ in range(30):
            '''增加1200个pv
            开10个zsh终端同时执行30分钟
            '''
            ipim = IPIM()
            loop = asyncio.get_event_loop()  # 创建一个事件循环对象loop
            task = asyncio.ensure_future(ipim.increase_more_pageviews())
            loop.run_until_complete(task)  # 完成事件循环，直到最后一个任务结束
        _print("任务执行完成")


if __name__ == '__main__':
    start = time.time()
    # Run.exec_proxy_pool()
    Run.exec_local()
    print('总耗时：', time.time() - start)
```