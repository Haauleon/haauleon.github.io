---
layout: post
title: "postman | Mac 使用 newman 生成测试报告"
subtitle: '如何使用 postman 快速且高效完成自动化测试'
author: "Haauleon"
header-style: text
tags:
  - Postman
---

## 一、环境准备
1.安装 **nodejs**，下载地址 [node官网](https://nodejs.org/zh-cn/)，使用默认安装即可，安装成功后进行验证   
```
$ node -v
```     
![](\img\in-post\post-postman\2021-01-30-postman-auto-1.png)     
2.安装 newman    
```
$ sudo npm install -g newman
$ newman -v
```   
![](\img\in-post\post-postman\2021-01-30-postman-auto-2.png)    
3.安装 newman-reporter-html     
```
$ sudo npm install -g newman-reporter-html
```    
<br>

## 二、自定义测试报告  
1.组合键 `command + space空格键` 打开搜索框，输入 `newman` 并点击进入访达      
![](\img\in-post\post-postman\2021-01-30-postman-auto-3.png)   

2.点击进入 `newman-reporter-html` 文件夹    
![](\img\in-post\post-postman\2021-01-30-postman-auto-4.png)     

3.进入 `newman-reporter-html/lib` 目录     
![](\img\in-post\post-postman\2021-01-30-postman-auto-5.png)    

4.找到文件 `template-default.hbs` 并点击打开编辑此 html 模板即可
![](\img\in-post\post-postman\2021-01-30-postman-auto-6.png)    

<br>

## 三、自动化测试执行
1.导出 postman 自动化测试集  
![](\img\in-post\post-postman\2021-01-30-postman-auto-7.png)    

2.导出环境变量并编辑环境变量     
![](\img\in-post\post-postman\2021-01-30-postman-auto-8.png)     
![](\img\in-post\post-postman\2021-01-30-postman-auto-9.png)    

3.导出全局变量    
![](\img\in-post\post-postman\2021-01-30-postman-auto-10.png)     
![](\img\in-post\post-postman\2021-01-30-postman-auto-11.png)   
![](\img\in-post\post-postman\2021-01-30-postman-auto-12.png) 

4.进入终端执行自动化测试命令   
```
$ newman run 测试集文件.json -e 环境变量文件.json -g 全局变量.json --reporters html --reporter-html-export 要生成的测试报告文件名
```    
![](\img\in-post\post-postman\2021-01-30-postman-auto-13.png)     
![](\img\in-post\post-postman\2021-01-30-postman-auto-14.png)   

5.打开测试报告
![](\img\in-post\post-postman\2021-01-30-postman-auto-15.png) 