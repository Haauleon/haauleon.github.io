---
layout:        post
title:         "Fiddler | 弱网测试及设置"
subtitle:      "参考自 https://www.jianshu.com/p/b9e349b8f411"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Fiddler
    - 性能测试
    - API 测试
---


### 一、为什么要做弱网络测试？
&emsp;&emsp;实际的客户现场可能网络不稳定或者网速低，恶劣的网络环境会导致出现一些 bug，影响用户体验甚至某些服务不可用。而公司内部的研发环境网络通常比较顺畅，难以复现这种 bug。要解决这种问题，就需要制造弱网络的环境进行测试、复现并修复问题。     

<br>
<br>

### 二、如何模拟恶劣网络环境？
&emsp;&emsp;这篇博文 [https://www.cnblogs.com/jinjiangongzuoshi/p/5272787.html](https://www.cnblogs.com/jinjiangongzuoshi/p/5272787.html) 介绍了 3 种详细的实现弱网络的手段，本文仅以 fiddler 为例，其他的做个了解，不具体研究。     

<br>
<br>

### 三、Fiddler怎样模拟弱网？
&emsp;&emsp;Fiddler 是一个 HTTP 调试代理，它能够记录所有你电脑和互联网之间的 HTTP 通讯，Fiddler 也可以让你检查所有的 HTTP 通讯，设置断点，以及修改所有的“进出”的数据（指 Cookie/HTML/JS/CSS 等文件）。      

&emsp;&emsp;利用 Fiddler 来模拟恶劣的网络环境，实现简单，较为直观，配置也较为方便。缺点是由于它是一个应用层的 HTTP 的代理，只能模拟该层上的行为，对于一些复杂的网络层的丢包、重传等恶劣情况就不能很好的模拟出来。而且，它只支持那些利用 HTTP 进行通信和交互的服务，对于其他协议的应用也不支持。           

&emsp;&emsp;打开 Fiddler，默认情况下 `Rules –> Performances –> Simulate Modem Speeds` 是未勾选状态，网络正常。当选中此选项（模拟光猫网速）后，网速就会变很慢，打开一个网页要加载很久。这样就实现了弱网络效果。         

![]()

<br>

如果想了解（上传和下载）网速的具体数值，可以使用一个工具 speedtest，测速方法很简单，网上有大把教程。[http://www.speedtest.net/](http://www.speedtest.net/) 是英文的网站，应该是国外版，访问比较慢。而且 Windows 系统只支持 Windows10 下载客户端，我用的 Windows7 使用 chrome 浏览器要安装Speedtest 扩展程序就得翻墙，所以不推荐使用。建议访问 [http://www.speedtest.cn/](http://www.speedtest.cn/) 网站，测速生成结果很快且是中文的。支持手机客户端 APP 下载。       

<br>
<br>

### 四、限速原理
Fiddler限速是以网络延迟的方式实现的，网络延迟时间*网速=传输字节数。

点击Rules – Customize Rules（快捷键Ctrl + R）打开Fiddler ScriptEditor，或者直接点开右侧主页签的FiddlerScript。
image.png
打开该文件后，Ctrl + F 查找m_SimulateModem标志位，可以看到如下代码：
        if (m_SimulateModem) {
            // Delay sends by 300ms per KB uploaded.
            oSession["request-trickle-delay"] = "300"; 
            // Delay receives by 150ms per KB downloaded.
            oSession["response-trickle-delay"] = "150"; 
        }
注释说明： request-trickle-delay中的值代表每KB的数据被上传时会被延时多少毫秒；response-trickle-delay则对应下载时每KB的数据会被延时多少毫秒。比如你要模拟上传速度100KBps的网络，那上传延迟就是1KB/100KBps=0.01s=10ms，就改成10。

当勾选了Simulate Modem Speeds时，request-trickle-delay与response-trickle-delay就会被设置，如果本身网速已经相当快的话，这里设置的值就可以近似地推算出开启模拟后的上传和下载带宽了，比如默认设置下上传延时为300ms下载延时为150ms，可以推算出大致的模拟带宽为：

上传带宽 = 1KB/300ms = (1 * 8/1000) /0.300 ≈ 0.027Mbps
下载带宽 = 1KB/150ms = (1 * 8/1000) /0.150 ≈ 0.053Mbps
（1MB = 1024 KB ≈ 1000 KB 这里为了运算简便就用了1000的倍数，忽略误差）

实际情况下得到的带宽可能会有误差，受各种外因影响不会这么精确。不懂公式换算的可以去看我的博文https://www.jianshu.com/p/492a1564d16d和https://www.jianshu.com/p/f417d328e0df
由此可见下载带宽是上传的两倍，也就是延时越小，带宽越大。带宽和这里的延时是成反比的。

五：调整网络环境参数
Fiddler默认的Simulate Modem Speeds速度实在太慢了，而这个限速的参数是可以调整的，如果需要再快一点可以修改配置文件\Fiddler2\Scripts\CustomRules.js。（如若修改勿忘备份原文件）在fiddler官网http://www.fiddlerbook.com/Fiddler/dev/ScriptSamples.asp可以找到参考示例。

下面提供了两种简单的修改脚本的方法，选择一种即可。

方法1
查找到if (m_SimulateModem)语句，修改代码。下面的脚本实现了一个随机延时量设置，使得网络带宽不是恒定为一个低速的值，而是会在一定范围内随机抖动：

static function randInt(min, max) {
    return Math.round(Math.random()*(max-min)+min);
}
if (m_SimulateModem) {
    // Delay sends by 300ms per KB uploaded.
    oSession["request-trickle-delay"] = ""+randInt(1,50);
    // Delay receives by 150ms per KB downloaded.
    oSession["response-trickle-delay"] = ""+randInt(1,50);
}
方法2
点击fiddlerScript 在代码里找到onBeforeRequest，这里定义了在发送请求前做什么。加入如下代码可以实现延迟：

oSession["request-trickle-delay"]="3000";  //请求阶段延迟3秒
oSession["response-trickle-delay"]="3000";  //响应阶段延迟3秒
添加代码
上面两种方法选其一，修改后保存配置文件（Ctrl+S）或者清掉缓存（Rules –> Performances –>Disable Caching），再次勾选Rules –> Performances –> Simulate Modem Speeds 进行测速。注意：每次编辑并保存配置文件后，Simulate Modem Speeds选项会被取消，请重新勾选。
限速完毕一定要取消勾选，不然会影响上网。像第二种方法由于请求和响应都延迟3秒，会导致访问网页很慢。

作者：Yvanna_15
链接：https://www.jianshu.com/p/b9e349b8f411
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。