---
layout:        post
title:         "python3 | 批量执行 postman 请求集合"
subtitle:      "使用 python 解析 postman 的 json 文件并批量发送请求"
author:        "Haauleon"
header-img:    "img/in-post/post-postman/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
  - Python
  - Postman
---

目前的思路如下：        
1. 把 postman 的请求集合文件、环境变量文件、全局变量文件全部下载到本地，分别存为 `xxx.collection.json`、`xxx.env.json` 和 `xxx.globals.json`     
2. 写脚本解析 `xxx.collection.json` 文件的请求，并使用 requests 发送请求。解析 `xxx.env.json` 文件的环境变量，读写并解析 `xxx.globals.json` 文件的全局变量            
3. 脚本放到 linux 服务器上去执行，我的是 ubuntu      

<br>

```python
import sys
import requests
import json
import time
import logging
from functools import wraps
from colorama import Fore, Style


# 日志配置
_logger = logging.getLogger('postman-test')     # 获取日志记录器
_logger.setLevel(logging.DEBUG)                 # 设置日志等级
_handler = logging.StreamHandler(sys.stdout)    # 输入到控制台的 handler
_logger.addHandler(_handler)     

def info(msg):
    '''日志函数'''
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


class DingDingNotice:
    '''钉钉发送类'''

    def __init__(self, ding_token=None, atMobiles=None, isAtAll=None):
        # 根据电话@用户
        self.atMobiles = ['13046367204',] if atMobiles==None else atMobiles
        # self.token = 'cbb3b771657ef' if ding_token==None else ding_token
        # 是否@所有人
        self.isAtAll = True if isAtAll==None else isAtAll
        self.token = 'xxxxxxxxxxx'  # 钉钉群机器人token
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


user = requests.Session()
with open(sys.argv[1]) as f:
    '''从命令行获取测试数据 xxx.collection.json(定时任务需要指定绝对路径)'''
    test_data = json.load(f)


class JsonRunner:
    '''测试执行'''
    def __init__(self):
        self.name = None
        self.url = None
        self.method = None
        self.headers = None
        self.data = None
        self.res = None
        self.success = None

    def run(self):
        '''测试执行'''
        for req in test_data['item']:
            self.url = req['request']['url']['raw']
            self.method = req['request']['method']
            self.headers = dict()
            self.name = req['name']
            # _print(self.name)
            # _print(self.url)
            # _print(self.method)

            if req['request']['header']:
                for self.header in req['request']['header']:
                    # print('{}: {}'.format(header['key'], header['value']))
                    self.headers[self.header['key']] = self.header['value']
            # print("headers: ", headers)

            if self.method == 'POST':
                if req['request']['body']['mode'] == 'raw':
                    self.data = req['request']['body']['raw']
                    # print("body: ", data)
                    self.res = user.post(self.url, headers=self.headers, data=self.data)
                    # success = res.json()["success"]

                elif req['request']['body']['mode'] == 'urlencoded':
                    self.data = dict()
                    if req['request']['body']['urlencoded']:
                        for param in req['request']['body']['urlencoded']:
                            self.data[param['key']] = param['value']
                    # print("data: ", data)
                    self.res = user.post(self.url, headers=self.headers, data=self.data)
                    # success = res.json()["success"]
            elif self.method == 'GET':
                self.res = user.get(self.url, headers=self.headers)
                # success = res.json()["success"]

            # print("success: ", self.success)
            # print("data: ", self.data)
            # print("headers: ", self.headers)
            # print("\n")

            if '.html' in self.url:
                pass
            else:
                # self.success = self.res.json()["success"]
                yield self.res.status_code


def run():
    runner = JsonRunner()
    r = runner.run()
    dingding_msg = []
    while True:
        try:
            runner.status_code = next(r)
            if runner.status_code == 200 and '"success":true' in runner.res.text:
                info("测试通过 >>>>>> {}   {}   {}".format(runner.name, runner.url, runner.method))
            else:
                error("测试失败 >>>>>> {}   {}   {}".format(runner.name, runner.url, runner.method))
                fail_msg = '异常接口: {}\n响应状态: {}\n响应数据: {}'.format(runner.url, runner.status_code, runner.res.text)
                dingding_msg.append(fail_msg)

        except StopIteration:
            _print("测试结束")
            break

    if dingding_msg:
        dingding_msg = '跨境说服务监控温馨提醒您：\n\n' + '\n\n'.join(dingding_msg)
        service = DingDingNotice()
        service.send_msg(content=dingding_msg)
        _print("钉钉消息发送成功")        


if __name__ == '__main__':
    run()
    _print("脚本执行完成")
```