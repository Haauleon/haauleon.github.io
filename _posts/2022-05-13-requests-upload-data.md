---
layout:        post
title:         "爬虫 | requests 模块实现商品数据上传"
subtitle:      "将客户提供的 upload 图片目录和 productTemplate.xlsx 文件的商品数据上传至壹壹车后台"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 爬虫
    - Python
---

### 项目背景
项目实现：   
1. 提取 excel 中的数据    
2. 使用 requests 模块将数据上传至后台      

![](\img\in-post\post-other\2022-05-13-requests-upload-data-1.png)

<br><br>

### 代码设计
```python
# -*- coding:utf-8 -*-
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   upload_product.py
@Date    :   2022-05-11 10:56:00
@Function:   将客户提供的 upload 图片目录和 productTemplate.xlsx 文件的商品数据上传至壹壹车后台
1. 处理 productTemplate.xlsx 文件的商品数据并返回
2. 保存商品数据至壹壹车后台商品管理列表
3.注意:
"""
import requests
import json
import xlrd
import logging
import sys
import time
from colorama import Fore, Style
import pprint
print = pprint.pprint

# 壹壹车后台认证签名
AUTHORIZATION = 'xxx'
# 壹壹车后台认证信息
COOKIE = 'xxx'
# 壹壹车后台访问渠道
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/90.0.4430.93 Safari/537.36 '


_logger = logging.getLogger('YiYiCar')        # 获取日志记录器
_logger.setLevel(logging.DEBUG)               # 设置日志等级
_handler = logging.StreamHandler(sys.stdout)  # 输入到控制台的 handler
_logger.addHandler(_handler)


def info(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.info(Fore.GREEN + now + " [INFO] " + str(msg) + Style.RESET_ALL)


def error(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.error(Fore.RED + now + " [ERROR] " + str(msg) + Style.RESET_ALL)


def _print(msg):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    _logger.debug(Fore.BLUE + now + " [PRINT] " + str(msg) + Style.RESET_ALL)


class ExcelHandler:
    """壹壹车商品清单文件处理"""

    def __init__(self, file_path, t_loc=0):
        """默认处理excel中的第一个table"""
        self.file_path = file_path
        self.xl = xlrd.open_workbook(file_path)
        self.table = self.xl.sheets()[t_loc]

    def table_nrows(self):
        """获取sheet表的总行数"""
        return self.table.nrows

    def get_row_value(self):
        """获取每一行的列值"""
        for row in range(1, self.table_nrows()):
            store_name = self.table.cell(row, 0).value      # 商品名称
            keyword = self.table.cell(row, 1).value         # 商品关键字
            image_loc = self.table.cell(row, 2).value       # 商品封面图
            slider_image = self.table.cell(row, 3).value    # 商品轮播图
            description = self.table.cell(row, 4).value     # 商品详情
            price = self.table.cell(row, 5).value           # 商品价格
            # _print([store_name, keyword, int(image_loc), slider_image, description, '{:.2f}'.format(price*10000)])
            yield store_name, keyword, int(image_loc), slider_image, description, '{:.2f}'.format(price*10000)


class YiYiCar:
    """壹壹车后台管理"""

    def __init__(self):
        self.base_url = 'http://boss.yyc.bringbuys.com'
        self.auth = AUTHORIZATION
        self.cookie = COOKIE
        self.user_agent = USER_AGENT
        self.user = requests.Session()

    def upload_file(self, file_path: str):
        """上传单个图片
        @param file_path: 本地文件路径
        @return: 服务器文件路径
        """
        upload_url = self.base_url + '/api/upload'
        p = {'type': '1'}
        file_name = file_path.split('/')[-1]
        f = [('file', (file_name, open(file_path, 'rb'), 'image/jpeg'))]
        header = {
            'Authorization': self.auth,
            'Cookie': self.cookie,
            'User-Agent': self.user_agent,
        }
        res = self.user.post(upload_url, headers=header, data=p, files=f)
        # _print(res.json()['link'])
        return res.json()['link']

    def save_product(self, store_name: str, keyword: str, image: str, slider_image: list, description: str, price: str):
        """创建商品
        @param store_name: 商品名称
        @param keyword: 商品关键字
        @param image: 商品封面图
        @param slider_image: 商品轮播图
        @param description: 商品详情
        @param price: 商品价格
        """
        payload = json.dumps({
            "imageArr": [],
            "sliderImageArr": [],
            "store_name": store_name,
            "cate_id": 24,
            "keyword": keyword,
            "unit_name": "辆",
            "store_info": "",
            "image": image,
            "slider_image": slider_image,
            "description": "<p>%s </p>" % description,
            "ficti": 0,
            "give_integral": 0,
            "sort": 0,
            "is_show": 1,
            "is_hot": 1,
            "is_benefit": 1,
            "is_best": 1,
            "is_new": 1,
            "is_good": 0,
            "is_postage": 0,
            "is_sub": 0,
            "is_integral": 0,
            "id": 0,
            "spec_type": 0,
            "temp_id": 37,
            "attrs": [
                {
                    "imageArr": [],
                    "pic": image,
                    "price": price,
                    "cost": price,
                    "ot_price": price,
                    "stock": "1",
                    "seckill_stock": 0,
                    "seckill_price": 0,
                    "pink_stock": 0,
                    "pink_price": 0,
                    "bar_code": "0",
                    "weight": 0,
                    "volume": 0,
                    "brokerage": 0,
                    "brokerage_two": 0,
                    "integral": 0
                }
            ],
            "items": [],
            "header": [],
            "selectRule": ""
        })
        save_url = self.base_url + '/api/yxStoreProduct/addOrSave'
        header = {
            'Authorization': self.auth,
            'Cookie': self.cookie,
            'User-Agent': self.user_agent,
            'Content-Type': 'application/json',
        }
        res = self.user.post(save_url, headers=header, data=payload)
        if res.status_code == 201:
            _print("商品创建成功: {}".format(store_name))


class YiYiCarRun:
    """执行壹壹车商品批量上传脚本"""

    @staticmethod
    def run_to_create_products():
        """从excel提取商品信息并创建商品"""
        excel = ExcelHandler('/Users/haauleon/陈巧伦-工作交接/code/bringbuys-python/壹壹车/productTemplate.xlsx')
        e = excel.get_row_value()
        yyc = YiYiCar()
        while True:
            # 获取商品数据
            store_name, keyword, image_loc, slider_image, description, price = next(e)
            try:
                new_slider_images = list()
                for file_path in slider_image.split('|'):
                    # 上传图片至服务器
                    img_path = yyc.upload_file('/Users/haauleon/陈巧伦-工作交接/code/bringbuys-python/壹壹车' + file_path)
                    # 组装商品轮播图
                    new_slider_images.append(img_path)
                # 设置商品封面图
                image = new_slider_images[image_loc-1]
                # 上传商品
                yyc.save_product(store_name, keyword, image, new_slider_images, description, price)
            except:
                # 可能存在图片不存在等异常
                error("商品创建失败: {}".format(store_name))


if __name__ == '__main__':
    YiYiCarRun.run_to_create_products()
```