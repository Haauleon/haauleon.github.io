---
layout:        post
title:         "Android | monkey 压力测试"
subtitle:      "使用压力测试工具测试 app 是否会 crash"
author:        "Haauleon"
header-img:    "img/in-post/post-app-test/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Android
---

## 一、monkey
###### 1.介绍
&emsp;&emsp;monkey 程序由 Android 系统自带，使用 Java 诧言写成，在 Android 文件系统中的存放路径是： `/system/framework/monkey.jar`。而 `monkey.jar` 程序则是由一个名为 `monkey` 的 shell 脚本来启动执行，shell 脚本在 Android 文件系统中的存放路径是： `/system/bin/monkey`。      

&emsp;&emsp;为了验证上面这句话，可以使用 `$ cat /system/bin/monkey` 来查看文件内容。其注释中就已经写到 *Script to start "monkey" on the device* 意思是说此 shell 脚本用于在设备上启动 monkey。                       
```
C:\Users\Haauleon>adb kill-server

C:\Users\Haauleon>adb start-server
* daemon not running; starting now at tcp:5037
* daemon started successfully

C:\Users\Haauleon>adb devices -l
List of devices attached
********         device product:R9sk model:OPPO_R9sk device:R9sk transport_id:1


C:\Users\Haauleon>adb shell
shell@R9sk:/ $ ls /system/framework/monkey.jar -al
-rw-r--r-- root     root          205 1971-04-23 04:24 monkey.jar
shell@R9sk:/ $ ls /system/bin/monkey -al
-rwxr-xr-x root     shell         217 2009-01-01 00:00 monkey
shell@R9sk:/ $ cat /system/bin/monkey
# Script to start "monkey" on the device, which has a very rudimentary
# shell.
#
base=/system
export CLASSPATH=$base/framework/monkey.jar
trap "" HUP
exec app_process $base/bin com.android.commands.monkey.Monkey $*
```

<br><br>

**monkey 命令启动方式：**            
（1）可以在 PC 端的 CMD 窗口中执行如下命令行进行 monkey 测试：          
```
$ adb shell monkey [参数列表]          
```

<br>

（2）在 PC 上使用 `$ adb shell` 进入 Android 系统，通过执行如下命令行进行 monkey 测试：       
```
$ monkey [参数列表]         
```

<br>

（3）在 Android 机或者模拟器上直接执行 monkey 命令。可以在 Android 机上安装 Android 终端模拟器。         

<br><br>

###### 2.原理
&emsp;&emsp;monkey 可以运行在模拟器里或实际设备中，它通过模拟用户的按键输入，触摸屏输入，手势输入等，用随机重复的方法将这些输入等操作发送给 Android 系统，来实现对应用程序的压力测试。

<br><br>

###### 3.用途
&emsp;&emsp;顾名思义，monkey 即猴子。monkey 测试，就像一只猴子在电脑面前乱敲键盘在测试。猴子什么都不懂，只知道乱敲。         

&emsp;&emsp;通过 monkey 程序模拟用户触摸屏幕、滑动 Trackball、按键等操作来对设备上的程序进行压力测试，检测程序在多久的时间会发生异常。       

&emsp;&emsp;monkey 主要用于 Android 的压力测试，是自动模拟用户行为的一个压力测试小工具，此测试的主要目的就是为了测试 app 是否会 Crash。      

<br><br>

###### 4.架构
&emsp;&emsp;monkey 运行在设备或模拟器上面，可以脱离 PC 运行（普遍做法是将 monkey 作为一个像待测应用发送随机按键消息的测试工具。验证待测应用在这些随机性的输入面前是否会闪退或者崩溃）。      

![](\img\in-post\post-app-test\2021-07-26-monkey-1.png)

<br><br>

###### 5.弱点
&emsp;&emsp;monkey 虽然可以根据一个指定的命令脚本发送按键消息，但其不支持条件判断，也不支持读取待测界面的信息来执行验证操作。       

<br><br>

## 二、实操部分
###### 1.测试环境准备
（1）配置 adb 命令行工具环境，保证可以在 cmd 中正常运行       
（2）用 USB 数据线连接安卓机和电脑      
（3）在安卓机的开发者选项中点击允许进行 USB 调试     

<br><br>

###### 2.初始化测试环境
```
$ adb kill-server
$ adb start-server    # 此过程需要再次进行授权调试
$ adb devices -l
```

<br><br>

###### 3.获取测试包名
获取要测试的 app 的包名：    
（1）方法一：查看手机上所有的安装包         
```
$ adb shell pm list package
```

<br>

（2）方法二：查看手机上安装的第三方安装包          
```
$ adb shell pm list package -3
```

<br><br>

###### 4.进行压力测试
```
$ adb shell monkey -v -v -v -p com.bringbuyshare -s 300 --throttle 100 5000 >d:\android-logs\com.bringbuyshare.log
```

<br>

测试效果如下：      

<iframe 
    frameborder="0" 
    id="1" 
    name="monkey" 
    scrolling="yes" 
    src="https://player.youku.com/embed/XNTE4NjE0MTM1Mg==" 
    style="height:100%;visibility:inherit; width:100%;z-index:1;"
    allowfullscreen>
</iframe>

<br>

测试执行完成后，打开指定的 log 存放路径。      
![](\img\in-post\post-app-test\2021-07-26-monkey-2.png)   

<br>

![](\img\in-post\post-app-test\2021-07-26-monkey-3.png)     

<br><br>

###### 5.日志分析
&emsp;&emsp;正常情况。如果 monkey 测试顺利执行完成。在 log 的最后会打印出当前执行事件的次数和所花费的时间。`Monkey finished` 代表执行完成。      

&emsp;&emsp;异常情况。monkey 测试出现错误后，需要查看 monkey 的日志（注意第一个 swith 以及异常信息等)。一般的分析步骤如下：                
（1）找到 monkey 里哪个地方出错。      
Ø 查看 monkey 执行的是哪一个 Activity，在 switch 后面找，两个 swtich 之间如果出现了崩溃或其他异常，可以在该 Activity 中查找问题的所在。        
![](\img\in-post\post-app-test\2021-07-26-monkey-5.png)     

<br>

（2）查看 monkey 里面出错前的一些事件动作，手动执行该动作。     
Ø `Sleeping for XX milliseconds` 是执行 monkey 测试时 throttle 设定的间隔时间，每出现一次，就代表一个事件。        
Ø `Sending XX` 代表一个操作，如下图的两个操作，应该就是一个点击事件。         
![](\img\in-post\post-app-test\2021-07-26-monkey-6.png)       

<br>

（3）monkey 执行中断， 在 log 最后也能看到当前执行次数。            

（4）若以上步骤还不能找出，则可以使用之前一样的 seed，再执行 monkey 命令一遍，便于复现。     

（5）测试结果分析：      
Ø 程序无响应为 ANR 问题：在日志中搜索 `ANR`         
Ø 崩溃问题：在日志中搜索 `CRASH`          
Ø 其他问题：在日志中搜索 `Exception`          

<br><br>

## 三、monkey 命令

```
C:\Users\Haauleon>adb shell monkey -h
usage: monkey [-p ALLOWED_PACKAGE [-p ALLOWED_PACKAGE] ...]
              [-c MAIN_CATEGORY [-c MAIN_CATEGORY] ...]
              [--ignore-crashes] [--ignore-timeouts]
              [--ignore-security-exceptions]
              [--monitor-native-crashes] [--ignore-native-crashes]
              [--kill-process-after-error] [--hprof]
              [--pct-touch PERCENT] [--pct-motion PERCENT]
              [--pct-trackball PERCENT] [--pct-syskeys PERCENT]
              [--pct-nav PERCENT] [--pct-majornav PERCENT]
              [--pct-appswitch PERCENT] [--pct-flip PERCENT]
              [--pct-anyevent PERCENT] [--pct-pinchzoom PERCENT]
              [--pct-permission PERCENT]
              [--pkg-blacklist-file PACKAGE_BLACKLIST_FILE]
              [--pkg-whitelist-file PACKAGE_WHITELIST_FILE]
              [--wait-dbg] [--dbg-no-events]
              [--setup scriptfile] [-f scriptfile [-f scriptfile] ...]
              [--port port]
              [-s SEED] [-v [-v] ...]
              [--throttle MILLISEC] [--randomize-throttle]
              [--profile-wait MILLISEC]
              [--device-sleep-time MILLISEC]
              [--randomize-script]
              [--script-log]
              [--bugreport]
              [--periodic-bugreport]
              [--permission-target-system]
              COUNT

```

<br>

###### 1.参数大全
![](\img\in-post\post-app-test\2021-07-26-monkey-4.png)

<br><br>

###### 2.参数介绍
**-p (允许的包名列表)**          
功能：用此参数指定一个或多个包。指定包之后，monkey 将只允许系统启动指定的app。如果不指定包，monkey 将允许系统启动设备中的所有 app。一般应用程序的压力测试都需要指定包。         
```
指定一个包：adb shell monkey -p com.shjt.map 100   

指定多个包：adb shell monkey -p fishjoy.control.menu  –p com.shjt.map  100  
```
 
<br>

**-v**             
功能：用于指定反馈信息级别（信息级别就是日志的详细程度），总共分 3 个级别，分别对应的参数如下所示：            
```
Level 0  :  adb shell monkey -p com.shjt.map -v 100              // 缺省值，仅提供启动提示、测试完成和最终结果等少量信息   

Level 1  :  adb shell monkey -p com.shjt.map -v -v 100           // 提供较为详细的日志，包括每个发送到Activity的事件信息

Level 2  :  adb shell monkey -p com.shjt.map -v -v -v 100        // 最详细的日志，包括了测试中选中/未选中的Activity信息
```

<br>

**-s (随机数种子)**                  
功能：用于指定伪随机数生成器的 seed 值，如果 seed 相同，则两次 monkey 测试所产生的事件序列也相同的。
示例：          
```
monkey测试1：adb shell monkey -p com.shjt.map –s 10 100                

monkey测试2：adb shell monkey -p com.shjt.map –s 10 100  
```

说明：          
Ø 两次测试的效果是相同的，因为模拟的用户操作序列（每次操作按照一定的先后顺序所组成的一系列操作，即一个序列）是一样的。（也就是说，重复执行上次的随机操作）   
Ø 操作序列虽然是随机生成的，但是只要我们指定了相同的Seed值，就可以保证两次测试产生的随机操作序列是完全相同的，所以这个操作序列伪随机的。      

<br>

**--throttle (毫秒)**                 
&emsp;&emsp;用于指定用户操作（即事件）间的时延，单位是毫秒。如果不指定这个参数，monkey 会尽可能快的生成和发送消息。示例：      
```
$ adb shell monkey -p com.shjt.map --throttle 3000 100  
```

<br><br>

###### 3.命令使用规则
（1）所有的参数都需要放在 monkey 和设置的次数之间      
（2）参数的顺序可以调整       
（3）若带了 -p ，则 -p 必须放在 monkey 之后，而参数必须在 -p 和次数之间     

<br>

monkey 基础命令模板：    
```
$ adb shell monkey -p 包名 -v -s seed值 压测次数 >输出的自定义日志路径
```