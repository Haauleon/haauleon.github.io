---
layout:        post
title:         "Fiddler | 微信小程序抓包"
subtitle:      "实现 windows 系统桌面版微信小程序抓包"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Fiddler
---

## 一、背景
&emsp;&emsp;今天前端同事给我加了体验版小程序的权限，正常反应就是手机微信扫一扫体验版二维码，然后授权登录进去看看页面接的数据对不对这样。果不其然，翻页失败，我就想要不就用 Charles 或者 Fiddler 代理看看是不是接口的问题。果不其然，在试过 N 多种配置方式、操作姿势后，仍然无法代理小程序的 https 接口。心想，要不就干脆用 postman 去请求接口检查一下？不，我就是我，是颜色不一样的花火。于是，我问了一下百度。果不其然，找到了答案。一顿操作猛如虎，终于实现了小程序抓包的愿望。                      

<br><br>

## 二、具体操作
###### 1.环境准备
一部 windows 10 系统的笔记本      
一个桌面版微信应用（当前版本 3.3.0.93）        
一个桌面版 Fiddler 应用（当前版本 v5.0.20）             

<br><br>

###### 2.操作步骤
（1）启动 Fiddler 应用                      
![](\img\in-post\post-fiddler\2021-07-09-fiddler-win-1.png)        

<br>

（2）配置 Fiddler 的 HTTPS 选项      
![](\img\in-post\post-fiddler\2021-07-09-fiddler-win-2.png)       

<br>

（3）点击桌面版微信侧边栏的小程序图标                
![](\img\in-post\post-fiddler\2021-07-09-fiddler-win-3.png)          

<br>

（4）选择并点击打开体验版小程序（需要权限）         
![](\img\in-post\post-fiddler\2021-07-09-fiddler-win-4.png)     

<br>

（5）成功抓包 HTTPS 接口     
![](\img\in-post\post-fiddler\2021-07-09-fiddler-win-5.png)