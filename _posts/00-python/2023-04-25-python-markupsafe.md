---
layout:        post
title:         "Python3 | markupsafe 模块异常"
subtitle:      "解决ImportError: cannot import name ‘soft_unicode‘ from ‘markupsafe‘"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### ImportError
```python
ImportError: cannot import name 'soft_unicode' from 'markupsafe'
```

![](https://img-blog.csdnimg.cn/1a9ba32efed54f73985945fe98bc0a9f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5byg5a6J6YeR,size_20,color_FFFFFF,t_70,g_se,x_16)


<br>
<br>

### 解决  
这个报错应该怎么解决呢？     
1、 根据错误提示，我们发现是导入markupsafe这个库引起的报错，首先我们先查看这个库是否存在。      
```
pip show markupsafe
```

![](https://img-blog.csdnimg.cn/350cb6dac4454d2ba674351aea28620a.png)     


2、经过查看我们发现这个库是已经安装过的。那我们尝试指定版本号覆盖安装一下这个库。      
```
python -m pip install markupsafe==2.0.1
```

![](https://img-blog.csdnimg.cn/75c199fcbe90489890099f595fda8729.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5byg5a6J6YeR,size_20,color_FFFFFF,t_70,g_se,x_16)    


3、启动成功，问题解决。


<br>
<br>

---

相关链接：    
[解决ImportError: cannot import name ‘soft_unicode‘ from ‘markupsafe‘](https://blog.csdn.net/weixin_45438997/article/details/124261720)