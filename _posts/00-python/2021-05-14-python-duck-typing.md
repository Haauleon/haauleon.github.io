---
layout:        post
title:         "Python3 | 鸭子类型"
subtitle:      "鸭子类型的含义与其在 python 中的表现形式"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 鸭子类型
![](\haauleon\img\in-post\post-other\2021-05-14-duck-1.jpg)         

<br><br>

### 在 python 中的表现形式
```python
class Duck:
    def quack(self): 
        print("呱呱呱！")
    def feathers(self): 
        print("这个鸭子拥有灰白灰白的羽毛。")
 
class Person:
    def quack(self):
        print("哈哈哈哈哈哈哈哈哈哈你在说啥")
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

![](\haauleon\img\in-post\post-other\2021-05-14-duck-2.jpg)         