---
layout:        post
title:         "爬虫 | 爬虫执行策略脚本"
subtitle:      "爬取源: http://www.hengqin.gov.cn/macao_zh_hans/hzqgl/dtyw/xwbb/"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
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

"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   run_hengqing_service_v2.py
@Date    :   2022-04-14 15:56:00
@Function:   
1. 同步成功的资讯判断当前日期和横琴官网资讯日期, 如果日期一致则更新资讯状态显示至澳门办事处网站前台
2. 爬取澳门政府防疫最新消息, 增加钉钉消息通知
"""

import requests
import time
import json
import logging
import sys
from colorama import Fore, Style
import sys
from functools import wraps
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver import Remote

# 改变标准输出的默认编码，cmd对utf-8不是很好支持会导致中文乱码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


COOKIE = 'xxxxxx'


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
        self.atMobiles = ['13976062467',] if atMobiles==None else atMobiles
        # self.token = 'cbb3b771657ef' if ding_token==None else ding_token
        # 是否@所有人
        self.isAtAll = True if isAtAll==None else isAtAll
        self.token = 'b2ceb739c43a05da7806406124b568860ef1946a91ca5362435a459d6c67c682'
        self.api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(self.token)
        self.headers = {'Content-Type': 'application/json;charset=utf-8'}

    @traceback_error
    def send_msg(self, content):
        msg = {
            'msgtype': 'text',
            'text': {'content': content},
            'at': {'atMobiles': self.atMobiles, 'isAtAll': self.isAtAll}
        }
        data = requests.post(self.api, data=json.dumps(msg), headers=self.headers).json()
        return json.dumps(data)


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


class SsmGovCovid:
    '''webdriver 隐式爬取澳门政府防疫最新消息'''

    def __init__(self):
        '''Ubuntu 系统下使用 selenium webdriver 脚本执行步骤: 
        1. 检查是否成功安装 chrome 浏览器 
        $ google-chrome --version

        2.未安装则执行如下命令安装最新版本的 Google Chrome 
        $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
        $ apt --fix-broken install (某种修复)
        $ sudo dpkg -i --force-depends google-chrome-stable_current_amd64.deb
        '''
        # 消除 Chrome正受到自动测试软件的控制 提示
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # 设置无头浏览器隐式访问
        self.chrome_options.add_argument('--headless')
        # "–no - sandbox" 参数是让 Chrome 在 root 权限下跑
        self.chrome_options.add_argument('--no-sandbox') 

    def driver_start(self):
        '''启动浏览器驱动
        若系统未安装 chromedriver 则进行自动安装, 无需手动判断浏览器版本进行安装
        '''
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
        self.driver.maximize_window()
        time.sleep(5)

    def driver_quit(self):
        '''关闭浏览器驱动'''
        self.driver.quit()

    def driver_get_url(self, url):
        '''访问 url 链接'''
        self.driver.get(url)
        self.driver.implicitly_wait(200)

    def driver_xpath(self, xpath):
        '''定位 xpath 元素'''
        return self.driver.find_element_by_xpath(xpath)

    def driver_iframe(self, xpath):
        '''切换至 iframe'''
        iframe_obj = self.driver_xpath(xpath)
        self.driver.switch_to.frame(iframe_obj)
        self.driver.implicitly_wait(200)

    def driver_run(self):
        '''执行数据的爬取'''
        # 启动浏览器驱动
        self.driver_start()
        # 访问爬取的页面
        self.driver_get_url('https://www.ssm.gov.mo/apps1/PreventCOVID-19/ch.aspx#clg17044')  
        # 关闭页面的弹窗  
        self.driver_xpath('//*[@id="reminderbox"]/div/div/div[1]/button').click()
        self.driver.implicitly_wait(200)
        # 切换至 iframe
        self.driver_iframe('//*[@id="cont_detail"]/div/iframe')
        # 最新消息的日期
        cms_date = self.driver_xpath('/html/body/div[2]/div/div[5]/div/div[2]/div').text
        # 最新消息的标题
        cms_title = self.driver_xpath('/html/body/div[2]/div/div[5]/div/span/b/a').text
        time.sleep(2)
        # 关闭浏览器驱动
        self.driver_quit()
        # 构造推送的消息
        latest_msg = '~~最新公告有料到~~\n\n' + cms_date + '\n' + cms_title + '\n\n' + '详情 : https://www.ssm.gov.mo/apps1/PreventCOVID-19/ch.aspx#clg17044\n\n'
        
        return latest_msg

    def dingding_push_msg(self):
        dingding_msg = self.driver_run()
        info(dingding_msg)
        dingding = DingDingNotice()
        with open("/Users/haauleon/陈巧伦-工作交接/macau_notice.json", "r") as load_f:
            load_dict = json.load(load_f)
            # print(load_dict)
        # 判断当前 dingding_msg 是否存在于文件中，如果没有就追加并发送钉钉消息
        if dingding_msg not in load_dict["notice"]:
            load_dict["notice"].append(dingding_msg)
            with open("/Users/haauleon/陈巧伦-工作交接/macau_notice.json", "w") as dump_f:
                json.dump(load_dict, dump_f, ensure_ascii=False)
                dingding.send_msg(dingding_msg)
                info("钉钉消息发送成")
        else:
            info("当前公告无更新")


def browser():
    '''启动浏览器驱动'''
    # 消除 Chrome正受到自动测试软件的控制 提示
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # 设置无头浏览器隐式访问
    chrome_options.add_argument('--headless')
    # “–no - sandbox”参数是让Chrome在root权限下跑
    chrome_options.add_argument('--no-sandbox')  

    # 启动浏览器驱动
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.maximize_window()
    driver.get('https://www.ssm.gov.mo/apps1/PreventCOVID-19/ch.aspx#clg17044')
    time.sleep(5)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="reminderbox"]/div/div/div[1]/button').click()
    time.sleep(100)
    iframe_obj = driver.find_element_by_xpath('//*[@id="cont_detail"]/div/iframe')
    driver.switch_to.frame(iframe_obj)
    driver.implicitly_wait(10)
    # 日期
    cms_date = driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/div[2]/div').text
    # 标题
    cms_title = driver.find_element_by_xpath('/html/body/div[2]/div/div[5]/div/span/b/a').text
    time.sleep(2)
    driver.quit()
    
    dingding_msg = '~~最新公告有料到~~\n\n' + cms_date + '\n' + cms_title + '\n\n' + '详情 : https://www.ssm.gov.mo/apps1/PreventCOVID-19/ch.aspx#clg17044\n\n'
    dingding = DingDingNotice()
    with open("/Users/haauleon/陈巧伦-工作交接/macau_notice.json", "r") as load_f:
        load_dict = json.load(load_f)
        # print(load_dict)
    # 判断当前 dingding_msg 是否存在于文件中，如果没有就追加并发送钉钉消息
    if dingding_msg not in load_dict["notice"]:
        load_dict["notice"].append(dingding_msg)
        with open("/Users/haauleon/陈巧伦-工作交接/macau_notice.json", "w") as dump_f:
            json.dump(load_dict, dump_f, ensure_ascii=False)
            dingding.send_msg(dingding_msg)
            info("钉钉消息发送成")
    else:
        info("当前公告无更新")


if __name__ == "__main__":
    _print("脚本开始执行")
    # 同步官网资讯且更新资讯
    # run_info()
    # 隐式爬取澳门防疫最新消息
    # browser()
    macau = SsmGovCovid()
    macau.dingding_push_msg()
    _print("脚本执行完成")
```