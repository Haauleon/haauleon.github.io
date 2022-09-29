---
layout:        post
title:         "禅道 | Python3 脚本获取产品列表"
subtitle:      "解决获取产品列表接口的编码解码、字典值查键等问题"
date:          2021-05-08
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Zentao
    - Python
---

## 背景
&emsp;&emsp;禅道的 API 接口调用可谓是一言难尽，百度了一下，它的接口主要有两种调用方式，一种是直接请求 html，像用户登录这样的请求我就是直接请求 html 页面；还有一种是将要请求的 `http://xxx/zentao/xxx.html` 后缀先改为 `http://xxx/zentao/xxx.json` 然后再去发送请求。      
&emsp;&emsp;用户登录请求 html 还可以解决，但是获取产品列表如果直接去请求 html 的话，它返回的就是一个 html 页面，要先进行 dom 树解析找元素等手段才能去拿到产品列表的 id 值，实在是太麻烦了，所以想着去发一个 json 后缀的请求。      
&emsp;&emsp;所以，我打算除了登录请求之外的接口均使用 json 去替换 html 后缀。但是，麻烦又来了，请求完成后，它返回的是一个 str 包起来的 dict，这个 dict 的值还包含 unicode，python3 以上的版本无法直接使用 `str.decode('unicode_escape')` 来进行解码。另外，这里再附上一段在 dict 中快速通过值查找对应键的思路。        

<br><br>

## 问题
###### 坑一、直接请求 html
&emsp;&emsp;一开始是通过抓包的方式抓到的获取产品列表接口，不需要参数，很直接了然。但是，它返回的 html 需要自己进行解析找到对应产品列表的值，很麻烦。          

```python
def get_product_list_test(self):
    '''获取禅道产品列表'''
    res_product = user.get("%s/zentao/product-index-no.html" %base)
    print(res_product.text)
```
<br><br>

运行结果：       
```html
<div class="panel-body has-table scrollbar-hover block-products">
  <table class='table table-borderless table-hover table-fixed table-fixed-head tablesorter table-fixed'>
    <thead>
      <tr>
        <th class='c-name'>产品名称</th>
                <th class='c-name c-project'>当前项目</th>
                <th class='c-num'>计划数</th>
        <th class='c-num'>发布数</th>
        <th class='c-num'>激活需求</th>
        <th class='c-num w-90px'>未解决Bug</th>
      </tr>
    </thead>
    <tbody>
                  <tr class='text-center' data-url='/zentao/product-browse-16.html' >
        <td class='c-name text-left' title='绿松石产业服务平台'>绿松石产业服务平台</td>
                <td class='c-name c-project text-left'>绿松石产业服务平台v1</td>
                <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">55</td>
        <td class="c-num">13</td>
      </tr> 
                  <tr class='text-center' data-url='/zentao/product-browse-15.html' >
        <td class='c-name text-left' title='华新小程序'>华新小程序</td>
                <td class='c-name c-project text-left'>华新支付</td>
                <td class="c-num">1</td>
        <td class="c-num">0</td>
        <td class="c-num">7</td>
        <td class="c-num">0</td>
      </tr> 
                  <tr class='text-center' data-url='/zentao/product-browse-14.html' >
        <td class='c-name text-left' title='saas'>saas</td>
                <td class='c-name c-project text-left'>saas-扫码收款应用</td>
                <td class="c-num">1</td>
        <td class="c-num">0</td>
        <td class="c-num">27</td>
        <td class="c-num">76</td>
      </tr> 
                  <tr class='text-center' data-url='/zentao/product-browse-13.html' >
        <td class='c-name text-left' title='技术研究院'>技术研究院</td>
                <td class='c-name c-project text-left'>技术研究院管理体系</td>
                <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">6</td>
        <td class="c-num">0</td>
      </tr> 
                  <tr class='text-center' data-url='/zentao/product-browse-12.html' >
        <td class='c-name text-left' title='绿松石'>绿松石</td>
                <td class='c-name c-project text-left'>绿松石-V1</td>
                <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">7</td>
      </tr> 
                  <tr class='text-center' data-url='/zentao/product-browse-11.html' >
        <td class='c-name text-left' title='新版商会馆'>新版商会馆</td>
                <td class='c-name c-project text-left'>新版商会馆V1</td>
                <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">0</td>
      </tr> 
                  <tr class='text-center' data-url='/zentao/product-browse-10.html' >
        <td class='c-name text-left' title='佛得角'>佛得角</td>
                <td class='c-name c-project text-left'>佛得角官网-V1</td>
                <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">0</td>
      </tr> 
                  <tr class='text-center' data-url='/zentao/product-browse-9.html' >
        <td class='c-name text-left' title='其他产品'>其他产品</td>
                <td class='c-name c-project text-left'>南沙黔掌柜</td>
                <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">26</td>
      </tr> 
                  <tr class='text-center' data-url='/zentao/product-browse-7.html' >
        <td class='c-name text-left' title='新版信息網'>新版信息網</td>
                <td class='c-name c-project text-left'>新版信息網</td>
                <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">2</td>
      </tr> 
                  <tr class='text-center' data-url='/zentao/product-browse-5.html' >
        <td class='c-name text-left' title='密西西比'>密西西比</td>
                <td class='c-name c-project text-left'>密西西比-第二期</td>
                <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">6</td>
      </tr> 
                  <tr class='text-center' data-url='/zentao/product-browse-4.html' >
        <td class='c-name text-left' title='澳博四合院项目'>澳博四合院项目</td>
                <td class='c-name c-project text-left'></td>
                <td class="c-num">0</td>
        <td class="c-num">1</td>
        <td class="c-num">2</td>
        <td class="c-num">0</td>
      </tr> 
                  <tr class='text-center' data-url='/zentao/product-browse-3.html' >
        <td class='c-name text-left' title='中拉跨境电商合作平台'>中拉跨境电商合作平台</td>
                <td class='c-name c-project text-left'>中拉跨境电商合作平台-第一期</td>
                <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">1</td>
        <td class="c-num">0</td>
      </tr> 
                  <tr class='text-center' data-url='/zentao/product-browse-2.html' >
        <td class='c-name text-left' title='信息网'>信息网</td>
                <td class='c-name c-project text-left'>信息网</td>
                <td class="c-num">2</td>
        <td class="c-num">1</td>
        <td class="c-num">12</td>
        <td class="c-num">0</td>
      </tr> 
                  <tr class='text-center' data-url='/zentao/product-browse-1.html' >
        <td class='c-name text-left' title='跨境说严选'>跨境说严选</td>
                <td class='c-name c-project text-left'>跨境说严选-特权版</td>
                <td class="c-num">0</td>
        <td class="c-num">0</td>
        <td class="c-num">6</td>
        <td class="c-num">24</td>
      </tr> 
          </tbody>
  </table>
</div>
```

<br>

&emsp;&emsp;返回的数据如上，要拿到产品名对应的 id 实在是太麻烦了，后续用到的接口不能总是请求 html。          

<br><br>

###### 坑二、解码问题
&emsp;&emsp;将 `.html` 后缀改为 `.json` 后再请求，发现返回的是一个 str 包起来的 dict，这个 dict 的值还包含 unicode，python3 以上的版本无法直接使用 `str.decode('unicode_escape')` 来进行解码。       

```python
def get_product_list_test(self):
    '''获取禅道产品列表'''
    res_product = user.get("%s/zentao/product-index-no.json" %base)
    print(res_product.json())
```
<br><br>

运行结果：      
```
{'status': 'success', 'data': '{"title":"\\u4ea7\\u54c1\\u4e3b\\u9875","products":{"16":"\\u7eff\\u677e\\u77f3\\u4ea7\\u4e1a\\u670d\\u52a1\\u5e73\\u53f0","15":"\\u534e\\u65b0\\u5c0f\\u7a0b\\u5e8f","14":"saas","13":"\\u6280\\u672f\\u7814\\u7a76\\u9662","12":"\\u7eff\\u677e\\u77f3","11":"\\u65b0\\u7248\\u5546\\u4f1a\\u9986","10":"\\u4f5b\\u5f97\\u89d2","9":"\\u5176\\u4ed6\\u4ea7\\u54c1","7":"\\u65b0\\u7248\\u4fe1\\u606f\\u7db2","5":"\\u5bc6\\u897f\\u897f\\u6bd4","4":"\\u6fb3\\u535a\\u56db\\u5408\\u9662\\u9879\\u76ee","3":"\\u4e2d\\u62c9\\u8de8\\u5883\\u7535\\u5546\\u5408\\u4f5c\\u5e73\\u53f0","2":"\\u4fe1\\u606f\\u7f51","1":"\\u8de8\\u5883\\u8bf4\\u4e25\\u9009","18":"saas-\\u626b\\u7801\\u6536\\u6b3e\\u5e94\\u7528","8":"\\u91c7\\u9500\\u5e73\\u53f0"},"pager":null}', 'md5': '5d42ad9091ca5336128cfd2117999c6c'}
```      
<br><br>

###### 字典值找键的思路
&emsp;&emsp;[参考链接](https://www.jianshu.com/p/488a99b7d40d)               

```
>>> dct = {'Name': 'Alice', 'Age': 18, 'uid': 1001, 'id': 1001}
 
>>> def get_key1(dct, value):
...     return list(filter(lambda k:dct[k] == value, dct))
 
>>> get_key1(dct, 1001)
['id', 'uid']
```

<br><br>

## 代码实现
```python
#! /usr/bin/env python

import requests
import re
import hashlib
import json

username = "username"             # 登录用户
pw = "password"                   # 登录密码
base = "http://localhost:8080"    # 服务地址

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

    def get_product_list(self, product_name):
        '''获取产品列表'''
        res_product = user.get(self.product_url).json()
        # print(res_product)
        products_str = res_product["data"].encode('utf-8').decode('unicode_escape') # python3 取消了decode，要想str中的unicode转中文需要先编码再解码
        # print(products_str)
        products_dict = json.loads(products_str)["products"]  # str 转 dict
        self.product_id = list(filter(lambda k:products_dict[k] == product_name, products_dict))[0]
        print(self.product_id)


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
14
```   