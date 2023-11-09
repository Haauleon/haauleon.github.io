---
layout:        post
title:         "影刀RPA | 自动清除影刀浏览器缓存"
subtitle:      "解决在影刀RPA软件启动运行的条件下无法删除cache文件夹的问题"
author:        "Haauleon"
header-img:    "img/in-post/post-rpa/bg.jpg"
header-mask:   0.4
catalog:       true
tags:
    - 影刀RPA
---

### 问题描述
&emsp;&emsp;官方的方法是使用命令删除缓存文件夹，但是很多用户都反馈无法删除，因为文件正在使用。我测试了，关闭影刀浏览器也依旧显示无法删除。只要影刀主程序开启了的，就无法无法删除 cache 这个文件夹。<mark>手动清除浏览器缓存的方法：程序运行之前需要干掉影刀进程，然后在运行命令框内输入 `%localappdata%\ShadowBot\cef` 找到 cache 文件夹并删除。</mark>          

<br>
<br>

### 分析解决
&emsp;&emsp;原来需要退出影刀才能清缓存，原因是在影刀启动的时候，为了性能，后台预启动了一个影刀浏览器进程。目前如果需要的话可以写个子流程解决；后面他们会升级影刀浏览器，解决相关使用问题。           

**子流程如下：**             
![](\img\in-post\post-rpa\2023-11-09-yingdao-cache-1.png)             

<br>

**指令配置如下：**        
（1）关闭网页          
![](\img\in-post\post-rpa\2023-11-09-yingdao-cache-2.png)             

（2）获取系统文件路径           
![](\img\in-post\post-rpa\2023-11-09-yingdao-cache-3.png)             

（3）删除文件夹          
![](\img\in-post\post-rpa\2023-11-09-yingdao-cache-4.png)             


<br>
<br>

---

相关链接：          
[影刀浏览器清除缓存问题解决了吗？](https://www.yingdao.com/community/detaildiscuss?id=d17b2e57-65e0-4b88-b8f7-7907b19f013d)    