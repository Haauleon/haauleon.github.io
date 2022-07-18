---
layout:        post
title:         "Jmeter | MacOS 系统下的安装"
subtitle:      "下载、安装和汉化"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
---

### 一、安装 jdk
jmeter 安装需要依赖 jdk，jdk 版本要求 8 以上。安装步骤如下：           

###### 1、下载
在 [https://www.oracle.com/java/technologies/downloads/](https://www.oracle.com/java/technologies/downloads/) 下载jdk     
![](\img\in-post\post-jmeter\2022-07-08-jmeter-install-mac-1.png)    

<br>

###### 2、安装
下载成功后对 dmg 文件进行打开，安装(一直下一步就好了)。最后终端输入命令 `$ java -version`，正常显示 java 版本就说明安装完毕。      
![](\img\in-post\post-jmeter\2022-07-08-jmeter-install-mac-2.png)    

<br>

###### 3、配置环境变量
MAC OS 系统安装 JDK 不需要配置环境变量即可使用，但是一些特殊的开发环境需要明确配置 JAVA_HOME 环境变量。(根据实际情况可选)     

（1）查询 jdk 的安装目录         
终端执行 `$ /usr/libexec/java_home -V`, 由此可知 jdk 的目录在 /Library/Java/JavaVirtualMachines/jdk-12.0.1.jdk/Contents/Home      
![](\img\in-post\post-jmeter\2022-07-08-jmeter-install-mac-3.png)     

（2）进行环境变量配置       
1. 终端输入 `$ sudo vim ~/.bash_profile`    
2. 设置内容 （写自己的 JDK 路径）
    ```
    JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_291.jdk/Contents/Home   
    PATH=$JAVA_HOME/bin:$PATH:
    ```
3. 终端输入 `$ source .bash_profile`         
4. 终端输入 `$ echo $JAVA_HOME` , 返回路径即设置成功

<br>
<br>

### 二、安装 jmeter
###### 1、下载
jmeter下载： [https://jmeter.apache.org/download_jmeter.cgi](https://jmeter.apache.org/download_jmeter.cgi)        
![](\img\in-post\post-jmeter\2022-07-08-jmeter-install-mac-4.png)    

<br>

###### 2、解压
我这里下载的 tgz 包,这里对其进行解压得到 apache-jmeter-5.4.3     
```
$ tar zxvf apache-jmeter-5.4.3.tgz
```

<br>

###### 3、配置环境变量
1. 记录解压得到的 apache-jmeter-5.4.3 路径，如下路径为 /Users/shuozhuo/Applications/apache-jmeter-5.4.3        
    ![](\img\in-post\post-jmeter\2022-07-08-jmeter-install-mac-5.png)   
2. 终端输入 `$ open -e ~/.bash_profile` 打开文件，在其中加入如下语句保存后关闭           
    ```
    #jmeter相关配置
    export JMETER_HOME=/Users/shuozhuo/Applications/apache-jmeter-5.4.3
    export PATH=$PATH:$JMETER_HOME/bin
    ```
3. 终端输入 `$ source ~/.bash_profile` 使配置生效      

<br>

###### 4、jmeter 汉化
将 apache-jmeter-5.4.3/bin/jmeter.properties 文件中的 #language=en 更改为 language = zh_CN。      
![](\img\in-post\post-jmeter\2022-07-08-jmeter-install-mac-6.png)     

![](\img\in-post\post-jmeter\2022-07-08-jmeter-install-mac-7.png)

<br>

###### 5、打开 jmeter
终端输入 `$ jmeter` 即可打开汉化后的界面      
![](\img\in-post\post-jmeter\2022-07-08-jmeter-install-mac-8.png)

<br>
<br>

---
以上参考自 [https://blog.csdn.net/mijichui2153/article/details/125266695](https://blog.csdn.net/mijichui2153/article/details/125266695)