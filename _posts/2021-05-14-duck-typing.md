---
layout:        post
title:         "Python3 | 鸭子类型"
subtitle:      "鸭子类型的含义与其在 python 中的表现形式"
date:          2021-05-14
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - Pythoneer
---

## 鸭子类型
&emsp;&emsp;在程序设计中，鸭子类型（duck typing）是动态类型的一种风格。         

&emsp;&emsp;在这种风格中，一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由当前方法和属性的集合决定。         

&emsp;&emsp;这个概念的名字来源于由 James Whitcomb Riley 提出的鸭子测试，“鸭子测试”可以这样表述：当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。      

&emsp;&emsp;在鸭子类型中，关注的不是对象的类型本身，而是它是如何使用的。     

&emsp;&emsp;鸭子类型通常得益于不测试方法和函数中参数的类型，而是依赖文档、清晰的代码和测试来确保正确使用。从静态类型语言转向动态类型语言的用户通常试图添加一些静态的（在运行之前的）类型检查，从而影响了鸭子类型的益处和可伸缩性，并约束了语言的动态特性。Python 文档中有一句：鸭子类型应避免使用 type() 或 isinstance() 等测试类型是否合法。           

<br><br>

## 在 python 中的表现形式
```python
class Duck:
    def quack(self): 
        print("呱呱呱！")
    def feathers(self): 
        print("这个鸭子拥有灰白灰白的羽毛。")
 
class Person:
    def quack(self):
        print("你才是鸭子你们全家人是鸭子！")
    def feathers(self): 
        print("这个人穿着一件鸭绒大衣。")
 
def in_the_forest(duck):
    duck.quack()
    duck.feathers()
 
def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)
 
game()
```

<br>

&emsp;&emsp;从哪里可以看出 Python 是鸭子类型的风格呢?       

&emsp;&emsp;`in_the_forest()` 函数对参数 duck 只有一个要求：就是可以实现 quack() 和 feathers() 方法。然而 Duck 类和 Person 类都实现了 quack() 和 feathers() 方法，因此它们的实例对象 donald 和 john 都可以用作 `in_the_forest()` 的参数。这就是鸭子类型。        

&emsp;&emsp;鸭子类型给予 Python 这样的动态语言以多态。 但是这种多态的实现完全由程序员来约束强制实现（文档、清晰的代码和测试），并没有语言上的约束（如 C++ 继承和虚函数）。因此这种方法即灵活，又提高了对程序员的要求。