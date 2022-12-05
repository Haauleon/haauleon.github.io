---
layout:        post
title:         "Flask Web | 文件托管服务"
subtitle:      "实现一个文件托管服务"
author:        "Haauleon"
header-img:    "img/in-post/post-flask/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Flask
    - Python
    - Web开发
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、需求列表
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

文件托管服务的需求说明如下：     
1. 上传后的文件可以被永久存放。    
2. 上传后的文件有一个功能完备的预览页。预览页显示文件大小、文件类型、上传时间、下载地址和短链接等信息。     
3. 可以通过传参数对图片进行缩放和剪切。    
4. 不错的页面展示效果。    
5. 为节省空间，相同文件不重复上传，如果文件已经上传过，则直接返回之前上传的文件。    

<br>
<br>

### 二、项目准备
#### 1、环境准备
先安装一些依赖：    
```
> sudo apt-get install libjpeg8-dev -yq
> sudo pip install -r requirements.txt
```

requirements.txt 的 pip 第三方包列表如下：    
```python
python-magic==0.4.10  # libmagic 的 Python 绑定，用于确定文件类型 
Pillow==3.2.0         # PIL(Python Imaging Library) 的分支，用来替代 PIL 
cropresize2==0.1.9    # 用来剪切和调整图片大小
short-url==1.2.1      # 创建短链接
```

<br>

#### 2、建表语句
文件托管服务的建表语句如下（databases/schema.sql）:    
```

```