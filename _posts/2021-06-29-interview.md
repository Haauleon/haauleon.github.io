---
layout:        post
title:         "面试 | APP 面试题"
subtitle:      "参考自公众号：Python 测试社区"
date:          2021-06-29
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 面试
---

## APP 面试题
&emsp;&emsp;在原文的基础上增加了一些自己的经验和理解。

<br><br>

###### 一、web 和 app 测试的异同点
1. 相同点：都离不开测试的基础知识和测试原理。具体包括以下几个方面：           
    * 测试用例，均使用边界值分析法，等价类划分法等。           
    * 多数采用黑盒测试，来验证业务功能是否能得到正确的应用。            
    * 需要检查界面布局，风格，按钮是否美观、简洁，是否统一。              
    * 测试页面载入和翻页的速度、登录时长、内存是否溢出等。                
    * 测试应用系统的稳定性。

<br>

2. 不同点：web 测试更多的是考虑自身功能和浏览器兼容，app 测试还要考虑手机本身固有的属性。所以 app 测试还需要注意以下几点：            
    * 中断测试（来电去电，短信，蓝牙，NFC 支付，闹钟，数据线插拔，锁屏，断电，关机重启等）               
    * 安装卸载测试（全新安装，新版本覆盖旧版本，卸载旧版本安装新版本，卸载新版本安装旧版本）                  
    * 外在因素测试（网络切换，硬件按键，不同分辨率，兼容性，系统，系统版本）

<br><br>

###### 二、如何测试 app 的登录场景        

|序号|登录场景|
|---|---|
|1 |验证页面基本元素是否可以正常操作|
|2 |验证是否可以输入大量字符、特殊字符、边界值|
|3 |验证输入框是否做必填项校验|
|4 |验证注册手机号的特殊性需求（若存在邮箱，则要验证注册邮箱的输入格式）|
|5 |验证密码大小写是否敏感、是否加密显示、是否有可见按钮功能、密码框能否使用复制粘贴|
|6 |验证短信验证码是否做必填项校验、是否校验无效验证码（错误、过期）、无网络时能否获取验证码、一个时间段内能否多次获取、超过获取次数时能否再次获取、输入验证码后修改手机号能否注册成功、境外手机号能否正常接收短信验证码|
|7 |验证已登录条件下与系统的不同交互操作（锁屏、蓝牙、home、先干掉进程再重新启动、先后台运行再进入、后退、屏幕旋转、修改系统字体字号）是否有异常|
|8 |（逆向思维）验证已注册账号能否再次注册成功、未注册账号能否使用忘记密码功能、未注册账号能否成功登录、注册过程中退出然后再次注册时页面是否自动填充之前的数据|
|9 |验证输入框在切换输入法（系统输入法和搜狗输入法等）、切换输入模式（如全拼和简拼和中英文混拼等）、手写/九宫格下是否有异常|
|10|验证多个不同角色或等级或类型的账号在轮流切登录、同一个账号多角色登录是否出现错误|
|11|验证第三方登录功能是否成功账号授权、取消授权、授权信息正确/错误时是否异常、第三方客户端已下载/未下载时能否成功授权|
|12|验证登录页面能否成功返回、登录成功后能否成功跳转|
|13|验证 app 是否做手机兼容（机型、分辨率、系统类型、系统版本、app 版本）|
|14|验证 app 在网络切换（无网、弱网、2G、3G、4G、5G）下是否有异常|


<br><br>

###### 三、如何测试 push 消息       

|序号|检查项|
|---|---|
|1|检查 push 消息是否按照指定的业务规则发送|
|2|检查系统设置不接收推送消息时，用户是否还会再接收到 push 消息|
|3|如果用户设置了免打扰的时间段，检查在免打扰时间段内用户是否还会接收到 push，在非免打扰时间段内用户是否能正常接收到 push|
|4|当 push 消息是针对登录用户的时候，需要检查收到的 push 是否与当前用户身份相符，没有误将其他在此手机上登录过的用户的消息推送过来。一般情况下，只对手机上最后一个登录用户进行消息推送。|
|5|测试在开关机、待机状态下能否执行 push 推送、消息和推送跳转的正确性|
|6|push 消息时，会有红点展示，推送消息阅读前后数字的变化是否正确。|
|7|应用在开发、未打开状态、应用启动且在后台运行的情况下时 push 显示和跳转是否正确。|
|8|多条推送的合集的显示和跳转是否正确。|      

<br><br>

###### 四、什么原因会造成 app 闪退       

|序号|闪退的可能原因|
|---|---|
|1|缓存垃圾太多，Android 系统的特性，如果长时间不清理垃圾文件，会导致越来越卡，甚至闪退。|
|2|运行程序太多，导致内存不足。|
|3|应用版本兼容问题，分辨率兼容问题。|
|4|app 中访问网络的地方，组件能否正常下载并显示。|
|5|app 的 SDK 与手机系统不兼容。|
|6|系统升级后，新版本不兼容老版本的 API，返回对象失败，报空指针。|
|7|软件权限未开放。|
               

<br><br>

###### 五、测试时 app 出现 crash 或者 ANR 要怎么处理
app 出现 crash 或者 ANR时，可以从以下几个方面处理：      

|步骤|处理方法|
|---|---|
|step 1|可以先把日志过滤出来：adb logcat &Iota; findstr xxxxx (过滤日志信息) |   
|step 2|然后再搜索其中的关键字，比如：exception、crash，看看是哪些方法或者异常导致了问题。|
|step 3|初步定位问题原因后，可以交给开发人员去具体查找深层原因并修复。|            

<br><br>

###### 六、一般会出现哪些异常（Exception）
&emsp;&emsp;这个主要是面试官考察你会不会看日志，是不是看得懂 Java 里面抛出的异常。一般面试中 Java Exception（runtimeException ）是必会被问到的问题，app 崩溃的常见原因应该也是这些了。常见的异常列出四五种，是基本要求。                   

常见的几种如下：          

|序号|异常|描述|
|---|---|---|
|1|NullPointerException|空指针引用异常|
|2|ClassCastException|类型强制转换异常|
|3|IllegalArgumentException|传递非法参数异常|
|4|ArithmeticException|算术运算异常|
|5|ArrayStoreException|向数组中存放与声明类型不兼容对象异常|
|6|IndexOutOfBoundsException|下标越界异常|
|7|NegativeArraySizeException|创建一个大小为负数的数组错误异常|
|8|NumberFormatException|数字格式异常|
|9|SecurityException|安全异常|
|10|UnsupportedOperationException|不支持的操作异常|               

<br><br>

###### 七、如何开展 app 测试
app 测试的进行，可以从以下几个方面展开：                  

|序号|测试类型|测试项|
|---|---|---|
|1|功能测试|业务逻辑正确性测试：依据产品文档->测试用例编写。|
|2|兼容性测试|系统版本：Android（官方版本，定制版本）、IOS（官方提供版本）。<br>分辨率：720 * 1280、1080 * 1920。<br>网络情况：2g、3g、4g、5g、Wi-Fi。|
|3|异常测试|热启动应用：应用在后台长时间待机、应用在后台待机过程中、手机重启。<br>网络切换和中断恢复：网络切换、中断恢复。<br>电话信息中断恢复。|
|4|升级、安装、卸载测试|升级测试：临近版本升级(1.0->1.1)、跨版本(1.0->....->2.2)。<br>安装测试：首次安装、覆盖安装(同版本，不同版本覆盖)、卸载后安装。<br>卸载测试：首次卸载、卸载安装后再卸载。|
|5|健壮性测试|手机资源消耗：cpu，内存。<br>流量消耗：图片，数据，视频。<br>电量测试。<br>崩溃恢复。|


<br><br>

###### 八、app 性能测试关注点及常见性能测试工具
1. 性能关注点                
    * 包体大小：包体大小能被列为性能指标，是从 app 性能指标及运营两个维度考虑的，用户是更希望包体小的同时性能要好，有时它们会是一个互相取舍的关系。     

    * 启动时长：移动应用的启动时间是用户体验的一个重要方面，IOS 一直建议尽可能的缩短启动时间，防止用户不愿意使用它们。对于浏览器而言，由于程序启动时还会有教育页和闪屏的下发，因此启动时间的获取显得尤为重要。                

    * 启动时间分为冷启动时间和热启动时间，所谓的“冷启动”，就是一个完全没有运行的应用的启动时间，与热启动（应用已经在后台运行，某个事件将其带至前台）相比，由于此时系统尚未建立缓存，因此冷启动往往要较平时（热启动）耗费更长的时间。                     

    * 内存使用：在 Android 系统中，每个 app 进程除了同其他进程共享(shared dirty)外，还独用私有内存(private dirty)，通常我们使用 PSS(=私有内存+比例分配共享内存)来衡量一个 app 的内存开销。移动设备的内存资源是非常有限，为每个 app 进程分配的私有内存也是有限制。一方面我们要合理的申请内存使用，以免导致频繁的 GC（垃圾回收机制）影响性能和大对象申请发生内存溢出；另一方面，我们要及时释放内存，以免发生内存泄漏。          

    * CPU 占用率：一般情况下，用主流手机使用 app 20%-40% 的 CPU 占用率算是合理的，当然这个数值随着近年来手机硬件配置的提高，会略微下降，如果CPU占用率超过80%就非常值得我们去关注了。                

    * 图片处理器每秒刷新的帧数(FPS)：可用来指示页面是否平滑的渲染。手机 app 帧率 FPS，30-60都可接受，上了 60 对于人眼主观感受差别就不大了。对于移动应用开发而言，并不是 FPS 越高就一定越好，FPS 取决于显卡，其次是内存、CPU，然后是网络。故综合APP其他性能指标，选择一个适合的 FPS 即可。           

    * 电量：相对于 PC 来说，移动设备的电池电量是非常有限的，保持持久的续航能力尤为重要。另外，Android 的很多特性都比较耗电(如屏幕，GPS，sensor 传感器，唤醒机制，CPU，连网等的使用)，我们必须要慎重检查APP的电量使用，以免导致用户手机耗电发热，带来不良体验。                     

    * 流量：目前的网络类型包含 2G\3G\4G\5G\wifi，其中还有不同运营商的区分，我们在 app 的使用中经常遇到大资源，重复请求，调用响应慢，调用失败等各种情况。在不同的网络类型之下，我们不仅要控制流量使用，还需要加快请求的响应。另外，对于需要联网的手游来说，部分游戏对不同联网方式的网络类型采用了不同的流量消耗策略，主要分为 wifi 环境和蜂窝网络环境。所以针对不同的游戏，我们统计流量消耗时，可能要连接不同的网络进行测试。                

<br>

2. app性能测试工具             
    * GT 和 iTest           
    * Emmagee APT             
    * DDMS            
    * 手机自带开发者选项中的工具            
    * 也可以通过 adb 命令来查看等            

<br><br>

###### 九、如何对 app 进行弱网测试
&emsp;&emsp;一款 APP 针对不同网络情况下都需要保证不会崩溃，同时尽可能做到在弱网情况下也能达到功能正常使用，或者使用体验达到最佳。弱网测试可以测试 APP 的加载时间、可用性、稳定性和健壮性。这时我们就可以借助工具来模拟不同的网络状况，模拟 2G、3G 或弱网情况进行测试。工具可以选择 Fiddler 也可以选择 Charles 也可以选择其他工具。

<br><br>

###### 十、常见的 adb 命令
注：adb 使用的端口号是 5037，以下总结工作中常用到的 adb 命令。              

1.查看帮助手册列出所有的选项说明及子命令：           
```
$ adb help
```

<br>

2.获取设备列表及设备状态：          
```
$ adb devices
```

<br>

3.安装应用：             
```
$ adb install 路径\xx.apk        # 安装应用
$ adb install -r                 # 重新安装
```

<br>

4.获取设备的状态，设备的状态有 device , offline , unknown 3种。其中 device：设备正常连接，offline：连接出现异常或设备无响应，unknown：没有连接设备。    
```
$ adb get-state
```

<br>

5.卸载应用：           
```
$ adb uninstall <应用包名>     # 应用包名区别于 apk 文件名
```

<br>

6.将 Android 设备上的文件或者文件夹复制到电脑本地，如复制 Sdcard 下的 pull.txt 文件到 D 盘：`$ adb pull sdcard/pull.txt d:\`    
```
$ adb pull  <远程路径> <本地路径>           # 将 Android 设备上的文件或者文件夹复制到电脑本地
$ adb pull sdcard/pull.txt d:\rename.txt   # 将 Android 设备上的文件或者文件夹复制到电脑本地后重命名
```

<br>

7.推送本地文件至 Android 设备，如推送 D 盘下的 ITester.txt 至 Sdcard：`$ adb push d:\ITester.txt sdcard/`   （注意 sdcard 后面的斜杠不能少）。            
```
$ adb push  <本地路径> <远程路径>       # 推送本地文件至 Android 设备
```

<br>

8.结束和启动 adb 服务，通常两个命令一起用，设备状态异常时使用 kill-server，运行 start-server 进行重启服务。      
```
$ adb kill-server      # 结束 adb 服务
$ adb start-server     # 启动 adb 服务
```

<br>

9.打印及清除系统日志：     
```
$ adb logcat       # 打印 Android 的系统日志
$ adb logcat -c    # 清除日志
```

<br>

10.查找包名/活动名：          
```
$ adb logcat | findstr START
```

<br>

11.生成 bugreport 文件：              
```
$ adb bugreport                     # 打印 dumpsys、dumpstate、logcat 的输出，用于分析错误
$ adb bugreport > d:\bugreport.log  # 输出比较多时建议重定向到一个文件中
```


<br>

12.重启设备：           
```
$ adb reboot                  # 重启 Android 设备
$ adb reboot recovery         # 重启到 Recovery 界面
$ adb reboot bootloader       # 重启到 bootloader 界面
```

<br>

13.获取 root 权限：      
```
$ adb root       # 获取 root 权限
$ adb remount    # 直接获取 root 权限，并挂载系统文件系统为可读写状态
```

<br>

14.返回设备序列号 SN 值：      
```
$ adb get-serialno
```

<br>

15.获取设备的 ID：            
```
$ adb get-product
```

<br>

16.进入设备 shell：          
```
$ adb shell
```

<br>

17.列出所有的应用的包名：          
```
$ adb shell pm list package
```

<br>

18.截屏并保存至 sdcard 目录：            
```
$ adb shell screencap -p /sdcard/screen.png 
```

<br>

19.录制视频并保存至 sdcard，执行命令后操作手机，ctrl + c 结束录制。              
```
$ adb shell screenrecord sdcard/record.mp4      # 录制视频并保存至 sdcard
```

<br>

20.获取设备分辨率：              
```
$ adb shell wm size
```

<br>

21.列出指定应用的 dump 信息：                   
```
$ adb shell pm dump 包名
```

<br>

22.列出对应包名的 .apk 位置：               
```
$ adb shell pm path 包名
```

<br>

23.查看当前终端中的进程信息：          
```
$ adb shell ps
```

<br>

24.monkey 测试：             
```
$ adb shell monkey –p 程序包 –v 测试次数
$ adb shell monkey –p com.htc.Weather –v 20000   # 这个程序包单独进行一次20000次的monkey测试
```

<br>

25.显示所有程序包：              
```
$ adb shell ps | grep [process]
```

<br>

26.根据进程 pid 或包名查看进程占用的内存：                  
```
$ adb shell dumpsys meminfo<pid>
$ adb shell dumpsys meminfo<package_name>
```

<br>

27.APP 启动：         
```
$ adb shell am start -n packageName/activity
```

<br>

28.APP 关闭：            
```
$ adb shell am force-stop 包名
```

<br>

29.监控 APP 启动时间：             
```
$ adb shell am start -W packageName/activity
```