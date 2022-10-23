---
layout:        post
title:         "Nginx | 安装、配置、部署静态页"
subtitle:      ""
date:          2021-04-19
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Nginx
---

## 背景
&emsp;&emsp;自动化测试生成的报告可上传至已部署的阿里云服务器，便可访问此 html 了，即使离开办公室仍可访问。解决了本地启动 Apache 服务器后其他人需要位于相同网关才可访问的问题。

<br><br>

## 使用技巧
###### 一、更新 apt 库
```
$ sudo apt-get update
$ sudo apt-get upgrade
```

<br><br>

###### 二、安装 nginx
```
$ apt-get install nginx
```

<br><br>

###### 三、检查 nginx 配置
&emsp;&emsp;检查 `/etc/nginx/conf.d` 目录，列表为空就代表没有配置过。    

```
$ cd /etc/nginx/conf.d/
$ ls 
```

<br><br>

###### 四、新建配置文件
![](\haauleon\img\in-post\post-other\2021-04-20-nginx-server-3.jpg)

<br>

![](\haauleon\img\in-post\post-nginx\2021-04-20-nginx-server-1.jpg)

<br><br>

###### 五、重启 nginx 服务
```
$ sudo nginx -s reload
```

<br><br>

###### 六、访问首页
&emsp;&emsp;在浏览器地址栏输入 `112.74.205.108`，成功显示首页 `hello.html` 文件的内容。     

![](\haauleon\img\in-post\post-nginx\2021-04-20-nginx-server-2.jpg)

<br><br>

## 一些坑
![](\haauleon\img\in-post\post-other\2021-04-20-nginx-server-4.jpg)

<br><br>

## 结论
&emsp;&emsp;部署完成后即可访问静态资源。