---
layout:        post
title:         "Postman | Mock Server"
subtitle:      "如何使用模拟服务器来自定义一个 API？"
date:          2021-04-12
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - API 测试
    - Postman
---

## 背景
###### mock 在单元测试中的应用
&emsp;&emsp;`mock` 其中一个意思是模仿。主要应用于单元测试领域，用来辅助完成单元测试。在实际生产中对项目进行单元测试的时候，会遇到以下问题：      
* 接口的依赖     
* 外部接口调用    
* 测试环境非常复杂     

&emsp;&emsp;单元测试应该只针对当前单元进行测试，所有的内部或外部的依赖应该是稳定的。而使用 mock 可以通过对外部依赖组件实现进行模拟并替换，从而解除单元测试中的接口依赖性问题，降低编写单元测试用例的难度。因此，在单元测试中，开发人员只需要将焦点放在当前的单元功能即可。

<br><br>

###### mock 在架构模式中的应用
&emsp;&emsp;目前最常见的应用模式是**前后端分离**，即后端仅返回前端所需的数据，不再渲染 HTML 页面，不再控制前端的效果。所以，前端与后端的耦合度相对较低。       
&emsp;&emsp;后端开发的每一个视图都称为一个接口，或者 API，前端通过访问接口来对数据进行增删改查。在项目开发期间，前后端预先商定好数据接口的交互形式和数据格式（最好拟定一份 API 规范文档），然后实现前后端的并行开发。前端提前完成开发后通过创建 mock server 来模拟接口的响应以此调试代码，等后端开发完毕，仅需要将 mock server 的 host 地址替换成后端服务 host（可使用环境占位变量）即可。     

<br><br>

## 使用技巧
###### 一、创建 Mock Server 服务
1.在标题工具栏中，单击`NEW`按钮后，在新窗口选择 mock server。         

![](\img\in-post\post-postman\2021-04-12-postman-mock-1.jpg)      

<br>

2.在编辑窗口的左侧选择`New API`，在右侧依次输入`Request Path`、`Status Code`、`Response Body`，输入完成后点击`Next`。          
`Request Path`：要请求的路径名           
`Status Code`：响应状态码，比如 200、500、504 等等                   
`Response Body`：返回结果     

![](\img\in-post\post-postman\2021-04-12-postman-mock-2.jpg)       

<br>

3.在配置 mock server 时，默认创建公有的 mock server。输入`Name`后点击`Create`。           

![](\img\in-post\post-postman\2021-04-12-postman-mock-3.jpg)        

<br>

4.在最后一步时点击左半框内的`Host`，便可生成要请求的`Host`。          

![](\img\in-post\post-postman\2021-04-12-postman-mock-4.jpg)            

<br><br>

###### 二、发送 Mock 请求
1.把生成的 Host 拼接到 API 前（建议使用环境变量），并发送请求，可成功获取返回结果。        

![](\img\in-post\post-postman\2021-04-12-postman-mock-5.jpg)           

<br>

![](\img\in-post\post-postman\2021-04-12-postman-mock-6.jpg)       

<br><br>

###### 三、篡改 Mock 请求    
1.在页面右上角点击`Examples`，在下拉列表中选择`Default`。在`Default`编辑页面编辑要修改的信息，修改完成后点击`Save Examples`。          

![](\img\in-post\post-postman\2021-04-12-postman-mock-7.jpg)             

<br>

![](\img\in-post\post-postman\2021-04-12-postman-mock-8.jpg)              

<br>

2.修改完成后返回至请求页面，重新发送请求。在不改变原请求的情况下，请求后返回了 404。这是因为刚刚修改了请求方式，说明修改生效了。        

![](\img\in-post\post-postman\2021-04-12-postman-mock-9.jpg)           

<br>

3.修改请求方式和正确填写参数后，再次发送请求，请求成功。         

![](\img\in-post\post-postman\2021-04-12-postman-mock-10.jpg)              

<br><br>

## 结论
&emsp;&emsp;Postman 的 mock server 服务也可用于测试人员，主要使用场景为解决 API 接口自动化测试中的接口依赖问题。