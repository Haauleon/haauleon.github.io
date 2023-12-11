---
layout:        post
title:         "Python3 | 实现txt文本文件转换为Excel文件"
subtitle:      "使用该代码片段需了解txt文本文件内容的分隔符是什么，本文示例的txt文件内容是以'\t'隔开的"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

> 于2023年12月11日更新，发现直接将txt文件后缀改成xlsx即可完成转换，且转换后的内容均对齐（仅适用于txt文件内容是以'\t'隔开的）


### 实现代码
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   txt_to_xlsx.py 
@Date    :   2023-10-26 17:08
@Function:   文本文件转成xlsx类型的excel

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2023-10-26 17:08         haauleon         1.0           None
"""
import xlwt

def txt_to_xlsx(txt_path, xls_path):
    # 打开txt文件并读取内容
    with open(txt_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 将文本按行分割，并去除空格、换行符等无用符号
    lines = [line.strip() for line in content.split('\n') if line.strip()]

    # 创建一个新的Excel工作簿
    workbook = xlwt.Workbook()

    # 添加一个名为“Sheet1”的工作表对象
    worksheet = workbook.add_sheet('Sheet1')

    # 遍历文本中的每一行，将其写入Excel工作表中的相应位置
    for i, line in enumerate(lines):
        cols = line.split('\t')  # 分隔符根据实际情况而定，当前txt的内容以\t隔开，如果是逗号隔开则改成逗号 ','
        for j, col in enumerate(cols):
            worksheet.write(i, j, col)

    # 将生成的Excel文件保存到指定路径
    workbook.save(xls_path)


if __name__ == '__main__':
    txt_to_xlsx(r'..\测试.txt', r'..\测试.xlsx')

```

<br>
<br>

---

相关链接：   
[Python：实现文本转换为Excel文件（附代码）](https://blog.csdn.net/code_welike/article/details/131040265)          
[使用Python将TXT转为Excel](https://blog.csdn.net/zg_111/article/details/129367138)