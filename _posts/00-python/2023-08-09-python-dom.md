---
layout:        post
title:         "Python3 | xpath 获取 html 元素对象"
subtitle:      "获取 DOM 树各个节点的 xpath 路径"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---


### 代码实现     
在使用 python 进行网络爬虫并对网页解析成 DOM 树时，有时需要获取各个 DOM 树节点的 xpath 路径。具体代码如下：           

方法1、生成 DOM 各节点的 xpath 路径            
```python
import lxml
from lxml import etree
import collections

doc='''
<html>
 <head>
  <base href='http://example.com/' />
  <title>Example website</title>
 </head>
 <body>
  <div id='images'>
   <a href='image1.html' id="xxx">Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
   <h5>test</h5>
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
   <a href='image5.html' class='li li-item' name='items'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
   <a href='image6.html' name='items'><span><h5>test</h5></span>Name: My image 6 <br /><img src='image6_thumb.jpg' /></a>
  </div>
 </body>
</html>
'''
html=etree.HTML(doc)
tree=html.getroottree()
all_nodes=html.xpath('//*')
xpath=[]
for node in all_nodes:
    xpath.append(tree.getpath(node))
for node,path in zip(all_nodes,xpath):
    print("{}：{}".format(node.tag,path))

```

<br>

方法2     
```python
import lxml
from lxml import etree
import collections

doc='''
<html>
 <head>
  <base href='http://example.com/' />
  <title>Example website</title>
 </head>
 <body>
  <div id='images'>
   <a href='image1.html' id="xxx">Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
   <h5>test</h5>
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
   <a href='image5.html' class='li li-item' name='items'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
   <a href='image6.html' name='items'><span><h5>test</h5></span>Name: My image 6 <br /><img src='image6_thumb.jpg' /></a>
  </div>
 </body>
</html>
'''
html=etree.HTML(doc)
all_nodes=html.xpath('/html') #用于保存DOM树上的所有节点
idx=0
start=0
end=len(all_nodes)
xpath=['/'+str(all_nodes[0].tag)]
while start<end:
    for i in range(start,end):
        c_nodes=list(all_nodes[i]) #main_nodes[i]的子节点
        tmp_tag_count={key:1 for key,val in collections.Counter(node.tag for node in c_nodes).items()
                       if val>1}
        all_nodes.extend(c_nodes)
        tmp_xpath=xpath[i]
        for node in c_nodes:
            if node.tag in tmp_tag_count.keys():
                xpath.append(tmp_xpath+'/'+node.tag+'['+str(tmp_tag_count[node.tag])+']')
                tmp_tag_count[node.tag]+=1
            else:
                xpath.append(tmp_xpath+'/'+node.tag)
        idx+=1
    start=idx
    end=len(all_nodes)
    
for node,path in zip(all_nodes,xpath):
    print("{} {}".format(node.tag,path))

```

<br>

其计算结果如下：          
```bash
html  /html
head  /html/head
body  /html/body
base  /html/head/base
title  /html/head/title
div  /html/body/div
a  /html/body/div/a[1]
h5  /html/body/div/h5
a  /html/body/div/a[2]
a  /html/body/div/a[3]
a  /html/body/div/a[4]
a  /html/body/div/a[5]
a  /html/body/div/a[6]
br  /html/body/div/a[1]/br
img  /html/body/div/a[1]/img
br  /html/body/div/a[2]/br
img  /html/body/div/a[2]/img
br  /html/body/div/a[3]/br
img  /html/body/div/a[3]/img
br  /html/body/div/a[4]/br
img  /html/body/div/a[4]/img
br  /html/body/div/a[5]/br
img  /html/body/div/a[5]/img
span  /html/body/div/a[6]/span
br  /html/body/div/a[6]/br
img  /html/body/div/a[6]/img
h5  /html/body/div/a[6]/span/h5
```

<br>
<br>

### 项目实践
爬取猫眼电影票房网页的节点：      
```python
import requests
from lxml import etree
import random

user_agent = [
    'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; MI NOTE LTE Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.8.7',
    'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1',
    'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 5 Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Galaxy Nexus Build/IML74K) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Mobile Safari/535.7',
    'Mozilla/5.0 (Linux; U; Android-4.0.3; en-us; Xoom Build/IML77) AppleWebKit/535.7 (KHTML, like Gecko) CrMo/16.0.912.75 Safari/535.7',
    'Mozilla/5.0 (Linux;u;Android 4.2.2;zh-cn;) AppleWebKit/534.46 (KHTML,like Gecko) Version/5.1 Mobile Safari/10600.6.3',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e YisouSpider/5.0 Safari/602.1',
    'Mozilla/5.0 (Linux; Android 4.0; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/59.0.3071.92',
    'Mozilla/5.0 (Linux; Android 6.0.1; SOV33 Build/35.0.D.0.326) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.91 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 6.0; HUAWEI MLA-AL10 Build/HUAWEIMLA-AL10) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.96 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.1.1; vivo X20A Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/5.6.1.1',
    'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-CN; SM-J7108 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.9.7.977 Mobile Safari/537.36',
    'Mozilla/6.0 (Linux; Android 8.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Mobile Safari/537.36'
]

headers = {
    'Accept-Encoding': 'identity',
    'User-Agent': random.choice(user_agent)
}

page = requests.get("https://piaofang.maoyan.com/box-office?ver=normal", headers=headers)
# root = html.fromstring(page.text)
html = etree.HTML(page.text)
tree = html.getroottree()
all_nodes = html.xpath('//*')
xpath = []
for node in all_nodes:
    xpath.append(tree.getpath(node))
for node, path in zip(all_nodes, xpath):
    print("{}：{}".format(node.tag, path))

```

<br>

返回结果如下：   
```bash
html：/html
head：/html/head
title：/html/head/title
meta：/html/head/meta[1]
link：/html/head/link[1]
link：/html/head/link[2]
link：/html/head/link[3]
link：/html/head/link[4]
link：/html/head/link[5]
meta：/html/head/meta[2]
meta：/html/head/meta[3]
meta：/html/head/meta[4]
meta：/html/head/meta[5]
link：/html/head/link[6]
link：/html/head/link[7]
link：/html/head/link[8]
link：/html/head/link[9]
meta：/html/head/meta[6]
meta：/html/head/meta[7]
meta：/html/head/meta[8]
meta：/html/head/meta[9]
meta：/html/head/meta[10]
meta：/html/head/meta[11]
meta：/html/head/meta[12]
meta：/html/head/meta[13]
meta：/html/head/meta[14]
meta：/html/head/meta[15]
link：/html/head/link[10]
meta：/html/head/meta[16]
meta：/html/head/meta[17]
meta：/html/head/meta[18]
meta：/html/head/meta[19]
meta：/html/head/meta[20]
script：/html/head/script[1]
link：/html/head/link[11]
link：/html/head/link[12]
script：/html/head/script[2]
body：/html/body
script：/html/body/script[1]
div：/html/body/div
div：/html/body/div/div
div：/html/body/div/div/div[1]
div：/html/body/div/div/div[1]/div[1]
div：/html/body/div/div/div[1]/div[2]
div：/html/body/div/div/div[1]/div[2]/div[1]
ul：/html/body/div/div/div[1]/div[2]/div[1]/ul
li：/html/body/div/div/div[1]/div[2]/div[1]/ul/li[1]
li：/html/body/div/div/div[1]/div[2]/div[1]/ul/li[2]
li：/html/body/div/div/div[1]/div[2]/div[1]/ul/li[3]
li：/html/body/div/div/div[1]/div[2]/div[1]/ul/li[4]
li：/html/body/div/div/div[1]/div[2]/div[1]/ul/li[5]
div：/html/body/div/div/div[1]/div[2]/div[2]
div：/html/body/div/div/div[2]
div：/html/body/div/div/div[2]/div
div：/html/body/div/div/div[2]/div/div[1]
div：/html/body/div/div/div[2]/div/div[1]/div[1]
div：/html/body/div/div/div[2]/div/div[1]/div[1]/div[1]
div：/html/body/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]
div：/html/body/div/div/div[2]/div/div[1]/div[1]/div[1]/div[2]
i：/html/body/div/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/i
div：/html/body/div/div/div[2]/div/div[1]/div[1]/div[1]/div[3]
div：/html/body/div/div/div[2]/div/div[1]/div[1]/div[2]
div：/html/body/div/div/div[2]/div/div[1]/div[1]/div[2]/div
div：/html/body/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div
label：/html/body/div/div/div[2]/div/div[1]/div[1]/div[2]/div/label
span：/html/body/div/div/div[2]/div/div[1]/div[1]/div[2]/div/label/span
input：/html/body/div/div/div[2]/div/div[1]/div[1]/div[2]/div/label/input
div：/html/body/div/div/div[2]/div/div[1]/div[2]
div：/html/body/div/div/div[2]/div/div[1]/div[2]/div
div：/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[1]
p：/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[1]/p[1]
p：/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[1]/p[2]
div：/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[2]
div：/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div
span：/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/span
p：/html/body/div/div/div[2]/div/div[1]/div[2]/p
div：/html/body/div/div/div[2]/div/div[2]
h1：/html/body/div/div/div[2]/div/div[2]/h1
table：/html/body/div/div/div[2]/div/div[2]/table
thead：/html/body/div/div/div[2]/div/div[2]/table/thead
tr：/html/body/div/div/div[2]/div/div[2]/table/thead/tr
th：/html/body/div/div/div[2]/div/div[2]/table/thead/tr/th[1]
th：/html/body/div/div/div[2]/div/div[2]/table/thead/tr/th[2]
span：/html/body/div/div/div[2]/div/div[2]/table/thead/tr/th[2]/span[1]
br：/html/body/div/div/div[2]/div/div[2]/table/thead/tr/th[2]/br
span：/html/body/div/div/div[2]/div/div[2]/table/thead/tr/th[2]/span[2]
th：/html/body/div/div/div[2]/div/div[2]/table/thead/tr/th[3]
span：/html/body/div/div/div[2]/div/div[2]/table/thead/tr/th[3]/span[1]
br：/html/body/div/div/div[2]/div/div[2]/table/thead/tr/th[3]/br
span：/html/body/div/div/div[2]/div/div[2]/table/thead/tr/th[3]/span[2]
th：/html/body/div/div/div[2]/div/div[2]/table/thead/tr/th[4]
th：/html/body/div/div/div[2]/div/div[2]/table/thead/tr/th[5]
tbody：/html/body/div/div/div[2]/div/div[2]/table/tbody
tr：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/p[1]
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/p[2]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/p[2]/span[1]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/div/p[2]/span[2]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[3]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[4]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[4]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[5]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[5]/div
tr：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/div
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/div/p[1]
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/div/p[2]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/div/p[2]/span[1]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/div/p[2]/span[2]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[3]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[3]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[4]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[4]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[5]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[5]/div
tr：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[1]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[1]/div
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[1]/div/p[1]
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[1]/div/p[2]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[1]/div/p[2]/span[1]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[1]/div/p[2]/span[2]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[3]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[3]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[4]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[4]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[5]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[5]/div
tr：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[1]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[1]/div
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[1]/div/p[1]
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[1]/div/p[2]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[1]/div/p[2]/span[1]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[1]/div/p[2]/span[2]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[2]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[2]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[3]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[3]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[4]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[4]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[5]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[5]/div
tr：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[1]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/div
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/div/p[1]
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/div/p[2]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/div/p[2]/span[1]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/div/p[2]/span[2]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[2]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[3]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[3]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[4]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[4]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[5]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[5]/div
tr：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[1]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[1]/div
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[1]/div/p[1]
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[1]/div/p[2]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[1]/div/p[2]/span[1]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[1]/div/p[2]/span[2]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[2]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[2]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[3]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[3]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[4]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[4]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[5]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[5]/div
tr：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[1]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[1]/div
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[1]/div/p[1]
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[1]/div/p[2]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[1]/div/p[2]/span[1]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[1]/div/p[2]/span[2]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[2]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[2]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[3]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[3]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[4]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[4]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[5]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[7]/td[5]/div
tr：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[1]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[1]/div
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[1]/div/p[1]
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[1]/div/p[2]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[1]/div/p[2]/span[1]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[1]/div/p[2]/span[2]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[2]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[2]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[3]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[3]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[4]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[4]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[5]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[8]/td[5]/div
tr：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[1]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[1]/div
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[1]/div/p[1]
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[1]/div/p[2]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[1]/div/p[2]/span[1]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[1]/div/p[2]/span[2]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[2]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[2]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[3]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[3]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[4]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[4]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[5]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[9]/td[5]/div
tr：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[1]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[1]/div
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[1]/div/p[1]
p：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[1]/div/p[2]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[1]/div/p[2]/span[1]
span：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[1]/div/p[2]/span[2]
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[2]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[2]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[3]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[3]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[4]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[4]/div
td：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[5]
div：/html/body/div/div/div[2]/div/div[2]/table/tbody/tr[10]/td[5]/div
div：/html/body/div/div/div[2]/div/div[3]
div：/html/body/div/div/div[2]/div/div[3]/div[1]
div：/html/body/div/div/div[2]/div/div[3]/div[1]/div[1]
div：/html/body/div/div/div[2]/div/div[3]/div[1]/div[2]
div：/html/body/div/div/div[2]/div/div[3]/div[2]
div：/html/body/div/div/div[2]/div/div[4]
div：/html/body/div/div/div[2]/div/div[4]/div[1]
div：/html/body/div/div/div[2]/div/div[4]/div[2]
div：/html/body/div/div/div[2]/div/div[4]/div[3]
div：/html/body/div/div/div[2]/div/div[5]
i：/html/body/div/div/div[2]/div/div[5]/i
div：/html/body/div/div/div[3]
script：/html/body/script[2]
script：/html/body/script[3]
script：/html/body/script[4]
script：/html/body/script[5]
script：/html/body/script[6]
script：/html/body/script[7]
script：/html/body/script[8]
script：/html/body/script[9]
script：/html/body/script[10]
script：/html/body/script[11]
script：/html/body/script[12]
```

<br>
<br>

---

相关链接：    
[Python爬虫:获取DOM树各个节点的xpath路径](https://blog.csdn.net/yeshang_lady/article/details/122104779)