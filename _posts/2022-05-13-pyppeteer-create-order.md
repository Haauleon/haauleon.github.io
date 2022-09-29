---
layout:        post
title:         "爬虫 | 使用 pyppeteer 异步框架实现"
subtitle:      "跨境说出海易前台刷单 + 后台订单状态"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 爬虫
    - Python
---

### 项目背景
&emsp;&emsp;最近接到了刷单的需求，主要是为了数量和流量。这次用到了 pyppeteer 异步框架来实现，上一个版本用到了 selenium 来实现。两者相比，selenium 在隐式刷单条件下会出现元素无法定位的问题，切到有界面的模式去执行时，由于我设置了 jenkins 定时任务在本地跑脚本，导致每隔一个小时电脑桌面就会自动弹出一个浏览器窗口来执行，很影响工作。所以我这里换了 pyppeteer 来实现，这是一个异步框架，用到了协程，了解了一丢丢就上手了。不过，我的代码写的还算清晰，应该很简单易懂。     
&emsp;&emsp;为了模拟定时刷单的时候，在后台的数据显示是有起伏的效果，我这里写多了一个商品详情列表的随机切片分类，可以解决这个问题。其实也算是镀金了，不过为了好看也值得。     

<br><br>

### 代码设计
```python
# -*- coding:utf-8 -*-
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   pyppeteer_create_order.py
@Date    :   2022-05-12 14:56:00
@Function:
1. 去出海易前台 http://u.shop.bringbuys.com/ 找到商品并进行下单
2. 去出海易后台 http://u.shop.bringbuys.com/manage 处理订单的状态为已收款
3.注意:
- 此脚本使用 pyppeteer 异步框架实现
- 此脚本在 macOs 系统下使用 python 控制台运行成功, win 系统未调试过
"""
import asyncio  # 协程
from pyppeteer import launch
from pyppeteer_stealth import stealth
import random

# 信宜出海易后台
BOSS_URL = 'http://u.shop.bringbuys.com/manage'
USERNAME = 'xxx'
PASSWORD = 'xxx'


class ProductHandler:
    """商品数据"""

    def __init__(self):
        self.products = products

    def get_randint(self):
        """获取列表随机长度
        @return: 列表随机长度值
        """
        return random.randint(8, len(self.products))

    def get_random_seq(self):
        """获取列表随机切片
        @return: 随机列表切片
        """
        return random.sample(self.products, self.get_randint())

    def get_product_url(self):
        """获取商品详情url"""
        new_products = self.get_random_seq()
        for product in new_products:
            yield product


class XinYi:
    """信宜项目"""

    def __init__(self):
        self.width, self.height = 1366, 768

    async def _init(self):
        """初始化浏览器"""
        self.browser = await launch(
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
                         ],
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
        await asyncio.sleep(10)

    async def ele_click(self, selector):
        """点击操作"""
        await self.page.waitForSelector(selector, {'timeout': 20000})
        await self.page.click(selector)
        await asyncio.sleep(5)

    async def run_to_create_order(self, product_url):
        """出海易前台执行刷单"""
        await self.goto_page(product_url)
        # 进入下单页面
        await self.ele_click('#buynow_button')
        # 邮箱
        await self.page.type('#lib_cart > div.checkout_content > div.information_box.information_customer > '
                             'div.box_content > label > input', 'haauleon@bringbuys.com')
        # First Name
        await self.page.type('#ShipAddrFrom > div > form > div > div:nth-child(1) > div > div:nth-child(1) > label > '
                             'input', 'Haauleon')
        # Last Name
        await self.page.type('#ShipAddrFrom > div > form > div > div:nth-child(1) > div > div:nth-child(2) > label > '
                             'input', 'Haauleon')
        # 地址
        await self.page.type('#ShipAddrFrom > div > form > div > div:nth-child(2) > div > label > input',
                             '广东省珠海市香洲区')
        # 地区
        await self.page.type('#ShipAddrFrom > div > form > div > div:nth-child(4) > div > div:nth-child(1) > label > '
                             'input', '珠海')
        # 邮编
        await self.page.type('#ShipAddrFrom > div > form > div > div:nth-child(4) > div > div:nth-child(2) > label > '
                             'input', '412000')
        # 城市下拉框
        await self.ele_click('#zoneId > div')
        # 选择城市
        await self.ele_click('#zoneId > div > div > ul > li:nth-child(7)')
        # 电话
        await self.page.type('#ShipAddrFrom > div > form > div > div:nth-child(8) > div > div > label > input',
                             '13976062467')
        # 保存地址
        await self.ele_click('#save_address')
        # 支付方式
        await self.ele_click('#lib_cart > div.checkout_content > div.information_box.information_payment > '
                             'div.box_content > div.payment_list.clearfix > div:nth-child(2)')
        # 提交订单
        await self.ele_click('#orderFormSubmit')
        try:
            # 确认信息
            await self.ele_click('body > div.new_win_alert > div.win_btns > button')
            await self.ele_click('#orderFormSubmit')
        except:
            pass
        await asyncio.sleep(5)

    async def run_to_handle_order(self, boss_url, username, password):
        """出海易后台订单处理"""
        await self.goto_page(boss_url)
        # 输入账号
        await self.page.type('#UserName', username)
        # 输入密码
        await self.page.type('#Password', password)
        # 进入后台主页
        await self.ele_click('#login > div.rbar > form > div > input')
        # 进入订单管理
        await self.ele_click('#main > div.menu > div.menu_ico.home_menu_ico > div:nth-child(1) > a')
        # 进入待付款列表
        await self.ele_click('#orders > div.inside_container > ul > li:nth-child(2) > a')
        # 进入订单详情
        await self.ele_click('#orders > div.inside_table > table > tbody > tr:nth-child(1) > td:nth-child(2) > a')
        # 更新订单状态
        await self.ele_click('#orders_inside > div > div.left_container > div > div.global_container.box_order_info > '
                             'div.orders_parent_box.orders_parent_top_box.mb20 > div > div:nth-child(2) > '
                             'div.global_container.orders_status.ml5 > div.box_button.clean > '
                             'input.btn_global.btn_orders_status.btn_next')

    async def main(self, product_url, boss_url, username, password):
        """主函数"""
        await self._init()
        await self._insert_js()
        await self.run_to_create_order(product_url)
        await self.run_to_handle_order(boss_url, username, password)
        await self.page.close()      # 关闭标签页
        await self.browser.close()   # 关闭浏览器


products = [
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


if __name__ == '__main__':
    ph = ProductHandler()
    p = ph.get_product_url()
    while True:
        try:
            p_url = next(p)
            xy = XinYi()
            loop = asyncio.get_event_loop()  # 创建一个事件循环对象loop
            task = asyncio.ensure_future(    # 执行异步
                xy.main(p_url, BOSS_URL, USERNAME, PASSWORD)
            )
            loop.run_until_complete(task)    # 完成事件循环，直到最后一个任务结束
        except StopIteration:
            break
```