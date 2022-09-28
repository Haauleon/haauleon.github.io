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
```python
'''
http://www.7160.com/meishitupian/list_15_2.html
pip install beautifulsoup4  # 需要先安装此模块

'''

# 0. 导包
import os
import requests
from bs4 import BeautifulSoup  # 不能直接import BeautifulSoup导入，会报错

#  在代码之前先定义全局常量
# os.path.abspath(__file__) 指当前文件的绝对路径
# os.path.dirname() 指父级目录的绝对路径
# os.path.dirname(os.path.abspath(__file__)) 指以当前文件的绝对路径找到父级目录的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. 模拟浏览器发请求
response = requests.get(url='http://www.7160.com/meishitupian/list_15_2.html')
# print(response.status_code)  # 查看是否请求成功
# print(response.encoding)  # 查看编码类型
response.encoding = 'gbk'  # 获取的文件信息是乱码，需要转码，可以尝试多种，直到正常显示

# 2. 获取字符串形式的请求内容，方便后续代码中使用
text = response.text

# 3. 使用bs4库解析请求，需要传入需要解析的文件，指定解析器
soup = BeautifulSoup(text, 'html.parser')  # 需要解析的文件是text文本类型的，所以使用html.parser:解析器负责解析文本
# print(soup)  # 结果同text相同，拿到解析结果去分析和操作数据

# 从整个文本中进一步缩小定位范围
# 查找name是div盒子，这个div中class的名字为news_bom-left的内容
# find方法中此类参数的固定写法
div_obj = soup.find(name='div', attrs={"class": "news_bom-left"})

# 4. 定位图片位置
li_list = div_obj.find_all(name="li")  # 从这个盒子中找所有li标签

# 图片要一张一张去处理并保存，所以要循环，
for li in li_list:
    # 5. 获取图片链接
    img = li.find(name='img')  # 查看这一条li中name是img的标签
    src = img.get("src")  # 从这个标签中获取图片的链接
    
    # 6. 使用requests模块向图片链接发请求
    res = requests.get(url=src)
    
    # 7. 保存图片到本地
    # os.path.join 是拼接路径，BASE_DIR指当前文件的父级目录的绝对路径
    # src.rsplit('/', 1)[-1] 是切割了图片地址，使用切片后的字符串作为要保存的文件的名字，也可以用其他的字段进行处理作为文件名
    # 这一步实际就是给即将保存的文件安排一个路径，这个路径就是当前文件所处的父文件夹下的7160这个文件夹
    # 注意：'7160'这个文件夹要先创建好，不然会报错
    file_path = os.path.join(BASE_DIR, '7160', src.rsplit('/', 1)[-1])
    with open(file_path, 'wb') as f:  # 图片信息是二进制形式，所以要用wb写入
        f.write(res.content)  # 将请求图片获取到的二进制响应内容写入文件中
    # break  # 调试时候用，只获取第一条信息，调试结束，注释掉break,即可全部获取到文件
```

