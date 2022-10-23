---
layout:        post
title:         "Postman | 全局变量"
subtitle:      "全局变量可以解决什么问题？"
date:          2021-04-12
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - API 测试
    - Postman
---

## 背景
&emsp;&emsp;一般来说，环境变量的值基本都是写死的，所以环境变量`baseUrl`、`userName`等等这些一般只能用于指定环境，故而写死。但全局变量，我希望它的值是可以更新的，不受环境的影响，也就是说不管切到任何环境都能使用这些变量，比如在接口传递的参数值等等。而全局变量，目前我的应用是在接口有依赖时，即当前接口的参数值依赖于上一个接口响应的字段值时，可以在上一个接口的 Tests 脚本里设置一个全局变量用来存该字段值。          

<br><br>

## 使用技巧
###### 一、设置全局变量
![](\img\in-post\post-postman\2021-04-12-postman-global-1.png)         

<br>

![](\img\in-post\post-postman\2021-04-12-postman-global-2.png)        

<br>

![](\img\in-post\post-postman\2021-04-12-postman-global-3.png)     

<br><br>

###### 二、使用全局变量
![](\img\in-post\post-postman\2021-04-12-postman-global-4.png)         

<br>

![](\img\in-post\post-postman\2021-04-12-postman-global-5.png)     

<br><br>

###### 三、更新全局变量     
```js
// 定义一个响应体res，获取body中所有的参数并以json格式返回
var res = JSON.parse(responseBody);

// 获取字段res.key的值并存在全局变量中
postman.setGlobalVariable("全局变量名", res.key)
```

<br><br>

## 结论
&emsp;&emsp;全局变量的实用性很强，确实是接口测试的得力助手。 