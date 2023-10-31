---
layout:        post
title:         "Linux | selenium 的 chrome 缓存文件清理"
subtitle:      "定时删除服务器 /tmp 下的所有 chrome 浏览器缓存文件"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - 操作系统
    - Ubuntu
    - Linux
    - Debian
---

### 背景
&emsp;&emsp;部署 selenium 的服务器预警磁盘空间不足，某一文件系统磁盘容量使用率 99%，`sudo du -h --max-depth=0 /tmp` 命令发现 /tmp 文件夹大小有差不多40个G，`ll -a` 查看文件夹内全是 `.com.google.Chrome.xJUHXb` 之类的 chrome 缓存文件，太久不清理都爆了，手动删除即可。              
```bash
> cd /tmp/ && rm -rf .com.google.Chrome.*
```

<br>
<br>

### 解决方法
或者定时任务每日 10:30 自动删除缓存文件：    
```bash
# 定时清理 /tmp 目录下的chrome浏览器缓存
30 13 * * * /bin/rm -rf /tmp/.com.google.Chrome.*
```

<br>
<br>

---

相关链接：    
[selenium 的 chrome 缓存文件清理](https://www.jianshu.com/p/7f770b72fe0f)