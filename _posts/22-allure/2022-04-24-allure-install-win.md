---
layout:        post
title:         "Windows | 安装配置 allure"
subtitle:      ""
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Allure
---


### 一、前言
&emsp;&emsp;自己电脑是 win 系统，所以还得装一个 win 环境的 allure。          

<br><br>

### 二、安装配置步骤
###### 1、下载 allure 的 zip 压缩包
[压缩包下载地址](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/)

<br>

###### 2、解压 zip 包获取 bin 的路径
`/Users/haauleon/allure-2.17.3/bin`

<br>

###### 3、配置 allure 的环境变量
1. 在桌面找到 `此电脑`，右键点击打开 `属性` 
2. 选择 `高级配置`，打开 `环境变量` 编辑框
3. 在系统变量 path 编辑框中添加一条 allure 的 bin 目录即可
4. 打开 cmd 命令行窗口执行 `$ allure --version` 有返回版本号则安装配置成功