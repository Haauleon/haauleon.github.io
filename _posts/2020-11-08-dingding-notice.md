---
layout: post
title: "报警 | 钉钉报警机器人"
subtitle: "我心目中的潮流之选"
author: "Haauleon"
header-style: text
tags:
    - API 测试
    - Python
    - Newman
    - Postman
---

## 背景
&emsp;&emsp;一直都觉得使用邮件做报警提示或者消息推送实在太 low 了，别说是邮件了，邮箱我都讨厌打开，一堆乱七八糟的广告推送，太烦了。而且我又属于能少打开一个就少打开一个页面的那种人。    
&emsp;&emsp;后来考虑了使用短信推送、电话推送，但因为种种难题（亦或是要收钱）就放弃了。刚在 OT 的时候浏览到一个好东西~也就是使用钉钉机器人作为报警提示。有几个好处，一就是现在的打工人是人手一个钉钉，二来就是这玩意的效果跟群聊差不多。总之，这玩意也挺好玩的，先送上效果图。     

![](\img\in-post\post-postman\2020-11-08-dingding-notice-1.jpg)  

<br><br>

## 自定义钉钉机器人
附上[钉钉开发文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq)

<br><br>

## 代码
```python
# -*- coding:utf-8 -*-
import requests,json
# from utils.traceback_error import traceback_error
from functools import wraps


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
        self.atMobiles = ['139',] if atMobiles==None else atMobiles
        # self.token = 'cbb3b771657ef' if ding_token==None else ding_token
        # 是否@所有人
        self.isAtAll = True if isAtAll==None else isAtAll
        self.token = '保密'
        self.api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(self.token)
        self.headers = {'Content-Type': 'application/json;charset=utf-8'}

    # 钉钉报警
    @traceback_error
    def send_msg(self,content):
        msg = {
            'msgtype': 'text',
            'text': {'content': content},
            'at': {'atMobiles': self.atMobiles, 'isAtAll': self.isAtAll}
        }
        data = requests.post(self.api, data=json.dumps(msg), headers=self.headers).json()
        return json.dumps(data)


if __name__ == '__main__':
    try:
        service=dingding_notice()
        error_list = "host:{}\napi:{}\nstatus_code:{}\nres_msg:{}\n".format("xxxxx.com", "/user/login", "200", "请求成功")
        content='起火了起火了，接口请求报错了，接口请求失败了！\n\n'+error_list
        result=service.send_msg(content=content)
        print(result)
    except Exception as e:
        import traceback
        ex_msg = '{exception}'.format(exception=traceback.format_exc())
        print(ex_msg)
```