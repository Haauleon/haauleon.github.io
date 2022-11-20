---
layout:        post
title:         "Jmeter | 提取响应值并设为全局变量"
subtitle:      "使用 JSON 提取器获取响应字段值、设置全局变量和引用"
author:        "Haauleon"
header-img:    "img/in-post/post-jmeter/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Jmeter
---

### 一、背景
&emsp;&emsp;想让 Jmeter 像 postman 一样有设置全局变量的能力，因为有些时候需要将上一个接口获取到的数据作为下一个接口的参数来使用。在 Jmeter 中，可以将响应字段设置为全局变量，这样就可以跨请求使用，实现联动。      

<br>
<br>

### 二、操作
###### 1、分析查看结果树
&emsp;&emsp;由以下查看结果树中的 HTTP 响应来看，我希望把 totalCount 这个字段作为全局变量，从而在其他接口中引用此 totalCount 的值。     

![](\img\in-post\post-jmeter\2022-07-21-jmeter-json-path-1.png) 

<br>

###### 2、使用JSON路径测试
&emsp;&emsp;JSON Path Tester 即 JSON 路径测试视图将允许测试 JSON-PATH 表达式，并从特定响应中查看所提取的数据。      

- `$` 表示根节点，一级一级的往下走可以用 `.` 来表示，
- 有如下两种写法示范
    -  字典 result 嵌字典 data，找到字典 data 的 totalCount 键
    ```
    $.result.data.totalCount
    ```
    - 字典 result 嵌列表 list，列表 list 的元素为字典，找到字典第一个元素的 titie 键
    ```
    $.result.data.list[0].title
    ```

![](\img\in-post\post-jmeter\2022-07-21-jmeter-json-path-2.png)       

<br>

&emsp;&emsp;由以上可知，totalCount 的 JSON 路径为 `$.result.data.totalCount`。    

![](\img\in-post\post-jmeter\2022-07-21-jmeter-json-path-3.png)


<br>

###### 3、添加JSON提取器
&emsp;&emsp;totalCount 的 JSON 路径为 `$.result.data.totalCount`，经过测试已成功获取到它的值。现在需要在此 HTTP 请求后面添加 JSON 提取器，如下：    
![](\img\in-post\post-jmeter\2022-07-21-jmeter-json-path-4.png)

<br>

配置提取器：     
- Names of created variables：自定义变量名称
- JSON Path expressions：JSON 路径表达式
- Match No.(0 for Random)：列表下标数字，如果只想匹配结果中的第一个元素就写 0    

![](\img\in-post\post-jmeter\2022-07-21-jmeter-json-path-5.png)

<br>

###### 4、设置全局变量
&emsp;&emsp;提取后设为全局变量才能被引用，这里需要添加为该 HTTP 请求添加一个 BeanShell 后置处理程序。脚本格式：`${__setProperty(全局变量名,${JSON提取的变量名},)}`            
![](\img\in-post\post-jmeter\2022-07-21-jmeter-json-path-6.png) 

<br>

写入脚本：`${__setProperty(total_count,${totalCount},)}`         
![](\img\in-post\post-jmeter\2022-07-21-jmeter-json-path-8.png)    

<br>

###### 5、使用全局变量
方法(1)：`${__P(全局变量名)}`          
示例：`${__P(total_count)}`        

方法(2)：`${JSON提取的变量名}`           
示例：`${totalCount}`

---
以上参考自：    
[https://blog.csdn.net/Psanji_isme/article/details/120442519](https://blog.csdn.net/Psanji_isme/article/details/120442519)     
[https://www.likecs.com/show-204743022.html](https://www.likecs.com/show-204743022.html)