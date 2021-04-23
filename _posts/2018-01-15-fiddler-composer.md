---
layout:        post
title:         "Fiddler | 创建请求"
subtitle:      "如何创建一个请求？"
date:          2018-01-15
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Fiddler
---


## Composer 原理
&emsp;&emsp;Composer 可以篡改数据，但是篡改的数据是经过处理后的，例如Cookie中的数据，其实密码已经是加密了的。         
&emsp;&emsp;除此之外，该功能可以代替 postman 创建请求，或者说模拟发送请求。           

<br>

它能达到以下效果：
* 篡改请求
    * 更改 Cookie 后创建新的请求
    * 篡改请求数据后创建新的请求
* 单纯创建一个新的请求

<br><br>

## 使用方法
###### 篡改请求
**Step1：抓取源请求**         
&emsp;&emsp;先抓取到一个请求，然后将界面切到 Composer。   
![](\img\in-post\post-fiddler\2018-01-15-fiddler-composer-1.png)    

<br><br>

**Step2：添加请求副本**      
&emsp;&emsp;单击选定源请求，然后长按鼠标左键将源请求拖拽到 Composer 的空白框内，即创建了一个与源请求相同的副本。    
![](\img\in-post\post-fiddler\2018-01-15-fiddler-composer-2.png)     

<br><br>

**Step3：篡改请求数据**   
&emsp;&emsp;直接在 Composer 中存放数据的数据框内进行更改。   

<br><br>

**Step4：执行请求**   
&emsp;&emsp;篡改数据后，单击 Execute 按钮执行即可。（为了防止数据过多造成困扰，可以在 Execute 之前先清除下数据，这时候 Composer 中数据不会被清除）    
![](\img\in-post\post-fiddler\2018-01-15-fiddler-composer-3.png)      

<br><br>

###### 创建请求
&emsp;&emsp;创建一个新的请求，即不需要根据源请求来创建副本来进行编辑。直接进入 Composer 的空白框内自行根据需求进行添加即可。
![](\img\in-post\post-fiddler\2018-01-15-fiddler-composer-4.png)  