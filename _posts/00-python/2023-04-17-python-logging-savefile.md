---
layout:        post
title:         "Python3 | python 中 的 logging 模块"
subtitle:      "使用 logging 模块将日志保存到文件中"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### logging 模块的使用
相关链接：    
[python中的logging模块——将日志保存到文件中](https://blog.csdn.net/scp_6453/article/details/126218810)      

<br>
<br>

```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   log.py 
@Date    :   2023/4/12 11:16
@Function:   日志类

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2023/4/12 11:16         haauleon         1.0           None
"""
import sys
import logging.handlers
from colorama import Fore, Style
from common.setting import ConfigHandler
from utils.timesUtils.timeControl import get_now_time


log_path = ConfigHandler.log_path
# 创建一个Logger，并设置日志级别
_logger = logging.getLogger('spider')
_logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件，并设置日志级别
fh = logging.FileHandler(filename=log_path+f'{get_now_time()}.log', encoding='utf-8', mode='w')
fh.setLevel(logging.DEBUG)
# 创建一个handler，用于将日志输出到控制台，并设置日志级别
_handler = logging.StreamHandler(sys.stdout)
_handler.setLevel(logging.DEBUG)
# 分别定义fh和_handler的输出格式
fh.setFormatter(logging.Formatter("%(asctime)s [%(threadName)s:%(thread)d] %(name)s - %(message)s"))
_handler.setFormatter(logging.Formatter("%(asctime)s [%(threadName)s:%(thread)d] %(name)s - %(message)s"))
# 给logger添加handler
_logger.addHandler(_handler)
_logger.addHandler(fh)


class Logger:
    """
    日志类封装
    """

    @staticmethod
    def debug(msg):
        _logger.debug("[DEBUG] " + str(msg))

    @staticmethod
    def info(msg):
        _logger.info(Fore.GREEN + "[INFO] " + str(msg) + Style.RESET_ALL)

    @staticmethod
    def error(msg):
        _logger.error(Fore.RED + "[ERROR] " + str(msg) + Style.RESET_ALL)

    @staticmethod
    def warn(msg):
        _logger.warning(Fore.YELLOW + "[WARNING] " + str(msg) + Style.RESET_ALL)

    @staticmethod
    def print(msg):
        _logger.debug(Fore.BLUE + "[PRINT] " + str(msg) + Style.RESET_ALL)

    @staticmethod
    def set_level(level):
        """ 设置log级别

        :param level: logging.DEBUG, logging.INFO, logging.WARN, logging.ERROR
        :return:
        """
        _logger.setLevel(level)

    @staticmethod
    def set_level_to_debug():
        _logger.setLevel(logging.DEBUG)

    @staticmethod
    def set_level_to_info():
        _logger.setLevel(logging.INFO)

    @staticmethod
    def set_level_to_warn():
        _logger.setLevel(logging.WARN)

    @staticmethod
    def set_level_to_error():
        _logger.setLevel(logging.ERROR)
```