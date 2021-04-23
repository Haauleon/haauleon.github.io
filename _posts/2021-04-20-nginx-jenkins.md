---
layout:        post
title:         "Jenkins | 多命令行持续集成"
subtitle:      "Jenkins + Newman + Nodejs + python3 + Nginx 实现自动化测试"
date:          2021-04-19
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Nginx
    - Jenkins
    - Nodejs
    - Python
    - Newman
    - Postman
    - API 测试
---

## Ⅰ 背景
目前已实现的 jenkins 持续集成如下：       
* 使用 jenkins 定时构建自动化测试      
* 使用 postman + newman 执行自动化测试并生成测试报告       
* 使用 python3 脚本对测试报告进行解析，若接口异常数不为 0 则发送钉钉消息      
* 使用 nodejs 工具包 publish-sftp 自动上传测试报告至阿里云服务器，可远程访问测试报告       

<br><br>

## Ⅱ 测试目录结构分析
![](\haauleon\img\in-post\post-jenkins\2021-04-20-nginx-jenkins-1.png)

<br><br>

## Ⅲ Jenkins 配置信息     
###### 一、定时构建
&emsp;&emsp;当前定时构建的日程表为 `H/10 * * * *`，即为每十分钟执行一次。          

![](\haauleon\img\in-post\post-jenkins\2021-04-20-nginx-jenkins-2.jpg)

<br><br>

###### 二、构建内容
&emsp;&emsp;Jenkins 的构建内容的填写：由于是使用本地的解释器、工具包，因此均需要指定环境路径。若不想使用环境路径，则需要在 Jenkins 服务器中安装环境即可。         

![](\haauleon\img\in-post\post-jenkins\2021-04-20-nginx-jenkins-3.png)                    
<br>

```
# newman 自动化测试并生成测试报告
/usr/local/lib/node_modules/newman/bin/newman.js run /Users/haauleon/PythonTest/jsonRequest/saas/saas-collection.json -e /Users/haauleon/PythonTest/jsonRequest/saas/saas-env-online.json -g /Users/haauleon/PythonTest/jsonRequest/saas/saas-globals.json --reporters html --reporter-html-export /Users/haauleon/PythonTest/jsonRequest/report/saas_online_report.html

# python3 解析测试报告并发送钉钉消息预警
/usr/local/bin/python3 /Users/haauleon/PythonTest/jsonRequest/saas/online_notice.py

# 进入报告所在目录 (新建的 sftp.json 配置文件在此 report 目录，目前只能有一个配置文件，两个配置文件的我还没试过，估计会报错)
cd /Users/haauleon/PythonTest/jsonRequest/report

# 上传文件至服务器
/usr/local/lib/node_modules/publish-sftp/index.js -c
```

<br><br>

## Ⅳ Jenkins 构建内容分析
###### 一、Newman 自动化测试
&emsp;&emsp;在 Postman 上调试通过之后，下载 **环境变量文件**、**全局变量文件**、**测试集合文件** 至本地，通过 Newman 命令行执行自动化测试并生成测试报告。可指定测试报告生成的路径。         
&emsp;&emsp;下面通过 json 格式来描述我从 Postman 导出的文件路径和自定义的测试报告路径。         
```json
{
    "测试集合文件": "/Users/haauleon/PythonTest/jsonRequest/saas/saas-collection.json",
    "环境变量文件": "/Users/haauleon/PythonTest/jsonRequest/saas/saas-env-online.json",
    "全局变量文件": "/Users/haauleon/PythonTest/jsonRequest/saas/saas-globals.json",
    "测试报告路径": "/Users/haauleon/PythonTest/jsonRequest/report/saas_online_report.html"
}
```
<br>

&emsp;&emsp;然后使用 newman 命令行进行自动化测试。         
**格式**：      
```
$ newman run "测试集合文件" -e "环境变量文件" -g "全局变量文件" -reportershtml --reporter-html-export "测试报告路径"
```    
<br>

**实例**：
&emsp;&emsp;在 Jenkins 服务器上使用本地的解释器或者 nodejs 工具，需要指定环境路径，我这里的路径是 `/usr/local/lib/node_modules/newman/bin/newman.js`。                  
```
/usr/local/lib/node_modules/newman/bin/newman.js run /Users/haauleon/PythonTest/jsonRequest/saas/saas-collection.json -e /Users/haauleon/PythonTest/jsonRequest/saas/saas-env-online.json -g /Users/haauleon/PythonTest/jsonRequest/saas/saas-globals.json --reporters html --reporter-html-export /Users/haauleon/PythonTest/jsonRequest/report/saas_online_report.html
```

<br><br>

###### 二、Python3 解析测试报告
&emsp;&emsp;写 python3 脚本解析 html 测试报告，若接口数量数量不为 0 则使用 outgoing 向钉钉群组发送消息。            
&emsp;&emsp;由 newman 生成的测试报告样式如下：       
![](\haauleon\img\in-post\post-jenkins\2021-04-20-nginx-jenkins-4.png)

**消息模板如下**:                   
```
项目运行环境: saas生产环境
接口异常数量: 4
测试报告路径: http://112.74.205.108/saas_online_report.html
```
<br><br>

**具体脚本如下**:        
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
        self.isAtAll = True if isAtAll==None else isAtAll
        self.token = '3433c13a652fe25fd6ae796bffd00eab47ab8b9a26cd734c20d34fdfec641d97'
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


if __name__ == '__main__':
    try:
        service = dingding_notice()
        testdir = sys.path[0]
        # command_url = "/usr/local/lib/node_modules/newman/bin/newman.js run {base}/saas-collection.json -e {base}/saas-env-online.json -g {base}/saas-globals.json --reporters html --reporter-html-export {base}/saas_online_report.html".format(base=testdir)
        # print(command_url)
        # pipeline = os.popen(command_url)
        # pipeline.read()
        report_name = '%s/saas_online_report.html' %testdir
        with open (report_name, 'r', encoding="utf-8") as htmlf:
            htmlt = htmlf.read()
        html = etree.HTML(htmlt)
        fail_count = int(html.xpath("/html/body/div/div[1]/div[35]/strong/text()")[0])  # 提取测试报告中断言失败数量字段的值。
        if fail_count:
            content = "项目运行环境: saas生产环境 \n"      \
                      "接口异常数量: %s \n"               \
                      "测试报告路径: %s" %(fail_count,"http://112.74.205.108/saas_online_report.html")
            result=service.send_msg(content=content)
            print(result)
        else:
            print("saas生产环境接口测试执行完成且无任何异常")
    except Exception as e:
        import traceback
        ex_msg = '{exception}'.format(exception=traceback.format_exc())
        print(ex_msg)
```

<br><br>

###### 三、上传文件至服务器
&emsp;&emsp;使用 nodejs 工具包 sftp-publish 将本地文件自动上传至阿里云服务器。sftp.json 文件配置如下：      

```json
{
    "localPath": "./",
    "remotePath": "/usr/test-haauleon",
    "protectedRemotePath": "/usr/test-haauleon",
    "connect": {
        "host": "112.74.205.108",
        "port": 22,
        "username": "root",
        "password": "服务器root密码"
    }
}
```

<br>

&emsp;&emsp;使用该工具时，需要 cd 进入到配置文件 sftp.json 所在的 report 目录，然后使用命令行进行文件上传。若不指定配置文件所在的目录，则命令执行失败且会提示在 xxxxx 目录下找不到 sftp.json 文件。        

```
# 进入报告所在目录（由于我将配置文件放在 report 目录下，所以需要先进入 sftp.json 配置文件所在的目录。否则会报错，提示此配置文件在 report 目录找不到）
cd /Users/haauleon/PythonTest/jsonRequest/report

# 使用命令行上传文件至服务器（在 Jenkins 服务器使用本地环境的 nodejs 包，需要指定环境路径）
/usr/local/lib/node_modules/publish-sftp/index.js -c
```

<br><br>

## 结论
&emsp;&emsp;愉快的构建，省了很多麻烦。