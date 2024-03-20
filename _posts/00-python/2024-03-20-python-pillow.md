---
layout:        post
title:         "Python3 | 图像识别异常 module 'PIL.Image'"
subtitle:      "AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 程序环境
（1）操作系统：windows10         
（2）python版本：3.8.10       

<br>
<br>

### 问题分析    
```bash
AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'        
AttributeError: 'FreeTypeFont' object has no attribute 'getsize'    
```

&emsp;&emsp;原因是 pillow 库版本不支持，我的 pillow 版本是 10.0.1。        
&emsp;&emsp;ANTIALIAS 在 Pillow 10.0.0 中被删除（在许多以前的版本中被弃用后）。现在您需要使用 PIL.Image.LANCZOS 或 PIL.Image.Resampling.LANCZOS。（这与所引用的算法完全相同ANTIALIAS，只是您无法再通过名称访问它ANTIALIAS。）
&emsp;&emsp;解决办法就是降低版本为 9.5.0。     

```bash
> pip install pillow==9.5.0
```

<br>
<br>

---

相关链接：    
[解决bug：AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'](https://blog.csdn.net/qq_44442727/article/details/134113614)