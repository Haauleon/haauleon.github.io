---
layout: post
title: "Postman应用之mock server"
subtitle: 'mock server定义'
author: "Haauleon"
header-style: text
tags:
  - Postman
  - mockServer
---


&emsp;&emsp;之前浏览技术网站的时候，看到很多走在前沿的大神们都在使用mock&#32;server进行单元测试，当时还看得云里雾里，直到刚刚看到postman里面有mock&#32;server的介绍，就翻来看看，还不错，挺好玩的。         




## mock简介 

### 为什么要用到mock
&emsp;&emsp;mock这词其中一个意思是模仿。主要是针对单元测试的应用，用来辅助做单元测试。因为实际生产中的项目是非常复杂的，对其进行单元测试的时候，会遇到以下问题：         
（1）接口的依赖       
（2）外部接口调用         
（3）测试环境非常复杂        

### mock解决了什么问题
&emsp;&emsp;使用mock可以很方便的解除单元测试中各种依赖，大大的降低了编写单元测试的难度。单元测试应该只针对当前单元进行测试，所有的内部或外部的依赖应该是稳定的。使用mock就可以对外部依赖组件实现进行模拟并且替换掉，从而使得单元测试将焦点只放在当前的单元功能。

### 使用mock的前提
&emsp;&emsp;这就得谈到**前后端分离**这种web架构模式中的数据接口规范流程了。在开发期间前后端共同商定好**数据接口**的交互形式和数据格式，然后实现前后端的并行开发。其中前端工程师在开发完成之后可以独自进行mock测试，而后端也可以使用接口测试平台进行接口自测，然后前后端一起进行**功能联调**并**校验格式**，最终进行单元自动化测试。    
   
&emsp;&emsp;所以这就很清楚了，mock测试的前提就是得有一份共同商定好的API规范文档。否则前端代码刚写完，后端的接口又变了，或者接口文档永远都是不对的，再或者前端团队的开发速度永远都跟不上后端出接口的速度，那么基本上就要和mock测试say googbye了。

### 如何使用mock      
&emsp;&emsp;在进行前端开发的时候，为了不依赖后端的进度（即开发进度：前端>后端），我们可以根据既定的API规范，搭建mock&#32;server，这样可以独立进行开发。等后端开发完毕，只是需要将请求地址由mock请求地址修改为后端服务地址既可。postman是个厉害的API工具，除了可以调试API之外，也支持创建mock服务。           


## mock server简介

### 定义
&emsp;&emsp;Postman的官方介绍是&#34;Delays&#32;on&#32;the&#32;front&#45;&#32;or&#32;back&#45;end&#32;make&#32;it&#32;difficult&#32;for&#32;dependent&#32;teams&#32;to&#32;complete&#32;their&#32;work&#32;efficiently&#46;&#32;Postman&#39;s&#32;mock&#32;servers&#32;can&#32;alleviate&#32;those&#32;delays&#32;in&#32;the&#32;development&#32;process&#46;Before&#32;sending&#32;an&#32;actual&#32;request&#44;&#32;front&#45;end&#32;developers&#32;can&#32;create&#32;a&#32;mock&#32;server&#32;to&#32;simulate&#32;each&#32;endpoint&#32;and&#32;its&#32;corresponding&#32;response&#32;in&#32;a&#32;Postman&#32;Collection&#46;&#32;Developers&#32;can&#32;view&#32;potential&#32;responses&#44;&#32;without&#32;spinning&#32;up&#32;a&#32;back&#32;end&#46;&#34;                   

&emsp;&emsp;意思是说：“前端或后端的延迟使得相互间有依赖的团队难以有效地完成工作，而Postman的mock&#32;server可以减轻开发过程中的延迟。在发送实际请求之前，前端开发人员可以创建mock&#32;server来模拟Postman&#32;Collection中的每个端点及其相应的响应。开发人员可以查看潜在的响应，而无需启动后端。”      


### 类型
Postman允许创建两种类型的mock&#32;server：private和public。

#### private 私有
&emsp;&emsp;私有mock&#32;server要求用户在请求标头中添加Postman API密钥。x&#45;api&#45;key&#58;&#60;your&#32;postman&#32;API&#32;key&#62;             

&emsp;&emsp;如果创建私有mock&#32;server，则用户可以与团队或特定团队成员共享基础集合，并提供编辑或查看的权限。团队成员可以使用他们的Postman API密钥来使用模拟。如果团队成员有权访问基础集合，则可以使用mock。     


#### public 公有
&emsp;&emsp;mock&#32;server默认是公共的。任何人都可以访问公共mock&#32;server。共享公共mock&#32;server时，用户无需添加Postman&#32;API密钥。
