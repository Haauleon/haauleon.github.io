---
layout:        post
title:         "Flask Web | 信号机制"
subtitle:      "使用信号在触发动作时发送通知，对应用业务进行解耦"
author:        "Haauleon"
header-img:    "img/in-post/post-flask/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Flask
    - Python
    - Web开发
    - Vagrant
    - Ubuntu
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、Flask 的信号机制
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     
werkzeug==0.11.10       

&emsp;&emsp;项目功能越复杂，代码量越大，就越需要做 **业务解耦**，否则在其之上做开发和维护是很痛苦的，尤其是对团队的新人。Flask 从 0.6 开始，通过 [Blinker](https://github.com/pallets-eco/blinker) 提供了信号支持。       

&emsp;&emsp;信号就是在框架核心功能或者一些 Flask 扩展发生动作时所发送的通知，用于帮助程序员解耦应用。    

<br>

#### 1、Blinker 的使用
&emsp;&emsp;Blinker 不像 werkzeug 一样是 Flask 的默认依赖，所以如果不安装 Blinker 就无法使用信号。使用以下命令进行安装：    
```
> pip2 install blinker
```

&emsp;&emsp;以下代码简单使用了 blinker.signal 信号对象，设置一个信号接收器 started，而 connect（用于订阅信号）和 send（用于发送信号）则通过 started 作为桥梁达到解耦的作用，因此实现不用将 connect 和 send 放在一个文件中。      
```python
# coding=utf-8
from blinker import signal

# 设置一个信号接收器
started = signal('test-started')


def each(round):
    print 'Round {}!'.format(round)


def round_two(round):
    print 'Only {}'.format(round)


# 将信号接收器连接到信号发送端
started.connect(each)
started.connect(round_two, sender=2)  # 值为2的时候才会接收

for round in range(1, 4):
    # 信号接收器开始发送信号
    started.send(round)
```

执行结果如下：    
```
Round 1!
Round 2!
Only 2
Round 3!
```

&emsp;&emsp;信号和钩子做的事情其实很像，如 [Flask 的钩子 before_request 和 after_request](https://haauleon.gitee.io/2022/12/01/flask-ctx/#2%E6%B7%BB%E5%8A%A0%E4%B8%8A%E4%B8%8B%E6%96%87%E7%9A%84%E9%92%A9%E5%AD%90)，这些钩子不需要 Blinker 库且允许你改变请求对象（request）或者响应对象（response），而信号并不会对请求对象和响应对象做改变，仅承担记录和通知的工作。       

<br>
<br>

#### 2、Flask 中内置的信号