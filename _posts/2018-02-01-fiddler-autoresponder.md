---
layout:        post
title:         "Fiddler | URL 映射请求"
subtitle:      "如何使用 Fiddler 代理映射请求？"
date:          2018-02-01
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Fiddler
---

## 背景
* 已发布线上 APP 出现接口错误，如何调试线上 APP 访问本地请求？       
* 已发布线上 H5页面，静态资源或 js 调试，如何映射本地 js？            

<br><br>

## 解决方案
###### 一般解决方案
&emsp;&emsp;猜测（一般明显问题）。                
&emsp;&emsp;找到原发布包，修改请求资源url重新打包测试。需要前后端协调配合，耗时费力。                

<br><br>

###### Fiddler 解决方案 (映射响应)
&emsp;&emsp;原理：通过 fidder 拦截，将需要加载的资源映射到本地开发环境，而无需切换测试版 APP。             
&emsp;&emsp;例如线上资源：[http://online.com/api/page](http://online.com/api/page)                   
&emsp;&emsp;映射加载本地资源：[http://127.0.0.1/api/page](http://127.0.0.1/api/page)                

<br><br>

**方法一：使用 Fiddler 自带的 AutoResponder**                                       
添加正则替换主机名规则：  
&emsp;&emsp;regex:(?insx)[http://online.com](http://online.com/)\\/(?.+)$                            
&emsp;&emsp;\*redir:[http://127.0.0.1/${name}](http://127.0.0.1/$%7Bname%7D)                           

![](\img\in-post\post-fiddler\2018-02-01-fiddler-autoresponder-1.png)                         

<br>
     
&emsp;&emsp;AutoResponder 是 Fiddler 比较重要且比较强大的功能之一。它可以用来调试服务器端代码而无需修改服务器端的代码和配置，因为它拦截某一请求并重定向到本地的资源后，实际上访问的是本地的文件或者得到的是 Fiddler 的内置响应。         
&emsp;&emsp;因此，如果要调试生产环境服务器的某个 js 文件，则可以用它将该生产环境的 js 文件拦截并重定向到本地的 js 文件后，修改本地 js 文件来验证程序或者查找问题。在本地修改完 js 脚本之后，再修改服务器端的内容。这可以保证，**尽量在真实的环境下去调试，从而最大限度的减少 bug 发生的可能性。**     
&emsp;&emsp;此外，为了紧急修复了生产环境的 bug 后可以让测试员配合进行本地测试，即让测试员连上你的代理后，他就可以对你本地的代码文件进行测试了。    

<br><br>

**方法二：使用 Stave 插件**                           
添加规则：                      
&emsp;&emsp;匹配：[online.com](http://online.com/)                     
&emsp;&emsp;替换为：127.0.0.1                            

![](\img\in-post\post-fiddler\2018-02-01-fiddler-autoresponder-2.png)          

<br><br>

## 正则匹配
一、前缀为`EXACT:`                   
&emsp;&emsp;表示完全匹配（大小写敏感）                    
&emsp;&emsp;只有 match=rules 时，才匹配                   
  
<br>

二、无前缀  
&emsp;&emsp;表示基本搜索  
&emsp;&emsp;表示搜索到字符串就匹配  
&emsp;&emsp;只要 match 中包含了 rules 的字符串，即可  
  
<br>

三、前缀为`NOT:`  
&emsp;&emsp;表示发现就不匹配  
&emsp;&emsp;与无前缀的基本搜索同理，只是发现了就不匹配，其他默认匹配  

<br>

四、前缀为`REGEX:`  
&emsp;&emsp;表示使用正则表达式匹配  
&emsp;&emsp;如regex:(?insx).+.(jpg|gif|bmp)$ 包含以jpg或gif或bmp字符串结尾的，不区分大小写，且是单行的，即可匹配
  
<br>

| 规则 | 解释 |
| --- | --- |
| `.+` | 匹配一个或多个字符。 <br>如`regex:.+jpg`包含有 jpg 字符串且以 jpg 字符串结尾的，即可匹配 |
| `.\*` | 匹配0个或多个字符。<br>如`regex:.+.jpg.\*`包含有 .jpg 字符串即可匹配 |
| `^` | 匹配字符串开始位置。 |
| `$` | 匹配字符串结束位置。<br>如`regex:.+.(jpg|gif|bmp)$`包含以 jpg 或 gif 或 bmp 字符串结尾的，即可匹配 |         

<br><br>

五、前缀为`REGEX:(?insx)`  
&emsp;&emsp;表示匹配方式      
<br>

| 规则 | 解释 |
| --- | --- |
| `i` | 表示不区分大小写 |
| `n` | 表示指定的唯一有效的捕获是显式命名或编号的形式 |
| `s` | 表示单行模式 |
| `x` | 表示空格说明的 |