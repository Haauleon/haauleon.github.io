---
layout:        post
title:         "macOs | Pycharm for mac 永久激活"
subtitle:      ""
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - macOs
    - Python
---

### 一、背景
&emsp;&emsp;通常我们使用激活码激活都有截止期限，下面介绍一下激活方法。

<br><br>

### 二、安装配置
###### 1、下载软件
pycharm2017 专业版   
链接: https://pan.baidu.com/s/1nYiUjm1Lc8zDPo-w93eU8w?pwd=ess2 提取码: ess2 

<br>

###### 2、下载补丁
补丁下载后放到一个安全的地方，我这里就是把补丁文件误删了，现在又重新破解的。           
链接: https://pan.baidu.com/s/1DjYZ-TGT1W9GKcIp7SXZ8Q?pwd=kiwt 提取码: kiwt 

<br>

###### 3、修改配置文件
(1) 打开路径：打开访达 -> `command+shift+g` -> 将路径`/Applications/PyCharm.app/Contents/bin/pycharm.vmoptions`复制进去          
(2) 使用文本编辑打开文件 pycharm.vmoptions      
(3) 获取补丁完整路径：使用鼠标将补丁文件拖入终端中      
(4) 将补丁路径添加至文件 pycharm.vmoptions 的最后一行，加入格式为 `-javaagent:你的jar包路径（绝对路径）`，然后保存退出            
(5) 打开软件，输入以下 active code：
```
active code:

ThisCrackLicenseId-{'licenseId':'11011','licenseeName':'WeChat','assigneeName':'IT--Pig','assigneeEmail':'1113449881@qq.com','licenseRestriction':'','checkConcurrentUse':false,'products':[ {'code':'II','paidUpTo':'2099-12-31'}, {'code':'DM','paidUpTo':'2099-12-31'}, {'code':'AC','paidUpTo':'2099-12-31'}, {'code':'RS0','paidUpTo':'2099-12-31'}, {'code':'WS','paidUpTo':'2099-12-31'}, {'code':'DPN','paidUpTo':'2099-12-31'}, {'code':'RC','paidUpTo':'2099-12-31'}, {'code':'PS','paidUpTo':'2099-12-31'}, {'code':'DC','paidUpTo':'2099-12-31'}, {'code':'RM','paidUpTo':'2099-12-31'}, {'code':'CL','paidUpTo':'2099-12-31'}, {'code':'PC','paidUpTo':'2099-12-31'} ],'hash':'2911276/0','gracePeriodDays':7,'autoProlongated':false}
```

(6) 点击 `help -> Register` 可以看到 pycharm 激活到 2099 年