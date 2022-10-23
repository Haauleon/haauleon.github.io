---
layout:        post
title:         "Postman | Tests Script"
subtitle:      "如何使用 Postman 自带的 API 完成测试断言？"
date:          2021-04-12
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - API 测试
    - Postman
---

## 背景
&emsp;&emsp;Postman 提供了丰富的断言，同时也提供了发送请求的前置脚本功能。前置脚本功能，我目前用得最多的是添加或者更新当前时间戳，然后在发送请求时带过去，而后置的请求断言则用于检查接口响应是否符合我的预期要求。脚本语言使用的是 JavaScript。

<br><br>

## 使用技巧      
###### 一、Pre-request Script
&emsp;&emsp;此脚本在发送请求前运行，示例脚本如下：        
```js
var moment = require('moment');                        
// 获取当前时间并格式化
var data = moment().format(" YYYY-MM-DD HH:mm:ss");        
console.log(data);

// 添加全局变量
pm.globals.set("time", data);  
```    

![](\img\in-post\post-postman\2021-04-12-postman-script-1.png)

<br><br>

&emsp;&emsp;打开 Postman 控制台查看请求顺序。预期是先执行前置请求脚本，再发送请求。         

![](\img\in-post\post-postman\2021-04-12-postman-script-2.png)       

<br>

![](\img\in-post\post-postman\2021-04-12-postman-script-3.png)       

<br>

![](\img\in-post\post-postman\2021-04-12-postman-script-4.png)

<br><br>

###### 二、Tests
&emsp;&emsp;测试脚本是在发送请求之后才执行，一般用于检查接口返回的字段值是否符合预期，或者检查接口的数据是否完整等等主要测试断言。Postman 提供了 API，可直接调用。       

![](\img\in-post\post-postman\2021-04-12-postman-script-5.png)      

<br>

&emsp;&emsp;Test 脚本除了可以断言响应之外，最常见的还有设置或者更新全局变量，用于解决接口的依赖问题，例如接口 A 的参数列表中需要用到接口 B 的响应字段值。       

![](\img\in-post\post-postman\2021-04-12-postman-script-6.png)       

<br><br>

## 结论
&emsp;&emsp;总体来说，Postman 提供的 API 测试功能已经很完善了，集自动化测试于一身，基本满足于日常工作。