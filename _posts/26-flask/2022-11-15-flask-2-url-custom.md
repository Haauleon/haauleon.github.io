---
layout:        post
title:         "Flask Web | 自定义转换器"
subtitle:      "自定义一个 URL 转换器来实现同时接收多个参数并处理"
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

### 一、URL 转换器
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1    

&emsp;&emsp;Reddit 可以通过在 URL 中使用一个加号 `+` 隔开各个社区的名字，方便同时查看多个社区的帖子。比如访问 http://reddit.com/r/flask+lisp ，就可以同时查看 flask 和 lisp 这两个社区的帖子，如下图所示：      
![](\img\in-post\post-flask\2022-11-15-url-translator-custom-1.jpg)  

<br>
<br>

### 二、自定义转换器
&emsp;&emsp;现在来自定义一个 URL 转换器实现上述 Reddit 社区查看多个帖子的功能，除此之外还可以设置所使用的分隔符，不一定要用加号 `+`。自定义转换器需要继承自 BaseConverter 类，要设置 to_python 和 to_url 这两个方法：            
```python
# -*- coding: utf-8 -*-#
import urllib
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class ListConverter(BaseConverter):

    def __init__(self, url_map, separator='+'):
        super(ListConverter, self).__init__(url_map)
        self.separator = urllib.unquote(separator)

    def to_python(self, value):
        """把路径转换成一个 Python 对象"""
        return value.split(self.separator)

    def to_url(self, values):
        """把参数转换成符合 URL 的形式"""
        return self.separator.join(BaseConverter.to_url(self, value) for value in values)


app.url_map.converters['list'] = ListConverter


@app.route('/list1/<list:page_names>')
def list1(page_names):
    """使用 + 作分隔符"""
    return 'Separator: {} {}'.format('+', page_names)


@app.route('/list2/<list(separator=u"|"):page_names>')
def list2(page_names):
    """使用 | 作分隔符"""
    return 'Separator: {} {}'.format('|', page_names)


@app.route('/list3/<list(separator=u" "):page_names>')
def list3(page_names):
    """使用空格作分隔符"""
    return 'Separator: {} {}'.format(' ', page_names)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

```

<br>

执行结果如下：    
1. `访问 http://127.0.0.1:9000/list1/a+b+c+d+e`          
    ![](\img\in-post\post-flask\2022-11-15-url-translator-custom-2.jpg)   

2. `访问 http://127.0.0.1:9000/list2/a|b|c|d|e`                 
    ![](\img\in-post\post-flask\2022-11-15-url-translator-custom-3.jpg)  

3. `访问 http://127.0.0.1:9000/list3/a b c d e`            
    ![](\img\in-post\post-flask\2022-11-15-url-translator-custom-4.jpg)  