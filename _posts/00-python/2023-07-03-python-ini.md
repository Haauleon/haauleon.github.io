---
layout:        post
title:         "Python3 | ini 文件配置多用户"
subtitle:      "ini 配置文件中配置字典列表（List of Dicts）的最佳实践"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 一、需求背景
&emsp;&emsp;最近爬的接口常常会提示 `"当前账号同时登录次数已超过限制数量!"`，刚好领导给了十个账号给我，我这边就想着写一个多个用户的 ini 文件配置，然后在调用登录接口的时候循环判断一下，如果账号登录成功就写入缓存给被爬接口，如果账号登录失败就切换账号。       

<br>
<br>

### 二、实现代码    
`account.ini` 文件中写入以下内容：      
```
[account.0]
username = account1
password = AAAAAA

[account.1]
username = account2
password = BBBBBB

[account.2]
username = account3
password = CCCCCC

[account.3]
username = account4
password = DDDDDD

...
```

使用 ConfigParser 来解析 `account.ini` 文件的内容：      
```python
from configparser import ConfigParser
 
 
config = ConfigParser()
config.read('account.ini')
 
accounts = []
 
for s in config.sections():
    if s.startswith('account.'):
        accounts.append(dict(config.items(s)))

for account in accounts:
    print(account['username'], account['password'])
```

<br>
<br>

---

相关链接：    
[.ini 配置文件中配置字典列表（List of Dicts）的最佳实践](https://blog.csdn.net/imliutao2/article/details/128531251)