---
layout: post
title: "有趣的Bug"
subtitle: '似乎高级玩家才会输入实体编号来试错？'
author: "Haauleon"
header-style: text
tags:
  - HTML
  - 特殊字符
  - Bug
---

&emsp;&emsp;最近客户反馈的问题让我脑壳顿时一疼，貌似生活当中应该没啥人会喜欢在标题内容用实体编号来替代字符吧，当然这确实也是编码的问题，所以今天来说说HTML实体编号的那事儿。自从粉上毛不易，每天下班都要刷下他的经典语录，很庆幸自己喜欢的是这么一个温暖的人，照旧放张毛毛的图片来镇楼。            

![](\img\in-post\2018-10-25-SurpriseBug\1.jpg)




## 背景

&emsp;&emsp;我们都知道，在网页的制作过程中有一些特殊的符号需要代码进行替代。在HTML中不能使用小于号（&lt;）和大于号（&gt;），这是因为浏览器会误认为它们是标签。如果希望正确地显示预留字符，我们必须在HTML源代码中使用字符实体（character entities）。如需显示小于号，我们必须这样写：&amp;lt; 或 &amp;#60;。       

```
字符实体类似这样：

&entity_name;     /*实体名称*/

或者

&#entity_number;  /*实体编号*/
```         



## Bug重现        

![](\img\in-post\2018-10-25-SurpriseBug\2.jpg)    

![](\img\in-post\2018-10-25-SurpriseBug\3.jpg)       



## Bug扩展       

![](\img\in-post\2018-10-25-SurpriseBug\4.jpg)      

![](\img\in-post\2018-10-25-SurpriseBug\5.jpg)      



## 附件       

[HTML字符实体](http://www.w3school.com.cn/html/html_entities.asp)      

[HTML转义字符对照表-部分](https://blog.csdn.net/qq_42374362/article/details/80867292)     