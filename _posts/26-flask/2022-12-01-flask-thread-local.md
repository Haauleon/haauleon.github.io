---
layout:        post
title:         "Flask Web | 本地线程"
subtitle:      "本地线程 threading.local 和 Werkzeug.local 的使用"
author:        "Haauleon"
header-img:    "img/in-post/post-flask/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Flask
    - Python
    - Web开发
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、本地线程
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

<br>

#### 1、threading.local
&emsp;&emsp;本地线程（Thread Local）希望不同的线程对于内容的修改只在线程内发挥作用，线程之间互不影响。简单来说，我们定义并启动了多个线程来执行任务，但是每个线程只能执行自己线程内部的代码块，不去影响其他线程，为了获取线程执行的进度/结果，需要定义一个 threading.local() 对象来保存这些线程的状态。如下代码所示：     
```python
# coding=utf-8
import threading

mydata = threading.local()
mydata.number = 42
print mydata.number
log = []


def f1():
    mydata.number = 11
    log.append(mydata.number)


def f2():
    mydata.number = 12
    log.append(mydata.number)


def f3():
    mydata.number = 13
    log.append(mydata.number)


"""
定义三个线程 thread1、thread2和thread3 并启动
"""
thread1 = threading.Thread(target=f1)
thread2 = threading.Thread(target=f2)
thread3 = threading.Thread(target=f3)
thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()
print log
print mydata.number
```

执行结果如下：     
```
42
[11, 12, 13]  # 在线程内变成了 mydata.number 的值
42            # 但是没有影响到开始设置的值
```

&emsp;&emsp;本地线程的原理就是：在 `threading.current_thread().__dict__` 里添加一个包含对象 mydata 的 id 值的 key，用来保存不同线程的状态。   

<br>
<br>

#### 2、Werkzeug 的 Local

