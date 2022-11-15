---
layout:        post
title:         "Flask Web | 动态 URL 规则"
subtitle:      "将符合同种规则的 URL 抽象成一个 URL 模式"
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

### 一、URL 规则
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.12.1    

<br>

#### 1、URL 不抽象写法
&emsp;&emsp;URL 规则可以添加变量部分，也就是将符合同种规则的 URL 抽象成一个 URL 模式，如 /item/1、/item/2、/item/3 ...假如不抽象，就得这样写：     
```python
# coding=utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/item/1')
def item1():
    return 'item: 1'


@app.route('/item/2')
def item2():
    return 'item: 2'


@app.route('/item/3')
def item3():
    return 'item: 3'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
```

<br>
<br>

#### 2、URL 抽象写法
&emsp;&emsp;如上所述，如果不抽象，那么当 /item/ 后拼接多少 id，就写写多少 URL 和视图函数，这样的代码既不简洁也不美观。正确的用法如下：      
```python
# coding=utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/item/<id>')
def item(id):
    return 'item: {}'.format(id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
```

&emsp;&emsp;其中，`@app.route('/item/<id>')` 尖括号中的内容是动态的，凡是匹配到 /item/ 前缀的 URL 都会被映射到这个路由上，在内部把 id 作为参数而获得。     
&emsp;&emsp;它使用了特殊的字段标记 <variable_name> ，默认类型是字符串，也就是说我们在浏览器输入的字符会被当做是字符串传给对应的 item() 函数进行处理。