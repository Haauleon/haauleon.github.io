---
layout:        post
title:         "macOs | 安装配置 allure"
subtitle:      ""
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Allure
---


### 一、前言
&emsp;&emsp;在 Mac 上安装 allure，一般来说最简单的是直接打开终端使用 `$ brew install allure` 命令行。但是，由于网络原因或者是其他的原因，往往会安装不成功，那么我们可以使用另外一种。          

<br><br>

### 二、安装配置步骤
###### 1、下载 allure 的 zip 压缩包
&emsp;&emsp;从 github 上下载 allure 的 zip 形式的压缩包，[allure 在 github 上的地址](https://github.com/allure-framework/allure2/releases)。      
&emsp;&emsp;如果无法访问 github，可以直接上我的百度网盘下载，提取码: 2cki。     
[https://pan.baidu.com/s/1-pfUn1qavlaPFZ84gAGO6g?pwd=2cki](https://pan.baidu.com/s/1-pfUn1qavlaPFZ84gAGO6g?pwd=2cki)

<br>

###### 2、解压 zip 包获取 bin 的路径
`/Users/haauleon/allure-2.17.3/bin`

<br>

###### 3、配置 allure 的环境变量
1. 在终端输入命令
    `$ vi ~/.bash_profile`
2. 添加allure的路径
    ```
    export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin
    export PATH=${PATH}:自己本地allure的bin目录的路径
    ```
3. 保存 :wq
4. 使环境变量生效
    `source ~/.bash_profile`
5. 验证是否生生效
    在终端输入命令 `$ allure --version`，若返回版本号则说明配置成功