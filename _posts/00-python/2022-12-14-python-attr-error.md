---
layout:        post
title:         "Python | AttributeError 属性异常"
subtitle:      "AttributeError: 'Request' object has no attribute 'is_xhr'"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

属性异常出现的场景：   
&emsp;&emsp;通常是自己使用 pip 安装了第三方包，在运行的时候会提示这个属性不存在。     

解决属性异常的方法：    
&emsp;&emsp;出现这个问题的原因是安装了第三方包后，由于第三方包存在很多版本，好巧不巧我们调用的方法或者属性在当前下载的这个版本中不存在，那么就需要去 PYPI 市场去根据包名进行搜索，找到其他符合的版本来重新下载安装。
