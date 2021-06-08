---
layout: post
title: "钉钉 | 业务报警脚本"
subtitle: "python + node + newman + dingtalk + crontab"
author: "Haauleon"
header-style: text
tags:
  - API 测试
  - Python
  - Newman
  - Postman
---


## 背景
&emsp;&emsp;最近接盘了绿松石爬虫项目代码，换句话说，我除了要搞自己手头的工作，同时还得维护爬虫代码。记得刚接手的第一天就出现了个异常，原因是爬的百度指数接口返回的数据格式改变了，但是这边的脚本没有更新，导致迟迟没有往数据库插数据，然后后端接口由于读不到数据于是抛了个空指针异常。也就是这么一个多变的爬虫环境，既想维护他而同时又想搞自己的事情。怎么办呢？        
<br><br><br>

## 需求
&emsp;&emsp;想写一个脚本，这个脚本作为我的第三只眼睛，专门盯着绿松石那些接口，最好每隔一个小时就去请求这些业务接口，若接口有异常，就往我的钉钉发送通知并提醒钉钉群里的每个人，这样的话我就可以留意到接口有异常，然后我还可以打开此接口测试报告看看是哪些接口有异常。预警功能写到这里就可以了，后面的异常排查再由我人工进行即可。       
<br><br><br>

## 验收标准
&emsp;&emsp;目前可以简单实现需求功能即可，后面再优化。     
<br><br><br>

## 功能实现
**一、环境准备**      
1. 操作系统：MacOS    
2. 语言版本：python37   
3. 辅助工具：Postman     
<br><br>

**二、环境准备**      
1. 下载安装基于 MacOS 的 nodejs 安装包。点击[链接](https://npm.taobao.org/mirrors/node/v14.16.0/node-v14.16.0.pkg)进行下载安装。        
2. 安装脚本运行依赖工具    
    * 使用 newman 来运行由 postman 生成的测试脚本        
    `$ sudo npm install -g newman`     
    * 使用 newman-reporter-html 来生成测试报告    
    `$ sudo npm install -g newman-reporter-html`     
    * 使用 requests 模块来向钉钉群组发送消息    
    `$ pip install requests`      
    * 使用 lxml 模块来定位测试报告 html 元素      
    `$ pip install lxml`       
3. 添加钉钉机器人并获取 token 值。参考[钉钉开发文档](https://developers.dingtalk.com/document/app/custom-robot-access)        

<br><br>

**三、数据准备**       
使用 postman 生成接口自动化测试脚本（需要在 tests 里面写上断言）    
  * 下载接口测试脚本集合文件     
  * 下载脚本所需的环境变量文件    
  * 下载脚本所需的全局变量文件     
<br><br>

**四、脚本功能**       
&emsp;&emsp;使用 traceback 模块来跟踪异常返回信息。    
```python
def traceback_error(func):
    @wraps(func)
    def wraper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
        except Exception as e:
            import traceback
            ex_msg = '{exception}'.format(exception=traceback.format_exc())
            print(ex_msg)
            result=ex_msg
        return result
    return wraper
```
<br><br>

&emsp;&emsp;自定义一个类，用 outgoing 机器人向钉钉群组发送消息。可发送的数据格式需要查看钉钉开发文档，这里仅定义了一种数据格式及文本。       

```python
class dingding_notice():
    '''钉钉发送消息方法'''
    def __init__(self,ding_token=None,atMobiles=None,isAtAll=None):
        # 根据手机号码@用户
        self.atMobiles = ['13976062467',] if atMobiles==None else atMobiles
        # self.token = 'cbb3b771657ef' if ding_token==None else ding_token
        # 是否@所有人
        self.isAtAll = True if isAtAll==None else isAtAll
        # 根据钉钉文档新增机器人并获取 token 值
        self.token = '...'
        self.api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(self.token)
        self.headers = {'Content-Type': 'application/json;charset=utf-8'}

    # 钉钉报警
    @traceback_error
    def send_msg(self,content):
        '''定义发送的数据格式'''
        msg = {
            'msgtype': 'text',
            'text': {'content': content},
            'at': {'atMobiles': self.atMobiles, 'isAtAll': self.isAtAll}
        }
        data = requests.post(self.api, data=json.dumps(msg), headers=self.headers).json()
        return json.dumps(data)
```
<br><br>

&emsp;&emsp;使用`os.popen()`方法会打开一个管道，返回结果是一个连接管道的文件对象，该文件对象的操作方法同`open()`，可以从该文件对象中读取返回结果。如果执行成功，不会返回状态码，如果执行失败，则会返回错误信息。类似于使用`open()`内置函数返回一个`_io.TextIOWrapper`对象，可对此对象进行读操作。在 Unix，Windows 中有效。       
```python
>>> a = open('demo.txt', 'r')
>>> type(a)
<class '_io.TextIOWrapper'>
```
<br>

```python
pipeline = os.popen("newman run 接口测试集合的路径 -e 环境变量文件的路径 --reporters html --reporter-html-export 自定义生成的测试报告路径")
# 读取文件内容，如果能成功读取，说明命令执行成功
pipeline.read()
```
<br><br>

&emsp;&emsp;打开测试报告文件，`etree.HTML`构建 DOM 节点后，可使用 xpath 表达式来定位元素并打印。  
```python
with open('测试报告路径', 'r', encoding="utf-8") as htmlf:
    htmlt = htmlf.read()
html = etree.HTML(htmlt)
fail_count = int(html.xpath("/html/body/div/div[1]/div[35]/strong/text()")[0])
print("fail_count: %i" %fail_count)
```
<br><br>

&emsp;&emsp;MacOS 系统的 crontab 跟真正的 Linux 系统还是有区别的，MacOS 要用 launchctl 来启动定时任务。可参考[在 Mac 上使用 crontab 服务](https://cloud.tencent.com/developer/article/1330768)和[其他问题解决方法](https://www.jianshu.com/p/e2995b3a0b53)。
<br><br><br>

## 脚本代码    
```python
#!/usr/local/bin/python3 python3
# -*- coding:utf-8 -*-
import requests,json
# from utils.traceback_error import traceback_error
from functools import wraps
import os
import time
from lxml import etree


def traceback_error(func):
    @wraps(func)
    def wraper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
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
        self.isAtAll = True if isAtAll==None else isAtAll
        # 根据钉钉文档新增机器人并获取 token 值
        self.token = '...'
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
        service = dingding_notice()
        pipeline = os.popen("newman run 接口测试集合的路径 -e 环境变量文件的路径 --reporters html --reporter-html-export 自定义生成的测试报告路径")
        # 读取文件内容，如果能成功读取，说明命令执行成功
        pipeline.read()
        with open('测试报告路径', 'r', encoding="utf-8") as htmlf:
            htmlt = htmlf.read()
        html = etree.HTML(htmlt)
        fail_count = int(html.xpath("/html/body/div/div[1]/div[35]/strong/text()")[0])
        print("fail_count: %i" %fail_count)
        if fail_count:
            content = "绿松石异常接口数量： %s" %fail_count
            result=service.send_msg(content=content)
            print(result)
        else:
            pass
    except Exception as e:
        import traceback
        ex_msg = '{exception}'.format(exception=traceback.format_exc())
        print(ex_msg)
```