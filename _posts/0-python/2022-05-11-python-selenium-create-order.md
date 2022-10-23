---
layout:        post
title:         "爬虫 | 使用 selenium 框架实现"
subtitle:      "跨境说出海易前台刷单 + 后台订单状态"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
---

### 项目背景
&emsp;&emsp;用到了 selenium 框架来实现，也是我的老朋友了，但这个脚本无法在无头模式下运行，因为运行时会提示元素无法定位。但在某些网站又可以开启隐式刷单，原理我现在还不明白。总而言之，这个脚本只能在有界面的条件下运行。

<br><br>

### 代码设计
```python
# -*- coding:utf-8 -*-
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   selenium_create_order.py
@Date    :   2022-05-07 14:56:00
@Function:
1. 去出海易前台 http://u.shop.bringbuys.com/ 找到商品并进行下单
2. 去出海易后台 http://u.shop.bringbuys.com/manage 处理订单的状态为已收款
3.注意:
- 此脚本在 selenium 的无头模式运行会报错
- Linux 系统下运行需要安装 chrome 浏览器
- 此脚本在 macOs 系统下使用 python 控制台运行成功, win 系统未调试过
"""

import requests
import time
import json
import logging
import sys
from colorama import Fore, Style
import sys
import random
from functools import wraps
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import pprint

print = pprint.pprint

# from selenium.webdriver import Remote

# 改变标准输出的默认编码，cmd对utf-8不是很好支持会导致中文乱码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


# 日志配置
_logger = logging.getLogger('xinyi')             # 获取日志记录器
_logger.setLevel(logging.DEBUG)                  # 设置日志等级
_handler = logging.StreamHandler(sys.stdout)     # 输入到控制台的 handler
_logger.addHandler(_handler)                     # 日志记录器增加 handler


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


class RestClient:
    """请求方法封装"""

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


class XinYiSelenium:
    """webdriver 隐式刷单"""

    def __init__(self):
        """Ubuntu 系统下使用 selenium webdriver 脚本执行步骤:
        1. 检查是否成功安装 chrome 浏览器
        $ google-chrome --version

        2.未安装则执行如下命令安装最新版本的 Google Chrome
        $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        $ apt --fix-broken install (某种修复)
        $ sudo dpkg -i --force-depends google-chrome-stable_current_amd64.deb
        """
        # 消除 Chrome正受到自动测试软件的控制 提示
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # 设置无头浏览器隐式访问
        # self.chrome_options.add_argument('--headless')
        # "–no - sandbox" 参数是让 Chrome 在 root 权限下跑
        self.chrome_options.add_argument('--no-sandbox')
        self.driver = None

    def driver_start(self):
        """启动浏览器驱动
        若系统未安装 chromedriver 则进行自动安装, 无需手动判断浏览器版本进行安装
        """
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
        self.driver.maximize_window()

    def driver_quit(self):
        """关闭浏览器驱动"""
        self.driver.quit()

    def driver_get_url(self, url):
        """访问 url 链接"""
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        time.sleep(2)

    def driver_xpath(self, xpath):
        """定位 xpath 元素"""
        return self.driver.find_element_by_xpath(xpath)

    def ele_click(self, xpath):
        """点击操作"""
        self.driver_xpath(xpath).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    def ele_input(self, xpath, text):
        """输入操作"""
        self.driver_xpath(xpath).send_keys(text)
        self.driver.implicitly_wait(10)

    def driver_iframe(self, xpath):
        """切换至 iframe"""
        iframe_obj = self.driver_xpath(xpath)
        self.driver.switch_to.frame(iframe_obj)
        self.driver.implicitly_wait(10)

    def get_randint(self, seq: list):
        """获取随机长度"""
        return random.randint(8, len(seq))

    def get_random_seq(self, seq: list):
        """获取随机切片"""
        return random.sample(seq, self.get_randint(seq))

    def run_to_create_order(self, url):
        """出海易前台执行刷单"""
        self.driver_start()
        self.driver_get_url(url)
        self.ele_click('//*[@id="buynow_button"]')
        self.ele_input('//*[@id="lib_cart"]/div[2]/div[2]/div[2]/label/input', "haauleon@bringbuys.com")
        self.ele_input('//*[@id="ShipAddrFrom"]/div/form/div/div[1]/div/div[1]/label/input', 'Haauleon')
        self.ele_input('//*[@id="ShipAddrFrom"]/div/form/div/div[1]/div/div[2]/label/input', 'Haauleon')
        self.ele_input('//*[@id="ShipAddrFrom"]/div/form/div/div[2]/div/label/input', '珠海')
        self.ele_input('//*[@id="ShipAddrFrom"]/div/form/div/div[4]/div/div[1]/label/input', '珠海')
        self.ele_input('//*[@id="ShipAddrFrom"]/div/form/div/div[4]/div/div[2]/label/input', '412000')
        self.ele_click('//*[@id="zoneId"]/div')
        self.ele_click('//*[@id="zoneId"]/div/div/ul/li[5]')
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "Province")))
        # select = driver.find_element_by_name('Province')
        # Select(select).select_by_index(1)
        # driver.implicitly_wait(10)
        self.ele_input('//*[@id="ShipAddrFrom"]/div/form/div/div[8]/div/div/label/input', '13976062467')
        self.ele_click('//*[@id="save_address"]')
        self.ele_click('//*[@id="lib_cart"]/div[2]/div[5]/div[2]/div[1]/div[2]/div[1]/input')
        self.ele_click('//*[@id="orderFormSubmit"]')
        try:
            self.ele_click('/html/body/div[1]/div[3]/button')
            self.ele_click('//*[@id="orderFormSubmit"]')
        except:
            error('元素未找到, 继续执行')
        finally:
            self.driver_quit()

    def run_to_handle_order(self, url, username, password, num):
        """出海易后台执行"""
        self.driver_start()
        self.driver_get_url(url)
        self.ele_input('//*[@id="UserName"]', username)
        self.ele_input('//*[@id="Password"]', password)
        self.ele_click('//*[@id="login"]/div[2]/form/div/input')
        self.ele_click('//*[@id="main"]/div[2]/div[1]/div[1]/a')
        self.ele_click('//*[@id="orders"]/div[1]/ul/li[2]/a')
        for _ in range(num):
            self.ele_click('//*[@id="orders"]/div[2]/table/tbody/tr[1]/td[2]/a')
            self.ele_click('//*[@id="orders_inside"]/div/div[1]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/input[1]')
            self.ele_click('//*[@id="orders_inside"]/div/a')
        self.driver_quit()


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


if __name__ == "__main__":
    _print("脚本开始执行")
    xy = XinYiSelenium()
    new_products = xy.get_random_seq(products)
    # print(new_products)
    for product in new_products:
        xy.run_to_create_order(product)
    xy.run_to_handle_order('http://u.shop.bringbuys.com/manage', 'xxx', 'xxx', len(new_products))
    _print("脚本执行完成")

```