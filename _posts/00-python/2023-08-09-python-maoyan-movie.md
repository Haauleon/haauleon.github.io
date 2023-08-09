---
layout:        post
title:         "Python3 | 猫眼电影国内票房排行榜钉钉推送"
subtitle:      "实现抓取猫眼电影国内票房排行榜前十名进行钉钉消息推送"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---


### 实现效果
![](\img\in-post\post-python\2023-08-09-python-maoyan-movie-1.jpg)     

<br>
<br>

### 代码实现
#### 1.安装第三方包
```bash
$ pip install DingtalkChatbot==1.5.3
```

<br>

#### 2.完整代码实现
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
"""
import calendar
import datetime
import base64
import hashlib
import hmac
import time
import urllib.parse
from typing import Any
from dingtalkchatbot.chatbot import DingtalkChatbot, FeedLink

WEBHOOK = 'WEBHOOK'
SECRET = '加签'


class DingTalkSendMsg(object):

    def __init__(self):
        self.timeStamp = str(round(time.time() * 1000))
        self.sign = self.get_sign()
        # self.devConfig = ConfigHandler()
        # 从yaml文件中获取钉钉配置信息
        # self.getDingTalk = GetYamlData(self.devConfig.setting_path).get_yaml_data()['DingTalk']

        # 获取 webhook地址
        # self.webhook = self.getDingTalk["webhook"] + "&timestamp=" + self.timeStamp + "&sign=" + self.sign
        self.webhook = WEBHOOK + "&timestamp=" + self.timeStamp + "&sign=" + self.sign
        self.xiaoDing = DingtalkChatbot(self.webhook)

    def get_sign(self) -> str:
        """
        根据时间戳 + "sign" 生成密钥
        :return:
        """
        secret = SECRET
        string_to_sign = '{}\n{}'.format(self.timeStamp, secret).encode('utf-8')
        hmac_code = hmac.new(secret.encode('utf-8'), string_to_sign, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return sign

    def send_text(self, msg: str, mobiles=None) -> None:
        """
        发送文本信息
        :param msg: 文本内容
        :param mobiles: 艾特用户电话
        :return:
        """
        if not mobiles:
            self.xiaoDing.send_text(msg=msg, is_at_all=True)
        else:
            if isinstance(mobiles, list):
                self.xiaoDing.send_text(msg=msg, at_mobiles=mobiles)
            else:
                raise TypeError("mobiles类型错误 不是list类型.")

    def send_link(self, title: str, text: str, message_url: str, pic_url: str) -> None:
        """
        发送link通知
        :return:
        """
        try:
            self.xiaoDing.send_link(title=title, text=text, message_url=message_url, pic_url=pic_url)
        except Exception:
            raise

    def send_markdown(self, title: str, msg: str, mobiles=None, is_at_all=False) -> None:
        """

        :param is_at_all:
        :param mobiles:
        :param title:
        :param msg:
        markdown 格式
        """

        if mobiles is None:
            self.xiaoDing.send_markdown(title=title, text=msg, is_at_all=is_at_all)
        else:
            if isinstance(mobiles, list):
                self.xiaoDing.send_markdown(title=title, text=msg, at_mobiles=mobiles)
            else:
                raise TypeError("mobiles类型错误 不是list类型.")

    @staticmethod
    def feed_link(title: str, message_url: str, pic_url: str) -> Any:

        return FeedLink(title=title, message_url=message_url, pic_url=pic_url)

    def send_feed_link(self, *arg) -> None:
        try:
            self.xiaoDing.send_feed_card(list(arg))
        except Exception:
            raise

    @staticmethod
    def send_ding_notification(msg):
        # 发送钉钉通知
        text = f"<strong>【摸鱼办】</strong>提醒您：国内实时票房排行榜如下\n\n" \
               f"{msg}"
        DingTalkSendMsg().send_markdown(
            title="【国内票房通知】",
            msg=text
        )


def run():
    dingtalk = DingTalkSendMsg()

    import requests
    from lxml import etree
    import random

    user_agent = [
        'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.8.7',
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1',
        'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7',
        'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Xoom Build/IML77) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Safari/535.7',
        'Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) AppleWebKit/534.46 (KHTML,like Gecko) Version/5.1 Mobile Safari/10600.6.3',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e YisouSpider/5.0 Safari/602.1',
        'Mozilla/5.0 (Linux; Android 4.0; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/59.0.3071.92',
        'Mozilla/5.0 (Linux; Android 6.0.1; SOV33 Build/35.0.D.0.326) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.91 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 7.1.1; vivo X20A Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.6.1.1',
        'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-J7108 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.7.977 Mobile Safari/537.36',
        'Mozilla/6.0 (Linux; Android 8.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Mobile Safari/537.36'
    ]
    headers = {
        'Accept-Encoding': 'identity',
        'User-Agent': random.choice(user_agent)
    }
    page = requests.get("https://piaofang.maoyan.com/box-office?ver=normal", headers=headers)
    root = etree.HTML(page.text)
    msg = list()
    for index in range(1, 11):
        title = root.xpath(f'//*[@id="app"]/div/div[2]/div/div[2]/table/tbody/tr[{index}]/td[1]/div/p[1]/text()')
        date = root.xpath(f'//*[@id="app"]/div/div[2]/div/div[2]/table/tbody/tr[{index}]/td[1]/div/p[2]/span[1]/text()')
        box_office = root.xpath(f'//*[@id="app"]/div/div[2]/div/div[2]/table/tbody/tr[{index}]/td[1]/div/p[2]/span[2]/text()')
        # print(title, date, box_office)
        msg.append(f"<font color=\"#FF0000\">Top {index}</font>：{title[0].replace(' ', '')}\n\n{date[0]} {box_office[0]}")
    msg = '\n\n'.join(msg)
    dingtalk.send_ding_notification(msg=msg)


if __name__ == '__main__':
    run()
```