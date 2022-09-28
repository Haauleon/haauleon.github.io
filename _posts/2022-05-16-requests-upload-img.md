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

![](\img\in-post\post-other\2022-05-16-requests-1.jpg)     

<br>

###### 获取响应   
当一个请求被发送后，会有一个 response 响应。requests 同样为这个 response 赋予了相关方法：         

![](\img\in-post\post-other\2022-05-16-requests-2.jpg)   


<br><br>

### 示例代码
###### 获取7160网站的图片
&emsp;&emsp;获取 7160 网站当前页面的图片，使用 requests 和 BeautifulSoup 获取图片并保存到本地（一次性全部写入）。     
