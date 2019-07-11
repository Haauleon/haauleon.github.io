---
layout: post
title: "Fiddler代理设置"
subtitle: '一次性填完Fiddler设置的所有坑'
author: "Haauleon"
header-style: text
tags:
  - Fiddler
---

&emsp;&emsp;在装完了全部的环境之后，终于在今天用上了台式机，然而抓包工具fiddler在设置代理的时候踩了不少坑，现在来总结一下。下面放一张图来冷静冷静。
![](https://wx4.sinaimg.cn/mw1024/9c1edeb6gy1fw26mogygej20kb0bp0us.jpg)


## 背景

&emsp;&emsp;之前使用的是一台i3_2GHz处理器、4.00GB的64位笔记本电脑，明显感觉做啥啥不行，后来换了台台式机，最糟心的就是要重新装环境。由于之前一直用的笔记本电脑，突然要我驾驭台式机多少有点不习惯。虽说都是电脑，但还是有一些明显的区别的。比如大多数的笔记本天生自带无线网卡，而大部分的台式机都没有这方面的需求，主要靠用户后期自行安装无线网卡。


## 目的

1.台式机连接无线网络     

2.Fiddler设置手机代理，成功抓取手机http网络数据      

3.Fiddler设置PC端代理，浏览器导入Fiddler证书并成功抓取https网络数据      

4.解决Chrome导入Fiddler证书问题 

   


## 台式机连接无线网络

Step1:                               

检查台式机有无安装无线网卡（我这台是已经安装好了的）。大部分的台式机都没有安装无线网卡，都是需要后期自己手动安装的，无线网卡的功能在这里体现为wifi的接收。   

![](https://wx2.sinaimg.cn/mw1024/9c1edeb6gy1fw27o1m2c4j20xc0ir0wz.jpg)                  
                                                                                    
Step2:           

购买无线网卡（我这里安装的是USB无线网卡）。这还是我跟公司的前台妹妹拿的，拿回来的时候只有一个USB接口的无线网卡，没有驱动。建议可以从某宝上买一个无线网卡，里面会有配套的无线网卡和光盘驱动。某宝好多产品都说是免驱安装，没试过，我用的是下面这款。   

![](https://wx1.sinaimg.cn/mw1024/9c1edeb6gy1fw27o2evx8j20kz07stfs.jpg)   
                  
Step3:     

安装驱动。根据无线网卡的型号，百度搜索对应的驱动并下载安装，安装成功后如Step1的图片显示。   
              
![](https://wx3.sinaimg.cn/mw1024/9c1edeb6gy1fw27o1f9nrj20i902i745.jpg)   
               
Step4：     

插上USB无线网卡。插上无线网卡后，点击电脑右下角-连接到网络，将会显示无线网络供选择。   

![](https://wx1.sinaimg.cn/mw1024/9c1edeb6gy1fw27o1fyjij20960axta1.jpg)   
                
## Fiddler设置手机代理   

Step1:      

搜索fiddler并下载安装。我这里为了方便直接在“软件管理”客户端进行下载安装，快速敏捷又方便。       

![](http://wx3.sinaimg.cn/mw690/9c1edeb6gy1fw37v0xhp3j20vb0h7772.jpg)     
               
Step2:     

设置fiddler--Tools>Fiddler Options>https选项。     

![](http://wx1.sinaimg.cn/mw690/9c1edeb6gy1fw37v56jnnj20ml0d1dhh.jpg)       
                
Step3:       

设置fiddler--Tools>Fiddler Options>connections选项。这里的端口port需要记一下，手机设置代理时需要用到。       

![](http://wx2.sinaimg.cn/mw690/9c1edeb6gy1fw37v9g3pfj20mp0d0dh5.jpg)      
            
Step4:       

设置完之后，重启fiddler。打开cmd控制台，输入ipconfig获取IPV4地址。这里的IP也需要记一下，手机设置代理时需要用到。          

![](http://wx3.sinaimg.cn/mw690/9c1edeb6gy1fw37vcjraxj20it0caaas.jpg)       
                             
Step5:            

打开手机WLAN，连接的wifi需要和电脑连接的wifi是一样的，然后在wifi详情页面设置代理信息，分别写入IP地址和端口port。估计不同的手机系统对应的页面不一样，但是设置的的信息是一样的。设置完成后打开fiddler，会有不一样的惊喜。以上步骤只能抓取到http，抓取https的操作步骤后期会进行更新。         

![](http://wx3.sinaimg.cn/mw690/9c1edeb6gy1fw37vfy3uhj20u01hc0xn.jpg)              
                                    
## Chrome导入Fiddler证书问题 

下面来展示一下我遇到的第一个坑--在Fiddler中导出证书，却提示“creation of the root certificate was not located”无法生成证书。Tools>Fiddler Options>https选项>Action>Export Root...          

![](http://wx1.sinaimg.cn/mw690/9c1edeb6gy1fw490bmrm1j20jm08bdis.jpg)        

Step1:          

无法生成证书时，需要下载证书生成器，下载完成后进行安装，我是直接安装到桌面。        
[fiddlercertmaker证书生成器地址](http://www.telerik.com/docs/default-source/fiddler/addons/fiddlercertmaker.exe?sfvrsn=2)          

![](http://wx2.sinaimg.cn/mw690/9c1edeb6gy1fw490ggajuj207s049js2.jpg)        

Step2:        

再在fiddler重复证书导出步骤。       

![](http://wx1.sinaimg.cn/mw690/9c1edeb6gy1fw490j9ahlj20mc0coadl.jpg)      

![](http://wx4.sinaimg.cn/mw690/9c1edeb6gy1fw490n613ej20fh0act9a.jpg)       

Step3:        

这时在我的桌面会生成一个证书，长这个样子。       

![](https://wx2.sinaimg.cn/mw1024/9c1edeb6gy1fw55fmv005j207k03jq3d.jpg)      

Step4:       

证书生成后，导入证书至Chrome浏览器。     

![](https://wx3.sinaimg.cn/mw1024/9c1edeb6gy1fw58a1cshoj219k0pgmyu.jpg)     

![](https://wx2.sinaimg.cn/mw1024/9c1edeb6gy1fw58a611wkj20mp0cvjsz.jpg)         

![](https://wx4.sinaimg.cn/mw1024/9c1edeb6gy1fw58a80n2cj20mi0920ta.jpg)      

![](https://wx2.sinaimg.cn/mw1024/9c1edeb6gy1fw58aalib9j20m00c8wf2.jpg)      

![](https://wx1.sinaimg.cn/mw1024/9c1edeb6gy1fw58ac5wxvj20lv0cedh7.jpg)        

![](https://wx2.sinaimg.cn/mw1024/9c1edeb6gy1fw58agu43hj20ea0ccweu.jpg)           

![](https://wx2.sinaimg.cn/mw1024/9c1edeb6gy1fw58akq2k5j20ef0cadgc.jpg)               

Step5:        

重启fiddler，再次打开fiddler设置，重置证书。      

![](https://wx3.sinaimg.cn/mw1024/9c1edeb6gy1fw58anfce4j20l30c1mzy.jpg)         

Step6:        

重启浏览器和fiddler，浏览器进行百度搜索，即可以抓取https数据包。      

![](https://wx4.sinaimg.cn/mw1024/9c1edeb6gy1fw58argiplj21h40cewhk.jpg)         

<font face="STCAIYUN">以上就是填坑的全部过程啦，自己挖的坑最终还是要自己填滴，年轻人。如对以上说明存有疑惑，请点击下方的邮箱联系我吧。</font>