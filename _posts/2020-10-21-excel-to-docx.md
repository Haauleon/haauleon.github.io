---
layout: post
title: "python3 | excel 转 docx"
subtitle: "读取 excel 表的单元格的值，填充 docx 文档的表格"
author: "Haauleon"
header-style: text
tags:
  - Python
---


## 背景
&emsp;&emsp;目前接的外包项目需要提供 docx 类型的测试用例文档，但是一般来说测试人员的测试用例都是写在 excel 表里面的，因为方便复制粘贴嘛。       

<br><br>

## 解决方案
&emsp;&emsp;使用 python3 来实现 excel 转 docx 的需求。     

<br><br>

## 具体思路
1.安装 python-docx 和 xlrd  

```
$ pip install python-docx
$ pip install xlrd
```    

2.使用 python-docx 绘制 docx 文档的测试用例的表格模板      

3.使用 xlrd 读取 excel 表的每一行的各个单元格的值，填充至已绘制的 docx 文档的表格中     

<br><br>

## 数据准备    
1.excel类型的测试用例      

![](\img\in-post\post-python\2020-10-21-excel-to-docx-1.jpg)  

<br>

2.绘制好脑海中的docx模板     

![](\img\in-post\post-python\2020-10-21-excel-to-docx-2.jpg)  

<br><br>

## 完整代码
```python
from docx import Document   # 功能是打开文档
#from docx.enum.text import WD_ALIGN_PARAGRAPH  # 功能是对齐
from docx.shared import Pt # 设置磅数
from docx.oxml.ns import qn  # 负责中文格式  以上是每次使用word要使用的库
from docx.shared import Cm   # 调整行高和列宽
import xlrd
import time  # 需要导入时间
#year =  time.strftime("%Y")
today = time.strftime("%Y{y}%m{m}%d{d}",time.localtime()).format(y='年',m='月',d='日')  # 可以更具需求任意修改中间的内容，带式不能显示中文，通过formate可以实现显示中文

document = Document()   # 初始化文档
document.styles['Normal'].font.name = u'仿宋'  # 设置整个文档的字体
document.styles['Normal'].font.size = Pt(12)   # 置文档磅号
document.styles['Normal'].element.rPr.rFonts.set(qn('w:esatAsia'),u'仿宋')  # 设置文档的基础中文字体，否则显示中文有问题


xlsx = xlrd.open_workbook('测试用例.xlsx')
sheetname = xlsx.sheet_names()[0]
sheet_c = xlsx.sheet_by_index(0) # 获取行


for i in range(1,sheet_c.nrows):
    data = sheet_c.row_values(i)

    P1 = document.add_paragraph()  # 增加一个自然段
    #P1.alignment = WD_ALIGN_PARAGRAPH.CENTER  #对其方式为居中，不设置默认左对齐

    run1 = P1.add_run(data[1])    # 增加自然段的内容
    run1.font.name = '仿宋'  # 设置自然段的字体
    run1.element.rPr.rFonts.set(qn('w:eastAsia'),u'仿宋')  # 为显示中文正确
    run1.font.size =Pt(14)  # 设置中文字体磅数
    run1.font.bold = True    # 设置加粗
    P1.space_after = Pt(5)  # 段前的距离
    P1.space_before = Pt(5)  # 段后的距离

    table = document.add_table(rows=15,cols=6,style='Table Grid')  # 使用word自带格式插入一个15行6列的表格
    table.run1 = table.cell(0,0).paragraphs[0].add_run('用例标识:')  # 对于合并后的单元格，table（0，0），使用当中的任何一个单元格都可以
    table.run1.font.name = u'仿宋'
    table.run1.element.rPr.rFonts.set(qn('w:eastAisa'),u'仿宋')
    table.cell(0,0).paragraphs[0].aligment =WD_ALIGN_PARAGRAPH.CENTER   # 设置表格内容居中

    table.cell(0,0).width = Cm(2.1)  # 设置列宽
    table.cell(0,1).width = Cm(1.2)
    table.cell(0,2).width = Cm(3.9)
    table.cell(0,3).width = Cm(2.4)
    table.cell(0,4).width = Cm(3.3)
    table.cell(0,5).width = Cm(1.2)

    table.rows[0].height = Cm(1)   # 设置行高
    table.rows[1].height = Cm(1)
    table.rows[2].height = Cm(1)
    table.rows[3].height = Cm(1)
    table.rows[4].height = Cm(1)
    table.rows[5].height = Cm(1)
    table.rows[6].height = Cm(1)
    table.rows[7].height = Cm(1)
    table.rows[8].height = Cm(1)
    table.rows[9].height = Cm(1)
    table.rows[10].height = Cm(3)
    table.rows[11].height = Cm(3)
    table.rows[12].height = Cm(1)
    table.rows[13].height = Cm(1)
    table.rows[14].height = Cm(1)

    table.cell(0,1).merge(table.cell(0,2)) # 合并单元格 table.cell(行, 列)
    table.cell(0,4).merge(table.cell(0,5))
    table.cell(1,1).merge(table.cell(1,5))
    table.cell(2,1).merge(table.cell(2,5))
    table.cell(3,1).merge(table.cell(3,5))
    table.cell(4,1).merge(table.cell(4,5))
    table.cell(5,3).merge(table.cell(5,5))
    table.cell(8,1).merge(table.cell(8,5))
    table.cell(9,1).merge(table.cell(9,5))
    table.cell(10,1).merge(table.cell(10,5))
    table.cell(11,1).merge(table.cell(11,5))
    table.cell(12,1).merge(table.cell(12,5))
    table.cell(13,1).merge(table.cell(13,5))
    table.cell(14,1).merge(table.cell(14,5))

    table.cell(0,0).text = '用例标识'
    table.cell(0,1).text = data[0]
    table.cell(0,3).text = '用例责任人'
    table.cell(0,4).text = data[6]

    table.cell(1,0).text = '测试类型'
    table.cell(1,1).text = '手工测试'

    table.cell(2,0).text = '测试阶段'
    table.cell(2,1).text = '系统测试'

    table.cell(3,0).text = '测试项'
    table.cell(3,1).text = '功能测试'

    table.cell(4,0).text = '参考文档'
    table.cell(4,1).text = data[12]

    table.cell(5,0).text = '开发人员'
    table.cell(5,1).text = data[7]
    table.cell(5,2).text = '测试对象版本号'
    table.cell(5,3).text = data[8]

    table.cell(6,0).text = '用例作者'
    table.cell(6,1).text = data[9]
    table.cell(6,2).text = '用例编写日期'
    table.cell(6,3).text = str(data[10])
    table.cell(6,4).text = '用例执行人员'
    table.cell(6,5).text = data[11]

    table.cell(7,0).text = '优先级'
    table.cell(7,1).text = '高'
    table.cell(7,2).text = '执行频度'
    table.cell(7,3).text = '高'
    table.cell(7,4).text = '辅助工具'
    table.cell(7,5).text = ' '

    table.cell(8,0).text = '用例描述'
    table.cell(8,1).text = data[2]

    table.cell(9,0).text = '前置条件'
    table.cell(9,1).text = data[3]

    table.cell(10,0).text = '步骤'
    table.cell(10,1).text = data[4]

    table.cell(11,0).text = '预期结果'
    table.cell(11,1).text = data[5]

    table.cell(12,0).text = '实际结果'
    table.cell(12,1).text = ' '

    table.cell(13,0).text = '结论'
    table.cell(13,1).text = '[ ]通过  [ ]未通过'

    table.cell(14,0).text = '测试日期'
    table.cell(14,1).text = ' '

    document.add_page_break()  # 插入分页符
document.save('%s测试用例.docx'%today)
```