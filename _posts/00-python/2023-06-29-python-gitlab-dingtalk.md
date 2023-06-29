---
layout:        post
title:         "Pytest | Gitlab 推送钉钉机器人配置"
subtitle:      "使用钉钉接收 Gitlab 仓库的推送消息"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - Gitlab
---


### 一、实现需求
&emsp;&emsp;近期有项目上线，目前是我这边去拉代码打包部署，在不知道什么时候才能去拉代码打包的条件下，需要挨个去问他们“代码提交了吗”之类的话，我自己也烦。于是，想实现一个代码提交推送到钉钉的需求，这样一来，他们一提交代码，我的钉钉就会受到推送消息。    

<br>
<br>

### 二、钉钉配置Gitlab机器人
配置机器人的前提是自己得有一个群组，然后在群组里面新建一个 `极狐Gitlab` 钉钉机器人，然后拿到钉钉机器人的 webhook。              
![](\img\in-post\post-python\2023-06-29-python-gitlab-dingtalk-1.png)           
![](\img\in-post\post-python\2023-06-29-python-gitlab-dingtalk-2.png)            

<br>
<br>

### 三、Gitlab配置webhook
在 Gitlab 上找到配置 webhook 的入口：Settings > Webhooks          
![](\img\in-post\post-python\2023-06-29-python-gitlab-dingtalk-3.png)     

写入以下配置数据     
1、URL: 钉钉机器人 webhook      
2、触发的事件: Push events （代码推到仓库后就推送消息至钉钉）           
![](\img\in-post\post-python\2023-06-29-python-gitlab-dingtalk-4.png)     

<br>
<br>

### 四、最终效果
![](\img\in-post\post-python\2023-06-29-python-gitlab-dingtalk-5.png)       
