---
layout:        post
title:         "影刀RPA | 紫鸟浏览器自动化"
subtitle:      "解决紫鸟浏览器自动化插件安装问题"
author:        "Haauleon"
header-img:    "img/in-post/post-rpa/bg.jpg"
header-mask:   0.4
catalog:       true
tags:
    - 影刀RPA
---

### 介绍
&emsp;&emsp;紫鸟超级浏览器是一款专门针对跨境电商卖家、安全的多店铺管理工具一站式轻松解决亚马逊、Wish、eBay等所有电商平台多店铺管理问题。许多小伙伴对紫鸟浏览器自动化也是有较大的需求。早期由于一些原因，影刀无法直接驱动紫鸟浏览器，只能将之当做一个普通软件去操作。流程的编写和维护也是需要相当多的时间（没错就是在下了，采用了很多图像识别和 win 元素判断....）                  
&emsp;&emsp;But 时代变了~经过双方不断的沟通交流，影刀现在已经再次支持操作紫鸟浏览器了。还有一些小伙伴在紫鸟自动化方面有些疑问，小白在这边分享如何安装自动化插件以及踩坑的一些经验。（后附几个问题点）          

<mark>必要条件：请将紫鸟浏览器升级至5.240.0.14及以上</mark>          
![](\img\in-post\post-rpa\2023-12-13-yingdao-ziniao-1.png)       

<br>
<br>

### 插件安装
1、紫鸟浏览器账号登录，进入到插件管理界面          
![](\img\in-post\post-rpa\2023-12-13-yingdao-ziniao-2.png)                 
![](\img\in-post\post-rpa\2023-12-13-yingdao-ziniao-3.png)                 

<br>

2、搜索影刀插件，授权，获取       
![](\img\in-post\post-rpa\2023-12-13-yingdao-ziniao-4.png)                 

<br>

3、分配账号（重点来了）            
![](\img\in-post\post-rpa\2023-12-13-yingdao-ziniao-5.png)           

<mark>控制台（工作台）这边千万不要分配上</mark>。用过紫鸟的都知道，紫鸟有2个窗口。如下图所示，左侧是工作台（以下简称大S浏览器），右侧才是我们想要的打开的跨境网页（简称小s浏览器）。实测，如果分配了控制台，会出现以下情况：大S浏览器的元素都能捕获，能驱动但是没法操作。而且最核心的我们需要的小s浏览器这边在捕获元素的时候就会提示重装插件。                                  
![](\img\in-post\post-rpa\2023-12-13-yingdao-ziniao-6.png)           

<br>

4、分配好插件之后做客户端配置             
注意：此步骤是临时解决方案，5.10版本后只需执行一次自定义浏览器安装流程，无需手动查找superbrowser.exe的路径。                
打开紫鸟浏览器后打开任务管理器，找到浏览器的可执行文件路径。注：浏览器的进程名是superbrowser，启动器的进程名是Launcher，需要获取superbrowser.exe的可执行文件路径。                    
<mark>在只有工作台的情况下，打开任务管理器。选中紫鸟浏览器的进程</mark>。                      
![](\img\in-post\post-rpa\2023-12-13-yingdao-ziniao-7.png)           

<br>

5、随便打开一个跨境店铺网页（小s浏览器），你就会发现进程里面多了一个紫鸟浏览器，那个才是我们真正需要的。移动到小s浏览器，右键，转到文件所在位置，记录下这个位置。            
![](\img\in-post\post-rpa\2023-12-13-yingdao-ziniao-8.png)           

<br>

6、在工具-自动化插件-添加自定义浏览器自动化-手动选择-找到浏览器的可执行文件         
注意：添加自定义浏览器时会自动扫描到一个紫鸟浏览器，请勿选择这个，一定要通过<mark>点击手动选择按钮</mark>，然后在对话框里面选择上面找到的superbrowser.exe文件路径（上面记录的路径）                   
![](\img\in-post\post-rpa\2023-12-13-yingdao-ziniao-9.png)         
![](\img\in-post\post-rpa\2023-12-13-yingdao-ziniao-10.png)         
![](\img\in-post\post-rpa\2023-12-13-yingdao-ziniao-11.png)         
![](\img\in-post\post-rpa\2023-12-13-yingdao-ziniao-12.png)         

<br>
<br>

### 还存在的问题
&emsp;&emsp;目前还存在的几个问题，欢迎大家提出解决办法相互交流。          
&emsp;&emsp;因为工作台和浏览器只能分配一个插件，所以只有一个能通过驱动操作。并且紫鸟浏览器不像Hubstudio一样能通过接口获取环境数量、情况（可能也是我没找到，翻了一圈。如果有找到接口的小伙伴欢迎提出更正）所以如果想打开店铺环境，需要将工作台（大S浏览器）当做win元素或者结合图像识别去做。               
&emsp;&emsp;并行问题。实测下来无法同时打开多个店铺环境，如果打开了多个环境，只有第一个店铺环境能正常捕获操作，后续环境均会提示安装插件。                
&emsp;&emsp;打开店铺环境之后，当前界面为控制台界面（虽然是小s浏览器上的），捕获的元素均为win元素。此时就可以通过点击图标打开店铺或者直接通过影刀指令（打开网页）打开对应的店铺登陆界面。在没有打开店铺环境（即没打开小s浏览器）的情况下如果直接用指令打开网页会报错。                  
![](\img\in-post\post-rpa\2023-12-13-yingdao-ziniao-13.png)         

<br>
<br>

---

相关链接：    
[紫鸟浏览器自动化插件安装问题（踩坑）----By福建组](https://www.yingdao.com/community/detaildiscuss?id=953968fd-8221-42e5-a1bf-258f6f408600&tag=&from=userCenter&sort=createTime&page=1)