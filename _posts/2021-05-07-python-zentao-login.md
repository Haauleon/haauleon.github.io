---
layout:        post
title:         "禅道 | Python3 脚本登录"
subtitle:      "解决禅道登录接口的密码加密等问题"
date:          2021-05-07
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Zentao
    - Python
---

## 背景
&emsp;&emsp;搞了那么久的自动化测试，灵机一动，可以在自动化项目里面加多一个功能：在自动化测试断言失败后自动向禅道提交 bug。以往都是测试结果直接输出，输出的形式目前暂定钉钉和测试报告，现在想要加多一个 bug 自动提交的功能。可以想象成自己有一个分身，她可以自己完成测试任务，测试过程中遇到 bug 就提交到禅道。岂不美哉~       

<br><br>

## 问题
&emsp;&emsp;目前使用的禅道专业版本 10.4。看了禅道的登录接口，找到它的接口参数如下：          
```
Request URL: http://localhost:8080/zentao/user-login.html      
Request Method: POST

Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36


form-data
    account: username
    password: 95868bb5e73c6fb5ad280abf63fbsfg
    referer: http://localhost:8080/zentao/bug-browse-14-0-openedbyme.html
    verifyRand: 2010824780
```
<br>

&emsp;&emsp;`form-data` 里的 `password` 和 `verifyRand` ，可以看到前端在请求前均进行了加密。检查登录页面 `http://localhost:8080/zentao/user-login.html` 的源代码：          
```
$(document).ready(function()
{
    $('#verifyPassword').closest('form').find('#submit').click(function()
    {
        var password = $('input#verifyPassword').val().trim();
        var rand = $('input#verifyRand').val();
        $('input#verifyPassword').val(md5(md5(password) + rand));
    });
});
```
&emsp;&emsp;由源代码可以看出，`password` 和 `rand` 均使用 md5 进行了加密，而接口的 `verifyRand == rand`。       

<br><br>

## 代码实现
```python
#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
import re
import hashlib

username = "username"                   # 登录账户
pw = "password"                         # 登录密码
base = "http://localhost:8080"          # 服务地址

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

    def union_option(self):
        self.get_rand()
        self.get_password()
        self.user_login()
        self.check_login()
        self.get_product_list("saas")

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
            "referer": "%s/zentao/bug-browse-14-0-openedbyme.html" %base,
            "verifyRand": self.rand
        }
        res_login = user.post(self.login_url, headers=headers, data=data)
        # res_login.encoding = 'utf-8'
        # print("res_login.text = %s" %res_login.text)

    def check_login(self):
        '''检查登录'''
        res_check = user.get("%s/zentao/bug-browse-14-0-openedbyme.html" %base, headers=headers)
        # res_check.encoding = 'utf-8'
        # print("res_check.text = %s" %res_check.text)
        result = re.findall(r"\<a href=\'\/zentao\/user-logout.html' \>(.+?)\<\/a\>", res_check.text)
        # print("result = {}".format(result))
        if result[0] == "退出":
            print("登录成功")


if __name__ == '__main__':
    zentao = Zentao()
    zentao.union_option()
    
```

<br><br>

运行结果：    
```
1490976266
pwd = f6bddcc70263e1d26f946ca8e6f38970
登录成功
```