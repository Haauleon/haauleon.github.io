---
layout:        post
title:         "Android | 获取 apk 的包名和主类名"
subtitle:      "对 apk 进行 debug 签名"
date:          2021-07-14
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - APP 测试
---

## 一、背景
&emsp;&emsp;Android 的相关测试是要重新签名的，在没有拿到开发人员签名文件时，只能自己对 apk 进行重新签名。市面上有相关插件可以辅助进行 debug 签名，如 re-sign 工具。       

&emsp;&emsp;获取 apk 文件的包名 `package name` 和 `main activity` 的目的，是为了对 apk 也就是被测试应用使用 adb 命令行进行调试，比如监控应用的启动时间和获取日志等等。     

<br>

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-1.png)   

<br><br>

## 二、环境配置
###### 1.环境准备
一部 windows 10 系统的笔记本

<br><br>

###### 2.安装 jdk
链接：https://pan.baidu.com/s/1v_7s29r8RAiZ5pWmBEI6XQ          
提取码：u8xd     

&emsp;&emsp;把网盘中的 jdk 二进制文件下载下来后自动安装到 C 盘 `C:\Program Files\Java\jdk1.8.0_291` 即可。   

<br><br>

###### 3.配置 JAVA_HOME 
（1）右键点击打开 `此电脑 > 属性 > 高级系统设置 > 环境变量`。       

（2）新增一个系统变量 JAVA_HOME，变量配置如下：      
```
变量名    JAVA_HOME
变量值    C:\Program Files\Java\jdk1.8.0_291
```

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-7.png)    

<br>

（3）编辑 Path 变量值后点击保存即可：    
```
新增变量值：
%JAVA_HOME%\bin
```    

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-8.png)

<br>

（4）进入 cmd 检查是否配置成功：     
```
$ java -version
```

<br><br>

###### 4.下载 android-sdk
链接：https://pan.baidu.com/s/12qz2QbF3EIcNAqovTBpq2Q       
提取码：afos    

&emsp;&emsp;下载后解压即可，我这里是解压到 `D:\software\android-sdk-windows`。    

<br><br>

###### 5.配置 ANDROID_HOME 
（1）右键点击打开 `此电脑 > 属性 > 高级系统设置 > 环境变量`。       

（2）新增一个系统变量 ANDROID_HOME，变量配置如下：      
```
变量名    ANDROID_HOME
变量值    D:\software\android-sdk-windows
```

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-9.png)    

<br>

（3）编辑 Path 变量值后点击保存即可：         
```
新增变量值：
%ANDROID_HOME%\platform-tools
%ANDROID_HOME%\tools
%ANDROID_HOME%\build-tools\29.0.3
```

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-10.png)    

<br>

（4）新增一个系统变量 CLASSPATH，变量配置如下：      
```
变量名    CLASSPATH
变量值    %JAVA_HOME%\bin;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar
```

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-11.png) 

<br><br>

###### 6.下载 zipalign.exe 
链接：https://pan.baidu.com/s/1n1SzDpkM6JcPYAMaTV5v5A        
提取码：5t1u     

&emsp;&emsp;下载后将此文件复制到路径 `D:\software\android-sdk-windows\tools` 下即可。

<br><br>

###### 7.下载 re-sign.jar
链接：https://pan.baidu.com/s/1wfBzhnavObWva1_Rd9wmyg          
提取码：5dzu 

<br><br>

## 三、获取 apk 文件
1.使用 usb 数据线连接安卓设备     
2.初始化环境    
```
$ adb kill-server
$ adb start-server
```   

3.获取设备所有 apk 的包名     
```
$ adb shell pm list package
```   

4.获取指定包名的 apk 存放位置     
```
$ adb shell pm path [package name]

示例：
$ adb shell pm path com.bringbuyshare
package:/data/app/com.bringbuyshare-1/base.apk
```  

5.将 apk 安装包拉到本地电脑     
```
$ adb pull [包名的绝对路径] [拉取到本地的绝对路径] 

示例：
$ adb pull /data/app/com.bringbuyshare-1/base.apk D:\software\android-sdk-windows\apks
```

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-2.png)

<br><br>

## 四、debug 签名
###### 1.启动 re-sign 工具
```
$ java -jar [re-sign.jar 文件的绝对路径]

示例：
C:\Users\Haauleon>java -jar d:\software\re-sign.jar
Running jarsigner
Command line: C:\Program Files\Java\jdk1.8.0_291/bin/jarsigner -keystore C:\Users\Haauleon/.android/debug.keystore -storepass android -keypass android C:\Users\Haauleon\AppData\Local\Temp\resigner2212093146033715047.apk androiddebugkey
jarsigner finished with following output:
jarsigner ?í?ó: java.lang.RuntimeException: ??????????: C:\Users\Haauleon\.android\debug.keystore (?????????????¨????????)
Running zipalign
Command line: D:\software\android-sdk-windows/tools/zipalign -f 4 C:\Users\Haauleon\AppData\Local\Temp\resigner2212093146033715047.apk D:\software\android-sdk-windows\apks\base_debug.apk
```   

&emsp;&emsp;工具启动成功，即可打开一个小窗口。    

<br>

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-3.png)

<br><br>

###### 2.获取包名和主类名
&emsp;&emsp;将本地拉取到的 base.apk 文件拉取到上图的小窗口中，生成一个新的 base_debug.apk 文件的同时提示重新签名成功，获取包名和主类名成功。        

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-4.png)    

<br>

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-5.png)   

<br>

![](\img\in-post\post-app-test\2021-07-14-adb-apk-pull-6.png)