---
layout:        post
title:         "Newman | 接口自动化测试"
subtitle:      "基于 Newman + 钉钉 outgoing 实现接口自动化测试及预警"
date:          2021-04-16
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - API 测试
    - Python
    - Newman
    - Postman
---

## 前言
&emsp;&emsp;Newman 结合 Jenkins 在定时构建接口自动化测试任务方面已经有了良好的表现，目前也已经成功应用到工作中。本文要说到的实现接口自动化的方式，不适用于 crontab 定时任务自动执行。经验证，crontab 任务系统无法执行 newman 命令行，即使我已经加了 newman.js 的绝对路径，还是无法执行。所以，这种方式仅适用于在本地终端手动输入 `$ python3 xxx.py` 来临时指定环境变量来跑一遍脚本，看看自己写的脚本有没有问题这一类不具备定时执行的场景。         

&emsp;&emsp;这个 python 脚本只是一个 demo，优化的空间还很大，在这里简单记录一下脚本实现的功能。              

<br><br>

## demo 代码
```python
#!/usr/local/bin/python3 python3
# -*- coding:utf-8 -*-
import requests,json
# from utils.traceback_error import traceback_error
from functools import wraps
import os
import sys
import time
from lxml import etree
import socket


def traceback_error(func):
    @wraps(func)
    def wraper(self, *args, **kwargs):
        try:
            result = func(self,*args, **kwargs)
        except Exception as e:
            import traceback
            ex_msg = '{exception}'.format(exception=traceback.format_exc())
            print(ex_msg)
            result=ex_msg
        return result
    return wraper

'''钉钉发送通知方法'''
class dingding_notice():

    def __init__(self, ding_token=None, atMobiles=None, isAtAll=None):
        # 根据电话@用户
        self.atMobiles = ['xxxxxxxx',] if atMobiles==None else atMobiles
        # self.token = 'cbb3b771657ef' if ding_token==None else ding_token
        # 是否@所有人
        self.isAtAll = True if isAtAll==None else isAtAll
        self.token = 'xxxxxx'
        self.api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(self.token)
        self.headers = {'Content-Type': 'application/json;charset=utf-8'}

    @traceback_error
    def send_msg(self,content):
        msg = {
            'msgtype': 'text',
            'text': {'content': content},
            'at': {'atMobiles': self.atMobiles, 'isAtAll': self.isAtAll}
        }
        data = requests.post(self.api, data=json.dumps(msg), headers=self.headers).json()
        return json.dumps(data)

'''执行接口自动化测试'''
class RunCollection():

    def __init__(self, test_type, testdir, report_name):
        self.test_type = test_type
        self.testdir = testdir
        self.report_name = report_name
    
    def run_collection(self):
        # 本地终端运行时不需要指定 newman.js 的环境路径
        command = "newman run {base}/saas-collection.json" \
                  "-e {base}/saas-env-{type}.json"    \
                  "-g {base}/saas-globals.json"            \
                  "--reporters html --reporter-html-export {report}".format(base=self.testdir, type=self.test_type, report=self.report_name)
        # subprocess.call(command, shell=True) # 功能同 os.popen()
        pipeline = os.popen("command")
        pipeline.read()
        with open (self.report_name, 'r', encoding="utf-8") as htmlf:
            htmlt = htmlf.read()
        html = etree.HTML(htmlt)
        fail_count = int(html.xpath("/html/body/div/div[1]/div[35]/strong/text()")[0])
        return fail_count


if __name__ == '__main__':
    try:
        service = dingding_notice()
        testdir = sys.path[0]
        test_type = input("请输入测试类型: ") # test or online  有两套环境变量
        # report_name = "%s/saas_%s_report.html" %(testdir,test_type)
        report_name = "/Library/WebServer/Documents/saas_%s_report.html" %test_type # 启动本地 Apache 服务后同一局域网的其他机器均可访问
        test = RunCollection(test_type, testdir, report_name)
        test_res = test.run_collection()
        if test_res:
            content = "项目运行环境: saas-%s \n" \
                      "接口异常数量: %s \n" \
                      "测试报告路径: %s" %(test_type, test_res, report_name)
            result = service.send_msg(content=content) # 发送钉钉消息
            print(result)
        else:
            print("saas-%s 接口测试执行完成且无任何异常" %test_type)
    except Exception as e:
        import traceback
        ex_msg = '{exception}'.format(exception=traceback.format_exc())
        print(ex_msg)
```