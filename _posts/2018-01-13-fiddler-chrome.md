---
layout:        post
title:         "Fiddler | 设置浏览器代理"
subtitle:      "Chrome 浏览器导入 fiddler 证书"
date:          2018-01-13
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Fiddler
---


## 背景
&emsp;&emsp;在 Fiddler 中导出证书。执行完操作 `Tools > Fiddler Options > https选项 > Action > Export Root…` 后，却提示 `“creation of the root certificate was not located”` 无法生成证书。         
![](\img\in-post\post-fiddler\2018-01-13-fiddler-chrome-1.png)          

<br><br>

## 解决方法
###### 一、下载安装证书生成器     
&emsp;&emsp;无法生成证书时，需要下载证书生成器，下载完成后进行安装，我是直接安装到桌面。[fiddlercertmaker证书生成器地址](http://www.telerik.com/docs/default-source/fiddler/addons/fiddlercertmaker.exe?sfvrsn=2)         

<br><br>

###### 二、fiddler 导出证书       
&emsp;&emsp;再在fiddler重复证书导出步骤。                    
![](\img\in-post\post-fiddler\2018-01-13-fiddler-chrome-2.png)          

<br>
 
![](\img\in-post\post-fiddler\2018-01-13-fiddler-chrome-3.png)            

<br><br>

###### 三、检查证书导出情况        
&emsp;&emsp;导出成功后，在桌面会生成一个证书，长这个样子。         
![](\img\in-post\post-fiddler\2018-01-13-fiddler-chrome-4.png)          

<br><br>

###### 四、Chrome 浏览器导入证书     
&emsp;&emsp;证书生成后，导入证书至 Chrome 浏览器。                
![](\img\in-post\post-fiddler\2018-01-13-fiddler-chrome-5.png)          

<br>

![](\img\in-post\post-fiddler\2018-01-13-fiddler-chrome-6.png)       

<br>
 
![](\img\in-post\post-fiddler\2018-01-13-fiddler-chrome-7.png)       

<br>

![](\img\in-post\post-fiddler\2018-01-13-fiddler-chrome-8.png)       

<br>   

![](\img\in-post\post-fiddler\2018-01-13-fiddler-chrome-9.png)       

<br>

![](\img\in-post\post-fiddler\2018-01-13-fiddler-chrome-10.png)       

<br> 

![](\img\in-post\post-fiddler\2018-01-13-fiddler-chrome-11.png)          

<br><br>

###### 五、重启 fiddler，重置证书        
&emsp;&emsp;重启 fiddler，再次打开 fiddler 设置，重置证书。      
![](\img\in-post\post-fiddler\2018-01-13-fiddler-chrome-12.png)         

<br><br>  

###### 六、重启浏览器和 fiddler    
&emsp;&emsp;重启浏览器和 fiddler，浏览器进行百度搜索，即可以抓取 https 数据包。             
![](\img\in-post\post-fiddler\2018-01-13-fiddler-chrome-13.png) 









