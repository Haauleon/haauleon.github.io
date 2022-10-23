---
layout:        post
title:         "Postman | Newman"
subtitle:      "如何使用 Newman 来完成 API 自动化测试？"
date:          2021-04-12
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - API 测试
    - Postman
---

## 背景
&emsp;&emsp;Postman 提供丰富的接口测试断言，使用 Postman 结合 Newman 来完成 API 自动测试可以大大降低时间成本，生成的测试报告非常可观且测试报告模板可以按需修改。本文是基于 MacOs 系统来操作且截图的，Windows 系统需要替换命令行。                

<br><br>

## 使用技巧
###### 一、环境准备
1.安装 nodejs     
下载地址：[node官网](https://nodejs.org/zh-cn/)，使用默认安装即可，安装成功后进行验证。      
```
$ node -v
```    

![](\img\in-post\post-postman\2021-04-12-postman-newman-1.png)    

<br>

2.安装 newman        
```
$ sudo npm install -g newman
$ newman -v
```     

![](\img\in-post\post-postman\2021-04-12-postman-newman-2.png)        

<br>

3.安装 newman-reporter-html        
```
$ sudo npm install -g newman-reporter-html
```
<br><br>

###### 二、自定义测试报告
1.组合键 `command + space(空格键)` 打开搜索框，输入 newman 并点击进入访达        

![](\img\in-post\post-postman\2021-04-12-postman-newman-3.png)       

<br>

2.点击进入 `newman-reporter-html` 文件夹         

![](\img\in-post\post-postman\2021-04-12-postman-newman-4.png)       

<br>

3.进入 `newman-reporter-html/lib` 目录       

![](\img\in-post\post-postman\2021-04-12-postman-newman-5.png)      

<br>

4.找到文件 `template-default.hbs` 并点击打开编辑此 html 模板即可        

![](\img\in-post\post-postman\2021-04-12-postman-newman-6.png)     

<br><br>

###### 三、执行自动化测试
1.导出 postman 自动化测试集       

![](\img\in-post\post-postman\2021-04-12-postman-newman-7.png)      

<br>

2.导出环境变量             

![](\img\in-post\post-postman\2021-04-12-postman-newman-8.png)      

<br>

![](\img\in-post\post-postman\2021-04-12-postman-newman-9.png)     

<br>

3.导出全局变量      

![](\img\in-post\post-postman\2021-04-12-postman-newman-10.png)      

<br>

![](\img\in-post\post-postman\2021-04-12-postman-newman-11.png)     

<br>

4.进入终端执行自动化测试命令        

```
$ newman run 测试集文件.json -e 环境变量文件.json -g 全局变量.json --reporters html --reporter-html-export 要生成的测试报告文件名
```     

![](\img\in-post\post-postman\2021-04-12-postman-newman-12.png)      

<br>

![](\img\in-post\post-postman\2021-04-12-postman-newman-13.png)     

<br>

5.打开测试报告       

![](\img\in-post\post-postman\2021-04-12-postman-newman-14.png)      

<br><br>

###### 四、填坑      
&emsp;&emsp;在导出环境变量文件和全局变量文件时，需要将变量列表的当前值全部赋给初始值，否则导出的文件中环境变量的值均为空字符串。       

![](\img\in-post\post-postman\2021-04-12-postman-newman-15.png)     

<br>

![](\img\in-post\post-postman\2021-04-12-postman-newman-16.png)

<br><br>

## 结论
&emsp;&emsp;Newman 生成的测试报告模板可按需修改。