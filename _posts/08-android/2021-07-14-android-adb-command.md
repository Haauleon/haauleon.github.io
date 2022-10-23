---
layout:        post
title:         "Android | adb 常用命令"
subtitle:      "列举了一些工作中常用的 adb 命令"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Android
---


## adb 常用命令集

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