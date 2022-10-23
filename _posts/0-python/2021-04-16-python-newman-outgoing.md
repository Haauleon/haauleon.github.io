---
layout:        post
title:         "Newman | 接口自动化测试"
subtitle:      "基于 Newman + 钉钉 outgoing 实现接口自动化测试及预警"
date:          2021-04-16
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - Newman
    - Nodejs
    - 数据监控
---

> 增加 os.system() 上传本地文件至服务器

## 背景
&emsp;&emsp;Newman 结合 Jenkins 在定时构建接口自动化测试任务方面已经有了良好的表现，目前也已经成功应用到工作中。本文要说到的实现接口自动化的方式，不适用于 crontab 定时任务自动执行。经验证，crontab 任务系统无法执行 newman 命令行，即使我已经加了 newman.js 的绝对路径，还是无法执行。所以，这种方式仅适用于在本地终端手动输入 `$ python3 xxx.py` 来临时指定环境变量来跑一遍脚本，看看自己写的脚本有没有问题这一类不具备定时执行的场景。         

&emsp;&emsp;这个 python 脚本只是一个 demo，优化的空间还很大，在这里简单记录一下脚本实现的功能。              

<br><br>

## 测试目录接口
![](\haauleon\img\in-post\post-postman\2021-04-16-newman-outgoing-1.png)

<br><br>

## demo 代码
```python
"""
import subprocess

p = subprocess.Popen("newman run saas.postman_collection.json -e saas.postman_environment.json -g saas.postman_globals.json --reporters html --reporter-html-export report.html")
#p = subprocess.Popen("ls")
p.wait()
"""

"""
os.popen()
功能：该方法是通过调用管道的方式来实现的，在调用后会导致当前线程阻塞，直到调用的执行指令执行完毕；在调用结束后，会返回一个记录调用输出结果的 file 对象。

原型：os.popen(command [, mode, buffering])
command：调用命令
mode：返回 file 对象的模式，默认为 “r” 只读模式
buffering：缓冲区大小，默认 -1 为无限制
"""
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
import subprocess


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

    def __init__(self,ding_token=None,atMobiles=None,isAtAll=None):
        # 根据电话@用户
        self.atMobiles = ['13976062467',] if atMobiles==None else atMobiles
        # self.token = 'cbb3b771657ef' if ding_token==None else ding_token
        # 是否@所有人
        self.isAtAll = False if isAtAll==None else isAtAll
        self.token = 'xxxxxxxxxxxxxxxxxxxx8b9a26cd734c20d34fdfec641d97'
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

'''执行自动化测试'''
class RunCollection():

    def __init__(self, test_type, testdir, report_name):
        self.test_type = test_type
        self.testdir = testdir
        self.report_name = report_name
    
    def run_collection(self):
        '''执行接口测试用例'''
        # 本地终端运行不需要指定 node 包的环境路径
        # pipeline = os.popen("/usr/local/lib/node_modules/newman/bin/newman.js run {base}/saas-collection.json -e {base}/saas-env-{test_type}.json -g {base}/saas-globals.json --reporters html --reporter-html-export {base}/saas_{test_type}_report.html".format(base=self.testdir,test_type=self.test_type))
        exec_test_command = "newman run {base}/saas-collection.json " \
                            "-e {base}/saas-env-{test_type}.json "    \
                            "-g {base}/saas-globals.json "            \
                            "--reporters html --reporter-html-export {report}".format(base=self.testdir,test_type=self.test_type,report=self.report_name)
        pipeline = os.popen(exec_test_command)
        print(pipeline.read())
        with open (self.report_name, 'r', encoding="utf-8") as htmlf:
            htmlt = htmlf.read()
        html = etree.HTML(htmlt)
        fail_count = int(html.xpath("/html/body/div/div[1]/div[35]/strong/text()")[0])
        return fail_count

'''自动上传文件至服务器'''
class UploadFile():

    def exec_upload_file(self):
        # to_dir_command = "cd /Users/haauleon/PythonTest/jsonRequest/report"
        # 进入目标文件夹（目前要上传的文件夹内一定要有 sftp.json 配置文件，不然会报错）
        # subprocess.call(to_dir_command, shell=True)
        # 本地终端执行不需要执行 node 包的环境路径
        # exec_upload_command = "/usr/local/lib/node_modules/publish-sftp/index.js -c"
        # exec_upload_command = "publish-sftp -c"
        # subprocess.call(exec_upload_command, shell=True)
        # pipeline = os.popen(exec_upload_command)
        # print(pipeline.read())

        # python 在指定的目录下执行命令 >>>>> os.system('cd 指定的目录 && 执行的命令')
        os.system('cd /Users/haauleon/PythonTest/jsonRequest/report && /usr/local/lib/node_modules/publish-sftp/index.js -c')


if __name__ == '__main__':

    ip = "http://112.74.205.108"
    try:
        service = dingding_notice()
        testdir = sys.path[0]
        test_type = input("请输入测试类型: ") # test or online or lssonline  
        # report = "%s/saas_%s_report.html" %(testdir,test_type)
        report = "../report/saas_%s_report.html" %test_type
        test = RunCollection(test_type, testdir, report)
        test_res = test.run_collection()
        if test_res:
            content = "项目运行环境: saas-{type} \n" \
                      "接口异常数量: {fail} \n"      \
                      "测试报告路径: {ip}/saas_{type}_report.html".format(type=test_type,fail=test_res,ip=ip)
            result = service.send_msg(content=content)
            print(result)
        else:
            print("saas-%s 接口测试执行完成且无任何异常" %test_type)
        # upload = UploadFile()
        # upload.exec_upload_file()
        print("文件已上传至服务器，访问: \n%s/saas_%s_report.html" %(ip,test_type))
    except Exception as e:
        import traceback
        ex_msg = '{exception}'.format(exception=traceback.format_exc())
        print(ex_msg)
```