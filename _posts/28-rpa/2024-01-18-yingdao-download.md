---
layout:        post
title:         "影刀RPA | 文件下载"
subtitle:      "开发 python 脚本实现文件下载并返回文件存放的本地路径"
author:        "Haauleon"
header-img:    "img/in-post/post-rpa/bg.jpg"
header-mask:   0.4
catalog:       true
tags:
    - 影刀RPA
    - Python
---

### 实现代码
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


# 全局变量
SAVE_PATH = glv['IMAGE_FOLDER']


def image_download(image_url):
    """网络图片下载至本地并返回图片存放的绝对路径"""
    image_path = xbot_visual.web_service.download(url=image_url, save_folder=SAVE_PATH, custom_filename=False, save_filename=None, wait_complete_timeout="3000", connect_timeout_seconds="3000", send_by_web=False, browser=None)
    # xbot_visual.programing.log(type="info", text=f"图片已成功下载至 >>> {image_path}")
    return image_path


def main(args):
    image_download("https://m.media-amazon.com/images/I/71ol0jPDlOS.jpg")

```        
