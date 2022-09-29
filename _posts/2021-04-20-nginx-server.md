---
layout:        post
title:         "Nginx | 部署静态页面"
subtitle:      "安装和配置 nginx"
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
###### 第一个坑
操作：执行 `sudo nginx -s reload`                          
问题：提示 `nginx: [emerg] "server"; directive is not allowed here in /etc/nginx/nginx.conf:87`                        
解决： `vim /etc/nginx/nginx.conf` 检查 87 行代码， 检查 server 的配置是否少了一个花括号 `}`；或者将 server 的配置全局注释。   

<br><br>

###### 第二个坑
操作：执行 `sudo nginx -s reload`                          
问题：提示 `nginx: [error] open() "/run/nginx.pid" failed (2: No such file or directory)`                  
解决：找到 `nginx.conf` 文件所在的目录，我的是在 `/etc/nginx` 目录下，然后使用以下命令行即可解决。               

```
$ nginx -c /etc/nginx/nginx.conf
$ sudo nginx -s reload
```

<br><br>

## 结论
&emsp;&emsp;部署完成后即可访问静态资源，接下来出一个部署多域名的教程。