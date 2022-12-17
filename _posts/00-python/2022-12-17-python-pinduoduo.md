---
layout:        post
title:         "Python3 | 刷拼多多视频"
subtitle:      "用 python + uiautomator2 脚本实现自动刷多多视频"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
    - Android
---

### 一、背景
&emsp;&emsp;最近因为在拼多多上买沙田柚只花了一分钱于是对拼多多这个软件多了一些关注，发现他的刷视频种菜里面可以薅羊毛哈哈哈哈哈，于是想着写个脚本来自动刷视频。    

<br>
<br>

### 二、环境准备
PC 端： windows 11 系统     
手机端：红米 K50     

<br>

#### 1、手机开启开发者模式
（1）用 USB 数据线将手机和电脑连接，在手机设置页面搜索 `MIUI版本` 并进入     
（2）连续点击【MIUI版本】，直到提示已开启开发者模式     
（3）回到设置界面，点击【更多设置】 > 【开发者选项】     

<br>
<br>

#### 2、开发者选项设置
（1）开启 `开启开发者选项`     
（2）开启 `USB 调试`    
（3）开启 `USB 安装`      
（3）开启 `USB 调试（安全设置）`

<br>
<br>

#### 3、下载 abd
进入 [https://adbshell.com/downloads](https://adbshell.com/downloads) 下载 [ADB Kits (1364 KB)](https://adbshell.com/upload/adb.zip) 至本地即可。      

<br>
<br>

#### 4、获取设备号
（1）打开 cmd 进入 adb.exe 所在的目录     
（2）输入命令行 `> adb devices` 获取设备序列号      

<br>
<br>

#### 5、安装 uiautomator2
**电脑端安装**     
```
> pip3 install --pre uiautomator2   
> pip3 install -U weditor==0.6.3
```


**手机端安装**     
```
> python3 -m uiautomator2 init
```

<br>
<br>

### 三、编写和执行脚本
&emsp;&emsp;命令行执行 weditor 会自动打开浏览器，输入设备的 IP 或者序列号(序列号可以通过 adb devices 命令查看得到 )，然后点击 Connect。weditor 可以用来获取页面元素，用于后期做滑动、点击操作等。如下为部分代码仅作参考：             

```python
import uiautomator2 as d
import time


def pinduoduo():
    # 通过usb连接
    a = d.connect_usb('J7ZTWCV8UHHJHII5')  # 设备序列号
    while True:
        time.sleep(10)
        # 滑动视频
        a.swipe(0.453, 0.801, 0.453, 0.101)


if __name__ == '__main__':
    pinduoduo()
```

<br>
<br>

相关链接：   
[红米K50开发者模式在哪](https://jingyan.baidu.com/article/19192ad809c912a43e5707ee.html)     
[用python来自动刷多多视频，自动赚钱（结合abd脚本实现操作）](https://blog.csdn.net/qq_59848320/article/details/120391969)    
[安卓手机 Python 自动化（ uiautomation、uiautomation2、weditor ）](https://blog.csdn.net/lyshark_lyshark/article/details/125848426)    
[超详细的uiautomator2运行前环境准备及各种问题解决](https://blog.csdn.net/qq_44540071/article/details/125246007)    