---
layout:        post
title:         "百度 API | 百度翻译"
subtitle:      "每秒只能请求一次"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 百度API
---

### 背景
&emsp;&emsp;虽然百度翻译不是很地道，但是能解决问题，而且免费！！！！

<br><br>

### 代码实现
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   baidu_translate.py
@Date    :   2022-07-05 09:30
@Function:   百度翻译类
@tips    :   百度翻译开放平台 http://api.fanyi.baidu.com/doc/21
"""
import hashlib
import json
import requests
import urllib
import time
import xlrd
import xlwt
from common.setting import ConfigHandler
from common.log import Logger
from common.counter import Counter

# 百度翻译开发者信息配置
BAIDU_APPID = ''         
BAIDU_SECRET_KEY = ''


class BaiduTranslate:
    """
    百度翻译
    """

    def __init__(self):
        self.url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'BAIDUID=60E38BE81B936900EF3C5CDF623397B7:FG=1'
        }
        # self.langs = ["cht", "pt", "en", "jp", "kor"]
        self.langs = ["cht", "pt", "en", ]

    @staticmethod
    def get_signmd5(content):
        """
        生成 md5 加密后的 sign

        :return:
        """
        sign = BAIDU_APPID + content + 'baidu' + BAIDU_SECRET_KEY
        # sign.encode() 变成 bytes 类型后才能加密
        signmd5 = hashlib.md5(sign.encode())
        signmd5 = signmd5.hexdigest()
        return signmd5

    def translate_content(self, content):
        """
        文本翻译
        自动识别文本并分别翻译成繁体、葡语、英语

        :param content: 文本
        :return: 元组 (简体, 繁体, 葡文, 英文)
        """
        # 在 python3 中将中文进行 urlencode 编码
        q = urllib.parse.quote(content, safe='/', encoding=None, errors=None)
        contents = dict()
        for lang in self.langs:
            '''自动识别文本并分别翻译成繁体、葡语、英语'''
            payload = 'q=%s&from=auto&to=%s&appid=%s&salt=baidu&sign=%s' % (
                q, lang, BAIDU_APPID, self.get_signmd5(content))
            res = requests.request("POST", self.url, headers=self.headers, data=payload).json()
            contents[lang] = res['trans_result'][0]['dst']
            time.sleep(1)  # 免费接口只能一秒种请求一次，否则会报错
        return content, contents['cht'], contents['pt'], contents['en']
```