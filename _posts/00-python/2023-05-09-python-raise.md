---
layout:        post
title:         "Python3 | 自定义异常 raise 关键字"
subtitle:      "一旦执行了raise语句，raise后面的语句将不能执行"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 异常捕获
在编程过程中合理的使用异常可以使得程序正常的执行。有直接抛出异常的形式，也能通过捕获异常加入异常时的业务逻辑处理。     

<br>
<br>

### 自定义抛出异常关键字 - raise
raise 关键字的功能：可以将信息已报错的形式抛出。     

当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行。

<br>
<br>

### 使用raise主动引发异常
```
raise 异常名
raise 异常名, 附加数据
raise 类名
```

<br>
<br>

### raise 关键字的用法
```python
try:
    s = None
    if s is None:
        print "s 是空对象"
        raise NameError     #如果引发NameError异常，后面的代码将不能执行
    print len(s)  #这句不会执行，但是后面的except还是会走到
except TypeError:
    print "空对象没有长度"
 
s = None
if s is None:
    raise NameError 
print 'is here?' #如果不使用try......except这种形式，那么直接抛出异常，不会执行到这里
```

<br>
<br>

### 触发异常
我们可以使用raise语句自己触发异常。     

raise语法格式如下：    
```
raise [Exception [, args [, traceback]]]
```

语句中 Exception 是异常的类型（例如，NameError）参数标准异常中任一种，args 是自已提供的异常参数。      

最后一个参数是可选的（在实践中很少使用），如果存在，是跟踪异常对象。      

实例:     

一个异常可以是一个字符串，类或对象。 Python 的内核提供的异常，大多数都是实例化的类，这是一个类的实例的参数。      

定义一个异常非常简单，如下所示：    
```python
def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
        # 触发异常后，后面的代码就不会再执行
```

<br>

**注意： **为了能够捕获异常，`except` 语句必须有用相同的异常来抛出类对象或者字符串。     

例如我们捕获以上异常，`except` 语句如下所示：    
```
try:
    正常逻辑
except Exception,err:
    触发自定义异常   
else:
    其余代码
```

实例:       
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 定义函数
def mye( level ):
    if level < 1:
        raise Exception,"Invalid level!"
        # 触发异常后，后面的代码就不会再执行
try:
    mye(0)            # 触发异常
except Exception,err:
    print 1,err
else:
    print 2
```

执行以上代码，输出结果为：    
```
$ python test.py
1 Invalid level!
```

python3.6以后 改为:      
```python
def mye( level ):
    if level < 1:
        raise Exception("Invalid level!")
        # 触发异常后，后面的代码就不会再执行
try:
    mye(0)            # 触发异常
except Exception as err:
    print(1,err)
else:
    print(2)
```

<br>
<br>

### 自定义异常类
python 的异常分为两种     
1. 内建异常，就是 python 自己定义的异常     
2. 不够用，用户自定义异常

<br>

首先看看 python 的异常继承树     
我们可以看到 python 的异常有个大基类。然后继承的是 Exception。所以我们自定义类也必须继承 Exception。

（1）创建自定义异常类案例     
```python
class MyException(Exception):
    def __init__(self, msg):
        '''
        :param msg: 异常信息
        '''
        self.msg = msg
```

<br>

（2）最简单的自定义异常     
```python
class FError(Exception):
    pass
```

<br>

（3）抛出异常、用try-except抛出      
```python
try:
    raise FError("自定义异常")
except FError as e:
    print(e)
```

<br>

（4）实例            
```python
class CustomError(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self) #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo
 
if __name__ == '__main__':
    try:
        raise CustomError('客户异常')
    except CustomError as e:
        print(e)
```

<br>

总结：    
- 自定义异常必须继承基类：Exception    
- 需要在构造函数中自定义错误的信息

<br>
<br>

相关链接：    
[自定义异常 raise 关键字](https://blog.csdn.net/weixin_67859959/article/details/129104953)