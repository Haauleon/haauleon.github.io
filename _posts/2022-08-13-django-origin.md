---
layout:        post
title:         "Django | 跨域报错"
subtitle:      "django3 跨域报错 Origin '*' in CORS_ORIGIN_WHITELIST"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Django
    - Python
---

### 问题描述
&emsp;&emsp;使用 django-cors-header，在 settings 中进行相关配置后，报错如下，分享一种更好的解决办法（网上其他解决办法索性就不配置这个参数了）。              
```
(corsheaders.E013) Origin '*' in CORS_ORIGIN_WHITELIST is missing  scheme or netloc
```

<br>
<br>

### 解决方法
&emsp;&emsp;根据报错上下文提示，将 CORS_ORIGIN_WHITELIST 改成        
```
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:*'
)
```

<br>

&emsp;&emsp;报错依旧存在且更多了，`http://127.0.0.1:*` 中的每一个字符都出现了上面 `*` 相同的报错。为什么会将字符串拆分成字符进行检测？django 会对 `http://127.0.0.1:*` 进行迭代处理？直接配置成一个列表试试，改成下面：            
```
CORS_ORIGIN_WHITELIST = (
    ['http://127.0.0.1:*']
)
```

&emsp;&emsp;没有报错了，感觉这种配置方法相比不配置会更加的安全，更加可控！

