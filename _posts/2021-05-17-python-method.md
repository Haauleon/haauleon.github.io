---
layout:        post
title:         "Python3 | 函数和方法"
subtitle:      "python 中函数和方法的区别"
date:          2021-05-17
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - Pythoneer
---


## 函数(FunctionType)
1. 函数是封装了一些独立的功能，可以直接调用，能将一些数据（参数）传递进去进行处理，然后返回一些数据（返回值），也可以没有返回值。      
2. 可以直接在模块中进行定义使用。        
3. 所有传递给函数的数据都是显式传递的。        

<br><br>


## 方法(MethodType)
1. 方法和函数类似，同样封装了独立的功能，但是方法是只能依靠类或者对象来调用的，表示针对性的操作。         
2. 方法中的数据self和cls是隐式传递的，即方法的调用者。            
3. 方法可以操作类内部的数据。     

<br>

python 类语法中有三种方法，实例方法，静态方法，类方法。             
1. 实例方法只能被实例对象调用，静态方法(由@staticmethod装饰的方法)、类方法(由@classmethod装饰的方法)，可以被类或类的实例对象调用。       
2. 实例方法，第一个参数必须要默认传实例对象，一般习惯用 self。        
3. 静态方法，参数没有要求。         
4. 类方法，第一个参数必须要默认传类，一般习惯用 cls。          

```python
# coding:utf-8
class Foo(object):
    """类三种方法语法形式"""
 
    def instance_method(self):
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))
 
    @staticmethod
    def static_method():
        print("是静态方法")
 
    @classmethod
    def class_method(cls):
        print("是类方法")
 

if __name__ == "__main__":
    foo = Foo()
    foo.instance_method()
    foo.static_method()
    foo.class_method()
    print("===========================")
    Foo.static_method()
    Foo.class_method()
``` 

运行结果：          
```
是类<class '__main__.Foo'>的实例方法，只能被实例对象调用
是静态方法
是类方法
===========================
是静态方法
是类方法
```

<br><br>


## 区别
```python
from types import MethodType, FunctionType


class Foo(object):
    def __init__(self):
        self.name = "haiyan"

    def func(self):
        print(self.name)


if __name__ == '__main__':         
    obj = Foo()
    print(isinstance(obj.func,FunctionType))  # False
    print(isinstance(obj.func,MethodType))    # True   #说明这是一个方法
    print(isinstance(Foo.func,FunctionType))  # True   #说明这是一个函数。
    print(isinstance(Foo.func,MethodType))    # False
```

运行结果：       
```
False
True
True
False
```

<br>

&emsp;&emsp;以上例子中，类对象调用 func 是方法，类调用 func 是函数。这只是在 python3 中才有的区分，python2 中全部称为方法。            

<br><br>

###### 一、传参
&emsp;&emsp;最大的区别是参数的传递参数，方法是自动传参 self，函数是主动传参。         
```python
# 函数
def func():
    print("函数")

class Test:

    def method(self):
        print("方法")    
```

<br><br>

###### 二、位置
&emsp;&emsp;函数是直接写文件中而不是 class 中，方法是只能写在 class 中。         

<br><br>

###### 三、定义
&emsp;&emsp;函数定义的方式。def 关键字，然后接函数名，再是括号。括号里面写形参也可以省略不写形参：            
```python
def functionName():
    """这里是函数的注释"""
    print("这一块写函数的内容")
```

<br>

&emsp;&emsp;方法定义的方式。首先方法是定义在类中的，其他大体上和函数定义差不多，这里需要注意的一点就是方法必须带一个默认参数(相当于 this)，静态方法除外。                   
```python
class className(super):
    
    def methodName(self):
        """这里是方法的注释
        self 相当于this
        """
        print("这里是方法的内容")
```

<br><br>

###### 四、调用
函数的调用：函数的调用是直接写函数名(函数参数1,函数参数2,......)              
```python
def functionName():
    print("这是一个函数")
 
#调用
functionName()
```

<br>

方法的调用：方法是通过对象点方法调用的（这里是指对象方法）             
```python
class className:
    
    def method(self):
        print("这是一个方法")
 
#调用---------------------
#实例化对象
c = className()
c.method()
```