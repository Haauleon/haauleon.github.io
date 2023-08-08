---
layout:        post
title:         "Python3 | 剩余工作日消息钉钉推送"
subtitle:      "本月全部工作日、剩余工作日倒计时、每月日薪计算等推送"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 实现效果
![](\img\in-post\post-python\2023-08-08-python-working-days-1.jpg)     

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
    def send_ding_notification(salary, total_days, remaining_days):
        # 发送钉钉通知
        text = f"<strong>【摸鱼办】</strong>提醒您：" \
               f"本月总共需要上 <font color=\"#FF0000\">{total_days}</font> 天班，" \
               f"还剩余 <font color=\"#FF0000\">{remaining_days}</font> 天班。" \
               f"终于结束一天的工作了，今天又赚了 <font color=\"#009900\"><strong>{int(salary/total_days)}</strong></font> 元人民币，实在是太棒啦！收工回家~"
        DingTalkSendMsg().send_markdown(
            title="【钱包入账通知】",
            msg=text
        )


def run():
    dingtalk = DingTalkSendMsg()

    now = datetime.datetime.now()
    cal = calendar.Calendar()
    working_days = [x for x in cal.itermonthdays2(now.year, now.month) if x[0] !=0 and x[1] < 5]
    # print(working_days)
    for working_day in working_days:
        if working_day[0] == int(now.strftime("%m")):
            # print(working_days.index(working_day))  # 获取当前工作日所在的工作日列表的下标
            working_day_index = working_days.index(working_day)
            remaining_days = len(working_days[working_day_index:-1])
            break
    total_days = len(working_days)
    dingtalk.send_ding_notification(salary=5000, total_days=total_days, remaining_days=remaining_days)


if __name__ == '__main__':
    run()

---

相关链接：   
[使用Python计算一个月的工作日数？ - 问答 - Python中文网](https://www.cnpython.com/qa/68095)     