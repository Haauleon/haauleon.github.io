---
layout:        post
title:         "Python3 | 绑定与未绑定方法"
subtitle:      "类中的绑定方法与未绑定方法的区别"
date:          2021-05-17
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - Pythoneer
---

与类和实例无绑定关系的 function 都属于函数（function）            
与类和实例有绑定关系的 function 都属于方法（method）           

类中的方法有两类：绑定方法和非绑定方法。             

## 一、绑定方法 
###### 1.对象的绑定方法
&emsp;&emsp;凡是类中的方法或函数，默认情况下都是绑定给对象使用的。以下的结果表明：Foo.instance_method 这个方法是绑定给 Foo object 使用的。                         
```python
# coding:utf-8
class Foo(object):

    def instance_method(self):
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))


if __name__ == "__main__":
    foo = Foo()
    print(foo.instance_method)
```

运行结果：        
```
<bound method Foo.instance_method of <__main__.Foo object at 0x7fdda85cf350>>
```

<br>

&emsp;&emsp;将 instance_method() 的参数 self 去掉，结果显示如上。这说明，不管是类中的方法，还是类中函数，默认情况下都是绑定给对象使用的。                          
```python
class Foo(object):

    def instance_method():
        print("是类{}的实例方法，只能被实例对象调用".format(Foo))


if __name__ == "__main__":
    foo = Foo()
    print(foo.instance_method)
```

运行结果：         
```
<bound method Foo.instance_method of <__main__.Foo object at 0x7fdda85cf850>>
```

<br>

&emsp;&emsp;绑定给对象使用有一种好处，那就是不用手动将对象传入。对象是自动传到类中。如果是类来调用类中绑定给对象使用的方法时，那么这个方法仅仅只是一个函数，函数没有自动传值功能，只能在调用方法的时候一一传参。        
```python
# coding:utf-8
class Foo(object):

    def __init__(self, age):
        self.age = age

    def instance_method(self):
        pass


if __name__ == "__main__":
    print(Foo.instance_method)       # 类调用类方法时，那么这个方法是一个函数 function
    print(Foo.instance_method(18))   # 类调用类方法时，需要一一传参
    print(Foo.instance_method())     # 类调用类方法时，不传参则报错
```

运行结果：         
```
<function Foo.instance_method at 0x7fdda85c4b00>
None
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
~/xxx/xxx/xxx/xxx/test.py in 
     12     print(Foo.instance_method)
     13     print(Foo.instance_method(18))
---> 14     print(Foo.instance_method())

TypeError: instance_method() missing 1 required positional argument: 'self'
```

<br><br>


###### 2.类的绑定方法
&emsp;&emsp;在 python 中，引入了 @classmethod 方法，将类中的绑定方法解除对象绑定关系，进而绑定到类上。           
```python
# coding:utf-8
class Foo(object):
 
    @classmethod
    def class_method(cls):
        print("是类方法")
 

if __name__ == "__main__":
    foo = Foo()
    print(foo.class_method)
    print(Foo.class_method)
```

运行结果：        
```
<bound method Foo.class_method of <class '__main__.Foo'>>
<bound method Foo.class_method of <class '__main__.Foo'>>
```

<br>

&emsp;&emsp;若对象来调用绑定到类上的方法时，被 @classmethod 修饰的方法需要传入参数 cls，否则会报错。          
```python
# coding:utf-8
class Foo(object):
 
    @classmethod
    def class_method(cls):
        print("是类方法")
 

if __name__ == "__main__":
    foo = Foo()
    print(foo.class_method())
```

运行结果：         
```
# coding:utf-8...
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
~/xxx/xxx/xxx/xxx/test.py in 
      9 if __name__ == "__main__":
     10     foo = Foo()
---> 11     print(foo.class_method())

TypeError: class_method() takes 0 positional arguments but 1 was given
```

<br><br>

###### 3.总结
&emsp;&emsp;对于类中的绑定方法，也基本上就这两种，不管怎么变化，只要记住以下规则，遇到这种情况，都不会再错。                  

&emsp;&emsp;类中方法默认都是绑定给对象使用，当对象调用绑定方法时，会自动将对象作为第一个参数传递进去；而类来调用，则必须遵循函数参数一一对应的规则，有几个参数，就必须传递几个参数。如果一个方法是用了 @classmethodn 装饰器，那么這个方法绑定到类身上，不管是对象来调用还是类调用，都会将类作为第一个参数传递进去。           

<br><br>

## 二、非绑定方法
&emsp;&emsp;python 给我们提供了 @staticmethod，可以解除绑定关系，将一个类中的方法，变为一个普通函数。即既不绑定类同时也不绑定对象。              
```python
# coding:utf-8
class Foo(object):
 
    @staticmethod
    def static_method():
        print("是静态方法")
 

if __name__ == "__main__":
    foo = Foo()
    print(foo.static_method)
    print(Foo.static_method)
```

运行结果：         
```
<function Foo.static_method at 0x7fdda86217a0>
<function Foo.static_method at 0x7fdda86217a0>
```

<br>

&emsp;&emsp;既然是普通函数，那么就遵从函数参数传递规则，有几个参数就传递几个参数。            
```python
# coding:utf-8
from typing import AsyncGenerator


class Foo(object):
 
    @staticmethod
    def static_method(age, name):
        pass
 

if __name__ == "__main__":
    print(Foo.static_method(18, "haauleon"))
    print(Foo.static_method())
```

运行结果：         
```
None
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
~/xxx/xxx/xxx/xxx/test.py in 
     12 if __name__ == "__main__":
     13     print(Foo.static_method(18, "haauleon"))
---> 14     print(Foo.static_method())

TypeError: static_method() missing 2 required positional arguments: 'age' and 'name'
```