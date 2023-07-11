---
layout:        post
title:         "Python3 | 读取execl 、csv"
subtitle:      "实现读取execl 、csv工具类"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 自动化办公
---

### execl - python xlrd  
```python
# -*- coding: utf-8 -*-
"""
@Time    : 2022/10/27 14:00
@FileName: execl_handler.py
"""
 
import xlrd, json
 
 
class Excel(object):
    """Excel文件操作工具类"""
 
    def __init__(self, filename):
        self.workbook = xlrd.open_workbook(filename, formatting_info=True)
 
    def get_sheet_names(self):
        """
        获取当前excel文件所有的工作表的表名
        :return:
        """
        return self.workbook.sheet_names()
 
    def __get_sheet(self, sheet_index_or_name):
        """
        根据sheet的索引或名称，获取sheet对象
        :param sheet_index_or_name: sheet的索引或名称
        :return:sheet对象
        """
        if isinstance(sheet_index_or_name, int):
            if len(self.workbook.sheet_names()) > sheet_index_or_name:
                return self.workbook.sheet_by_index(sheet_index_or_name)
            else:
                raise Exception("Invalid Sheet Index!")
        elif isinstance(sheet_index_or_name, str):
            if sheet_index_or_name in self.workbook.sheet_names():
                return self.workbook.sheet_by_name(sheet_index_or_name)
            else:
                raise Exception("Invalid Sheet Name!")
 
    def get_rows_num(self, sheet_index_or_name):
        """
        获取指定工作表的数据总行数
        :param sheet_index_or_name: 工作表名或索引
        :return:
        """
        return self.__get_sheet(sheet_index_or_name).nrows
 
    def get_cols_num(self, sheet_index_or_name):
        """
        获取指定工作表的数据总列数
        :param sheet_index_or_name: 工作表名或索引
        :return:
        """
        return self.__get_sheet(sheet_index_or_name).ncols
 
    def get_cell_value(self, sheet_index_or_name, row_index, col_index):
        """
        获取指定工作表的指定位置的数据值
        :param sheet_index_or_name: 工作表名或索引
        :param row_index: 行下标，从0开始
        :param col_index: 列下标，从0开始
        :return:
        """
        sheet = self.__get_sheet(sheet_index_or_name)
        if sheet.nrows and sheet.ncols:
            return sheet.cell_value(row_index, col_index)
        else:
            raise Exception("Index out of range!")
 
    def get_data(self, sheet_index_or_name, fields, first_line_is_header=True):
        """
        获取工作表的所有数据
        :param sheet_index_or_name: 工作表名或索引
        :param fields: 返回数据的字段名
        :param first_line_is_header: 工作表是否是否表头，也就是非数据
        :return:
        """
        rows = self.get_rows_num(sheet_index_or_name)
        cols = self.get_cols_num(sheet_index_or_name)
        data = []
        for row in range(int(first_line_is_header), rows):
            row_data = {}
            for col in range(cols):
                cell_data = self.get_cell_value(sheet_index_or_name, row, col)
                if type(cell_data) is str and (
                        "{" in cell_data and "}" in cell_data or "[" in cell_data and "]" in cell_data):
                    """判断如果表格中填写的数据是json格式键值对，则采用json模块转换成字典"""
                    cell_data = json.loads(cell_data)
                row_data[fields[col]] = cell_data
            data.append(row_data)
 
        return data
 
 
if __name__ == '__main__':
    xls = Excel(r"./data/case_user.xls")
    fields = [
        "case_id",
        "module_name",
        "case_name",
        "method",
        "url",
        "headers",
        "params_desc",
        "params",
        "assert_result",
        "real_result",
        "remark",
    ]
 
    print(xls.get_data(0, fields))
 
"""
[
 
    {'case_id': 1.0, 'module_name': '用户模块', 'case_name': '用户登录-测试用户名为空的情况', 'method': 'post', 'url': 'http://127.0.0.1:8000/user/login', 'headers': '', 'params_desc': 'username: 用户名\npassword: 密码', 'params': {'username': '', 'password': '123456'}, 'assert_result': 'code==400', 'real_result': '', 'remark': ''}, 
    {'case_id': 2.0, 'module_name': '用户模块', 'case_name': '用户登录-测试密码为空的情况', 'method': 'post', 'url': 'http://127.0.0.1:8000/user/login', 'headers': '', 'params_desc': 'username: 用户名\npassword: 密码', 'params': {'username': 'xiaoming', 'password': ''}, 'assert_result': 'code==400', 'real_result': '', 'remark': ''}, 
    {'case_id': 3.0, 'module_name': '用户模块', 'case_name': '用户登录-测试账号密码正确的情况', 'method': 'post', 'url': 'http://127.0.0.1:8000/user/login', 'headers': '', 'params_desc': 'username: 用户名\npassword: 密码', 'params': {'username': 'xiaoming', 'password': '123456'}, 'assert_result': ['code==200', "'data' in json"], 'real_result': '', 'remark': ''}, 
    {'case_id': 4.0, 'module_name': '用户模块', 'case_name': '用户登录-测试使用手机号码登录', 'method': 'post', 'url': 'http://127.0.0.1:8000/user/login', 'headers': '', 'params_desc': 'username: 手机号\npassword: 密码', 'params': {'username': '13312345678', 'password': '123456'}, 'assert_result': 'code==200', 'real_result': '', 'remark': ''}
]
"""
```

<br>
<br>

### csv - python csv 
CSV 工具类是 Python 中的自带包，用来解析 CSV 文件。     

1、实例化一个 CSV 对象，需要传入一个 CSV 文件的路径     
```python
with open('./case.csv') as casefile
```

2、`csv.DictReader()` 将 CSV 读取成字典的形式     
```python
rows2 = csv.DictReader(casefile)
print rows2
# [{'paxID': '111', 'daxID': '222', 'merID': '333'}, {'paxID': '444', 'daxID': '555', 'merID': '666'}]
```

3、`csv.reader()` 将 CSV 读取成 list     
```python
rows = csv.reader(casefile)
row_list = [row for row in rows]
        print row_list
# [['paxID', 'daxID', 'merID'], ['111', '222', '333'], ['444', '555', '666']]
```

4、封装一个 csv 工具类     
```python
#coding=UTF-8
import csv
import traceback
 
class CSV:
    def __init__(self,filePath):
        self.filePath = filePath
        self.allRows = None
        try:
            with open(self.filePath) as csvfile:
                rows = csv.DictReader(csvfile)
                self.allRows = [row for row in rows]
        except:
            traceback.print_exc()
 
    def getAll(self):
        return self.allRows
 
    def getCell(self, rowNum, colunmName):
        cell = ''
        if rowNum > 0 and colunmName != None:
            try:
                cell = self.allRows[rowNum-1][colunmName]
            except:
                print 'colunmName is inexistent'
        else:
            print 'rowNum should begin from 1 or colunmName is invalid'
        return cell
 
    #取csv的标题行,字典中的keys
    def getFirstRow(self):
        try:
            dict1 = self.allRows[0]
            keys = dict1.keys()
        except:
            traceback.print_exc()
        return keys
 
    #取某一纵列的值
    def getColunmName(self, name):
        #创建一个数组，循环大数据，每个字典取Key是name的值，追加到数组中，返回
        result = None
        for d in self.allRows:
            try:
                result.append(d[name])
            except:
                traceback.print_exc()
        return result
```

```python
class OperationCSV:
    def __init__(self):
        pass
 
    @staticmethod
    def is_exist(file_path):
        if os.path.exists(file_path):
            return True
        else:
            logger.error("file is not exist！")
            raise Exception("file is not exist！")
 
    def list_reader(self, file_path):
        if self.is_exist(file_path):
            try:
                with open(file_path, 'r', newline="", encoding='utf-8') as f:
                    rows = csv.reader(f)
                    row_list = [row for row in rows]
                    return row_list
            except Exception as e:
                logger.error(e)
 
    @staticmethod
    def list_writer(file_path, headers, data):
        try:
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(data)
                logger.info(f"成功生成文件:{file_path}!")
        except Exception as e:
            logger.error(e)
 
    def dict_reader(self, file_path):
        if self.is_exist(file_path):
            with open(file_path, 'r', newline="", encoding='utf-8') as f:
                rows = csv.DictReader(f, )
                row_list = [row for row in rows]
                return row_list
 
    @staticmethod
    def dict_writer(file_path, data, fields):
        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fields)
            writer.writerows(data)
            logger.info(f"成功生成文件:{file_path}!")
```

<br>
<br>

---

相关链接：   
[常用的工具类 读取execl 、csv](https://www.cnblogs.com/hanfe1/p/16832120.html)