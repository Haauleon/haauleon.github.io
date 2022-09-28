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

&emsp;&emsp;使用此种方法有个弊端，如果文件过大，可能会导致下载到本地之后，导致本地存储空间不足，下载完毕之后会有部分文件丢失。如果是大文件或者多个文件，建议循环下载，如果存储空间不足，之前的文件不会缺失。可以使用 iter_content 方法按字节大小循环下载，代码如下。               
```python
# stream默认情况下是false，会立即开始下载文件并存放到内存当中
# 当把stream的参数设置成True时，它不会立即开始下载，当你使用iter_content遍历内容或访问内容属性时才开始下载
response = requests.get(url_file, stream=True)
with open("file_path", "wb") as f:
# iter_content：一块一块的遍历要下载的内容，chunk_size是每一块的字节数，结合使用可以防止占用过多的内存
# 循环下载文件，按照chunk_size设置的字节数，每次只下载这一大小的数据
    for i in response.iter_content(chunk_size=512):
            f.write(i)
```

<br>

###### 获取天极网的图片
&emsp;&emsp;获取天极网的图片，保存图片时有多级文件夹，可以使用循环内部套循环获取二级页面的图片,并分两级文件夹保存，代码如下。       
```python
'''
http://pic.yesky.com/c/6_3655_5.shtml
需求：
将图片上的文件按页面的分类保存，一共两级文件夹，保存的格式如下
               'tianji'                # 一级文件夹
                  '赵薇图片'            # 二级文件夹
                      '赵薇图片111'     # 具体图片文件
                      '赵薇图片222'
                      '赵薇图片333'
                  '林心如图片'
                  '李沁图片'
'''
import os
import requests
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 1、向指定连接发请求
response = requests.get(url='http://pic.yesky.com/c/6_3655_5.shtml')

# 2、使用bs4解析requests请求的响应文本
soup = BeautifulSoup(response.text, 'html.parser')   # 延伸可搜索lxml，学习python3解析库lxml
div_obj = soup.find(name='div', attrs={"class": "lb_box"})
dd_list = div_obj.find_all(name='dd')

for dd in dd_list:
    # 获取div中所有图片所在a标签的url
    a_url = dd.find(name='a').get('href')
    # 要先创建好'tianji'文件夹，再在此文件夹下创建N个二级文件夹用来存放图片
    path = os.path.join(BASE_DIR, 'tianji', dd.find(name='a').text)
    if not os.path.isdir(path):  # 如果不存在这个二级文件夹，则创建，不加这一步可能会报错
        os.mkdir(path)
    
    # 向url发请求
    a_response = requests.get(url=a_url)
    a_response.encoding = 'gbk'

    # 拿到url中的text文本
    a_text = a_response.text
    son_soup = BeautifulSoup(a_text, 'html.parser')  # lxml
    son_div_obj = son_soup.find(name='div', attrs={"id": "scroll"})
    
    for img in son_div_obj.find_all(name='img'):
        # 获取图片链接，并发请求
        son_src = img.get('src').replace('113x113', '740x-')  # 使用大图的像素替换图片链接中的小图像素，达到获取大图的目的
        son_response = requests.get(url=son_src)
        
        # 打开文件写入
        img_path = os.path.join(path, son_src.rsplit("/", 1)[-1])
        with open(img_path, 'wb') as f:
            f.write(son_response.content)
        break
    break
```

<br>

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