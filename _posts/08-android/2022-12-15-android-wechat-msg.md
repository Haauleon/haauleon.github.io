---
layout:        post
title:         "数据分析 | 微信聊天记录统计"
subtitle:      "获取自己和朋友的微信聊天记录，并做简单的数据分析统计"
author:        "Haauleon"
header-img:    "img/in-post/post-app-test/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - 数据分析
    - Android
    - Python
---

### 背景
&emsp;&emsp;需求是获取我和欢欢的全部微信聊天记录存为文本数据，然后进行数据分析和生成词云。由于我的安卓手机没有越狱，所以这里用到了模拟器。      

<br>
<br>

### 一、获取微信聊天记录
&emsp;&emsp;通过模拟器获取聊天记录文件。    

<br>

#### 1、安装蓝叠模拟器
**方法 1**      
去[官网](https://www.bluestacks.cn/) 下载 BlueStacks 蓝叠4，下载地址：      
[http://aliosscdn.bluestacks.cn/client/BlueStacks4Setup.exe](http://aliosscdn.bluestacks.cn/client/BlueStacks4Setup.exe)     

**方法 2**     
百度网盘离线下载安装：       
链接：[https://pan.baidu.com/s/1CHMQ5890bKNhYkca_7t4Ow?pwd=6qmp](https://pan.baidu.com/s/1CHMQ5890bKNhYkca_7t4Ow?pwd=6qmp)           
提取码：6qmp   

<br>
<br>

#### 2、模拟器安装微信
&emsp;&emsp;需要进入模拟器，并在模拟器中安装微信应用。     

1. 进入应用中心     
    ![](\img\in-post\post-python\2022-12-15-python-wechat-1.jpg)    
2. 搜索微信并安装    
    ![](\img\in-post\post-python\2022-12-15-python-wechat-2.jpg)    

<br>
<br>

#### 3、聊天记录备份到电脑
&emsp;&emsp;手机和电脑同时登录微信且都处于同一局域网中，然后将手机中的聊天记录备份到电脑中。     

1. 手机和电脑同时登录且处于同一局域网     
2. 电脑版微信点击左下角的 `迁移与备份`      
    ![](\img\in-post\post-python\2022-12-15-python-wechat-3.jpg)      
3. 选择 `备份与恢复`     
    ![](\img\in-post\post-python\2022-12-15-python-wechat-4.jpg)      
4. 点击 `备份聊天记录至电脑`     
    ![](\img\in-post\post-python\2022-12-15-python-wechat-5.jpg)      
5. 在手机微信中点击 `选择聊天记录` 来选取上传     
    ![](\img\in-post\post-python\2022-12-15-python-wechat-6.jpg)   
    ![](\img\in-post\post-python\2022-12-15-python-wechat-7.jpg)         
6. 等待备份完成即可

<br>
<br>

#### 4、聊天记录恢复到模拟器
&emsp;&emsp;恢复到模拟器的微信中这一步有个小技巧。     

1. 在模拟器的微信中使用账号进行登录（由于是新设备，所以需要手机微信进行授权，授权成功后手机微信会自动退登并且电脑微信也会退登）          
    ![](\img\in-post\post-python\2022-12-15-python-wechat-8.jpg)  
2. 登录电脑微信会提示你需要重新扫码，这里有个小技巧，就是先用手机把二维码拍下来，然后进入模拟器的微信页面点击 `扫一扫`，这时候就将刚拍下来的二维码给它识别就可以登录电脑版微信了      
    ![](\img\in-post\post-python\2022-12-15-python-wechat-9.jpg)  
    ![](\img\in-post\post-python\2022-12-15-python-wechat-10.jpg)  
3. 在电脑版微信中点击 `恢复聊天记录至手机`     
    ![](\img\in-post\post-python\2022-12-15-python-wechat-11.jpg)    
    ![](\img\in-post\post-python\2022-12-15-python-wechat-12.jpg)    
    ![](\img\in-post\post-python\2022-12-15-python-wechat-13.jpg)     
4. 在模拟器微信弹出的窗口中点击 `开始恢复`    
    ![](\img\in-post\post-python\2022-12-15-python-wechat-14.jpg)    
    ![](\img\in-post\post-python\2022-12-15-python-wechat-15.jpg)        
5. 等待记录上传完成即可

<br>
<br>


#### 5、开启获取 ROOT 权限 
&emsp;&emsp;获取 root 权限，是为了为获取聊天记录文件做准备。    

1. 打开模拟器的设置下拉框     
    ![](\img\in-post\post-python\2022-12-15-python-wechat-16.jpg)  
2. 在引擎设置页面勾选 `获取Root权限` 并点击 `确定`         
    ![](\img\in-post\post-python\2022-12-15-python-wechat-17.jpg)  
3. 打开模拟器的设置下拉框并点击 `重启引擎` 即可    

<br>
<br>

### 二、查看微信聊天记录
&emsp;&emsp;将聊天记录文件进行解密以此来查看。     

<br>

#### 1、


### 三、生成微信聊天词云
&emsp;&emsp;将微信聊天记录文本进行数据分析后生成词云。    

<br>

#### 1、