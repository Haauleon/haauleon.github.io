---
layout:        post
title:         "Python3 | 懂车帝价格监控钉钉推送"
subtitle:      "实现懂车帝珠海地区指定车型价格监控并进行钉钉消息推送"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---


### 实现效果
![](\img\in-post\post-python\2023-10-30-python-dongchedi-search-1.jpg)     

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
from enum import Enum
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
        text = f"<strong>【摸鱼办】</strong>今日懂车帝珠海地区价格监控结果如下\n" \
               f"{msg}"
        DingTalkSendMsg().send_markdown(
            title="【懂车帝价格监控】",
            msg=text
        )


class PageEle(Enum):
    ai_8_price = '//div[contains(@data-log-click, "艾瑞泽8")]/div[4]/text()'
    ai_5_price = '//div[contains(@data-log-click, "艾瑞泽5")]/div[4]/text()'
    ai_5_gt_price = '//div[contains(@data-log-click, "艾瑞泽5 GT")]/div[4]/text()'
    ai_5_plus_price = '//div[contains(@data-log-click, "艾瑞泽5 PLUS")]/div[4]/text()'


def run():
    dingtalk = DingTalkSendMsg()

    import requests
    from lxml import etree

    page = requests.get("https://www.dongchedi.com/search?keyword=%E8%89%BE%E7%91%9E%E6%B3%BD&currTab=6&city_name=%E7%8F%A0%E6%B5%B7&search_mode=common")
    root = etree.HTML(page.text)
    title_msg = list()

    ai_8_price = root.xpath(PageEle.ai_8_price.value)
    title_msg.append(f"- [艾瑞泽8](https://www.dongchedi.com/auto/series/5852) > {ai_8_price[0]}")

    ai_5_price = root.xpath(PageEle.ai_5_price.value)
    title_msg.append(f"- [艾瑞泽5](https://www.dongchedi.com/auto/series/1081) > {ai_5_price[0]}")

    ai_5_gt_price = root.xpath(PageEle.ai_5_gt_price.value)
    title_msg.append(f"- [艾瑞泽5 GT](https://www.dongchedi.com/auto/series/6033) > {ai_5_gt_price[0]}")

    ai_5_plus_price = root.xpath(PageEle.ai_5_plus_price.value)
    title_msg.append(f"- [艾瑞泽5 PLUS](https://www.dongchedi.com/auto/series/4803) > {ai_5_plus_price[0]}")

    msg = '\n'.join(title_msg)

    dingtalk.send_ding_notification(msg=msg)


if __name__ == '__main__':
    run()

```