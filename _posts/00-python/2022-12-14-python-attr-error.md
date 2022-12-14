---
layout:        post
title:         "Python | AttributeError 属性异常"
subtitle:      "AttributeError: 'Request' object has no attribute 'is_xhr'"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### AttributeError
&emsp;&emsp;在运行 flask 项目时，报错信息如下：      
```
127.0.0.1 - - [14/Dec/2022 18:20:11] "GET / HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/mnt/d/gitee/flask_web/venv/lib/python2.7/site-packages/flask/app.py", line 2000, in __call__
    return self.wsgi_app(environ, start_response)
  File "/mnt/d/gitee/flask_web/venv/lib/python2.7/site-packages/flask/app.py", line 1991, in wsgi_app
    response = self.make_response(self.handle_exception(e))
  File "/mnt/d/gitee/flask_web/venv/lib/python2.7/site-packages/flask/app.py", line 1567, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/mnt/d/gitee/flask_web/venv/lib/python2.7/site-packages/flask/app.py", line 1988, in wsgi_app
    response = self.full_dispatch_request()
  File "/mnt/d/gitee/flask_web/venv/lib/python2.7/site-packages/flask/app.py", line 1642, in full_dispatch_request
    response = self.make_response(rv)
  File "/mnt/d/gitee/flask_web/venv/lib/python2.7/site-packages/flask/app.py", line 1746, in make_response
    rv = self.response_class.force_type(rv, request.environ)
  File "/mnt/d/gitee/flask_web/app_response.py", line 13, in force_type
    rv = jsonify(rv)
  File "/mnt/d/gitee/flask_web/venv/lib/python2.7/site-packages/flask/json.py", line 254, in jsonify
    if current_app.config['JSONIFY_PRETTYPRINT_REGULAR'] and not request.is_xhr:
  File "/mnt/d/gitee/flask_web/venv/lib/python2.7/site-packages/werkzeug/local.py", line 347, in __getattr__
    return getattr(self._get_current_object(), name)
AttributeError: 'Request' object has no attribute 'is_xhr'
```

<br>

解决属性异常的方法：    
```
  ...
  File "/mnt/d/gitee/flask_web/app_response.py", line 13, in force_type
    rv = jsonify(rv)
  File "/mnt/d/gitee/flask_web/venv/lib/python2.7/site-packages/flask/json.py", line 254, in jsonify
    if current_app.config['JSONIFY_PRETTYPRINT_REGULAR'] and not request.is_xhr:
  File "/mnt/d/gitee/flask_web/venv/lib/python2.7/site-packages/werkzeug/local.py", line 347, in __getattr__
    return getattr(self._get_current_object(), name)
AttributeError: 'Request' object has no attribute 'is_xhr'
```
&emsp;&emsp;如上代码片段，往上溯源，发现这个异常是出现在 `.../venv/lib/python2.7/site-packages/werkzeug/local.py` 文件中的，而与这个文件 local.py 有关系的就是 werkzeug 这个第三方包；再往上溯源，发现 werkzeug 又是 flask 的依赖包，执行到 `if current_app.config['JSONIFY_PRETTYPRINT_REGULAR'] and not request.is_xhr:` 发现 request 对象没有 is_xhr 这个属性。所以问题很明显了，在运行 flask 项目的时候，依赖的 werkzeug 包中不存在 `Request.is_xhr` 这个属性导致项目运行失败。                
&emsp;&emsp;出现这个问题的原因是由于第三方包存在很多版本，好巧我们调用的方法或者属性在这个包的当前版本中不存在，那么就需要去 PYPI 市场去根据包名进行搜索，找到其他符合的版本来重新下载安装。      
