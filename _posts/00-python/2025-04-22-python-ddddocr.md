---
layout:        post
title:         "爬虫 | DLL load failed: 找不到指定的模块"
subtitle:      "python 识别验证码，使用import ddddocr包时，报错 DLL load failed: 找不到指定的模块"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 报错原因
报错如下：       
`ImportError: DLL load failed` : 找不到指定的模块                
实际上是 win10 系统中缺少 Visual C++ 2005 应用程序使用的运行库组件包           

<br>
<br>

### 处理方法
先检查自己的系统是什么版本（32位/64位），然后去官网下载：[Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/zh-cn/download/details.aspx?id=48145&751be)      
下载完成后直接运行即可解决，若无法下载，请使用离线安装包：       
链接: https://pan.baidu.com/s/1FHi3uyVntQ_TLnpQvhAoWQ?pwd=bmed  
提取码: bmed
