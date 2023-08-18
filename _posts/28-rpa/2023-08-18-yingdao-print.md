---
layout:        post
title:         "影刀RPA | 自定义日志打印装饰器"
subtitle:      "在某个类方法开始执行时就打印此方法的操作内容，原生的语句太长太冗余了，使用语法糖免去了注释和打印语句"
author:        "Haauleon"
header-img:    "img/in-post/post-rpa/bg.jpg"
header-mask:   0.4
catalog:       true
tags:
    - 影刀RPA
---

### 一、背景
&emsp;&emsp;原生的影刀 RPA 的打印语句太长了，每次打印就要调用一次，而且还需要额外增加注释和打印语句。     


<br>
<br>

### 二、需求
&emsp;&emsp;自定义装饰器，实现在某个类方法进行自动化操作前就打印该操作的内容，使用语法糖进行装饰，比较美观而且实用。    

<br>
<br>

### 三、实现

- 自定义装饰器
- 语法糖装饰类方法
- 最终执行效果

<br>

#### 1、自定义装饰器
函数嵌套的方式实现装饰器 logger_print                      

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
import time


def logger_print(text):
    def decorator(func):
        def inner(self):
            xbot_visual.programing.log(type="info", text=text)
            return func(self)
        return inner
    return decorator

```

<br>
<br>

#### 2、语法糖装饰类方法

```python
# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
import xbot_visual
from . import package
from .package import variables as glv
import time
from . import decorator


class OrderPage:

    @decorator.logger_print("点击同步订单待审核按钮筛选列表")
    @decorator.check_windows
    def goto_check_list(self, u8_window):
        return xbot_visual.image.click(window_kind="screen", window=u8_window, template_images=[package.image_selector("u8-销售订单列表-同步订单待审核")], anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", clicks="click", button="left", keys="null", move_mouse=True, timeout="5", delay_after="15")

```

<br>
<br>

#### 3、最终执行效果

![](\img\in-post\post-rpa\2023-08-18-yingdao-print-1.png)        