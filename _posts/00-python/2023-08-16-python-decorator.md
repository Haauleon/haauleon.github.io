---
layout:        post
title:         "Python3 | 装饰器的使用"
subtitle:      "装饰函数、装饰类方法的应用"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 一、闭包
在今后的学习中装饰器会起到很大的作用，而<mark>装饰器就是基于闭包来实现的</mark>。         

<br>

#### 1.闭包的必要性
在一个函数中如果想要想要使用一个变量，我们最直接的方法就是设置一个全局变量。但是这个变量如果只会使用一两次，那么<mark>直到代码进行结束前，那个全局变量一直都会占用着资源，不会被销毁，会浪费资源</mark>。           

<br>
<br>

#### 2.定义
一个函数中若要用到另一个函数的参数，则可以通过闭包的形式来实行。             
顾名思义，闭包（封闭，包含），在下面这段函数中便能体现出来：     
```python
def A():
    a=1
    def B():
        b=2
        print(a)
```

对于函数闭包而言，某一个函数中用到的变量的作用域，取决于其上层或者本层函数函数的作用域。           
对于嵌套函数而言，内层函数中定义的变量是无法在外层函数进行使用的（即在 B() 函数中可以调用 a，但是不能在 A() 函数中调用 b）               
此外可以直接调用函数 A()，但是不能调用函数 B()。          

<br>
<br>

#### 3.调用和引用的区别
调用：会直接从内存中去取出相应的对象执行，代码会直接执行。                  
引用：设置了一个路标，该路标指向某一个内存地址中的对象。此时相当于加载了代码在一个缓存空间内，代码并没有被执行。                 
提醒：如果在没有返回值 return 的情况下调用闭包函数时，只会调用外层函数，不会调用内层函数。          

在下面的例子中，`decorator` 便是引用，`decorator()` 则是调用。在 `return decorator` 的情况下调用 func 函数会发现运行结果中出现的是 decorator 函数（即方式一）；如果调用 func 函数的基础上再加个（）那么 decorator 函数也会被调用（即方式三）。             

（1）方式一：只调用外层函数             
```python
def decorator():
    name = "haauleon"
    print(f"name: {name}")
    def func():
        age = 21
        print(f"name: {name}, age: {age}")
    return func


decorator()

```

输出：       
```bash
name: haauleon
```

<br>

（2）方式二：调用内层函数会报错        
```python
def decorator():
    name = "haauleon"
    print(f"name: {name}")
    def func():
        age = 21
        print(f"name: {name}, age: {age}")
    return func


decorator()
func()

```

输出：        
```bash
name: haauleon
Traceback (most recent call last):
  File "C:/Users/Haauleon/AppData/Roaming/JetBrains/PyCharm2020.1/scratches/scratch_10.py", line 28, in <module>
    func()
NameError: name 'func' is not defined
```

<br>

（3）方式三：调用内层函数的方法          
```python
def decorator():
    name = "haauleon"
    print(f"name: {name}")
    def func():
        age = 21
        print(f"name: {name}, age: {age}")
    return func


decorator()()

```

输出：    
```bash
name: haauleon
name: haauleon, age: 21
```

<br>

（4）方式四：调用内层函数的方法     
```python
def decorator():
    name = "haauleon"
    print(f"name: {name}")
    def func():
        age = 21
        print(f"name: {name}, age: {age}")
    return func()


decorator()

```

输出：    
```bash
name: haauleon
name: haauleon, age: 21
```

<br>
<br>

### 二、装饰器
#### 1.定义
能够在<mark>不改变原有函数</mark>的基础上，在原来的基础上添加额外的功能的代码，就叫做<mark>装饰器</mark>。     

<br>
<br>

#### 2.意义
登录注册（验证账号、密码的准确性）、爬虫中（某一个请求需要在异常之后补充请求头参数然后再去重新对当前请求进行发送）。         

<br>
<br>

#### 3.实现方式
对于装饰器的定义，基于函数闭包的形式来实现，即可以将某一个函数作为参数传递给另一个函数，在这另一个函数中去为函数添加功能。         

<br>
<br>

#### 4.使用案例
（1）原来思维             
```python
def index():
    """
    对于index而言，它的功能是已经实现了的，不希望重构代码
    （编程都流传着一句话，只要你的程序跑起来，哪怕你知道它有bug那也不要去改哈哈哈）所以登陆的权限就交给了其他的函数来实现
    """
    print("账号密码验证中...")


def login(func, username, password):
    if username == "haauleon" and password == "123456":
        func()  # 传递实参来调用函数
        print("账号密码验证成功！")
    else:
        print("你无权限，请与管理员联系")
        return 0


login(index, "haau", "123456")
login(index, "haauleon", "123")
login(index, "haauleon", "123456")

```

输出：    
```bash
你无权限，请与管理员联系
你无权限，请与管理员联系
账号密码验证中...
账号密码验证成功！
```

但是这样的代码可读性并不高。一个函数就添加了三个参数，阅读起来就需要一点一点地去理解，不用说肯定很烦。             

<br>

（2）使用闭包实现装饰器             
该实现可以直接调用 index 函数。     
```python
def index():
    """
    对于index而言，它的功能是已经实现了的，不希望重构代码
    （编程都流传着一句话，只要你的程序跑起来，哪怕你知道它有bug那也不要去改哈哈哈）所以登陆的权限就交给了其他的函数来实现
    """
    print("账号密码验证成功！")


def login(func):
    username = "haauleon"
    password = "123456"
    def inner():
        if username == "haauleon" and password == "123456":
            return func()
        else:
            print("你无权限，请与管理员联系")
            return 0
    return inner


login(index)()

```

输出：    
```bash
账号密码验证成功！
```

到底阅读起来还是不直观，还是需要一步一步地去理解。我们想要一个阅读性更强的代码，那么语法糖就可以解决这个问题。     

<br>
<br>

### 三、语法糖
#### 1.简介
语法糖是 python 中去执行修饰器的一种语法规则。          
写法：`@decorator` 语法糖都要写在某一个函数定义的头上，表示 decorator 函数修饰下面的函数。          
那为什么要去使用它呢。简单理解的话，就是如果你要去修饰一栋墙，你肯定不会是去把墙拆了重新修，而是在之前的基础上进行修饰。代码也是如此，原先的代码我们能不动的话就不动，然后写修饰代码来对原代码进行修饰。            

<br>
<br>

#### 2.使用案例
（1）简单的直接使用            
```python
def login(func):
    """
    接收被修饰的对象（对象可以是函数、类、类中的方法）
    """
    username = "haauleon"
    password = "123456"
    def inner():
        if username == "haauleon" and password == "123456":
            return func()
        else:
            print("你无权限，请与管理员联系")
            return 0
    return inner


# 语法糖出现在函数上方，此处表示index函数被装饰器login装饰，login叫做装饰器（n.也叫装饰函数）
# login修饰index的过程是叫装饰函数（v.）
@login
def index():
    """
    对于index而言，它的功能是已经实现了的，不希望重构代码
    （编程都流传着一句话，只要你的程序跑起来，哪怕你知道它有bug那也不要去改哈哈哈）所以登陆的权限就交给了其他的函数来实现
    """
    print("账号密码验证成功！")


index()

```

输出：     
```bash
账号密码验证成功！
```

<br>

（2）有传参            
```python
def login(func):
    """
    接收被修饰的对象（对象可以是函数、类、类中的方法）
    """
    def inner(username, password):  # 形参1
        if username == "haauleon" and password == "123456":
            return func(username, password)  # 形参2
        else:
            print("你无权限，请与管理员联系")
            return 0
    return inner


# 语法糖出现在函数上方，此处表示index函数被装饰器login装饰，login叫做装饰器（n.也叫装饰函数）
# login修饰index的过程是叫装饰函数（v.）
@login
def index(username, password):  # 形参3
    print(f"输入的账号:{username}, 密码:{password}")
    print("账号密码验证成功！")


index(username="haauleon", password="123456")  # 实参

```

输出：    
```bash
输入的账号:haauleon, 密码:123456
账号密码验证成功！
```

总的来说，添加一个实参，就需要添加三个形参，说到底我们还是将问题复杂了。      


<br>

（3）使用函数嵌套进行语法糖传参           
但是在进行传参时我们需要注意是不能在装饰器函数设置形参的。最好的方法就是再进行函数的嵌套。        
```python
def sugar(username, password):
    def login(func):
        def inner():
            if username == "haauleon" and password == "123456":
                return func(username, password)
            else:
                print("你无权限，请与管理员联系")
                return 0
        return inner
    return login


@sugar(username="haauleon", password="123456")
def index(username, password):
    print(f"输入的账号:{username}, 密码:{password}")
    print("账号密码验证成功！")


index()

```

输出：    
```bash
输入的账号:haauleon, 密码:123456
账号密码验证成功！
```

<br>
<br>

#### 3.类与装饰器的使用
（1）装饰类方法          
```python
def decorator(func):
    def inner():  # 1
        return func()  # 2
    return inner


class A:
    @decorator
    def index(self):
        print("haauleon")


a = A()
a.index()

```

输出：  
```bash
Traceback (most recent call last):
  File "C:/Users/Haauleon/AppData/Roaming/JetBrains/PyCharm2020.1/scratches/scratch_10.py", line 31, in <module>
    a.index()
TypeError: inner() takes 0 positional arguments but 1 was given
```

我们可以看出是类 A 的实例方法 index，那么在 1 和 2 处我们就需要接受一个 self。     
```python
def decorator(func):
    def inner(self):  # 1
        return func(self)  # 2
    return inner


class A:
    @decorator
    def index(self):
        print("haauleon")


a = A()
a.index()

```

输出：    
```bash
haauleon
```

<br>

（2）装饰类          
修饰类的话，那么类中的方法对会被修饰。     
```python
def decorator(func):
    def inner(name):
        if name == "haauleon":
            print(name)
            return func(name)
    return inner


@decorator  # 该装饰器装饰的是整个类，而不是一个单独的方法，在对类实例化的时候就会调用装饰器
class A:

    def __init__(self, name):
        self.name = name

    def func_1(self):
        print(f"func_1: {self.name}")

    def func_2(self):
        print(f"func_2: {self.name}")


a = A(name="haauleon")
a.func_1()
a.func_2()

```

输出：   
```bash
haauleon
func_1: haauleon
func_2: haauleon
```

<br>
<br>

### 四、实际应用示例
#### 1.装饰函数并返回形参给函数
实现效果：定义一个装饰器 decorator 用来装饰函数 func1，先由装饰器处理一部分逻辑并将处理结果的值返回给函数，而该处理结果的值又将作为函数的形参作用于函数内部。        
```python
def decorator(func):
    name = 'haauleon'
    name = name + "!!!"
    def inner():
        return func(name)
    return inner


@decorator
def func1(name):
    print(f"{name}")


func1()

```

输出：    
```bash
haauleon!!!
```

处理逻辑放在内层函数 inner 内也可以实现：        
```python
def decorator(func):
    def inner():
        name = 'haauleon'
        name = name + "!!!"
        return func(name)
    return inner


@decorator
def func1(name):
    print(f"{name}")


func1()

```

<br>

#### 2.装饰函数并处理函数传入的值
实现效果：定义一个装饰器 decorator 用来装饰函数 func2，装饰器接受函数传入的值并进行处理，处理完成后将处理结果的值返回给函数，而该处理结果的值又将作为函数的形参作用于函数内部。       
```python
def decorator(func):
    def inner(name):
        name = name + "!!!"
        return func(name)
    return inner


@decorator
def func1(name):
    print(f"{name}")


func1(name="haauleon")

```

输出：    
```bash
haauleon!!!
```

<br>

#### 3.装饰类方法
装饰器的处理逻辑与函数一致，但是在装饰类方法时需要多传入一个 self。      
```python
def decorator(func):
    def inner(self, name):
        name = name + "!!!"
        return func(self, name)
    return inner


class Func:

    @decorator
    def func1(self, name):
        print(f"{name}")


f = Func()
f.func1(name="haauleon")

```

输出：    
```bash
haauleon!!!
```

<br>
<br>

---

相关链接：    
[Python的装饰器](https://blog.csdn.net/m0_72154565/article/details/127936637)