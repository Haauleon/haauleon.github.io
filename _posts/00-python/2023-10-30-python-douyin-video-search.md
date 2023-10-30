---
layout:        post
title:         "Python3 | 抖音指定用户最新作品钉钉推送"
subtitle:      "实现爬取抖音指定用户最新作品并进行钉钉消息推送"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---


### 实现效果
![](\img\in-post\post-python\2023-10-30-python-douyin-video-search-1.jpg)     

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

import chardet
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
        text = f"<strong>【摸鱼办】</strong>提醒您：您关注的抖音用户“<mark>珠海市斗门区铭汇二手车汽贸中心</mark>”今日最新作品列表如下\n" \
               f"{msg}"
        DingTalkSendMsg().send_markdown(
            title="【抖音作品通知】",
            msg=text
        )


def run():
    dingtalk = DingTalkSendMsg()

    import requests

    url = "https://www.douyin.com/aweme/v1/web/aweme/post/?device_platform=webapp&aid=6383&channel=channel_pc_web&sec_user_id=MS4wLjABAAAAC6XV-8UZPCwP3XlI6_gSBP2yaHWFDb9ng6NSkce7S3Q&max_cursor=0&locate_query=false&show_live_replay_strategy=1&need_time_list=1&time_list_query=0&whale_cut_token=&cut_version=1&count=18&publish_video_strategy_type=2&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=114.0.0.0&browser_online=true&engine_name=Blink&engine_version=114.0.0.0&os_name=Windows&os_version=10&cpu_core_num=20&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=250&webid=7293774849616610843&msToken=jdFKE3F6RgR1p6l-bDWJ14xmla5Y0sMEGZHSthZDzfRxfyIwCnmspaA4nf0xuNa3rMxcGGvRrNP2cZ9tcz2wCesVjRe9y7x7j5AtgN-fNYt5G5w-Dr9Pofab7kHwq4g=&X-Bogus=DFSzswVOcxXANJ8btYyd4F9WX7rt"

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Cookie': 's_v_web_id=verify_lnlk0kcf_TTeiue3T_vjDU_4UV1_92lh_MayngbNgjNwV; ttwid=1%7CaWsl_uKQ7l-9o_gKEUIhZ3EubVkWsz-N4jqR420tlhw%7C1698214304%7C20a4a438d06942cb75e2f093ec62e670f30ab445b9006c493ee5f896a1588c99; home_can_add_dy_2_desktop=%220%22; passport_csrf_token=e3cba8440e501c0f4a461e11215ff256; passport_csrf_token_default=e3cba8440e501c0f4a461e11215ff256; ttcid=6e6c3b7060c3487f9148aea01af3ba7132; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; SEARCH_RESULT_LIST_TYPE=%22multi%22; douyin.com; device_web_cpu_core=20; device_web_memory_size=8; architecture=amd64; webcast_local_quality=null; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; download_guide=%223%2F20231025%2F1%22; __ac_nonce=06539c37e00c4f9d5b540; __ac_signature=_02B4Z6wo00f01z5I8KwAAIDDvkoK7Z7HYl8-aPQAAKq2BcTRuAXBq1EwIyx2.NaspNl8--4oBmvMlIObOuKTwADXO8KQL7tGXM0d4kq1CsKAt0mI37j7paXLpJWm9fc4vqBdMAgwA8iE7n5f7c; strategyABtestKey=%221698284415.316%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSVhTUE80dEIzYTk5dEdTWitvclpPbVRtWkFNSnJQWW9rOXMyRENCTFFyTkJIS0c4QktlSnB0YUY2RjRPVGo4RzlieDhzRU1IWVRoRTlFc3V1T2RQR0E9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A20%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; msToken=M3EJDkdxZz7hMlvJNRbXHRE_265PdK4IfJSOhtQI1shN5pXg0J_swL6MJt_blnsjWAoSUugYAzb7rkV-9XMrZrI7g4fAWOy0zOiP6qZCeWrywixqCLjh; msToken=oiy_U2EuLXeWrps8-lXAYUVQFGclUWwnqcim1jUSVawzb2yOiyOBgFOpCJ8okE2V1ZJvgGZkyfo9oxaKljbRTTVJNDmZrmbU_grpTE8SSfLAFqiuBnJxQx2p2c4FDA==; tt_scid=qgOfZX9xv8A-.uo7vT4RUyaumo5PEbVa4Ihg1u8rk5DbavV5l1nLvpQj1hlwx9ETaf48',
        'Pragma': 'no-cache',
        'Referer': 'https://www.douyin.com/user/MS4wLjABAAAAC6XV-8UZPCwP3XlI6_gSBP2yaHWFDb9ng6NSkce7S3Q',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    res = requests.get(url, headers=headers)
    search_data = res.json()["aweme_list"]
    # print(search_data)

    title_msg = list()
    for index in range(5):
        video_title = search_data[index]["desc"]
        video_url = search_data[index]["video"]["play_addr"]["url_list"][0]
        title_msg.append(f"- [{video_title}]({video_url})")
    msg = '\n'.join(title_msg)
    # print(msg)
    dingtalk.send_ding_notification(msg=msg)


if __name__ == '__main__':
    run()

```