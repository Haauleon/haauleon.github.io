---
layout: post
title: "基于Postman的mock server实际应用"
subtitle: 'mock server基础应用'
author: "Haauleon"
header-style: text
tags:
  - Postman
  - mockServer
---

&emsp;&emsp;今天来贴上基于Postman的mock&#32;server的一些基础的使用技巧，也算是mock&#32;server的开篇之作，来讲讲如何在Postman里面来设置mock&#32;server。                             
![](\img\in-post\2019-01-29-MockServer0\1.jpg)




## 新建mock并发送请求
### 新建mock server
在标题工具栏中，单击“NEW”按钮后，在新窗口选择mock&#32;server。        

![](\img\in-post\2019-01-29-MockServer0\2.jpg)

### 新建API
在编辑窗口的左侧选择“New&#32;API”，在右侧依次输入“Request&#32;Path”、“Status&#32;Code”、“Response&#32;Body”，输入完成后点击“Next”。          

Request&#32;Path：要请求的路径名           
Status&#32;Code：响应状态码，比如200、500、504等等          
Response&#32;Body：返回结果        

![](\img\in-post\2019-01-29-MockServer0\3.jpg)

### 配置mock server
在配置mock&#32;server时，默认创建公有的mock&#32;server。输入“Name”后点击“Create”。        

![](\img\in-post\2019-01-29-MockServer0\4.jpg)      

### 创建Host
在最后一步时点击左半框内的“Host”，便可生成要请求的Host。       

![](\img\in-post\2019-01-29-MockServer0\5.jpg)

### 发送请求
把生成的Host拼接到API前，并发送请求，可成功获取返回结果。      

![](\img\in-post\2019-01-29-MockServer0\6.jpg)      

![](\img\in-post\2019-01-29-MockServer0\7.jpg)


## 修改API的请求和响应
### 修改Default值
在页面右上角点击“Examples”，在下拉列表中选择“Default”。在Default编辑页面编辑要修改的信息，修改完成后点击“Save&#32;Examples”。      

![](\img\in-post\2019-01-29-MockServer0\8.jpg)     

![](\img\in-post\2019-01-29-MockServer0\9.jpg)

### 重新发送请求
修改完成后返回至请求页面，重新发送请求。会发现在不改变原请求的情况下，发送请求后返回了404，请求失败了。这是因为刚刚修改了请求方式，说明修改生效了。       

![](\img\in-post\2019-01-29-MockServer0\10.jpg)

### 修改后再请求
修改请求方式和正确填写参数后，再次发送请求，请求成功了。        

![](\img\in-post\2019-01-29-MockServer0\11.jpg)


## Summary
该篇博文简单的讲述了创建mock&#32;server的过程，以及如何修改API的请求和响应。