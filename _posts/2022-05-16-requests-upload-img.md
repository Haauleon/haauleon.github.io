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

![](\img\in-post\post-other\2022-05-16-requests-2.jpg)   


<br><br>

### 示例代码

###### 获取汽车之家图片
&emsp;&emsp;获取汽车之家图片，顺序获取前 20 页，将获取图片的代码封装成了函数，需要获取多少页只需简单修改参数就行，代码如下。       
```python
import os, time
import requests   # 模拟浏览器发请求
from bs4 import BeautifulSoup   # 解析请求结果，也就是去请求结果中，取数据

url = "https://www.autohome.com.cn/all/"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def spider(num):
    
    # 1. 使用requests模块向指定地址发请求，获取请求结果
    response = requests.get(url="https://www.autohome.com.cn/all/{}/#liststart".format(num))
    # 2. 转码
    response.encoding = "gbk"
    
    # 3. 使用bs4取数据，解析请求结果
    soup = BeautifulSoup(response.text, "html.parser")
    div_obj = soup.find(name='div', attrs={"id": "auto-channel-lazyload-article"})
    img_list = div_obj.find_all(name="img")
    
    for img in img_list:
        # 获取图片的url，因为源地址是不全的，我们要拼接
        img_url = "https:" + img.get("src")
        # 使用requests模块向图片地址发请求，获取图片数据，bytes
        img_response = requests.get(url=img_url)
        # 制作保存图片的路径
        file_path = os.path.join(BASE_DIR, '222', img_url.rsplit('/', 1)[-1])
        # 将bytes类型的数据保存到本地
        with open(file_path, 'wb') as f:
            f.write(img_response.content)
        print('{} 爬取完毕'.format(img_url))  # 下载时在控制台输入信息提示


if __name__ == '__main__':
    start = time.time()  # 开始执行时 当前时间的时间戳
    for num in range(1, 20):  # 循环获取1-20页的图片
        spider(num)  # 获取当前页的图片信息
    print(time.time() - start)  # 结束时的时间戳-开始时间的时间戳,计算差即用时时长
```

<br>
 
###### 通过线程池获取
&emsp;&emsp;通过线程池获取，无顺序，但是提高了效率，缩短了获取时间。     
```python
# 1、导包
from concurrent.futures import ThreadPoolExecutor  # 线程池

# 2、在代码中需要使用的位置上方加这一行
# 表示线程开始，将需要使用线程池的代码放进来
t = ThreadPoolExecutor(max_workers=10)  # max_workers表示线程数

# 3、在代码中结束的位置下方加这一行
# 当代码执行完，结束线程，不再往进加任务
t.shutdown()
```

&emsp;&emsp;线程池获取汽车之家新闻页前20页图片--提高效率，代码如下。      
```python
import os, time
import requests   # 模拟浏览器发请求
from bs4 import BeautifulSoup   # 解析请求结果，也就是去请求结果中，取数据
from concurrent.futures import ThreadPoolExecutor  # 线程池

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def spider(num):
    # 1. 使用requests模块向指定地址发请求
    # response = requests.request(method='get', url=url)
    page_url = "https://www.autohome.com.cn/all/{}/#liststart".format(num)
    response = requests.get(url=page_url)
    # 2. 获取请求结果
    # print(response.encoding)  # ISO-8859-1
    response.encoding = "gbk"
    # print(response.text)
    # 3. 使用bs4取数据，解析请求结果
    soup = BeautifulSoup(response.text, "html.parser")
    div_obj = soup.find(name='div', attrs={"id": "auto-channel-lazyload-article"})
    img_list = div_obj.find_all(name="img")

    for img in img_list:
        # 获取图片的url，因为源地址是不全的，我们要拼接
        img_url = "https:" + img.get("src")
        # 使用requests模块向图片地址发请求，获取图片数据，bytes
        img_response = requests.get(url=img_url)
        # 制作保存图片的路径
        file_path = os.path.join(BASE_DIR, '222', img_url.rsplit('/', 1)[-1])
        # 将bytes类型的数据保存到本地
        with open(file_path, 'wb') as f:
            f.write(img_response.content)
        print('正在爬取{} 页 中的{}图片 爬取完毕'.format(page_url, img_url))

if __name__ == '__main__':
    start = time.time()
    t = ThreadPoolExecutor(max_workers=10)  # 10个线程，每次10个线程去获取数据，可提高效率
    for num in range(1, 20):
        t.submit(spider, num)
    t.shutdown()  # 线程结束。当循环结束，结束线程，不再往进加任务
    print(time.time() - start)
```