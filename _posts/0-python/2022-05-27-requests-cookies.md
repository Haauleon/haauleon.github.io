---
layout:        post
title:         "爬虫 | requests 获取响应 cookies"
subtitle:      "介绍 cookies 的两种添加方式即 cookies 和 headers 传参"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
---

> 参考自: https://www.jianshu.com/p/8cbf309741e2

<br><br>

### 代码背景
&emsp;&emsp;很多网站的接口调用都需要保持状态的连接，不然服务器不知道你是谁，只有极少数网站不需要连接状态。目前，连接状态的方法我总结了三个。        
- requests.Session()  
- requests.post(cookies=dict(res.cookies))  
- requests.post(headers={'Cookies': res.headers['Set-Cookie']})

<br><br>

### 关于 cookie
###### 什么是 cookie
&emsp;&emsp;http 请求本身是无状态的，服务器没有办法区分这一次访问和下一次访问是不是同一个人。因为你这一秒的登录，下一秒网站就不再认识你了。很简单，你想通过网站拿到自己的信息，就需要告诉服务器你是你。        
&emsp;&emsp;因此，需要记住某些关键的信息，以便于下一次请求该网站时可以带上这些信息，以保持登录状态。       

<br>

###### 如何获取 cookie
&emsp;&emsp;通过 r.cookies 可以得到一个 RequestsCookieJar 对象，该对象中保存了 cookie 信息。该对象的行为类似于字典，可以通过 get 获取键对应的值，或者通过 dict 将其转为字典。还可以通过 r.headers 获得响应头字典里面的 Cookies 值。     
- r.cookies.get('Cookies')  
- dict(r.cookies)
- r.headers['Set-Cookie']

```python
import requests

url = "http://www.baidu.com"
r = requests.get(url)
print(r.cookies)                 # r.cookies 得到 RequestsCookieJar 对象
print(dict(r.cookies))           # 通过 dict 将 r.cookies 转为字典
print(r.cookies.get('Cookies'))  # 通过 get 获取键对应的值
print(r.headers['Set-Cookie'])   # 通过 r.headers 获得响应头字典里面的 Cookies 值
```

<br><br>

### 向服务器发送 cookie
###### Session() 对象
&emsp;&emsp;会话对象可以让你多次请求一个网站的时候，保持一些数据，包括自动带上 cookie。但是，手动通过 cookies 参数设置的 cookie 没有被 session 对象保持。       
```python
import requests

user = requests.Session()
url1 = "http://xxxxxx/1"
res1 = user.get(url1)

url2 = "http://xxxxxx/2"
res2 = user.get(url2)
```

<br>

###### cookies 参数
&emsp;&emsp;通过 cookies 参数传入字典。     
```python
import requests

url1 = "http://xxxxxx/1"
res1 = requests.get(url1)
cookie = dict(res1.cookies))           # 通过 dict 将 r.cookies 转为字典

url2 = "http://xxxxxx/2"
res2 = requests.get(url2, cookies=cookie)
```

<br>

###### headers 参数
&emsp;&emsp;通过 headers 参数传入字典 `{'Cookies': res.headers['Set-Cookie']}`。     
```python
import requests

url1 = "http://xxxxxx/1"
res1 = requests.get(url1)
cookie = res1.headers['Set-Cookie'])   # 通过 r.headers 获得响应头字典里面的 Cookies 值

url2 = "http://xxxxxx/2"
res2 = requests.get(url2, headers={'Cookies': cookie})
print(r.text)
```