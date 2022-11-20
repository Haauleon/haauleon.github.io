---
layout:        post
title:         "Charles | https 证书设置"
subtitle:      "在 win10 系统中导入 Charles CA 证书"
author:        "Others"
header-img:    "img/in-post/post-charles/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
  - Charles
---

&emsp;&emsp;首先说明一点，即使按照下面的操作，也不可能抓到所有的https请求，否则网络安全做的也太差了。要抓https，首先要安装证书。       

<br><br>

### 设置步骤
###### 一、PC端安装证书
1、安装证书：Charles -> Help -> SSL Proxying -> Install Charles Root Certificate，直接点击安装。     

**注意：**下面选项选择【将所有的证书都放入下列存储】，点击浏览，选择【受信任的根证书颁发机构】，这样安装的证书，直接就是受信任的证书。        

![](\img\in-post\post-charles\2021-10-15-charles-https-1.png)          

<br>

![](\img\in-post\post-charles\2021-10-15-charles-https-2.png)      

<br>

2、如果一直按照默认选项，装好之后该证书默认是不受信任的。还需要信任证书。为了不影响介绍 Charles 的整体性，在该篇最后再介绍在 windows 系统信任证书的步骤。        

<br><br>

###### 二、在移动端安装证书
方法1：手机连代理，在移动端浏览器输入 [http://charlesproxy.com/getssl](http://charlesproxy.com/getssl) ，然后会弹出一个界面，让输入证书的名字，直接输入 Charles 就可以。安装成功后会提示证书安装成功。      
方法2：手机连接电脑代理，用手机浏览器搜索 chls.pro/ssl ，下载并安装证书。      

**注意：**下载证书后，要记得在手机上信任证书。苹果手机可以在设置里搜索【信任】，点开证书信任设置，信任证书即可。      

<br><br>

###### 三、PC 端 Charles 设置
1、Charles -> Proxy -> Proxy Settings，勾选 Enabling transparent HTTP proxying      

![](\img\in-post\post-charles\2021-10-15-charles-https-3.png)    

<br>

2、Charles -> Proxy -> SSL Proxying Settings，点【Add】     

![](\img\in-post\post-charles\2021-10-15-charles-https-4.png)      

<br>

3、输入 host 和 port，如果都输入星号 `*`，则可以抓所有的 https 请求。    

![](\img\in-post\post-charles\2021-10-15-charles-https-5.png)      

<br>

&emsp;&emsp;到这里就设置完毕了，可以去抓包啦。        

<br><br>

###### 四、Windows 系统信任 Charles 证书步骤
（1）组合键 win + r 打开运行输入框，输入 mmc     

![](\img\in-post\post-charles\2021-10-15-charles-https-6.png)      

<br>

（2）弹出以下窗口      

![](\img\in-post\post-charles\2021-10-15-charles-https-7.png)      

<br>

（3）点击文件 -> 添加/删除管理单元，选择【证书】，并点击【添加】      

![](\img\in-post\post-charles\2021-10-15-charles-https-8.png)      

<br>

（4）在弹出的窗口选择【我的用户账户】，点【确定】      

![](\img\in-post\post-charles\2021-10-15-charles-https-9.png)      

<br>

（5）选择左边窗口的 中间证书颁发机构 -> 证书，找到 Charles Proxy CA，右键复制         

![](\img\in-post\post-charles\2021-10-15-charles-https-10.png)      

<br>

（6）在左边窗口 “个人” 右键粘贴       

![](\img\in-post\post-charles\2021-10-15-charles-https-11.png)      

<br>

（7）在 受信任的根证书颁发机构 -> 证书 右键粘贴      

![](\img\in-post\post-charles\2021-10-15-charles-https-12.png)      

<br>

（8）退出窗口并保存此控制台 1 即可      

（9）重启 Charles 即可抓取 https 请求