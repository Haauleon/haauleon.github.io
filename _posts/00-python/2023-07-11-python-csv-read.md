---
layout:        post
title:         "自动化办公 | 读取csv文件的几种方式"
subtitle:      "python读取csv文件的几种方式（含实例说明）"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 自动化办公
---

### 一、使用pandas库
举个例子：直接利用 `read_csv()` 方法读取，文本被转化成了 dataframe 格式。       
```python
import pandas as pd

df = pd.read_csv('../data_pro/audito_whole.csv')
print(df)
```

结果：    
![](\img\in-post\post-python\2023-07-11-python-csv-read-1.png)     

<br>
<br>

### 二、使用csv库
举个例子：先利用 `codecs.open` 方法读取文件 audito_whole.csv ，采用 `utf-8` 字符编码，再利用 `csv.DictReader()` 方法读取。这里可以换成 python 内置的 `open()` 方法，也可以把 `csv.DictReader()` 换成 `csv.reader()` 方法。   

<br>

1、`codecs.open + csv.DictReader`     
```python
import codecs
import csv

with codecs.open('../data_pro/audito_whole.csv', encoding='utf-8-sig') as f:
    for row in csv.DictReader(f, skipinitialspace=True):
        print(row)
f.close()
```

结果：     
![](\img\in-post\post-python\2023-07-11-python-csv-read-2.png)     

<br>

2、`open + csv.reader`         
```python
import csv

with open('../data_pro/audito_whole.csv', encoding='utf-8-sig') as f:
    for row in csv.reader(f, skipinitialspace=True):
        print(row)
f.close()
```

结果：     
![](\img\in-post\post-python\2023-07-11-python-csv-read-3.png)        

<br>
<br>

---

相关链接：   
[python读取csv文件的几种方式（含实例说明）](https://blog.csdn.net/qq_43160348/article/details/124331781)