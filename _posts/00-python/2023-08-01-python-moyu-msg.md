---
layout:        post
title:         "Python3 | 摸鱼办消息钉钉推送"
subtitle:      "周末、元旦、过年、清明、劳动、端午、中秋和国庆倒计时推送"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 实现效果
![](\img\in-post\post-python\2023-08-01-python-moyu-msg-1.png)     

<br>
<br>

### 代码实现
#### 1.安装第三方包
```bash
$ pip install DingtalkChatbot==1.5.3
$ pip install cnlunar~=0.1.1
$ pip install zhdate~=0.1
```

<br>

#### 2.完整代码实现
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   get_countdown.py
@Date    :   2023-08-01 14:56
@Function:   None

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2023-08-01 14:56         haauleon         1.0           None
"""
import datetime
import cnlunar
from zhdate import ZhDate
import base64
import hashlib
import hmac
import time
import urllib.parse
from typing import Any
from dingtalkchatbot.chatbot import DingtalkChatbot, FeedLink


WEBHOOK = '钉钉机器人WEBHOOK'
SECRET = '钉钉机器人价签字符串'


class DingTalkSendMsg(object):

    def __init__(self):
        self.timeStamp = str(round(time.time() * 1000))
        self.sign = self.get_sign()
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
    def send_ding_notification(now_date, week_day_date, countdown_msg):
        # 发送钉钉通知
        text = f'<strong>【摸鱼办】提醒您</strong>：{now_date}，{get_today_detail()}，{week_day_date}。' \
               f'大家中午好，工作虽然辛苦，但也不要忘了休息，起来去茶水间、厕所或者走廊活动活动身体，祝愿所有人愉快地度过每一天...\n{countdown_msg} '
        DingTalkSendMsg().send_markdown(
            title="【摸鱼办通知】",
            msg=text
        )


def get_today_detail():
    a = cnlunar.Lunar(datetime.datetime.now(), godType='8char')  # 常规算法
    # a = cnlunar.Lunar(datetime.datetime(2022, 2, 3, 10, 30), godType='8char', year8Char='beginningOfSpring')  # 八字立春切换算法
    dic = {
        # '日期': a.date,
        # '农历数字': (a.lunarYear, a.lunarMonth, a.lunarDay, '闰' if a.isLunarLeapMonth else ''),
        '农历': '%s %s[%s]年 %s%s' % (a.lunarYearCn, a.year8Char, a.chineseYearZodiac, a.lunarMonthCn, a.lunarDayCn),
        # '星期': a.weekDayCn,
        # 未增加除夕
        # '今日节日': (a.get_legalHolidays(), a.get_otherHolidays(), a.get_otherLunarHolidays()),
        # '八字': ' '.join([a.year8Char, a.month8Char, a.day8Char, a.twohour8Char]),
        # '今日节气': a.todaySolarTerms,
        # '下一节气': (a.nextSolarTerm, a.nextSolarTermDate, a.nextSolarTermYear),
        # '今年节气表': a.thisYearSolarTermsDic,
        # '季节': a.lunarSeason,
        #
        # '今日时辰': a.twohour8CharList,
        # '时辰凶吉': a.get_twohourLuckyList(),
        # '生肖冲煞': a.chineseZodiacClash,
        # '星座': a.starZodiac,
        # '星次': a.todayEastZodiac,
        #
        # '彭祖百忌': a.get_pengTaboo(),
        # '彭祖百忌精简': a.get_pengTaboo(long=4, delimit='<br>'),
        # '十二神': a.get_today12DayOfficer(),
        # '廿八宿': a.get_the28Stars(),
        #
        # '今日三合': a.zodiacMark3List,
        # '今日六合': a.zodiacMark6,
        # '今日五行': a.get_today5Elements(),
        #
        # '纳音': a.get_nayin(),
        # '九宫飞星': a.get_the9FlyStar(),
        # '吉神方位': a.get_luckyGodsDirection(),
        # '今日胎神': a.get_fetalGod(),
        # '神煞宜忌': a.angelDemon,
        # '今日吉神': a.goodGodName,
        # '今日凶煞': a.badGodName,
        # '宜忌等第': a.todayLevelName,
        # '宜': a.goodThing,
        # '忌': a.badThing,
        # '时辰经络': a.meridians
    }

    today_msg = list()
    for i in dic:
        # midstr = '\t' * (2 - len(i) // 2) + ':' + '\t'
        # print(i, midstr, dic[i])
        # print(dic[i])
        today_msg.append(dic[i].replace(' ', ''))

    today_msg = ''.join(today_msg)
    # print(today_msg)
    return today_msg


def get_week_day(date):
    week_day_dict = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }
    day = date.weekday()
    return week_day_dict[day]


def time_parse(today):
    distance_year = (datetime.datetime.strptime(f"{today.year}-01-01", "%Y-%m-%d").date() - today).days
    distance_year = distance_year if distance_year > 0 else (
            datetime.datetime.strptime(f"{today.year + 1}-01-01", "%Y-%m-%d").date() - today).days

    distance_big_year = (ZhDate(today.year, 1, 1).to_datetime().date() - today).days
    distance_big_year = distance_big_year if distance_big_year > 0 else (
            ZhDate(today.year + 1, 1, 1).to_datetime().date() - today).days

    distance_4_5 = (datetime.datetime.strptime(f"{today.year}-04-05", "%Y-%m-%d").date() - today).days
    distance_4_5 = distance_4_5 if distance_4_5 > 0 else (
            datetime.datetime.strptime(f"{today.year + 1}-04-05", "%Y-%m-%d").date() - today).days

    distance_5_1 = (datetime.datetime.strptime(f"{today.year}-05-01", "%Y-%m-%d").date() - today).days
    distance_5_1 = distance_5_1 if distance_5_1 > 0 else (
            datetime.datetime.strptime(f"{today.year + 1}-05-01", "%Y-%m-%d").date() - today).days

    distance_5_5 = (ZhDate(today.year, 5, 5).to_datetime().date() - today).days
    distance_5_5 = distance_5_5 if distance_5_5 > 0 else (
            ZhDate(today.year + 1, 5, 5).to_datetime().date() - today).days

    distance_8_15 = (ZhDate(today.year, 8, 15).to_datetime().date() - today).days
    distance_8_15 = distance_8_15 if distance_8_15 > 0 else (
            ZhDate(today.year + 1, 8, 15).to_datetime().date() - today).days

    distance_10_1 = (datetime.datetime.strptime(f"{today.year}-10-01", "%Y-%m-%d").date() - today).days
    distance_10_1 = distance_10_1 if distance_10_1 > 0 else (
            datetime.datetime.strptime(f"{today.year + 1}-10-01", "%Y-%m-%d").date() - today).days

    # print("距离周末: ", 5 - today.weekday())
    # print("距离元旦: ", distance_year)
    # print("距离大年: ", distance_big_year)
    # print("距离清明: ", distance_4_5)
    # print("距离劳动: ", distance_5_1)
    # print("距离端午: ", distance_5_5)
    # print("距离中秋: ", distance_8_15)
    # print("距离国庆: ", distance_10_1)

    time_ = [
        {"v_": 5 - 1 - today.weekday(), "title": "周末"},  # 距离周末
        {"v_": distance_year, "title": "元旦"},  # 距离元旦
        {"v_": distance_big_year, "title": "过年"},  # 距离过年
        {"v_": distance_4_5, "title": "清明节"},  # 距离清明
        {"v_": distance_5_1, "title": "劳动节"},  # 距离劳动
        {"v_": distance_5_5, "title": "端午节"},  # 距离端午
        {"v_": distance_8_15, "title": "中秋节"},  # 距离中秋
        {"v_": distance_10_1, "title": "国庆节"},  # 距离国庆
    ]

    time_ = sorted(time_, key=lambda x: x['v_'], reverse=False)
    return time_


def countdown():
    today = datetime.date.today()
    now_ = f"{today.year}年{today.month}月{today.day}日"
    week_day_ = get_week_day(today)
    # print(f'{now_} {week_day_}')

    time_ = time_parse(today)
    countdown_msg = list()
    for t_ in time_:
        # print(f'距离【{t_.get("title")}】还有 {t_.get("v_")} 天')
        countdown_msg.append(f'- 距离【{t_.get("title")}】还有 <font color=\"#009900\">{t_.get("v_")}</font> 天')
    countdown_msg = '\n\n'.join(countdown_msg)
    return now_, week_day_, countdown_msg


def main():
    dingtalk = DingTalkSendMsg()
    now_date, week_day_date, countdown_msg = countdown()
    dingtalk.send_ding_notification(now_date, week_day_date, countdown_msg)


if __name__ == '__main__':
    main()

```

<br>
<br>

---

相关链接：   
[Python3 | 获取旧历农历老黄历](2023-08-01-python-cnlunar.md)     
[Python3 | 统计节假日剩余天数](2023-08-01-python-moyu-msg.md)