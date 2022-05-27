---
layout:        post
title:         "数据分析 | 小试牛刀"
subtitle:      "创建数据分析图表类来玩玩"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - 爬虫
    - 数据分析
    - 小而美脚本
---

### 代码设计
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   data_analytics.py
@Date    :   2022-05-25 10:22
@Function:   数据分析图表类
注意:
参考自: https://jishuin.proginn.com/p/763bfbd660a0
1. mplfonts 安装 (解决 matplotlib 无法显示中文的问题)
pip install mplfonts -i https://pypi.tuna.tsinghua.edu.cn/simple
"""
import numpy as np
import matplotlib.pyplot as plt
from mplfonts import use_font
from mplfonts.bin.cli import init

init()
use_font('Noto Serif CJK SC')  # 指定中文字体


class DataAnalytics:

    @staticmethod
    def lollipop_illustration(title=None, *data):
        """棒棒糖图
        @param title: 图表标题
        @param data: 分别接收纵轴和横轴的数据
        """
        import pandas as pd
        # 获取纵轴和横轴的数据
        height, bars = data
        # 图表标题
        plt.title(title, color='black')
        # 创建数据
        df = pd.DataFrame({'group':  bars, 'values': height})
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


if __name__ == '__main__':
    # DataAnalytics.lollipop_illustration('Python分析', [3, 12, 5, 18, 45], ['Python', 'B', 'C', 'D', 'E'])
    # DataAnalytics.connect_scatter_plot('Python分析', [3, 12, 5, 18, 45], ['Python', 'B', 'C', 'D', 'E'])
    # DataAnalytics.bar_chart('Python分析', [3, 12, 5, 18, 45], ('Python', 'B', 'C', 'D', 'E'))
    # DataAnalytics.donut_chart('Python分析', [3, 12, 5, 18, 45])
    # DataAnalytics.pie_chart('Python分析', [3, 12, 5, 18, 45])
    # DataAnalytics.map()
    DataAnalytics.bubble_map()
```