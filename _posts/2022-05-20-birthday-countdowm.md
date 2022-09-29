---
layout:        post
title:         "Python3 | 生日自动发送sms"
subtitle:      "服务器跑脚本，可以在生日当天凌晨自动发送sms祝福给对方"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - 小而美脚本
---

### 代码设计
```python
# -*- coding:utf-8 -*-
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   birthday_date_countdown.py
@Date    :   2022-05-19 13:00:00
@Function:   生日监控器
注意:
1、版本 pip install sxtwl==1.0.5
"""

import requests
import json
import sys
import time
import logging
from datetime import datetime
from colorama import Fore, Style
from qcloudsms_py import SmsMultiSender, SmsSingleSender, sms
from qcloudsms_py.httpclient import HTTPError
from functools import wraps
import random
import sxtwl
import ssl
import certifi

# ssl_context = ssl.create_default_context()
# ssl_context.load_verify_locations(certifi.where())
ssl._create_default_https_context = ssl._create_unverified_context


# 腾讯云短信配置
TENCENT_SMS_APP_ID = '应用 ID'
TENCENT_SMS_APP_KEY = '应用 KEY'
TENCENT_SMS_SIGN = '短信签名'

# 短信接收者(主账号)
phone = [
    '电话号码',  # 自己的电话用作备份，第一时间知道发给了谁
]

# 日志配置
_logger = logging.getLogger('birthday')  # 获取日志记录器
_logger.setLevel(logging.DEBUG)  # 设置日志等级
_handler = logging.StreamHandler(sys.stdout)  # 输入到控制台的 handler
_logger.addHandler(_handler)  # 日志记录器增加 handler

# 日历中文索引
YMC = [
    "十一", "十二", "正", "二", "三",
    "四", "五", "六", "七", "八", "九", "十"
]

RMC = [
    "初一", "初二", "初三", "初四", "初五",
    "初六", "初七", "初八", "初九", "初十",
    "十一", "十二", "十三", "十四", "十五",
    "十六", "十七", "十八", "十九", "二十",
    "廿一", "廿二", "廿三", "廿四", "廿五",
    "廿六", "廿七", "廿八", "廿九", "三十", "卅一"
]


def info(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.info(Fore.GREEN + now + " [INFO] " + str(msg) + Style.RESET_ALL)


def error(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.error(Fore.RED + now + " [ERROR] " + str(msg) + Style.RESET_ALL)


def _print(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.debug(Fore.BLUE + now + " [PRINT] " + str(msg) + Style.RESET_ALL)


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


class SMSNotice:
    """短信发送类"""

    def __init__(self):
        self.appid = TENCENT_SMS_APP_ID  # 自己应用ID
        self.appkey = TENCENT_SMS_APP_KEY  # 自己应用Key
        self.sms_sign = TENCENT_SMS_SIGN  # 自己腾讯云创建签名时填写的签名内容（使用公众号的话这个值一般是公众号全称或简称）

    def send_sms_single(self, phone_num, template_id, template_param_list):
        """
        单条发送短信
        :param phone_num: 手机号(字符串格式，如 '111111')
        :param template_id: 腾讯云短信模板ID
        :param template_param_list: 短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
        :return:
        """
        sender = SmsSingleSender(self.appid, self.appkey)
        try:
            response = sender.send_with_param(86, phone_num, template_id, template_param_list, sign=self.sms_sign)
        except HTTPError as e:
            response = {'result': 1000, 'errmsg': "网络异常发送失败"}
        return response

    def send_sms_multi(self, phone_num_list, template_id, param_list):
        """
        批量发送短信
        :param phone_num_list:手机号列表(列表格式，如 ['11111', '22222'])
        :param template_id:腾讯云短信模板ID
        :param param_list:短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
        :return:
        """
        sender = SmsMultiSender(self.appid, self.appkey)
        try:
            response = sender.send_with_param(86, phone_num_list, template_id, param_list, sign=self.sms_sign)
        except HTTPError as e:
            response = {'result': 1000, 'errmsg': "网络异常发送失败"}
        return response


lunar = sxtwl.Lunar()  # 实例化日历库
today_year = int(datetime.now().strftime('%Y'))


class GetDay:
    """新旧历的转换"""

    @staticmethod
    def get_day_by_lunar(*solar_date):
        """旧历转新历"""
        year, month, day = solar_date
        lunar_date = lunar.getDayByLunar(year, month, day, False)
        return "%s年%s月%s日" % (lunar_date.y, str(lunar_date.m).rjust(2, '0'), str(lunar_date.d).rjust(2, '0'))

    @staticmethod
    def get_day_by_solar(*lunar_date):
        """新历转旧历"""
        year, month, day = lunar_date
        solar_date = lunar.getDayBySolar(year, month, day)
        # bool(solar_date.Lleap) 为True即润年，反之则不是
        return "%s月%s日" % (YMC[solar_date.Lmc], RMC[solar_date.Ldi])


# 生日(昵称-生日-电话号码)
birthday_data = [
    ('昵称1', GetDay.get_day_by_lunar(today_year, 8, 8), '电话号码1'),
    ('昵称2', '%d年05月20日' % today_year, '电话号码2')
]

# 红包(金额-寓意-口令)
red_envelope = [
    ('100.01', '你就是百里挑一', '你要去桃花岛吗？我有船'),
    ('166.66', '人生顺风顺水', '你的益达，不，是你的益达'),
    ('168.88', '一路发发发', '土豆土豆，我是牛肉'),
    ('178.88', '一起发发发', '天王盖地虎，小猫抓老鼠'),
    ('188.88', '一直发发发', '山无棱天地合，我是夏雨荷'),
]


class BirthdayNotice:
    def __init__(self):
        self.today = datetime.now().strftime('%Y年%m月%d日')
        self.red_envelope = red_envelope
        self.birthday_data = birthday_data
        self.new_phone = phone

    def get_random_red_envelope(self):
        return random.choice(self.red_envelope)

    def get_someone_birthday(self):
        for p in self.birthday_data:
            _, birthday, _ = p
            if birthday == self.today:
                yield p

    def push_msg(self):
        x = self.get_someone_birthday()
        while True:
            try:
                _, _, salt = self.get_random_red_envelope()
                nickname, _, phonenum = next(x)
                sms_msg = [
                    nickname,
                    salt,
                ]
                # _print(nickname, ':', balance, ':', mean)
                s = SMSNotice()
                self.new_phone.append(phonenum)
                sms_result = s.send_sms_multi(self.new_phone, 1409481, sms_msg)
                if "'errmsg': 'OK'" in str(sms_result):
                    _print("短信发送成功")
                else:
                    error("短信异常 >>> %s" % str(sms_result))
            except StopIteration:
                break


if __name__ == '__main__':

    b = BirthdayNotice()
    b.push_msg()
    _print("脚本执行完成")
```