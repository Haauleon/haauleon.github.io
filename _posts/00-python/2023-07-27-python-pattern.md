---
layout:        post
title:         "Python3 | 设计模式"
subtitle:      "单例模式、工厂模式、建造者模式"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 一、什么是设计模式
&emsp;&emsp;软件工程中，设计模式是指软件设计问题的推荐方案。设计模式一般是描述如何组织代码和使用最佳实践来解决常见的设计问题。需要记住一点：设计模式是高层次的方案，并不关注具体的实现细节，比如算法和数据结构。对于正在尝试解决的问题，何种算法和数据结构最优，则是由软件工程自己把握。          

**总结**：设计模式是一套<mark>被反复使用的、多数人知晓的、经过分类编目的、代码设计经验的总结</mark>。使用设计模式是为了重用代码，让代码更容易地被他人理解，保证代码地可靠性。         

<br>
<br>

### 二、python实现设计模式
设计模式共分为三类      
- 创建型模式
- 结构性模式
- 行为型模式

<br>

### 三、创建者模式
#### 1.单例模式
&emsp;&emsp;单例模式(Singleton Pattern)是一个常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在，<mark>当希望在某个系统中只出现一个实例时，单例对象就能派上用场</mark>。         

定义：<mark>保证了只有一个实例，并提供了一个访问它地全局访问点</mark>              
使用场景：当一个类只能由一个实例，而客户可以从一个众所周知的访问点访问它                     
优点:               
<mark>1.在内存中只有一个实例，减少了内存的开销</mark>，尤其是频繁的创建和销毁实例（比如管理学院首页页面缓存）。                
<mark>2.避免对资源的多重占用</mark>（比如写 文件操作）                     

&emsp;&emsp;比如，<mark>某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息</mark>。如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建AppConfig 对象的实例，这就导致系统中存放多个AppConfig的实例对象，而这样会严重浪费内存资源，类似AppConfig 这样的类，我们希望在程序运行时间只有一个实例对象。          
```python
class Singleton():
    _instance = None # 定义一个变量，来接收实例化对象
    def __new__(cls, *args,**kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
   
s1 = Singleton()
s2 = Singleton()
print(id(s1),id(s2))
```

<br>

**方法一：使用模块**             
实现方法：将需要实现的单例功能放到一个 `.py` 文件中                  
实现原理：<mark>Python 的模块就是天然的单例模式</mark>，<mark>因为模块在第一次导入时，会生成 `.pyc` 文件，当第二次导入时，就会直接加载 `.pyc` 文件，而不会再次执行模块代码</mark>。因此，我们只需要把相关的函数和数据定义在一个模块中，就可以获取到一个单例对象了。                   
```python
# mysingleton.py
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()
```

将代码保存到 mysingleton.py 中，需要使用，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象             
```python
from a import singleton
```

<br>

**方式二、装饰器实现**            
```python
def Singleton(cls):
    _instance = {}
    def _singleton(*args, **kwargs):
        if cls not in _instance: # 判断该实例是否存在，存在就直接返回，不存在就创建 
            _instance[cls] = cls(*agrs, **kwargs)
        return _instance[cls]
     return _singleton
   
@Singleton
class A(object):
    a = 1
    def __init(self, x=0)
    	self.x = x
      
# a1 = A(2)
a2 = A(3)
```

<br>

**方法三、基于__new__方法**               
&emsp;&emsp;我们知道，<mark>当我们实例化一个对象时，是先执行了类的 `__new__` 方法</mark>(没写的时候，默认调用 `object.new` )，实例化对象；然后再执行类的 `__init__` 方法，对这个对象进行初始化，所以我们可以基于这个，实现单例模式。         
&emsp;&emsp;我们最初最常用的是重写 `__new__` 方法的方式，但是用重写类的 `__new__` 方法，在多次创建对象时，尽管返回的都是同一个对象，但是每次执行创建对象执行语句时，内部的 `__init__` 方法都会被自动调用，而在某些应用场景，可能存在初始化方法只能循序运行一次的需求，这时这种实现单例的方式不可取。               
```python
class Download(object):
    instance = None
 
    def __init__(self):
        print("__init__")
 
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
 
 
obj1 = Download()
obj2 = Download()
print(obj1)
print(obj2)
```

运行结果，还是初始化多次执行了      
```python
__init__
__init__
<__main__.Download object at 0x00000223D9B11910>
<__main__.Download object at 0x00000223D9B11910>
```

原文链接：[https://blog.csdn.net/weixin_43783714/article/details/103352436](https://blog.csdn.net/weixin_43783714/article/details/103352436)         

<mark>init 方法通常在初始一个类的实例的时候，但其实他并不是实例化一个类的时候第一个被调用的方法</mark>，当使用 `Teacher(id, name)` 这样的表达式来实例化一个类时，<mark>最先被调用的方式，其实是 new 方法</mark>。            
new 方法接受的参数虽然也和 init 一样，但 init 是在类实例创建之后调用，<mark>而 new 方法正是创建这个类实例的方法</mark>。          
new 为对象分配空间，是内置的静态方法，new 在内存中为对象分配了空间也返回了对象的引用，init 获得了这个引用才初始化了这个实例。            

<br>
<br>

#### 2.工厂模式
**概念**     
定义一个创建对象的接口，但让实现这个接口的类来决定实例化哪个类。工厂方法类的实例化推迟到子类进行，属于创建型模式，它提供了一种创建对象的最佳方式。目标是当直接创建对象(在 python 中通过 `__int__()` 函数实现的)不方便时，提供更好的方式。       

在工厂设计模式中，客户端1 可以请求一个对象，而无须知道这个对象来自哪里；也就是，不用知道使用哪个类来生成这个对象。工厂背后的思想是简化对象的创建。与客户端自己i基于类实现化直接创建对象相比，基于一个中心化函数来实现，更易于追踪创建了哪些对象。      

通过将创建对象的代码和使用对象的代码解耦，工厂能够降低应用维护和复杂度。       

工厂方法创建对象时，我们并没有与某个特定类耦合/绑定到一起，而只是通过调用某个函数来提供关于我们想要什么的部分信息。这意味着修改这个函数比较容易，不需要同时修改使用这个函数的代码。        

工厂通常有两种形式：     
<mark>第一种是工厂方法（Factory Method)</mark>，它是一个方法(或以Python的术语来说，是一个函数)，对不同的输入参数返回不同的对象；       
<mark>第二种是抽象工厂</mark>，它是一组用于创建一系列关系事务对象的工厂          

两者区别详解：[https://www.cnblogs.com/Zzbj/p/15778464.html](https://www.cnblogs.com/Zzbj/p/15778464.html)    

在工厂模式(简单工厂)模式种，我们执行单个函数，传入一个参数(提供信息表明我们想要什么)，但并不知道要求任何关于对象如果实现以及对象来自哪里的细节。          

一个例子：           
我们有一个基类 Person，包含获取名字，性比的方法。有两个子类 male 和 female，可以打招呼，还有一个工厂类。工厂类有一个方法名 getPerson 有两个输入参数，名字和性别。用户使用工厂类，通过调用 getPerson 方法。              

<mark>实现一个工厂方法，通过输入无聊，然后产出不同的产品类。在程序运行期间，用户传递性别给工厂</mark>，工厂创建一个与性别有关的对象。因此工厂类在运行期，决定了哪个对象应该被创建。         

```python
class Person:

    def __init__(self):
        self.name = None
        self.gender = None
 
    def getName(self):
        return self.name
     
    def getGender(self):
        return self.gender
 

class Male(Person):
    def __init__(self, name):
        print("Hello Mr." + name)
 

class Female(Person):
    def __init__(self, name):
        print("Hello Miss." + name)
 

class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Female(name)


if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("Chetan", "M")

```

<br>
<br>

#### 3.建造者模式
将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。建造者模式将所有细节都由子类实现。需求，画任务，要求画一个人的头，左手，右手，左脚，右脚和身体，画一个瘦子，一个胖子。     

**不使用设计模式：**        
```python
if __name__=='__name__':
    print('画左手')
    print('画右手')
    print('画左脚')
    print('画右脚')
    print('画胖身体')
 
    print('画左手')
    print('画右手')
    print('画左脚')
    print('画右脚')
    print('画瘦身体')

```

这样写的缺点每画一个人，都要依次得画他的六个部位，这些部位有一些事可以重用的，所以调用起来会比较繁琐，而且客户调用的时候可能会忘记画其中的一个部位，所以容易出错。

**建造一个抽象的类 Builder，声明画六个部位的方法，每画一种人，就新建一个继承 Builder 的类，这样新建的类就必须要实现 Builder 的所有方法**，这里主要运用了抽象方法的特性，父类定义了几个抽象的方法，子类必须要实现这些方法，否则就报错，这里解决了会漏画一个部位的问题。建造一个指挥者类 Director，输入一个Builder类，定义一个 draw 的方法，把画这六个部位的方法调用都放在里面，这样调用起来就不会繁琐了。         

Python 本身不提供抽象类和接口机制，要想实现抽象类，可以借助 abc 模块。abc 是 Abstract Base Class 的缩写。         

被 `@abstractmethod` 装饰为抽象方法后，该方法不能被实例化；除非子类实现了基类的抽象方法，所以能实例化。         

```python
#encoding=utf-8
from abc import ABCMeta, abstractmethod
class Builder():
    __metaclass__ = ABCMeta
 
    @abstractmethod
    def draw_left_arm(self):
        pass
     
    @abstractmethod
    def draw_right_arm(self):
        pass
     
    @abstractmethod
    def draw_left_foot(self):
        pass
     
    @abstractmethod
    def draw_right_foot(self):
        pass
     
    @abstractmethod
    def draw_head(self):
        pass
     
    @abstractmethod
    def draw_body(self):
        pass
 

class Thin(Builder):#继承抽象类，必须实现其中定义的方法
    def draw_left_arm(self):
        print('画左手')
 
    def draw_right_arm(self):
        print('画右手')
     
    def draw_left_foot(self):
        print('画左脚')
     
    def draw_right_foot(self):
        print('画右脚')
     
    def draw_head(self):
        print('画头')
     
    def draw_body(self):
        print('画瘦身体')
 

class Fat(Builder):
    def draw_left_arm(self):
        print('画左手')
 
    def draw_right_arm(self):
        print('画右手')
     
    def draw_left_foot(self):
        print('画左脚')
     
    def draw_right_foot(self):
        print('画右脚')
     
    def draw_head(self):
        print('画头')
     
    def draw_body(self):
        print('画胖身体')
 

class Director():
    def __init__(self, person):
        self.person=person
 
    def draw(self):
        self.person.draw_left_arm()
        self.person.draw_right_arm()
        self.person.draw_left_foot()
        self.person.draw_right_foot()
        self.person.draw_head()
        self.person.draw_body()
 

if __name__=='__main__':
    thin=Thin()
    fat=Fat()
    director_thin=Director(thin)
    director_thin.draw()
    director_fat=Director(fat)
    director_fat.draw()

```