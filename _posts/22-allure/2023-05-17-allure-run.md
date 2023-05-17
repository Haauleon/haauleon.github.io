---
layout:        post
title:         "Windows | allure 生成报告后无法自动打开"
subtitle:      ""
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Allure
---


### 一、问题
关于allure生成报告后无法自动打开的问题并报      
```
“‘allure‘ �����ڲ����ⲿ���Ҳ”      
```

<br><br>

### 二、排查
pyCharm 首先设置一下编码格式： Settings > File Encodings，将 Global Encoding 的值修改为 GBK 并保存。   

发现报错信息为：allure不是内部或外部命令，也不是批处理程序或可运行的文件    

<br>
<br>

### 三、解决
解决方法：以管理员的身份运行 pychram 即可。

<br>
<br>

---

相关链接：    
[关于allure生成报告后无法自动打开的问题并报“‘allure‘ �����ڲ����ⲿ���Ҳ”](https://blog.csdn.net/qq_41721166/article/details/112433177)