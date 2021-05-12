---
layout:        post
title:         "禅道 | Python3 脚本创建 bug"
subtitle:      "写了一个创建 bug 的 python3 脚本 demo"
date:          2021-05-11
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Zentao
    - Python
---
 
## 背景
&emsp;&emsp;写了一个简单的脚本去禅道上创建 Bug，具体到时候怎么使用这个脚本还待研究。     

<br><br>

## 代码实现
```python
#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
import re
import hashlib
import json

username = "username"              # 登录账户
pw = "password"                    # 登录密码
base = "http://localhost:8080"     # 服务地址

user = requests.Session()
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}


class Zentao:

    def __init__(self):
        self.login_url = "%s/zentao/user-login.html" %base
        self.product_url = "%s/zentao/product-index-no.json" %base
        self.rand = None
        self.pwd = None
        self.product_id = None
        self.modules_dict = None

    def union_option(self):
        self.get_rand()
        self.get_password()
        self.user_login()
        self.get_product_list("saas")
        self.check_login()
        self.get_module_list()
        self.create_bug()

    def search_for_key(self, dict_value, dict_name):
        '''根据字典的值查找键'''
        return list(filter(lambda k:dict_name[k] == dict_value, dict_name))[0]

    def get_rand(self):
        '''获取 rand 值'''
        while True:
            res_rand = user.get(self.login_url, headers=headers)
            # res_rand.encoding = 'utf-8'
            # print("res_rand.text = %s" %res_rand.text)
            rand = re.findall(r"'verifyRand' value='(.+?)'", res_rand.text)
            # print("rand[0] = {}".format(rand[0]))
            if len(rand[0]) == 10:   # rand 的长度不固定可为9或10，判断长度为10时就不再请求登录页面接口
                self.rand = rand[0]
                break
        print(self.rand)

    def get_password(self):
        '''获取 password'''
        # 方式一
        hash = hashlib.md5()
        hash.update(pw.encode('utf-8'))
        f = hash.hexdigest() + self.rand
        # print("f = %s" %f)
        # 方式二
        hash2 = hashlib.md5(f.encode('utf-8'))
        self.pwd = hash2.hexdigest()
        print("pwd = %s" %self.pwd)

    def user_login(self):
        '''用户登录'''
        data = {
            "account": username,
            "password": self.pwd,
            "referer": "",
            "verifyRand": self.rand
        }
        res_login = user.post(self.login_url, headers=headers, data=data)
        # res_login.encoding = 'utf-8'
        # print("res_login.text = %s" %res_login.text)

    def check_login(self):
        '''检查登录'''
        res_check = user.get("%s/zentao/bug-browse-%s-0-openedbyme.html" %(base, self.product_id), headers=headers)
        # res_check.encoding = 'utf-8'
        # print("res_check.text = %s" %res_check.text)
        result = re.findall(r"\<a href=\'\/zentao\/user-logout.html' \>(.+?)\<\/a\>", res_check.text)
        if result[0] == "退出":
            print("登录成功")
    
    def get_product_list(self, product_name):
        '''获取产品列表'''
        res_product = user.get(self.product_url).json()
        products_str = res_product["data"].encode('utf-8').decode('unicode_escape') # python3 取消了decode，要想str中的unicode转中文需要先编码再解码
        products_dict = json.loads(products_str)["products"]  # str 转 dict
        self.product_id = self.search_for_key(product_name, products_dict)

    def get_module_list(self):
        '''获取各模块列表'''
        res_module = user.get("%s/zentao/bug-create-%s-0-moduleID=0.json" %(base, self.product_id)).json()
        modules_str = res_module["data"].encode('utf-8').decode('unicode_escape')
        self.modules_dict = json.loads(modules_str)

    def get_project_id(self, project_name):
        '''获取项目id'''
        project_id = self.search_for_key(project_name, self.modules_dict["projects"])
        return project_id

    def get_version(self, version_name):
        '''获取影响版本'''
        version_key = self.search_for_key(version_name, self.modules_dict["builds"])
        return version_key

    def get_member(self, member_name):
        '''获取指派成员'''
        member_key = self.search_for_key(member_name, self.modules_dict["projectMembers"])
        return member_key

    def create_bug(self):
        '''创建一个 bug 问题单'''
        data = {
            "product": self.product_id,
            "module": 0,
            "project": self.get_project_id("saas"),
            "openedBuild[]": self.get_version("主干"),
            "assignedTo": self.get_member("C:陈巧伦"),
            "deadline": "",
            "type": "automation",
            "os": "",
            "browser": "",
            "title": "[测试脚本]测试禅道自动发布bug问题单",
            "color": "",
            "severity": "3",
            "pri": "3",
            "steps": "<p>[步骤]</p><p>1</p><p><br /></p><p>[结果]</p><p>2</p><p><br /></p><p>[期望]</p>3",
            "story": "",
            "task": "",
            "oldTaskID": "0",
            "mailto[]": "", 
            "keywords": "",
            "labels[]": "",
            "files[]": "",
            "case": "0",
            "caseVersion": "0",
            "result": "0",
            "testtask": "0"
        }
        res_bug = user.post("%s/zentao/bug-create-%s-0-moduleID=0.html" %(base, self.product_id), data=data)

        
if __name__ == '__main__':
    zentao = Zentao()
    zentao.union_option()
```