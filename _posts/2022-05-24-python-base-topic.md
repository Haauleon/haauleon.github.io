---
layout:        post
title:         "面试 | Python 面试题"
subtitle:      "python 基础题、企业面试题、高级题"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - Pythoneer
    - 面试
---

### 基础题
- 给定一个日期，计算这是这一年中的第几天
- 打乱列表
- 根据字典值进行排序
- 反转字符串
- 将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
- 按alist中元素的age由大到小排序
- 找出两个列表的相同元素和不同元素
- 删除列表中的相同元素


```python
class BaseTopic:

    @staticmethod
    def day_of_year(year: int, month: int, day: int):
        """给定一个日期，计算这是这一年中的第几天"""
        import datetime
        date1 = datetime.date(year=year, month=month, day=day)
        date2 = datetime.date(year=year, month=1, day=1)
        return (date1 - date2).days + 1

    @staticmethod
    def upset_list(alist: list):
        """打乱列表"""
        import random
        # 改变原列表, 不返回值
        random.shuffle(alist)
        return alist

    @staticmethod
    def sort_by_value_in_dict(adict: dict):
        """根据字典值进行排序"""
        # x[0]代表用key进行排序, x[1]代表用value进行排序
        new_dict = sorted(adict.items(), key=lambda x: x[1])
        return new_dict

    @staticmethod
    def reverse_str(astr: str):
        """反转字符串"""
        return astr[::-1]

    @staticmethod
    def str_to_dict():
        """将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}"""
        str1 = "k:1 |k1:2|k2:3|k3:4"
        dict1 = dict()
        for items in str1.split('|'):
            key, value = items.split(':')
            dict1[key] = value
        return dict1

    @staticmethod
    def sort_by_dict_in_list():
        """按alist中元素的age由大到小排序"""
        alist = [
            {'name': 'a', 'age': 20},
            {'name': 'b', 'age': 30},
            {'name': 'c', 'age': 25}
        ]
        new_alist = sorted(alist, key=lambda x: x['age'], reverse=False)
        return new_alist

    @staticmethod
    def search_for_two_list():
        """找出两个列表的相同元素和不同元素"""
        list1 = [1, 2, 3, 4, 5]
        list2 = [3, 4, 5, 6, 7]
        set1 = set(list1)
        set2 = set(list2)
        same = set1 & set2
        diff = set1 ^ set2
        return same, diff

    @staticmethod
    def del_sample_element_in_list():
        """删除列表中的相同元素"""
        list1 = [1, 1, 2, 1, 3, 4]
        list2 = set(list1)
        return list2


if __name__ == '__main__':
    # print(BaseTopic.day_of_year(2022, 5, 24))
    # print(BaseTopic.upset_list([1, 2, 3, 4, 5]))
    # print(BaseTopic.sort_by_value_in_dict({'a': 13, 'y': 0, 'x': 9, 's': 2}))
    # print(BaseTopic.reverse_str("123456789"))
    # print(BaseTopic.str_to_dict())
    # print(BaseTopic.sort_by_dict_in_list())
    # print(BaseTopic.search_for_two_list())
    print(BaseTopic.del_sample_element_in_list())
```

<br><br>

### 企业面试题