---
layout: post
title: "xpath helper | Mac 下的离线安装与使用"
subtitle: '快速生成或解析 xpath 路径'
author: "Haauleon"
header-style: text
tags:
  - Chrome 扩展
---  


### 背景
&emsp;&emsp;最近接盘了 py 项目，里面用到了访问 HTML DOM 节点的 xpath 选择器，然后我又不想逐个逐个去看 html 源代码具体定位了什么，这真的太耗时间了。 
<br>    

### 插件介绍  
&emsp;&emsp;google 插件 XPath Helper，可以支持在网页点击元素生成 xpath，整个抓取使用了xpath、正则表达式、消息中间件、多线程调度框架（参考）。xpath 是一种结构化网页元素选择器，支持列表和单节点数据获取，他的好处可以支持规整网页数据抓取。
如果我们要查找某一个、或者某一块元素的 xpath 路径，可以按住 shift，并移动到这一块中，上面的框就会显示这个元素的 xpath 路径，右边则会显示解析出的文本内容。还可以编辑 xpath 路径，程序也会自动的显示对应的位置，可用于协助判断我们的 xpath 语句是否书写正确。     
<br>

### 插件安装      
链接：[https://pan.baidu.com/s/1Fk_nYik75LKkagIT1hxWZQ](https://pan.baidu.com/s/1Fk_nYik75LKkagIT1hxWZQ) &emsp;&emsp;提取码：lj06        

&emsp;&emsp;下载至本地后，在 chrome 浏览器地址栏输入 `chrome://extensions/` 打开扩展程序页面，启用右上角的**开发者模式**，再点击**加载已解压的扩展程序**，然后选择此目录即可。
<br>


### 插件使用
1. 在当前页面中启用插件   
`ctrl + shift + x`      
<br>
2. 快速生成 xpath 路径     
按住 `shift` 键并拖动鼠标移动到要定位的元素     
<br>
3. 解析 xpath 路径    
将 xpath 路径粘贴进 Query 输入框中，可自动解析      
<br>
4. 在当前页面中关闭插件   
`ctrl + shift + x`