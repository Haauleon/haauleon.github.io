---
layout:        post
title:         "爬虫 | requests 模块下载图片"
subtitle:      "通过 requests 请求文件链接，将文件下载至本地"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 爬虫
    - Python
    - API 测试
---

参考：[https://www.cnblogs.com/caoyinshan/p/12072847.html](https://www.cnblogs.com/caoyinshan/p/12072847.html)

<br><br>

### 通用代码设计
```python
import requests
import os


class ConfigHandler:
    _SLASH = os.sep

    # 项目路径
    root_path = os.path.dirname(os.path.abspath(__file__))
    # 图片路径
    img_path = os.path.join(root_path, 'img' + _SLASH)


class IMGHandler:

    @staticmethod
    def download_img(img_url):
        res = requests.get(img_url, stream=True)
        if res.status_code == 200:
            file_path = ConfigHandler.img_path + img_url.rsplit('/', 1)[-1]
            print(file_path)
            with open(file_path, 'wb') as f:
                f.write(res.content)


if __name__ == '__main__':
    IMGHandler.download_img('https://img.alicdn.com/imgextra/i4/2204820661060/O1CN01YGnn5C1JhWX2heNVv_!!2204820661060'
                            '-0-beehive-scenes.jpg')

```

<br><br>

### 使用 requests 获取图片并保存
&emsp;&emsp;获取某一个网站的图片信息需要用到 requests 模块,所以我们需要安装 requests。

###### 安装
```linux
$ pip install requests  # 直接安装
$ pip install -i https://pypi.doubanio.com/simple/ requests  # 指定地址安装
```

<br>

###### 测试是否安装成功
&emsp;&emsp;网络正常的情况下，可以访问百度，证明安装成功。    
```python
import requests   # 回车不报错就算安装成功
response = requests.get("https://www.baidu.com")
print(response.status_code)  # 200，证明访问成功
```

<br>

###### 发送请求
```python
import requests  # 导包
response = requests.request(method='get', url='https://www.baidu.com')  # 向百度首页发送请求，请求方式是get
print(response.status_code)  # 获取返回code码
```

<br>

###### requests 类中常用的参数      
- method：请求方式
- url：请求URL
- **kwargs
    - params：字典或者字节序列，使用这个参数可以把一些键值对以k1=v1&k2=v2的模式增加到url中，get请求中用的较多
    - data：字典、字节序列或者文件对象，重点作为向服务器提供或提交资源，作为请求的请求体，它也可以接受一个字符串对象
    - json：json格式的数据，可以向服务器提交json类型的数据
    - headers：字典，定义请求的请求头，比如可以headers字典定义user agent
    - cookies：字典或者CookieJar
    - auth：元组，用来支持HTTP认证功能
    - files：字典，用来向服务器传输文件
    - timeout：指定超时时间
    - proxies：字典，设置代理服务器
    - allow_redirects：开关，是否允许对URL进行重定向，默认为True
    - stream：开关，是否对获取内容进行立即下载，默认为False，也就是立即下载。stream一般应用于流式请求，比如说下载大文件，不可能一次请求就把整个文件都下载了，不现实。这种情况下，就要设置stream=True，requests无法将连接释放回连接池，除非下载完了所有数据，或者调用了response.close
    - verify：开关，用于SSL证书认证，默认为True
    - cert：用于设置保存本地SSL证书路径

<br>

