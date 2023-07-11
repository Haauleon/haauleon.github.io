---
layout:        post
title:         "自动化办公 | 使用 xlrd+xlwt 读取/写入 Excel 数据"
subtitle:      ""
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 自动化办公
---


### 一、开发前置环境
1、安装 Python（如 Python 3.7）    
2、安装 Office 办公软件（或 WPS Office）     
3、安装开发工具（如 PyCharm，下载地址：https://www.jetbrains.com/pycharm/download）        

<br>
<br>

### 二、xlrd模块读取Excel
xlrd 为 Python 第三方模块，用来读取 Excel 表格数据（仅支持 `.xls` 格式）。      

<br>

#### 1、xlrd常用函数
```python
import xlrd

# 读取Excel文件
data = xlrd.open_workbook("data1.xls")

# 加载索引为0的工作表  True
# print(data.sheet_loaded(0)) 

# 卸载
# data.unload_sheet(0)

# 未被加载，False
# print(data.sheet_loaded(0))

# 已被加载，True
# print(data.sheet_loaded(1))  # True

# 获取全部sheet  [Sheet  0:<Sheet1>, Sheet  1:<Sheet2>, Sheet  2:<Sheet3>]
print(data.sheets()) 

# 获取指定索引的工作表对象  Sheet  0:<Sheet1>
print(data.sheets()[0]) 

# 根据索引获取工作表 Sheet  0:<Sheet1>
print(data.sheet_by_index(0)) 

# 根据名字sheetname（区分大小写）获取工作表 Sheet  0:<Sheet1>
print(data.sheet_by_name('Sheet1'))

# 获取所有工作表的name ['Sheet1', 'Sheet2', 'Sheet3']
print(data.sheet_names()) 

# 查看共有多少个工作表
print(len(data.sheet_names())) # 返回所有工作表的名称组成的list的长度 3

# 返回excel工作表的数量 3
print(data.nsheets) 
```

`data1.xls——Sheet1`：       
![](\img\in-post\post-python\2022-07-07-python-xlwt-1.png)         

`data1.xls——Sheet2`：      
![](\img\in-post\post-python\2022-07-07-python-xlwt-2.png)         

<br>
<br>

#### 2、xlrd操作Excel行
```python
import xlrd

data = xlrd.open_workbook("data1.xls")

# 操作excel行
# 获取第一个工作表
sheet1 = data.sheet_by_index(0)

# 获取sheet下的有效行数  11
print(sheet1.nrows) 

# 获取第2个工作表
sheet2 = data.sheet_by_index(1)

# 获取sheet下的有效行数  10
print(sheet2.nrows)

# 输出第一行数据
print(sheet1.row(0)) 
# [text:'1月份销售额明细表', empty:'', empty:'', empty:'', empty:'', empty:'', empty:'']

# 输出第2行数据，返回该行单元格对象组成的列表
print(sheet1.row(1)) 
# [text:'日期', text:'货号', text:'颜色', text:'尺码', text:'原价', text:'折扣', text:'备注']

# 获取单元格的数据类型，返回指定行数据的数据类型
print(sheet1.row_types(1)) 
# （xlrd单元格数据类型表示：0：empty，1：string，2：number，3：date，4：boolean,5:error）
# array('B', [1, 1, 1, 1, 1, 1, 1])

# 获取单元格的数据类型 text:'颜色'
print(sheet1.row(1)[2]) 

# 获取单元格value 颜色
print(sheet1.row(1)[2].value)

# 得到指定行单元格的值 ['日期', '货号', '颜色', '尺码', '原价', '折扣', '备注']
print(sheet1.row_values(1)) 

# 得到单元格的长度 7
print(sheet1.row_len(1)) 
```

<br>
<br>

#### 3、xlrd操作Excel列     
```python
import xlrd

data = xlrd.open_workbook("data1.xls")

# 操作excel列
# 获取第一个工作表
sheet1 = data.sheet_by_index(0)

# 获取工作表有效列数
print(sheet1.ncols) 

# 该列单元格对象组成的列表
print(sheet1.col(1)) 
# [empty:'', text:'货号', text:'X0001', text:'X0002', text:'X0003', text:'X0004', text:'X0005', text:'X0006', text:'X0007', text:'X0008', text:'X0009']

# text:'X0001'
print(sheet1.col(1)[2]) 

# X0001
print(sheet1.col(1)[2].value)

# 返回该列所有单元格的value组成的列表
print(sheet1.col_values(1)) 
# ['', '货号', 'X0001', 'X0002', 'X0003', 'X0004', 'X0005', 'X0006', 'X0007', 'X0008', 'X0009']

print(sheet1.col_types(1)) 
# 获取该列单元格的数据类型 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

<br>
<br>

#### 4、xlrd操作Excel单元格
```python
import xlrd

data = xlrd.open_workbook("data1.xls")

# 操作excel单元格
# 获取第一个工作表
sheet1 = data.sheet_by_index(0) 

# text:'颜色'
print(sheet1.cell(1,2)) 

# 获取单元格数据类型
# 1
print(sheet1.cell_type(1,2)) 

# 1
print(sheet1.cell(1,2).ctype) 

# 获取单元格的值
# 获取第二行，第三列单元格的值 颜色
print(sheet1.cell(1,2).value)

# 颜色
print(sheet1.cell_value(1,2)) 
```

<br>
<br>

### 三、xlwt写入Excel
xlwt 为 Python 第三方模块，用来写入 Excel 表格数据（仅支持 `.xls` 格式）。     

<br>

#### 1、xlwt写入Excel步骤    
（1）创建工作簿       
（2）创建工作表       
（3）填充工作表内容        
（4）保存文件         

```python
import xlwt

# 第一步：创建工作簿
wb = xlwt.Workbook()
# 第二步：创建工作表
ws = wb.add_sheet("CNY")
# 第三步：填充数据
ws.write_merge(0, 1, 0, 5, "2019年货币兑换表")

# 写入货币数据
data = (("Date", "英镑", "人民币", "港币", "日元", "美元"),
        ("01/01/2019", 8.722551, 1, 0.877885, 0.062722, 6.8759),
        ("02/01/2019", 8.634922, 1, 0.875731, 0.062773, 6.8601))
for i,item in enumerate(data):
    for j,val in enumerate(item):
        ws.write(i+2, j, val)

# 创建第二个工作表
wsImage = wb.add_sheet("image")
# 写入图片
wsImage.insert_bitmap("2021-07-01_172956.bmp", 0, 0)
# 第四步：保存
wb.save("2019-CNY.xls")
```

执行效果：       
![](\img\in-post\post-python\2022-07-07-python-xlwt-3.png)        

![](\img\in-post\post-python\2022-07-07-python-xlwt-4.png)        

<br>
<br>

#### 2、写入格式化（添加样式）
```python
import xlwt

titleStyle = xlwt.XFStyle() # 初始化样式
titleFont = xlwt.Font()
titleFont.name = "宋体"
titleFont.bold = True # 加粗
titleFont.height = 11*20 # 字号
titleFont.colour_index = 0x08 # 字体颜色
titleStyle.font = titleFont

# 单元格对齐方式
cellAlign = xlwt.Alignment()
cellAlign.horz = 0x02 # 水平居中
cellAlign.vert = 0x01 # 垂直居中
titleStyle.alignment = cellAlign

# 边框
borders = xlwt.Borders()
borders.right = xlwt.Borders.DASHED
borders.bottom = xlwt.Borders.DOTTED
titleStyle.borders = borders

# 背景颜色
dataStyle = xlwt.XFStyle()
bgColor = xlwt.Pattern()
bgColor.pattern = xlwt.Pattern.SOLID_PATTERN
bgColor.pattern_fore_colour = 22 # 背景颜色
dataStyle.pattern = bgColor

# 第一步：创建工作簿
wb = xlwt.Workbook()
# 第二步：创建工作表
ws = wb.add_sheet("CNY")
# 第三步：填充数据
ws.write_merge(0, 1, 0, 5, "2019年货币兑换表", titleStyle) # 合并单元格，1~2行，1~6列

# 写入货币数据
data = (("Date", "英镑", "人民币", "港币", "日元", "美元"),
        ("01/01/2019", 8.722551, 1, 0.877885, 0.062722, 6.8759),
        ("02/01/2019", 8.634922, 1, 0.875731, 0.062773, 6.8601))
for i,item in enumerate(data):
    for j,val in enumerate(item):
        if j==0:
            ws.write(i+2, j, val, dataStyle)
        else:
            ws.write(i+2, j, val)

# 创建第二个工作表
wsImage = wb.add_sheet("image")
# 写入图片
wsImage.insert_bitmap("2021-07-01_172956.bmp", 0, 0)
# 第四步：保存
wb.save("2019-CNY.xls")
```

执行效果：     
![](\img\in-post\post-python\2022-07-07-python-xlwt-5.png)        

<br>
<br>

### 四、实战：基于xlrd模块实现考试系统题库管理
#### 1、Excel导入试题到数据库的操作步骤
（1）通过 xlrd 模块读取 Excel 数据    
（2）通过 pymysql 模块连接数据库      
（3）组装数据、执行插入操作   
（4）关闭数据库连接           

建表 sql：    
```python
DROP TABLE IF EXISTS `question`;
CREATE TABLE `question`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(255) DEFAULT NULL COMMENT '题目',
  `questionType` varchar(255) DEFAULT NULL COMMENT '题型',
  `optionA` varchar(255) DEFAULT NULL COMMENT '选项A',
  `optionB` varchar(255) DEFAULT NULL COMMENT '选项B',
  `optionC` varchar(255) DEFAULT NULL COMMENT '选项C',
  `optionD` varchar(255) DEFAULT NULL COMMENT '选项D',
  `score` int(11) DEFAULT NULL COMMENT '分值',
  `answer` varchar(255) DEFAULT NULL COMMENT '正确答案',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8;
```

mysqlhelper.py：      
```python
import pymysql

class dbhelper():
    def __init__(self,host,port,user,passwd,db,charset="utf8"):
        self.host=host
        self.port=port
        self.user=user
        self.passwd=passwd
        self.db=db
        self.charset=charset
    #创建一个链接
    def connection(self):
        #1. 创建连接
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,charset=self.charset)
        #2. 创建游标
        self.cur = self.conn.cursor()
    #关闭链接
    def closeconnection(self):
        self.cur.close()
        self.conn.close()
    #查询一条数据
    def getonedata(self,sql):
        try:
            self.connection()
            self.cur.execute(sql)
            result=self.cur.fetchone()
            self.closeconnection()
        except Exception:
            print(Exception)
        return result
    #查询多条数据
    def getalldata(self,sql):
        try:
            self.connection()
            self.cur.execute(sql)
            result=self.cur.fetchall()
            self.closeconnection()
        except Exception:
            print(Exception)
        return result
    #添加/修改/删除
    def executedata(self,sql):
        try:
            self.connection()
            self.cur.execute(sql)
            self.conn.commit()
            self.closeconnection()
        except Exception:
            print(Exception)
    #批量插入
    def executemanydata(self,sql,vals):
        try:
            self.connection()
            self.cur.executemany(sql,vals)
            self.conn.commit()
            self.closeconnection()
        except Exception as e:
            print(e)
```

data2.xls：     
![](\img\in-post\post-python\2022-07-07-python-xlwt-6.png)           

excelproject.py：     
```python
import xlrd

data = xlrd.open_workbook("data2.xls")
sheet = data.sheet_by_index(0) # 获取到工作表
questionList = []  # 构建试题列表

# 试题类
class Question:
    pass

for i in range(sheet.nrows):
    if i>1:
        obj = Question() # 构建试题对象
        obj.subject = sheet.cell(i, 1).value # 题目
        obj.questionType = sheet.cell(i, 2).value # 题型
        obj.optionA = sheet.cell(i, 3).value # 选项A
        obj.optionB = sheet.cell(i, 4).value # 选项B
        obj.optionC = sheet.cell(i, 5).value # 选项C
        obj.optionD = sheet.cell(i, 6).value # 选项D
        obj.score = sheet.cell(i, 7).value # 分值
        obj.answer = sheet.cell(i, 8).value # 正确答案
        questionList.append(obj)

print(questionList)
# 导入操作 pymysql pip install
from mysqlhelper import *
# 1.连接到数据库
db = dbhelper('127.0.0.1', 3306, "root", "123456", "test")
# 插入语句
sql = "insert into question(subject, questionType, optionA, optionB, optionC, optionD, score, answer) values (%s, %s, %s, %s, %s, %s, %s, %s)"
val = [] # 空列表来存储元组
for item in questionList:
    val.append((item.subject, item.questionType, item.optionA, item.optionB, item.optionC, item.optionD, item.score, item.answer))
#print(val)
db.executemanydata(sql, val)
```

执行效果：      
![](\img\in-post\post-python\2022-07-07-python-xlwt-7.png)          

<br>
<br>

---

相关链接：      
[Python 3使用xlrd+xlwt读取/写入Excel数据](https://blog.csdn.net/username666/article/details/118397439)