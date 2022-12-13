---
layout:        post
title:         "Flask Web | 动态 URL 规则"
subtitle:      "将符合同种规则的 URL 抽象成一个 URL 模式"
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

### 一、URL 规则
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1    

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
&emsp;&emsp;如上所述，如果不抽象，那么当 /item/ 后拼接多少个不同的 id 时，就要写多少个符合此 id 的 URL 和视图函数，这样的代码既不简洁也不美观。正确的写法如下：      
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
&emsp;&emsp;它使用了特殊的字段标记 `<variable_name>` ，默认类型是字符串，也就是说我们在浏览器输入的字符会被当做是字符串传给对应的 item() 函数进行处理。   

<br>
<br>

### 二、指定参数类型
如果需要指定参数类型，需要标记成 `<converter:variable_name>` 这样的格式， converter 有以下几种：      

|converter|释义|
|----|----|
|string|接受任何没有斜杠 `/` 的文本（不指定类型时默认是字符串类型）|
|int|接受整数|
|float|同 int，但是接受浮点数|
|path|和默认的相似，但也接受斜杆 `/`|
|uuid|只接受 uuid 字符串|
|any|可以指定多种路径，但是需要传入参数。相当于限制了参数的可选范围，不在范围内的参数则返回 404 Not Found|

<br>

#### 1、指定 any 类型
**any 类型代码片段：**       
```python
# coding=utf-8
from flask import Flask

app = Flask(__name__)


@app.route('/item/<any(a,b,c,d):id>')
def item(id):
    return 'item: {}'.format(id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
```

&emsp;&emsp;如上，在浏览器中访问 /item/a、/item/b、/item/c、/item/d 都符合这个规则，访问 /item/a 则返回 `item: a`，访问 /item/b 则返回 `item: b`，以此类推。如果访问了 /item/e 则返回 404 Not Found，因为参数 e 不在 any() 的可选范围内。         
```
> http GET http://127.0.0.1:9000/item/a
HTTP/1.0 200 OK
Content-Length: 7
Content-Type: text/html; charset=utf-8
Date: Tue, 13 Dec 2022 07:53:07 GMT
Server: Werkzeug/1.0.1 Python/2.7.18

item: a


> http GET http://127.0.0.1:9000/item/b
HTTP/1.0 200 OK
Content-Length: 7
Content-Type: text/html; charset=utf-8
Date: Tue, 13 Dec 2022 07:53:11 GMT
Server: Werkzeug/1.0.1 Python/2.7.18

item: b


> http GET http://127.0.0.1:9000/item/c
HTTP/1.0 200 OK
Content-Length: 7
Content-Type: text/html; charset=utf-8
Date: Tue, 13 Dec 2022 07:53:19 GMT
Server: Werkzeug/1.0.1 Python/2.7.18

item: c


> http GET http://127.0.0.1:9000/item/d
HTTP/1.0 200 OK
Content-Length: 7
Content-Type: text/html; charset=utf-8
Date: Tue, 13 Dec 2022 07:53:23 GMT
Server: Werkzeug/1.0.1 Python/2.7.18

item: d


> http GET http://127.0.0.1:9000/item/e
HTTP/1.0 404 NOT FOUND
Content-Length: 232
Content-Type: text/html; charset=utf-8
Date: Tue, 13 Dec 2022 07:53:26 GMT
Server: Werkzeug/1.0.1 Python/2.7.18

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
```

<br>
<br>

### 三、参数传递
&emsp;&emsp;如果不希望定制子路径，还可以通过传递参数的方式，需要导入 request：             
```python
# coding=utf-8
from flask import Flask, request

app = Flask(__name__)


@app.route('/item/')
def item():
    id = request.args.get('id')
    return 'item: {}'.format(id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
```

&emsp;&emsp;如上，在浏览器中访问 http://127.0.0.1/item/?id=1 则返回 `item: 1`。