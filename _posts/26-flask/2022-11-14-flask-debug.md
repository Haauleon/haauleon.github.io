---
layout:        post
title:         "Flask Web | app.run 调试模式"
subtitle:      "启用 app.run 的调试模式并使用 PIN 码"
author:        "Haauleon"
header-style:  text
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

### 一、调试器
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.12.1    

&emsp;&emsp;虽然 app.run 这样的方式适用于启动本地的开发服务器，但是每次修改代码后都要手动重启的话，既不方便也不够优雅。如果启用了调试模式，服务器则会在代码修改保存后（修改完成后按下 ctrl+s 保存）自动重新载入，不需要手动重启，并在发生错误时提供一个能获得错误上下文及可执行代码的调试页面。    

<br>
<br>

### 二、启用调试器
有两种途径来启用调试模式。

<br>

#### 1、直接在应用对象上设置
```python
# coding=utf-8
from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```

控制台输入：    
```
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 150-759-644
 * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)
```

<br>
<br>

#### 2、作为 run 的参数传入
```python
# coding=utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
```

控制台输入：    
```
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 150-759-644
 * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)
```

<br>
<br>

### 三、认识 PIN 码
&emsp;&emsp;需要注意，开启调试模式会成为一个巨大的安全隐患，因此它决不能用于生产环境中。      

&emsp;&emsp;Werkzeug 从 0.11 版本开始默认启用了 PIN （全称 Personal Identification Number）码的身份验证，旨在让调试环境下的攻击者更难利用调试器。启动程序时可以看到类似的启动提示：     
```
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 150-759-644
 * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)
```

&emsp;&emsp;当程序有异常而进入错误堆栈模式，第一次点击某个堆栈查看对应变量的值的时候，浏览器会弹出一个要求你输入这个 PIN 值的输入框。这个时候需要在输入框中输入 `150-759-644` ，然后确认，Werkzeug 会把这个 PIN 作为 cookie 的一部分存起来（失效时间默认是 8 小时），失效之前不需要重复输入。而这个 PIN 码攻击者是无法知道的。当然，也可以自己指定 PIN 码的值：      
```
WERKZEUG_DEBUG_PIN=123 python run.py
```