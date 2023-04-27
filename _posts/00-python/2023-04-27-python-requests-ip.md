---
layout:        post
title:         "Python3 | python搭建ip池"
subtitle:      "pyppeteer.errors.PageError: net::ERR_SSL_VERSION_OR_CIPHER_MISMATCH at ..."
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

> 在爬取网站的时候我们有时候会遭受封ip等显现，因此我们需要搭建自己的ip池用于爬虫。

<br>
<br>

### 代码过程简述
1、爬取代理ip网站信息    
2、将获取的信息处理得到ip等关键信息    
3、保存首次获取的ip信息并检测其是否可用    
4、检测完毕将可用ip保存，搭建完成     

![](https://img-blog.csdnimg.cn/082783ed2882434b80540976b8891aff.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rWpwrc=,size_20,color_FFFFFF,t_70,g_se,x_16)          

本文是单线程，比较简单但效率可能没有那么快。

<br>
<br>

下面是搭建完后的ip池展示：      
![](https://img-blog.csdnimg.cn/a719054604294592b42d249062ef57df.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rWpwrc=,size_20,color_FFFFFF,t_70,g_se,x_16)         

<br>
<br>

老规矩先放总的代码后再一步步解析：    
```python
# -*- coding: gbk -*-    # 防止出现乱码等格式错误
# ip代理网站：http://www.66ip.cn/areaindex_19/1.html
 
import requests
from fake_useragent import UserAgent
import pandas as pd
from lxml import etree # xpath
 
# ---------------爬取该网站并获取通过xpath获取主要信息----------------
def get_list_ip(city_id):
    url = 'http://www.66ip.cn/areaindex_{}/1.html'.format(city_id)
    headers = {
        'User-Agent': UserAgent().random,
    }
    data_html = requests.get(url=url, headers=headers)
    data_html.encoding = 'gbk'
    data_html = data_html.text
 
    html = etree.HTML(data_html)
    etree.tostring(html)
    list_ip = html.xpath('//div[@align="center"]/table/tr/td/text()')      # 获取html含有ip信息的那一行数据
    return list_ip
 
# --------------将爬取的list_ip关键信息进行处理、方便后续保存----------------
def dispose_list_ip(list_ip):
    num = int((int(len(list_ip)) / 5) - 1)  # 5个一行，计算有几行，其中第一行是标题直接去掉
    content_list = []
 
    for i in range(num):
        a = i * 5
        ip_index = 5 + a  # 省去前面的标题，第5个就是ip，往后每加5就是相对应ip
        location_index = 6 + a
        place_index = 7 + a
 
        items = []
        items.append(list_ip[ip_index])
        items.append(list_ip[location_index])
        items.append((list_ip[place_index]))
        content_list.append(items)
    return content_list
 
# -----------将处理结果保存在csv-------------
def save_list_ip(content_list,file_path):
    columns_name=["ip","port","place"]
    test=pd.DataFrame(columns=columns_name,data=content_list)         # 去掉索引值，否则会重复
    test.to_csv(file_path,mode='a',encoding='utf-8')
    print("保存成功")
 
# -----------读取爬取的ip并验证是否合格-----------
def verify_ip(file_path):
    file = pd.read_csv(file_path)
    df = pd.DataFrame(file)
    verify_ip = []
 
    for i in range(len(df)):
        ip_port = str(df["ip"][i]) + ":" + str(df["port"][i])  # 初步处理ip及端口号
        headers = {
            "User-Agent": UserAgent().random
        }
        proxies = {
            'http': 'http://' + ip_port
            # 'https': 'https://'+ip_port
        }
        '''http://icanhazip.com访问成功就会返回当前的IP地址'''
        try:
            p = requests.get('http://icanhazip.com', headers=headers, proxies=proxies, timeout=3)
            item = []  # 将可用ip写入csv中方便读取
            item.append(df["ip"][i])
            item.append(df["port"][i])
            item.append(df["place"][i])
            verify_ip.append(item)
            print(ip_port + "成功！")
        except Exception as e:
            print("失败")
    return verify_ip
 
 
if __name__ == '__main__':
 
    # ----------爬取与保存------------
 
    save_path = "test.csv"
    city_num = int(input("需要爬取几个城市ip"))   # 1~34之间，该网站只有34个城市页面
    content_list = []
    for i in range(city_num):             # 批量爬取list_ip关键信息并保存
        response = get_list_ip(i)
        list = dispose_list_ip(response)
        content_list += list        # 将每一页获取的列表连接起来
 
    save_list_ip(content_list,save_path)
    # -----------验证--------------
    open_path = "test.csv"
    ip = verify_ip(open_path)
    # ---------保存验证结果-----------
    save_path = "verify_ip.csv"
    save_list_ip(ip,save_path)
```

<br>
<br>

### 一、爬取代理ip网站信息     
先导入所用到的库：     
```python
import requests    
from fake_useragent import UserAgent    # 用来随机UserAgent值（用自己的也不影响）
import pandas as pd
from lxml import etree # xpath
```
<br>

随便找到一个免费的ip代理网站。这个网站没什么反爬机制，找到网站的url规律直接request  get他就行。       
![](https://img-blog.csdnimg.cn/429e16ac76974c4ca606ad543143e949.png)         

<br>

这里可以看出只是改了一下数字而已，直接get他      
```python
# ---------------爬取该网站并获取通过xpath获取主要信息----------------
def get_list_ip(city_id):      #  city_id用来询问要爬取多少个城市
    url = 'http://www.66ip.cn/areaindex_{}/1.html'.format(city_id)
    headers = {
        'User-Agent': UserAgent().random,
    }
    data_html = requests.get(url=url, headers=headers)
    data_html.encoding = 'gbk'
    data_html = data_html.text
 
    html = etree.HTML(data_html)
    etree.tostring(html)
    list_ip = html.xpath('//div[@align="center"]/table/tr/td/text()')      # 获取html含有ip信息的那一行数据
    return list_ip
```

<br>

尝试输出一下看一下结果      
```python
city_num = int(input("需要爬取几个城市ip"))   # 1~34之间，该网站只有34个城市页面
  
for i in range(city_num):             # 批量爬取list_ip关键信息并保存
    response = get_list_ip(i)
    print(response)
```
![](https://img-blog.csdnimg.cn/a01c62f03d974c21ba86597fb13ceeca.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rWpwrc=,size_20,color_FFFFFF,t_70,g_se,x_16)     

<br>
<br>

### 二、将获取的信息处理得到ip等关键信息  
从上面返回的结果看出，列表每隔五个出现一次循环，假设列表有n个元素，那么就有n/5个ip，第五个开始出现ip，第六个出现端口号，第七个出现地址，列表第5+5个出现第二个ip，6+5个位置出现第二个端口号，有这个规律后就可以开始处理。  
```python
def dispose_list_ip(list_ip):
    num = int((int(len(list_ip)) / 5) - 1)  # 5个一行，计算有几行，其中第一行是标题直接去掉
    content_list = []
 
    for i in range(num):
        a = i * 5
        ip_index = 5 + a  # 省去前面的标题，第5个就是ip，往后每加5就是相对应ip
        location_index = 6 + a
        place_index = 7 + a
 
        items = []
        items.append(list_ip[ip_index])
        items.append(list_ip[location_index])
        items.append((list_ip[place_index]))
        content_list.append(items)
    return content_list
```

尝试输出一下：    
```python
    city_num = int(input("需要爬取几个城市ip"))   # 1~34之间，该网站只有34个城市页面
    content_list = []
    for i in range(city_num):             # 批量爬取list_ip关键信息并保存
        response = get_list_ip(i)
 
        list = dispose_list_ip(response)
        content_list += list        # 将每一页获取的列表连接起来
    print(content_list)
```
![](https://img-blog.csdnimg.cn/99cc2480a0ab4cebba5bfadde79261eb.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5rWpwrc=,size_20,color_FFFFFF,t_70,g_se,x_16)    

<br>
<br>

### 三、保存首次获取的ip信息并检测其是否可用
保存代码：    
```python
def save_list_ip(content_list,file_path):
    columns_name=["ip","port","place"]
    test=pd.DataFrame(columns=columns_name,data=content_list)         # 去掉索引值，否则会重复
    test.to_csv(file_path,mode='a',encoding='utf-8')
    print("保存成功")
```

首次保存后，读取保存的ip并对其进行一个验证是否可用，验证完毕后再将可用ip保存到csv中      
```python
# -----------读取爬取的ip并验证是否合格-----------
def verify_ip(file_path):
    file = pd.read_csv(file_path)
    df = pd.DataFrame(file)
    verify_ip = []
 
    for i in range(len(df)):
        ip_port = str(df["ip"][i]) + ":" + str(df["port"][i])  # 初步处理ip及端口号
        headers = {
            "User-Agent": UserAgent().random
        }
        proxies = {
            'http': 'http://' + ip_port
            # 'https': 'https://'+ip_port
        }
        '''http://icanhazip.com访问成功就会返回当前的IP地址'''
        try:
            p = requests.get('http://icanhazip.com', headers=headers, proxies=proxies, timeout=3)
            item = []  # 将可用ip写入csv中方便读取
            item.append(df["ip"][i])
            item.append(df["port"][i])
            item.append(df["place"][i])
            verify_ip.append(item)
            print(ip_port + "成功！")
        except Exception as e:
            print("失败",e)
    return verify_ip
```

<br>
<br>

### 最终运行
将上面全部功能模块合并在一起就搭建完成啦！     
```python
if __name__ == '__main__':
 
    # ----------爬取与保存------------
    save_path = "test.csv"
    city_num = int(input("需要爬取几个城市ip"))   # 1~34之间，该网站只有34个城市页面
    content_list = []
    for i in range(city_num):             # 批量爬取list_ip关键信息并保存
        response = get_list_ip(i)
 
        list = dispose_list_ip(response)
        content_list += list        # 将每一页获取的列表连接起来
    print(content_list)
 
    save_list_ip(content_list,save_path)
    # -----------验证--------------
    open_path = "test.csv"
    ip = verify_ip(open_path)
    # ---------保存验证结果-----------
    save_path = "verify_ip.csv"
    save_list_ip(ip,save_path)
```

<br>
<br>

---

相关链接：   
[python搭建ip池](https://blog.csdn.net/m0_61720747/article/details/123757200?spm=1001.2014.3001.5502)