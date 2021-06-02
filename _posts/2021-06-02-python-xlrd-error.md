---
layout:        post
title:         "Python3 | xlrd 运行报错"
subtitle:      "xlrd.biffh.XLRDError: Excel xlsx file; not supported"
date:          2021-06-02
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - 异常库
---

## 背景
&emsp;&emsp;在使用了 `$ pip install xlrd` 安装完成 xlrd 之后，执行以下 demo 代码报错：                       
```python
import xlrd

def read_excel():
    # 打开文件
    workBook = xlrd.open_workbook('D:\code\python-learn\zhima\城市代码_芝麻.xlsx')

    # 1.获取sheet的名字
    # 1.1 获取所有sheet的名字(list类型)
    allSheetNames = workBook.sheet_names()
    print(allSheetNames)

    # 1.2 按索引号获取sheet的名字（string类型）
    sheet1Name = workBook.sheet_names()[0]
    print(sheet1Name)

    # 2. 获取sheet内容
    ## 2.1 法1：按索引号获取sheet内容
    sheet1_content1 = workBook.sheet_by_index(0) # sheet索引从0开始
    print(sheet1_content1)
    ## 2.2 法2：按sheet名字获取sheet内容
    #sheet1_content2 = workBook.sheet_by_name('Sheet1');

    # 3. sheet的名称，行数，列数
    print(sheet1_content1.name, sheet1_content1.nrows, sheet1_content1.ncols)
    #print(sheet1_content1.name, sheet1_content1.nrows);

read_excel()
```

<br>

执行结果：          
```
Traceback (most recent call last):
  File "d:/code/python-learn/zhima/get_city.py", line 27, in <module>
    read_excel()
  File "d:/code/python-learn/zhima/get_city.py", line 5, in read_excel
    workBook = xlrd.open_workbook('D:\code\python-learn\zhima\城市代码_芝麻.xlsx')
  File "C:\Users\Haauleon\AppData\Local\Programs\Python\Python37\lib\site-packages\xlrd\__init__.py", line 170, in open_workbook
    raise XLRDError(FILE_FORMAT_DESCRIPTIONS[file_format]+'; not supported')
xlrd.biffh.XLRDError: Excel xlsx file; not supported
```

<br><br>

## 解决方法
安装 pyexcel-xls 即可。                
```
$ pip install pyexcel-xls
```

<br>

再次执行脚本，输出正确。                 
```
['国家代码']
国家代码
<xlrd.sheet.Sheet object at 0x0000027368B328C8>
国家代码 137 4
```