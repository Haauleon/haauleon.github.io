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

#### 1、获取数据库文件
&emsp;&emsp;数据库文件中存储了微信聊天记录，我们需要找到这个文件的存放路径，并复制到模拟器的分享文件夹中。     

1. 打开模拟器的 `R.E.管理器`     
    ![](\img\in-post\post-python\2022-12-15-python-wechat-18.jpg)  
2. 点击进入目录 /data/data/com.tencent.mm/MicroMsg      
    ![](\img\in-post\post-python\2022-12-15-python-wechat-19.jpg)  
3. 进入第一个目录并找到 EnMicroMsg.db 文件      
    ![](\img\in-post\post-python\2022-12-15-python-wechat-20.jpg)   
    ![](\img\in-post\post-python\2022-12-15-python-wechat-21.jpg)    
4. 在模拟器中通过鼠标长按左键对 EnMicroMsg.db 文件进行复制      
    ![](\img\in-post\post-python\2022-12-15-python-wechat-22.jpg)    
5. 将文件复制后，粘贴到 /sdcard/windows/BstSharedFolder 目录下     
    ![](\img\in-post\post-python\2022-12-15-python-wechat-23.jpg)    
6. 粘贴成功后就可以在本地电脑路径 D:\Program Files (x86)\BluestacksCN\Engine\ProgramData\Engine\UserData\SharedFolder 中找到此文件     
    D:\Program Files (x86)\BluestacksCN 是蓝叠的安装目录。     
    ![](\img\in-post\post-python\2022-12-15-python-wechat-24.jpg)    
7. 如果想在模拟器中快速将 EnMicroMsg.db 文件转存到电脑本地的其他路径中，可以在多媒体管理器中进行转存       
    （1）在模拟器中打开多媒体管理器     
    ![](\img\in-post\post-python\2022-12-15-python-wechat-25.jpg)      
    （2）选择文件并导出到电脑本地    
    ![](\img\in-post\post-python\2022-12-15-python-wechat-26.jpg)      
    ![](\img\in-post\post-python\2022-12-15-python-wechat-27.jpg)      
    ![](\img\in-post\post-python\2022-12-15-python-wechat-28.jpg)      
    ![](\img\in-post\post-python\2022-12-15-python-wechat-29.jpg)      


<br>
<br>

#### 2、获取 IMEI 值
&emsp;&emsp;需要在模拟器中安装第三方 apk 包进行获取，将以下提供的 apk 包导入进本地共享文件夹 D:\Program Files (x86)\BluestacksCN\Engine\ProgramData\Engine\UserData\SharedFolder 中，然后在模拟器中安装此应用即可获取 IMEI 值。      

1. 离线百度云网盘下载     
    链接：https://pan.baidu.com/s/1rd4_2SvAUpmqZ4cKvBiBvA?pwd=ih6n     
    提取码：ih6n   
2. 将下载的文件复制粘贴到共享文件夹 D:\Program Files (x86)\BluestacksCN\Engine\ProgramData\Engine\UserData\SharedFolder 中     
    ![](\img\in-post\post-python\2022-12-15-python-wechat-30.jpg)      
3. 在模拟器中的 `R.E.管理器` 中的 /sdcard/windows/BstSharedFolder 找到此 apk 包并双击进行安装
    ![](\img\in-post\post-python\2022-12-15-python-wechat-31.jpg)     
4. 安装成功后点击打开即可获取到 IMEI 值      
    ![](\img\in-post\post-python\2022-12-15-python-wechat-32.jpg)     


<br>
<br>

#### 3、获取 uin 值


<br>
<br>


### 三、生成微信聊天词云
&emsp;&emsp;将微信聊天记录文本进行数据分析后生成词云。    

<br>

#### 1、