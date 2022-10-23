---
layout:        post
title:         "数据分析 | BOSS 直聘"
subtitle:      "爬取数据、处理数据、生成图表"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - 爬虫
    - 数据分析
---

### 代码简介
![](\img\in-post\post-other\2022-05-26-boss-1.jpg)     


<br><br>

### 代码设计
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   boss_analytics.py
@Date    :   2022-05-26 10:22
@Function:   boss直聘平台数据分析图表类
注意:
参考自: https://jishuin.proginn.com/p/763bfbd660a0
1. mplfonts 安装 (解决 matplotlib 无法显示中文的问题)
pip install mplfonts -i https://pypi.tuna.tsinghua.edu.cn/simple
2. 功能待完善, 目前需要手动更新 data_handler() 方法的返回值辅助生成图表
"""
import requests
import json
import logging
from colorama import Fore, Style
from functools import wraps
import time
import sys
# from datetime import date, timedelta
import numpy as np
import matplotlib.pyplot as plt
from mplfonts import use_font
from mplfonts.bin.cli import init

init()
# 指定中文字体
use_font('Noto Serif CJK SC')
# 公司小黑屋(拉黑名单)
BLACK_HOUSE = [
    '一微半导体股份有...',
    '......'
]
# boss直聘请求头
headers = {
    'Host': 'www.zhipin.com',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 '
                  'Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type': 'application/x-www-form-urlencoded',
    'miniappVersion': '4.0501',
    'mpt': 'xxx',
    'platform': 'zhipin/windows',
    'scene': '1001',
    'ua': '{"model":"microsoft","platform":"windows"}',
    'ver': '4.0501',
    'wt2': 'xxx',
    'x-requested-with': 'XMLHttpRequest',
    'zpAppId': '10002',
    'Referer': 'https://servicewechat.com/wxa8da525af05281f3/311/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br',
}

# 日志配置
_logger = logging.getLogger('boss-analytics')  # 获取日志记录器
_logger.setLevel(logging.DEBUG)  # 设置日志等级
_handler = logging.StreamHandler(sys.stdout)  # 输入到控制台的 handler
_logger.addHandler(_handler)  # 日志记录器增加 handler


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


class DataAnalytics:

    @staticmethod
    def lollipop_illustration(title=None, *data):
        """棒棒糖图
        @param title: 图表标题
        @param data: 分别接收纵轴和横轴的数据
        """
        import pandas as pd
        # 图表标题
        plt.title(title, color='black')
        # 获取纵轴和横轴的数据
        height, bars = data
        # 图表标题
        plt.title(title, color='black')
        # 创建数据
        df = pd.DataFrame({'group': bars, 'values': height})
        # 排序取值
        ordered_df = df.sort_values(by='values')
        my_range = range(len(df.index))
        # 创建图表
        plt.stem(ordered_df['values'])
        plt.xticks(my_range, ordered_df['group'])
        # 显示
        plt.show()

    @staticmethod
    def connect_scatter_plot(title=None, *data):
        """连接散点图
        @param title: 图表标题
        @param data: 分别接收纵轴和横轴的数据
        """
        import pandas as pd
        plt.title(title, color='black')
        # 获取纵轴和横轴的数据
        y_axis, x_axis = data
        # 创建数据
        df = pd.DataFrame({'x_axis': x_axis, 'y_axis': y_axis})
        # 绘制显示
        plt.plot('x_axis', 'y_axis', data=df, linestyle='-', marker='o')
        plt.show()

    @staticmethod
    def bar_chart(title=None, *data):
        """条形图
        @param title: 图表标题
        @param data: 分别接收纵横和横轴的数据
        """
        plt.title(title, color='black')
        # 获取纵轴和横轴的数据
        height, bars = data
        # 创建条形图
        y_pos = np.arange(len(bars))
        plt.bar(y_pos, height)
        # 横轴标签
        plt.xticks(y_pos, bars)
        # 窗口显示
        plt.show()

    @staticmethod
    def donut_chart(title: str = None, data: list = None):
        """环形图
        @param title: 图表标题
        @param data: 数据
        """
        plt.title(title, color='black')
        # 创建数据
        size_of_groups = data
        # 生成饼图
        plt.pie(size_of_groups)
        # 在中心添加一个圆, 生成环形图
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        plt.show()

    @staticmethod
    def pie_chart(title: str = None, data: list = None):
        """饼图
        @param title: 图表标题
        @param data: 数据
        """
        plt.title(title, color='black')
        # 创建数据
        size_of_groups = data
        # 生成饼图
        plt.pie(size_of_groups)
        plt.show()

    @staticmethod
    def map():
        """创建地图"""
        import pandas as pd
        import folium
        # 创建地图对象
        m = folium.Map(location=[0, 0], tiles="OpenStreetMap", zoom_start=2)
        # 创建图标数据
        data = pd.DataFrame({
            'northing': [113.578565, 113.553986, 113.497345, 113.536232, 113.604417],
            'easting': [22.253389, 22.215884, 22.219334, 22.120977, 22.34414],
            'name': ['吉大', '拱北', '南屏', '横琴', '唐家湾'],
            'value': [10, 12, 40, 70, 23]
        }, dtype=str)
        # 添加信息
        for i in range(0, len(data)):
            print(data.iloc[i]['northing'], data.iloc[i]['easting'])
            folium.Marker(
                location=[data.iloc[i]['easting'], data.iloc[i]['northing']],
                popup=data.iloc[i]['name'],
            ).add_to(m)

        # 保存
        m.save('map1.html')

    @staticmethod
    def bubble_map():
        """创建气泡地图"""
        import folium
        import pandas as pd
        # 创建地图对象
        m = folium.Map(location=[0, 0], tiles="OpenStreetMap", zoom_start=2)
        # 创建图标数据
        data = pd.DataFrame({
            'northing': [113.578565, 113.553986, 113.497345, 113.536232, 113.604417],
            'easting': [22.253389, 22.215884, 22.219334, 22.120977, 22.34414],
            'name': ['吉大', '拱北', '南屏', '横琴', '唐家湾'],
            'value': [10, 12, 40, 70, 23]
        }, dtype=str)

        # 添加气泡
        for i in range(0, len(data)):
            folium.Circle(
                location=[data.iloc[i]['easting'], data.iloc[i]['northing']],
                popup=data.iloc[i]['name'],
                radius=float(data.iloc[i]['value']) * 20000,
                color='crimson',
                fill=True,
                fill_color='crimson'
            ).add_to(m)

        # 保存
        m.save('bubble-map.html')


class DingDingNotice:
    """钉钉发送类"""

    def __init__(self, ding_token=None, atMobiles=None, isAtAll=None):
        # 根据电话@用户
        self.atMobiles = ['13046367204', ] if atMobiles is None else atMobiles
        # self.token = 'cbb3b771657ef' if ding_token==None else ding_token
        # 是否@所有人
        self.isAtAll = True if isAtAll is None else isAtAll
        self.token = 'xxx'
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


class BossZhiPin:
    """爬取 BOSS 直聘的职位"""

    def __init__(self):
        self.headers = headers
        self.boss_url = 'https://www.zhipin.com/wapi/zpgeek/miniapp/search/joblist.json?query=&city=101280700&source' \
                        '=undefined&stage=&scale=&degree=&industry=&salary=&experience=&sortType=0&subwayLineId' \
                        '=&subwayStationId=&districtCode=&businessCode=&longitude=&latitude=&position=&expectId' \
                        '=&expectPosition=&page=%s&pageSize=30&appId=10002'
        self.skills = []  # 工作技能
        self.businesses = []  # 工作地区
        self.brandnames = []  # 公司名称
        self.jobexperience = []  # 工作经验
        self.jobnames = []  # 岗位名称
        self.salarydescs = []  # 工作薪酬
        self.performance = []  # 岗位职责

    def get_boss_data(self):
        """爬取boss直聘的数据"""
        for i in range(1, 100):
            # print('---------------------------------------- 第%d页 ----------------------------------------' % i)
            res = requests.get(self.boss_url % str(i), headers=headers).json()
            # print(res)
            jobs = res['zpData']['list']
            if jobs:
                yield jobs
            else:
                break

    def get_boss_data_detail(self):
        """数据过滤处理"""
        data = self.get_boss_data()
        while True:
            try:
                jobs = next(data)
                for i in range(len(jobs)):
                    detail = jobs[i]
                    if detail['districtName'] not in ['金湾区', '斗门区']:
                        if detail['brandName'] not in BLACK_HOUSE:
                            if detail['jobExperience'] != '经验不限':
                                self.skills += detail['skills']
                                self.skills += detail['jobLabels']
                                self.salarydescs.append(detail['salaryDesc'].split('-')[0]+'k')
                                self.jobnames.append(detail['jobName'])
                                self.jobexperience.append(detail['jobExperience'])
                                self.brandnames.append(detail['brandName'])
                                if detail['businessName']:
                                    self.businesses.append(detail['businessName'])
            except StopIteration:
                break

    @staticmethod
    def all_list(arr: list):
        """list.count() 方法用于获取所有元素的出现次数
        @param arr: [指标1, 指标2, 指标3, 指标2, 指标3...]
        @return: 数据字典 {指标1:频率1, 指标2:频率2, 指标3:频率3}
        """
        result = {}
        for i in set(arr):
            result[i] = arr.count(i)
        return result

    def set_order(self, data: list):
        """处理排序，出现频率高的指标排在前面
        @param data: [指标1, 指标2, 指标3, 指标2, 指标3...]
        @return: 元组列表 [(指标1, 频率1), (指标2, 频率2), (指标3, 频率3)...]
        """
        d = self.all_list(data)
        # 根据字典的值进行倒序(大 -> 小)排序并返回一个列表, 列表元素是元组
        d_order = sorted(d.items(), key=lambda x: x[1], reverse=True)
        # for i in d_order:
        #     print(i)
        # print(d_order)
        return d_order

    def data_handler(self):
        """返回被处理完成的数据"""
        info('处理数据...')
        self.get_boss_data_detail()
        new_skills = self.set_order(self.skills)    # 技能
        new_salarydescs = self.set_order(self.salarydescs)    # 薪酬
        new_jobnames = self.set_order(self.jobnames)     # 职位
        new_jobexperience = self.set_order(self.jobexperience)    # 经验
        new_brandnames = self.set_order(self.brandnames)   # 公司
        new_businesses = self.set_order(self.businesses)    # 地区
        return new_skills

    def get_analytics_data(self):
        """获取数据分析图表纵轴和横轴的数据
        @rtype: tuple
        @return: 解析后的纵横(频率)列表、横轴(指标)列表
        """
        x = []
        y = []
        for d in self.data_handler()[:15]:
            x.append(d[0])
            y.append(d[1])
        return x, y


class BossAnalytics:
    """生成数据分析图表"""

    @staticmethod
    def get_lollipop_illustration():
        bz = BossZhiPin()
        info('爬取数据...')
        x, y = bz.get_analytics_data()
        # print(x)
        # print(y)
        info('生成图表...')
        DataAnalytics.lollipop_illustration('', y, x)


if __name__ == '__main__':
    _print("开始执行...")
    # b = BossZhiPin()
    # b.data_handler()
    BossAnalytics.get_lollipop_illustration()
    _print("执行完成")
```