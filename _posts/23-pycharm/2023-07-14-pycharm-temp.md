---
layout:        post
title:         "Pycharm | 自动生成文件模板"
subtitle:      "新建一个 python 文件成功后，pycharm 会自动向文件写入模板内容"
author:        "Haauleon"
header-img:    "img/in-post/post-jenkins/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Pycharm
---

### 背景
&emsp;&emsp;很多项目文件的头部都会有文件注释，标明文件的功能、文件名、作者、迭代版本等信息。如下图是我自己实现的效果：    
![](\img\in-post\post-pycharm\2023-07-14-pycharm-temp-1.png)      

<br>
<br>

### Pycharm设置步骤
1、进入设置页面     
![](\img\in-post\post-pycharm\2023-07-14-pycharm-temp-2.png)      

2、找到 File and Code Templates 选项   
![](\img\in-post\post-pycharm\2023-07-14-pycharm-temp-3.png)       

3、在模板输入框内写入以下内容后保存     
```python 
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   ${NAME}.py 
@Date    :   ${DATE} ${TIME}
@Function:   None

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
${DATE} ${TIME}        haauleon         1.0           None
"""
```