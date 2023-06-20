---
layout:        post
title:         "Python3 | werkzeug.wrappers 模块异常"
subtitle:      "ImportError: cannot import name ‘BaseResponse‘ from ‘werkzeug.wrappers‘"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### ImportError
```
ImportError: cannot import name ‘BaseResponse‘ from ‘werkzeug.wrappers‘
```

![](\img\in-post\post-python\2023-04-25-python-werkzeug-1.png)      
<!-- ![](https://img-blog.csdnimg.cn/1a9ba32efed54f73985945fe98bc0a9f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5byg5a6J6YeR,size_20,color_FFFFFF,t_70,g_se,x_16) -->


<br>
<br>

### 解决  
可以使用以下命令降级安装werkzeug：    
```
pip install --upgrade werkzeug==0.16.1
```

<br>
<br>

---

相关链接：    
[ImportError: cannot import name ‘BaseResponse‘ from ‘werkzeug.wrappers‘](https://blog.csdn.net/m0_51973071/article/details/124111746)