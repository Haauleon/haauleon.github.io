---
layout:        post
title:         "Fiddler | 部分实用的小功能"
subtitle:      "其他一些实用的小功能"
date:          2018-01-14
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Fiddler
---

## 实用功能
###### 快速查询本机 ip
&emsp;&emsp;一说到主机 IP，很多人的第一反应就是 windows+R 输入 cmd 进入控制台，然后使用 ipconfig 命令获取主机 IP 。But！在 Fiddler 友好的界面就提供了快捷查询方法。如下：               

![](\img\in-post\post-fiddler\2018-01-14-fiddler-other-1.png)

<br><br>

###### 过滤无用的 Host
&emsp;&emsp;虽然成功的连上了代理，但由于代理了浏览器又代理了手机端的应用而导致 Fiddler 可以抓取到来自不同 Host 下的无数接口，这样就增加了排查问题的难度。可以通过 Fiddler 过滤掉无用的域名只保留我们想要看到的 Host，如下：       
（1）步骤一：选择Use Filters  
（2）步骤二：选择Show only the following Hosts  
（3）步骤三：填写只想要保留的域名          
<br>

![](\img\in-post\post-fiddler\2018-01-14-fiddler-other-2.png)     

<br><br>

###### 多次执行同一请求
&emsp;&emsp;可以使用 Replay > Reissue Sequentially 实现对同一请求指定执行次数。        

![](\img\in-post\post-fiddler\2018-01-14-fiddler-other-3.png)        

<br>

![](\img\in-post\post-fiddler\2018-01-14-fiddler-other-4.png)