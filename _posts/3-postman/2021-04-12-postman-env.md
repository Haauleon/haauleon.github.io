---
layout:        post
title:         "Postman | 环境变量"
subtitle:      "如何高效地使用环境变量？"
date:          2021-04-12
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - API 测试
    - Postman
---

## 背景    
&emsp;&emsp;Postman 可以定义环境变量，目前我用得最多的是切换生产环境和测试环境，前提是变量名均使用`baseUrl`。在接口测试的时候，用于快速切换 host。其实就当然于一个占位变量，用环境变量的真实值来替换占位变量的值。

<br><br>

## 使用技巧
###### 一、设置环境变量
![](\img\in-post\post-postman\2021-04-12-postman-env-1.png)          

<br>

![](\img\in-post\post-postman\2021-04-12-postman-env-2.png)       

<br>

![](\img\in-post\post-postman\2021-04-12-postman-env-3.png)       

<br>

![](\img\in-post\post-postman\2021-04-12-postman-env-4.png)         

<br>

![](\img\in-post\post-postman\2021-04-12-postman-env-5.png)         

<br>

![](\img\in-post\post-postman\2021-04-12-postman-env-6.png)       

<br><br>

###### 二、使用环境变量
![](\img\in-post\post-postman\2021-04-12-postman-env-7.png)         

<br>

![](\img\in-post\post-postman\2021-04-12-postman-env-8.png)         

<br>

![](\img\in-post\post-postman\2021-04-12-postman-env-9.png)      

<br><br>

## 结论
&emsp;&emsp;使用占位变量的好处就是可以用不同环境下的变量去替代真实值，从而解决手动更改 host 的麻烦。以往测试 API 都是直接在请求地址栏上使用完整地址即`http://test.com/user/center`，但是要测试此 API 在其他 host 下的场景时，又得整个更改为`http://online.com/user/center`。现在使用了环境变量后，只需要在地址栏内填写`{{baseUrl}}/user/center`，然后切换至相应的环境即可。