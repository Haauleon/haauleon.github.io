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

## 前言
&emsp;&emsp;一般来说，环境变量的值基本都是写死的，所以环境变量`baseUrl`、`userName`等等这些一般只能用于特定的环境，故而写死的。但全局变量，我希望它的值是可以更新的，不受环境的影响，也就是说不管切到任何环境都能使用这些变量，比如在接口传递的参数值等等。所以，环境变量的值是死的，而全局变量的值是可变的。    

<br><br>

## 使用技巧
###### 设置全局变量
![](\img\in-post\post-postman\2021-04-12-postman-global-1.png)      

![](\img\in-post\post-postman\2021-04-12-postman-global-2.png)      

![](\img\in-post\post-postman\2021-04-12-postman-global-3.png)     

<br><br>

###### 使用全局变量
![](\img\in-post\post-postman\2021-04-12-postman-global-4.png)       

![](\img\in-post\post-postman\2021-04-12-postman-global-5.png)     

<br><br>

## 结束语
&emsp;&emsp;全局变量的实用性很强，确实是接口的得力助手。 