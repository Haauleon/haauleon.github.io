---
layout:        post
title:         "macOs | 端口占用查询"
subtitle:      "解决端口冲突的问题"
date:          2021-05-12
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - macOs
---

## 背景
&emsp;&emsp;之前在玩 mitmproxy 的时候，使用 mitmdump 命令启动监听，该命令会占用本地 8080 端口。由于启动 jenkins 服务时默认用的是 8080 端口，所以冲突了。          

<br><br>

## 使用技巧
如果已有其他进程占用此端口，可通过以下操作解决：         

```
$ lsof -i tcp:port    # 查看占用 port 的进程
$ kill -9 PID         # 干掉进程
```