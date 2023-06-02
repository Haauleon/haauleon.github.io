---
layout:        post
title:         "Python3 | excel 操作"
subtitle:      "读取 excel 并生成 json 文件"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---



### 读取excel并生成json文件
项目结构：    
```
- locales
  - en_US.json
  - pt_PT.json
  - zh_CN.json
  - zh_HK.json
- excel_to_json.py
- 多语言翻译.xlsx
```

<br>

项目资源：      
链接：https://pan.baidu.com/s/1yNAREbRfHTOmOTjI-oSH9A?pwd=kbdc      
提取码：kbdc     


<br>
<br>

### 代码实现
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   excel_to_json.py
@Date    :   2022/7/13 4:30 PM
@Function:   读取excel并生成json文件

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2022/7/13 4:30 PM      haauleon         1.0        读取excel并生成json文件
"""
import json
import xlrd
import os

_SLASH = os.sep

# 上级目录路径
root_path = os.path.dirname(os.path.abspath(__file__))
# 翻译文档路径
excel_path = os.path.join(root_path, '多语言翻译.xlsx')
# 多语言json包路径
locales_path = os.path.join(root_path, 'locales' + _SLASH)


class SaveDate:
    """
    读取excel表的翻译数据并分别存于json文件
    """

    def __init__(self):
        self.locales_path = locales_path  # 多语言翻译目录路径
        self.excel_path = excel_path

    def save_to_cn(self, k, v):
        """简体"""
        file_path = self.locales_path + "zh_CN.json"
        with open(file_path, "r") as cn:
            cn_dict = json.load(cn)

        cn_dict[k] = v
        with open(file_path, "w", encoding='utf-8') as cn_f:
            # 做dump与dumps操作时，会默认将中文转换为unicode，但在做逆向操作load和loads时会转换为中文，但是中间态(例如存储的json文件)的中文编码方式仍然是unicode， 解决办法
            json.dump(cn_dict, cn_f, ensure_ascii=False)
        print("简体: ", k, " >>>>>>>>>>> 添加成功")

    def save_to_hk(self, k, v):
        """繁体"""
        file_path = self.locales_path + "zh_HK.json"
        with open(file_path, "r") as hk:
            hk_dict = json.load(hk)

        hk_dict[k] = v
        with open(file_path, "w", encoding='utf-8') as cn_f:
            # 做dump与dumps操作时，会默认将中文转换为unicode，但在做逆向操作load和loads时会转换为中文，但是中间态(例如存储的json文件)的中文编码方式仍然是unicode， 解决办法
            json.dump(hk_dict, cn_f, ensure_ascii=False)
        print("繁体: ", k, " >>>>>>>>>>> 添加成功")

    def save_to_pt(self, k, v):
        """葡语"""
        file_path = self.locales_path + "pt_PT.json"
        with open(file_path, "r") as pt:
            pt_dict = json.load(pt)

        pt_dict[k] = v
        with open(file_path, "w", encoding='utf-8') as cn_f:
            json.dump(pt_dict, cn_f,
                      ensure_ascii=False)
        print("葡语: ", k, " >>>>>>>>>>> 添加成功")

    def save_to_en(self, k, v):
        """英语"""
        file_path = self.locales_path + "en_US.json"
        with open(file_path, "r") as us:
            us_dict = json.load(us)

        us_dict[k] = v
        with open(file_path, "w", encoding='utf-8') as cn_f:
            json.dump(us_dict, cn_f,
                      ensure_ascii=False)
        print("英语: ", k, " >>>>>>>>>>> 添加成功")

    def run_to_save_json(self):
        """将多语言翻译的excel文件的值追加到json文件中"""
        xl = xlrd.open_workbook(self.excel_path)
        table = xl.sheets()[0]
        for row in range(1, table.nrows):
            cn = table.cell(row, 0).value  # 值
            cht = table.cell(row, 1).value  # 键
            pt = table.cell(row, 2).value
            en = table.cell(row, 3).value
            self.save_to_cn(cn, cn)
            self.save_to_hk(cn, cht)
            self.save_to_pt(cn, pt)
            self.save_to_en(cn, en)


if __name__ == '__main__':
    # 执行生成json文件
    sd = SaveDate()
    sd.run_to_save_json()
```