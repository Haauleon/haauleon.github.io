---
layout:        post
title:         "Jmeter | 上传文件"
subtitle:      "使用 Jmeter 发送上传文件请求"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
    - API 测试
---

### 一、背景
&emsp;&emsp;HTTP 请求常见的 `content-type` 分为 3 种：`application/json`、`x-www-form-urlencoded`、`multipart/form-data`，当请求是上传文件时，需要用到 multipart/form-data 方式。      

<br>
<br>

### 二、请求配置
&emsp;&emsp;勾选 `Use multipart/form-data`，在随请求一起提交的文件中，添加文件路径（如果使用相对路径，则需要将文件置于和测试计划同一位置），参数名称为 `file`，类型为 `file`。         

**注意：**       
HTTP 请求头中不需要添加 content-type 为 multipart/form-data，否则所有的参数都会被当成文件以二进制形式传输。       

![](\img\in-post\post-jmeter\2022-07-21-jmeter-file-1.png) 