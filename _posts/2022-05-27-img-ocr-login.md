---
layout:        post
title:         "爬虫 | 需要图片验证码进行登录的网站"
subtitle:      "使用 ddddocr 模块进行普通图片识别"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 爬虫
    - Python
    - API 测试
    - 小而美脚本
---

### 代码简介
1. 路径配置类 ConfigHandler       
    原理：用于配置图片路径和项目目录根路径
2. 图片验证码识别类 IMGHandler     
    原理：用于识别普通图片并返回验证码, 具体情况具体分析。此模块在本地进行智能训练，偶现失误，需要自己通过多次调用判断后进行裁剪和调整。        
3. 用户登录类 UserLogin          
    原理：使用账号、密码和图片验证码进行登录, 使用 requests.Session() 保持连接状态

<br><br>

### 代码设计
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   pyppeteer_process_v3.py
@Date    :   2022-05-27 12:22
@Function:   通过账号、密码和图片验证码进行登录
说明:
1、路径配置类 ConfigHandler
2、图片验证码识别类 IMGHandler
3、用户登录类 UserLogin
"""
import requests
import os
import ddddocr


class ConfigHandler:
    _SLASH = os.sep

    # 项目路径
    root_path = os.path.dirname(os.path.abspath(__file__))
    # 图片路径
    img_path = os.path.join(root_path, 'img' + _SLASH)


class IMGHandler:
    """普通图片验证码处理类"""

    @staticmethod
    def img_identify(img_url):
        """图片识别"""
        ocr = ddddocr.DdddOcr()
        with open(img_url, 'rb') as f:
            img_bytes = f.read()
        ver_code = ocr.classification(img_bytes)
        # print(ver_code)
        # 剔除非数字或字母的字符, 构造新的字符串
        new_ver_code = ''.join([i for i in ver_code if i.isdigit() or i.isalpha()])
        # 研究系统的验证码长度为5, 超出5个则需要进行处理
        if len(new_ver_code) > 5:
            new_ver_code = new_ver_code[len(new_ver_code)-5:]
        # print(new_ver_code)
        return new_ver_code


class UserLogin:
    """用户登录类"""

    def __init__(self):
        self.ver_code = None
        self.user = requests.Session()
        self.base_url = 'http://xxx.com'
        self.img_url = self.base_url + '/captcha'
        self.login_url = self.base_url + '/sys/login'

    def download_img(self):
        """请求接口下载图片至本地"""
        res = self.user.get(self.img_url, stream=True, verify=False)
        if res.status_code == 200:
            # 图片路径 + 图片文件名
            # file_path = ConfigHandler.img_path + img_url.rsplit('/', 1)[-1]
            file_path = ConfigHandler.img_path + self.img_url.rsplit('/', 1)[-1] + '.jpeg'
            # print(file_path)
            with open(file_path, 'wb') as f:
                f.write(res.content)
            return file_path

    def get_ver_code(self):
        """识别图片验证码"""
        self.ver_code = IMGHandler.img_identify(self.download_img())

    def user_login(self):
        """用户登录"""
        self.get_ver_code()
        # print(self.ver_code)
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        payload = 'username=xxx&password=xxx&captcha=%s' % self.ver_code
        # print(payload)
        res = self.user.post(self.login_url, data=payload, headers=headers, verify=False)
        print(res.text)


if __name__ == '__main__':
    ul = UserLogin()
    ul.user_login()
```