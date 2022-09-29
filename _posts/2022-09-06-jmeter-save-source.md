---
layout:        post
title:         "Jmeter | 如何将负载机对测试结果的影响降到最低？"
subtitle:      "从运行方式、性能监控设置等方面提高负载机性能"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
---

### 提高负载机的性能    
&emsp;&emsp;降低负载机对测试结果的影响尤为重要，比如本可以产生 100TPS 的负载，但由于负载机的性能瓶颈，可能结果仅仅只产生 80TPS 的负载，使得测试结果大打折扣，不得不增加多台负载机。由此看来，提高负载机的性能很重要，避免产生不必要的资源消耗。     

&emsp;&emsp;Jmeter 的可视化界面和监听器动态展示结果都比较消耗负载机资源，在大并发情况下往往会导致负载机资源紧张，直接影响到性能测试结果。以下通过三种方式来提高负载机的性能。

<br>

###### 一、非GUI运行方式
&emsp;&emsp;非 GUI 运行方式虽然不显示界面，但也会以字符形式周期性显示执行结果，对负载机的资源消耗会小一些。所以，同等条件下非 GUI 方式的 Jmeter 机器产生的负载比 GUI 方式大一些。运行命令如下：（提前设置好环境变量 JMETER_HOME）         
```
$ java -jar %JMETER_HOME%/bin/ApacheJMeter.jar -n -t [测试计划的绝对路径.jmx] -l [测试结果绝对路径.txt] -e -o [web测试报告目录的绝对路径]

$ jmeter -n -t [测试计划的绝对路径.jmx] -l [测试结果绝对路径.txt] -e -o [web测试报告目录的绝对路径]  
```

&emsp;&emsp;可以使用以上两种命令来运行测试计划，其本质是通过运行 ApacheJMeter.jar 来完成的。     
![](\img\in-post\post-jmeter\2022-09-06-jmeter-save-source-1.jpg)   

<br>

实践步骤如下：    
1. 调试成功后，保存测试计划至本地     
    ![](\img\in-post\post-jmeter\2022-09-06-jmeter-save-source-2.jpg)     
2. 在 cmd 中使用命令行运行测试计划    
    ```
    C:\Users\Haauleon>jmeter -n -t D:/jmeter/获取列表.jmx -l D:/jmeter/result.txt -e -o D:/jmeter/webreport
    Creating summariser <summary>
    Created the tree successfully using D:/jmeter/获取列表.jmx
    Starting standalone test @ September 6, 2022 4:35:24 PM CST (1662453324482)
    Waiting for possible Shutdown/StopTestNow/HeapDump/ThreadDump message on port 4445
    summary =      1 in 00:00:01 =    0.8/s Avg:  1124 Min:  1124 Max:  1124 Err:     0 (0.00%)
    Tidying up ...    @ September 6, 2022 4:35:25 PM CST (1662453325996)
    ... end of run
    ```
    ![](\img\in-post\post-jmeter\2022-09-06-jmeter-save-source-3.jpg)    

    或者   

    ```
    C:\Users\Haauleon>java -jar %JMETER_HOME%/bin/ApacheJMeter.jar -n -t D:/jmeter/获取列表.jmx -l D:/jmeter/result.txt -e -o D:/jmeter/webreport
    Creating summariser <summary>
    Created the tree successfully using D:/jmeter/获取列表.jmx
    Starting standalone test @ September 6, 2022 4:38:53 PM CST (1662453533780)
    Waiting for possible Shutdown/StopTestNow/HeapDump/ThreadDump message on port 4445
    summary =      1 in 00:00:01 =    0.8/s Avg:  1139 Min:  1139 Max:  1139 Err:     0 (0.00%)
    Tidying up ...    @ September 6, 2022 4:38:55 PM CST (1662453535325)
    ... end of run
    ```
3. 查看测试结果   
    有两种测试报告，一种是 txt 文本简易版报告，一种是 web 测试报告。    
    ![](\img\in-post\post-jmeter\2022-09-06-jmeter-save-source-4.jpg) 

    <br>

    双击使用浏览器中打开 web 测试报告目录中的 index.html 文件即可看到报告详情。     
    ![](\img\in-post\post-jmeter\2022-09-06-jmeter-save-source-5.jpg) 

<br>
<br>


###### 二、监听器设置结果属性    
&emsp;&emsp;Jmeter 的监听器可以统计吞吐量、响应时间等指标。如下所示：    
![](\img\in-post\post-jmeter\2022-09-06-jmeter-save-source-6.jpg) 

<br>

&emsp;&emsp;点击`配置`按钮可以进入设置结果属性页面，如下图，可以看到只有部分字段默认被选中，这些字段已经能够说明测试结果了，无需额外选中其他字段。在长时间运行时只记录这些字段即可，并且有利于提高负载机性能。字段保存得越多，产生的 IO 越大，写磁盘是物理操作，对负载机的 IO 会产生影响，千万别让负载机 IO 产生性能瓶颈。       
![](\img\in-post\post-jmeter\2022-09-06-jmeter-save-source-7.jpg)

<br>
<br>

###### 三、★只在一个监听器中设置保存测试结果  
&emsp;&emsp;监听器中也可以保存测试结果，如下所示，点击`浏览`按钮保存即可。     
![](\img\in-post\post-jmeter\2022-09-06-jmeter-save-source-8.jpg)   

<br>

&emsp;&emsp;如果在测试计划中添加了多个监听器，需要记住只能在一个监听器中设置保存测试结果。如果分别在多个监听器中保存测试结果，则会导致重复写而且写的内容是一样的，这完全没有必要而且影响负载机性能。
