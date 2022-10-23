---
layout:        post
title:         "Gitbook | 安装与使用"
subtitle:      "Gitbook 的使用场景是什么？怎么安装？"
date:          2018-10-11
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Gitbook
---

## Ⅰ Gitbook简介
&emsp;&emsp;大概是同事的墙裂推荐，也就开始接触了Gitbook。GitBook 是一个基于 Node.js 的命令行工具，支持 Markdown 和 AsciiDoc 两种语法格式，可以输出 HTML、PDF、eBook 等格式的电子书。

&emsp;&emsp;在本地 windows 系统安装好了 gitbook 环境后，进入 Gitbook 官网[https://www.gitbook.com](https://www.gitbook.com)，目前新版官网的访问速度很慢，连注册登录都慢到访问失败，而他家旧版的官网虽然可以正常访问，但是要注册登录的话还是得进新版的页面。要解决这个问题，需要翻墙。

&emsp;&emsp;注意：gitbook 最新版本 3.2.3 安装到本地后，在使用`$ gitbook init`命令时报错了，下面来解决这个问题。

<br><br>

## Ⅱ 安装 Gitbook
###### 一、Windows 系统安装 Gitbook
&emsp;&emsp;进入 Windows 系统，使用管理员权限执行`cmd.exe`后，根据以下操作指引即可完成 Gitbook 的安装。
```
$ npm install gitbook-cli -g     # 安装gitbook，-g 表示全局安装
$ gitbook current                # 查看当前版本信息
$ gitbook init                   # cd 到书籍目录进行初始化，将生成两个 .md 文件
$ gitbook build                  # 在本地目录生成静态网页资源，存于本地 _book 目录
$ gitbook serve                  # 在本地目录生成静态网页资源的同时运行服务器，然后通过浏览器访问 localhost:4000 即可查看该书籍
```
![](\img\in-post\post-gitbook\2021-03-12-gitbook-install-1.png)
<br>

![](\img\in-post\post-gitbook\2021-03-12-gitbook-install-2.png)
<br>

&emsp;&emsp;安装完成之后进入已创建好的书籍目录，使用`gitbook init`命令初始化目录，若能成功创建`README.md`和`SUMMARY.md`这两个文件，则说明初始化成功。先来试试 3.2.3 这个版本，执行命令`gitbook init`后发现报错了。
![](\img\in-post\post-gitbook\2021-03-12-gitbook-install-3.png)
<br><br>

###### 二、解决 3.2.3 版本的 init 问题
&emsp;&emsp;解决方案：卸载 3.2.3 版本，安装 3.0.0 版本。
```
$ gitbook fetch 3.0.0          # 指定 3.0.0 版本进行安装
$ gitbook uninstall 3.2.3      # 指定 3.2.3 版本进行卸载
$ gitbook ls                   # 列出本地已安装的所有 gitbook 版本
$ gitbook current              # 列出当前活动的 gitbook 版本
```
![](\img\in-post\post-gitbook\2021-03-12-gitbook-install-4.png)
<br>

![](\img\in-post\post-gitbook\2021-03-12-gitbook-install-5.png)

<br>

&emsp;&emsp;执行完`$ gitbook serve`命令后，在浏览器地址栏输入[http://localhost:4000](http://localhost:4000) 将得到以下这个书籍预览页面。
![](\img\in-post\post-gitbook\2021-03-12-gitbook-install-6.png)

<br>

&emsp;&emsp;再次进入书籍目录查看目录结构，下图为此时的目录结构。
![](\img\in-post\post-gitbook\2021-03-12-gitbook-install-7.png)