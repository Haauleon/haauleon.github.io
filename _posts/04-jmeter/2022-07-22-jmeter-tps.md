---
layout:        post
title:         "Jmeter | 压力测试查看TPS"
subtitle:      "通过命令行执行查看详细报告"
author:        "Haauleon"
header-img:    "img/in-post/post-jmeter/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Jmeter
    - 数据分析
---

### 一、准备工作
###### 1、下载JMeter的压缩包
进入官网 [https://jmeter.apache.org/download_jmeter.cgi](https://jmeter.apache.org/download_jmeter.cgi) 进行下载。    

<br>

###### 2、启动JMeter
进入根目录的 `/bin` ，双击 `jmeter.bat` 启动，出现一个 cmd 的界面和我们的 JMeter 的 GUI 界面。      

![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-1.png)     

![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-2.png) 

<br>

###### 3.修改中文语言
官方默认为我们提供了简体中文。通过 `【Options】->【Choose Language】` 变更为简体中文。     

<br>
<br>

### 二、使用步骤
###### 1、创建测试计划
创建测试计划保存的路径。修改测试计划的名字，然后点击保存（Ctril+S）选择保存的路径。        

![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-3.png)      

<br>

###### 2、创建线程组
1. 在“接口测试”上右键 【添加】–>【线程(用户)】–>【线程组】      
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-4.png)      
2. 修改线程数，我这里先用5000，循环一次     
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-5.jpeg) 

<br>

###### 3、配置元件
1. 在我们刚刚创建的【线程组】上右键 【添加】–>【配置元件】–>【HTTP请求默认值】       
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-6.png) 
2. 配置我们需要进行测试的程序协议、地址和端口     
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-7.png) 

<br>

###### 4、构造HTTP请求
1. 在【线程组】右键 【添加】->【取样器】–>【HTTP 请求】       
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-8.jpeg) 
2. 设置我们需要测试的API的请求路径和参数     
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-9.png) 

<br>

###### 5、添加HTTP请求头
1. 在【线程组】上右键 【添加】–>【配置元件】–>【HTTP信息头管理器】     
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-10.png)
2. 为了传送json数据，我们需要设置 Content-Type:application/json       
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-11.png)

<br>

###### 6、添加断言
在【线程组】上右键 【添加】–>【断言】–>【响应断言】          
根据响应的数据来判断请求是否正常。我在这里只判断的响应代码是否为200。还可以配置错误信息     

![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-12.png)

<br>

###### 7、添加察看结果树
1. 在【线程组】上右键 【添加】–>【监听器】–>【察看结果树】      
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-13.jpeg)
2. 这时候如果你点击运行按钮，就可以看到他已经帮你发送请求了，如果你上面已经填写了要测试的接口，他就会出现一堆绿色的 http 请求          
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-14.png)    

<br>

###### 8、添加汇总报告
1. 在【线程组】上右键 【添加】–>【监听器】–>【汇总报告】    
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-15.jpeg) 
2. 这时候你可以点击运行按钮，可以看到这个简化版的压力测试数据      
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-16.png)    

<br>
<br>

### 三、专业测试与报告
###### 1、运行命令测试
**注意：**还记得前面的步骤有一个保存测试计划的目录吗，我是自己去建了一个目录 `D:\Jmeter\` 测试计划，然后测试计划文件是放在这里的，这个很重要，后面要用到这个目录的。     

去到 JMeter 的根目录的 /bin 下，打开cmd，运行命令：    
```
jmeter -n -t D:/Jmeter/测试计划/接口测试.jmx -l D:/Jmeter/测试计划/result/result.txt -e -o D:/Jmeter/测试计划/webreport
``` 

![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-17.png)    

<br>

说明：    
D:/Jmeter/测试计划/接口测试.jmx ------> 测试计划文件的路径     
D:/Jmeter/测试计划/result/result.txt ------> 将要生成的测试结果文件的存放路径      
D:/Jmeter/测试计划/webreport -------> 将要生成的web报告的保存路径     

<br>

###### 2、查看测试结果
1. 去到我们刚才指定的目录    
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-18.jpeg)     
2. 直接进去webreport 目录，双击 index.html ，打开测试报告，里面有你想要知道的一切！     
    ![](\img\in-post\post-jmeter\2022-07-22-jmeter-tps-19.png)  

---
以上参考自 [https://blog.csdn.net/weixin_42132143/article/details/118875293](https://blog.csdn.net/weixin_42132143/article/details/118875293)