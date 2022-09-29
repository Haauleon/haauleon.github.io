---
layout:        post
title:         "Gitbook | 编辑与发布"
subtitle:      "如何编辑、发布和远程访问电子书？"
date:          2018-10-11
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Gitbook
---

## 本地编辑电子书
&emsp;&emsp;需要使用 Gitbook 官方的图形化编辑工具 Gitbook Editor 来编辑电子书。                                
&emsp;&emsp;首先还是需要下载安装 [Gitbook Editor](http://www.pc6.com/softview/SoftView_368608.html)，安装好后运行它。这里我选择的是`Do that later`，因为 Gitbook 平台的账号登录功能需要翻墙才能使用。其实 Gitbook Editor 编辑器的使用同大多数 Markdown 编辑器的使用差不多，所以之后基于图形界面的操作就省略了，先来看一下 Gitbook Editor 编辑页面是什么样子。                             
![](\img\in-post\post-gitbook\2021-03-12-gitbook-update-1.png)                                  

<br>

![](\img\in-post\post-gitbook\2021-03-12-gitbook-update-2.png)                         

<br><br>

## 生成静态页面资源
&emsp;&emsp;Gitbook Editor 编辑电子书完成之后进入书籍目录，执行`$ gitbook build` 或者 `$ gitbook serve` 命令即可生成静态页面资源存于`_book`目录下。这两个命令的不同之处在于，使用`$gitbook serve`命令在生成静态资源的同时还可以打开浏览器输入`localhost:4000` 在本地预览电子书。             
```
$ cd 书籍目录
$ gitbook build

或者：
$ gitbook serve
```

<br><br>

## 发布电子书
&emsp;&emsp;本地库的电子书编辑好了后要想发布并进行远程访问，首先需要在 Gitbook 官网使用平台账号或者第三方账号进行登录，然后在此平台创建跟本地相同的书名等等，后面的就没有再研究了，因为需要翻墙。下面列举了几个可以远程访问电子书的方法。                            

<br><br>

###### 方法一：发布到私有云服务器
&emsp;&emsp;此处省略一千字。                         

<br><br>

###### 方法二：托管到第三方平台
&emsp;&emsp;详见下一章：使用 Github Pages 托管静态资源。                          

<br><br>

###### 方法三：发布到看云
&emsp;&emsp;先进行本地仓库备份到github远程库，在看云[https://www.kancloud.cn](https://www.kancloud.cn/)上导入github仓库，编辑完成同步到版本库后直接发布，即可访问电子书。还可在自己的域名解析内增加一条记录，即自定义域名。比如这本书的访问地址是[book.haauleon.com](book.haauleon.com)。