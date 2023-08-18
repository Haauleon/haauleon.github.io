---
layout:        post
title:         "影刀RPA | 自定义窗体捕获失败语法糖"
subtitle:      "在桌面软件自动化作业时，遇到应用奔溃或者卡顿时可使用装饰器进行异常重试处理"
author:        "Haauleon"
header-img:    "img/in-post/post-rpa/bg.jpg"
header-mask:   0.4
catalog:       true
tags:
    - 影刀RPA
    - Python
---

### 一、背景
&emsp;&emsp;一般来说，使用RPA在进行桌面软件自动化操作时，通常需要捕获到当前作业的窗体来供程序识别需要在哪个窗口进行自动化操作。而有个问题是，如果有大批量的操作时，就会造成窗口卡顿甚至应用奔溃，在卡顿无响应和奔溃时，如果没有做异常处理和异常重试，程序就会停止运行。        

<br>
<br>

### 二、需求
&emsp;&emsp;自定义装饰器，然后使用装饰需要借助于该窗体的自动化操作（函数或者类方法），在卡顿无响应和奔溃时，能实现窗体捕获异常/失败重试的效果，如果捕获 5 次之后还失败，就抛出异常给外层的程序进行处理。      

<br>
<br>

### 三、实现

- 自定义窗口元素
- 自定义装饰器
- 装饰函数/类方法
- 最终执行效果

<br>

#### 1、自定义窗口元素
元素库 > 捕获新元素      

![](\img\in-post\post-rpa\2023-08-18-yingdao-decorator-1.png)        

<br>
<br>

#### 2、自定义装饰器
实现装饰器 check_windows         

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


def check_windows(func):
    def inner(self):
        for retry_time in range(1, 6):
            """窗体获取/等待失败重试"""
            try:
                # 窗体等待
                # win_wait_result = xbot_visual.win32.element.wait(window="0", element=package.selector("客户端_yonyou U8"), state="appear", iswait=True, timeout="20")
                # 窗体获取/激活
                u8_window = xbot_visual.win32.window.get(window_type="window_selector", selector=package.selector("客户端_yonyou U8"), handle_checked=False, use_wildcard=False)
                break
            except Exception as e:
                if retry_time == 5:
                    raise e
                else:
                    xbot_visual.programing.log(type='info', text=f'激活 客户端_yonyou U8 窗体失败重试第{retry_time}次')
                time.sleep(10)
        return func(self, u8_window)
    return inner

```

<br>
<br>

#### 3、装饰函数/类方法
在类方法中使用装饰器      

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
from . import exception
from . import decorator


class OrderPage:

    @decorator.logger_print("点击进入销售订单列表页面")
    @decorator.check_windows
    def goto_check_page(self, u8_window):
        return xbot_visual.image.click(window_kind="screen", window=u8_window, template_images=[package.image_selector("u8_销售订单列表")], anchor_type="center", sudoku_part="MiddleCenter", offset_x="0", offset_y="0", clicks="click", button="left", keys="null", move_mouse=True, timeout="20", delay_after="3")

    @decorator.logger_print("是否进入销售订单列表页面")
    @decorator.check_windows
    def is_goto_success(self, u8_window):
        is_success = False
        if xbot_visual.image.exist(window_kind="screen", window=u8_window, exist_mode="exist", template_images=[package.image_selector("销售订单列表-同步订单待审核按钮")], is_find_all_images=False):
            is_success = True
        return is_success


def main(arg):
    # 进入销售订单列表页面
    order = OrderPage()
    order.goto_check_page()
    while True:
        try:
            if order.is_goto_success():
                break
            time.sleep(1)
        except xbot.errors.UIAError:
            break
        except Exception as e:
            xbot_visual.programing.log(type='info', text=e)

```

<br>
<br>

#### 4、最终执行效果

![](\img\in-post\post-rpa\2023-08-18-yingdao-decorator-2.png)        