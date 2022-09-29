---
layout: post
title: "Windows 定时任务"
subtitle: 'Jenkins太复杂？Windows定时任务了解一下'
author: "Haauleon"
header-style: text
tags:
  - Windows
---

&emsp;&emsp;之前使用Jenkins来完成定时构建，后来想想如果只是单纯想跑定时任务的话，用windows自带的定时任务其实也是个不错的选择，简单方便，照旧还是放毛老师的照片来镇楼镇妖&#94;&#95;&#94;。      
![](\img\in-post\post-windows\2018-11-19-WindowsCrontab-1.gif)




### 认识Windows任务计划程序界面
第一步：打开开始&#45;&#45;&#62;控制面板，选择&#34;大图标&#34;查看方式，点击&#34;管理工具&#34;        
![](\img\in-post\post-windows\2018-11-19-WindowsCrontab-1.jpg)      

第二步：点击&#34;任务计划程序&#34;       
![](\img\in-post\post-windows\2018-11-19-WindowsCrontab-2.jpg)      

第三步：进入Windows任务计划程序界面       
![](\img\in-post\post-windows\2018-11-19-WindowsCrontab-3.jpg)


### 实践：定时任务执行python脚本
#### 创建任务
任务介绍：由于工作需要，需要每天定时构建python脚本。还因为该脚本为WebUI自动化脚本，因此需要在执行时隐藏窗口。        
![](\img\in-post\post-windows\2018-11-19-WindowsCrontab-4.jpg)        

#### 编辑常规
![](\img\in-post\post-windows\2018-11-19-WindowsCrontab-5.jpg)

#### 新建触发器
![](\img\in-post\post-windows\2018-11-19-WindowsCrontab-6.jpg)

#### 新建操作
![](\img\in-post\post-windows\2018-11-19-WindowsCrontab-7.jpg)

#### 确认创建
![](\img\in-post\post-windows\2018-11-19-WindowsCrontab-9.jpg)

#### 完成创建
![](\img\in-post\post-windows\2018-11-19-WindowsCrontab-10.jpg)

### 小贴士
&emsp;&emsp;若执行结果有输出的文件，而在脚本中并未指定该文件存放的路径。则运行完之后，该脚本是由哪个用户账户执行的就存放在哪个用户路径下面。比如我的是&#34;C&#58;&#92;Users&#92;Administrator&#92;&#34;。