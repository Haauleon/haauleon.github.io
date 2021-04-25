---
layout:        post
title:         "Python3 | numba 库的 jit 模块"
subtitle:      "使用 jit 加速程序运行速度"
date:          2021-04-25
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
---

## 背景
&emsp;&emsp;python 一直被病垢运行速度太慢，但是实际上 python 的执行效率并不慢，慢的是 python 用的解释器 Cpython 运行效率太差。        
&emsp;&emsp;numba 所完成的工作就是：解析 Python 函数的 ast 语法树并加以改造，添加类型信息；将带类型信息的 ast 语法树通过 llvmpy 动态地转换为机器码函数，然后再通过和 ctypes 类似的技术为机器码函数创建包装函数供 Python 调用。（说实话我看不懂）        
&emsp;&emsp;看网上说得很牛掰的样子，我自己也来试试。              

<br><br>

## 使用技巧
###### 未使用 jit 的运行速度
```python
%%time

def my_power(x):
    return (x**2)

def my_power_sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + my_power(i)
    return (s)

print(my_power_sum(1000000))
```
<br>

运行结果：       
```
333333833333500000
CPU times: user 374 ms, sys: 6.73 ms, total: 380 ms
Wall time: 383 ms
```

<br><br>

###### 使用 jit 后的运行速度
```python
%%time
from numba import jit

@jit
def my_power(x):
    return (x**2)

@jit
def my_power_sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + my_power(i)
    return (s)

print(my_power_sum(1000000))
```
<br>

运行结果：         
```

    for i in range(1, n+1):
        s = s + my_power(i)
    return (s)

print(my_power_sum(1000000))
333333833333500000
CPU times: user 109 ms, sys: 2.45 ms, total: 111 ms
Wall time: 113 ms
```