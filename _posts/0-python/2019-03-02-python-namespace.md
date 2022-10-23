---
layout:        post
title:         "Python3 | 命名空间 locals"
subtitle:      "如何在全局和局部作用域中使用命名空间？"
date:          2017-11-07
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
---

## 背景
###### 一、什么是命名空间
&emsp;&emsp;命名空间其实就是一个字典 dict，通过键值的方式来存储作用域中的变量名和变量值。即： `dict = {'变量名1': '变量值1', '变量名2': '变量值2', ...}`。          

<br><br>

###### 二、命名空间的作用
&emsp;&emsp;由于命名空间是一个字典，可以通过 python 内置的字典操作方式来访问命名空间里的变量名和变量值。          

<br><br>

###### 三、命名空间的使用
使用方法：        
```python
# 定义一个字典类型的对象来指向当前命名空间
locals()
```
<br><br>

## 使用技巧
###### 一、全局作用域
```python
a = 1 
b = 2

# 定义一个变量接收全局命名空间里的变量名和变量值
global_namespace = locals()
print(type(global_namespace)) # <class 'dict'>

# 访问全局命名空间中的变量的值
print(global_namespace['a'])  # 1

# 向全局命名空间中添加一对键值
global_namespace['c'] = 3
print(global_namespace)
```
<br><br>

###### 二、局部作用域
```python
def test():
    a = 3
    b = 4
    c = 5

    # 定义一个变量接收局部命名空间里的变量名和变量值
    local_namespace = locals()
    return local_namespace

# 定义一个变量获取局部命名空间中所有的变量名和变量值
local_test = test()  
print(local_test)     # {'a': 3, 'b': 4, 'c': 5}

# 向局部命名空间中添加一对键值
local_test['d'] = 6
print(local_test)     # {'a': 3, 'b': 4, 'c': 5, 'd': 6}
```

<br>

```python
class TestNameSpace(object):

    def test(self):
        a = 3
        b = 4
        c = 5
        local_namespace = locals()
        return local_namespace


if __name__ == '__main__':
    test_namespace = TestNameSpace()
    test_local = test_namespace.test()

    print(test_local)        # {'self': <__main__.TestNameSpace object at 0x7f870bed6d90>, 'a': 3, 'b': 4, 'c': 5}
    print(test_local['c'])   # 5
    
    test_local['d'] = 6
    print(test_local)        # {'self': <__main__.TestNameSpace object at 0x7f870bed6d90>, 'a': 3, 'b': 4, 'c': 5, 'd': 6}
```