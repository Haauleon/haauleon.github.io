---
layout:        post
title:         "影刀RPA | 文件下载"
subtitle:      "操作 workbook 模块实现在 excel 文件中指定单元格填充图片"
author:        "Haauleon"
header-img:    "img/in-post/post-rpa/bg.jpg"
header-mask:   0.4
catalog:       true
tags:
    - 影刀RPA
    - Python
---

### 需求描述
&emsp;&emsp;读取 `test.xlsx` 文件的最后两列数据，通过对比，将倒数第二列的图片链接先下载到本地，然后填充到最后一列对应的单元格中。如下图所示：       
![](\img\in-post\post-rpa\2024-01-18-yingdao-workbook-1.png)        

<br>
<br>

### 代码实现
```python
# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
import xbot_visual
from xbot import print, sleep
from .import package
from .package import variables as glv
from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image
from openpyxl.drawing.spreadsheet_drawing import AnchorMarker, TwoCellAnchor


# 全局变量
SAVE_PATH = glv['IMAGE_FOLDER']


def image_download(image_url):
    """网络图片下载至本地并返回图片存放的绝对路径"""
    image_path = xbot_visual.web_service.download(url=image_url, save_folder=SAVE_PATH, custom_filename=False, save_filename=None, wait_complete_timeout="3000", connect_timeout_seconds="3000", send_by_web=False, browser=None)
    # xbot_visual.programing.log(type="info", text=f"图片已成功下载至 >>> {image_path}")
    return image_path


class WorkBookOperation:

    def __init__(self, file_path):
        self.file_path = file_path
        self.wb = None
        self.ws = None

    def open_new_excel(self):
        """新建excel"""
        self.wb = Workbook()
        self.ws = self.wb.active
        
    def open_excel(self):
        """打开已有的excel"""
        self.wb = load_workbook(self.file_path)
        self.ws = self.wb.active

    def get_sheet_data(self, min_row=2, max_row=52):
        """获取sheet表的数据"""
        # 默认获取从第二行开始的后两列数据
        # for row in self.ws.iter_rows(min_row=2, max_row=self.ws.max_row, min_col=self.ws.max_column-1, max_col=self.ws.max_column):
        index = min_row
        for row in self.ws.iter_rows(min_row=min_row, max_row=max_row, min_col=self.ws.max_column-1, max_col=self.ws.max_column):
            yield index, [cell.value for cell in row]
            index += 1

    def cell_fill_image(self, image_path, row_num=2):
        """默认在最后一列的单元格里填充图片"""
        img = Image(image_path)
        _from = AnchorMarker(self.ws.max_column-1, 50000, row_num-1, 50000)
        to = AnchorMarker(self.ws.max_column, -50000, row_num, -50000)
        img.anchor = TwoCellAnchor('twoCell', _from, to)
        self.ws.add_image(img)

    def save_excel(self):
        self.wb.save(self.file_path)

    def close_excel(self):
        self.wb.close()


def run_to_cell_fill_image(file_path):
    """单元格填充图片
    （1）将昨日正常的图片链接转成图片填充到今日变狗的单元格中
    （2）保留 "变狗" 的文字，便于表格筛选
    （3）目前只能实现图片浮动在单元格中，后续需要人工进行图片编辑
    """
    wb = WorkBookOperation(file_path)
    wb.open_excel()
    for cell_data in wb.get_sheet_data():
        print(f"第{cell_data[0]}行      昨日 >>> {cell_data[1][0]}      今日 >>> {cell_data[1][1]}")
        if cell_data[1][0] != '变狗' and cell_data[1][1] == '变狗':
            wb.cell_fill_image(image_download(cell_data[1][0]), cell_data[0])
    wb.save_excel()
    wb.close_excel()


def main(args):
    run_to_cell_fill_image(r'D:\陈巧伦-工作文档\影刀RPA\20240115亚马逊商品图片状态办公自动化统计机器人\ASIN-US-CA-DE.xlsx')

```