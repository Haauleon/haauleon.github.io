---
layout:        post
title:         "Python3 | 加速的方法"
subtitle:      "列举了一些让程序运行加速的方法"
date:          2021-04-25
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
---

## numba.jit 加速函数                  
###### 一、背景
&emsp;&emsp;python 一直被病垢运行速度太慢，但是实际上 python 的执行效率并不慢，慢的是 python 用的解释器 Cpython 运行效率太差。        
&emsp;&emsp;numba 所完成的工作就是：解析 Python 函数的 ast 语法树并加以改造，添加类型信息；将带类型信息的 ast 语法树通过 llvmpy 动态地转换为机器码函数，然后再通过和 ctypes 类似的技术为机器码函数创建包装函数供 Python 调用。（说实话我看不懂）        
&emsp;&emsp;看网上说得很牛掰的样子，我自己也来试试。              

<br><br>

###### 二、未使用 jit 
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

###### 三、使用 jit
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

<br><br>

## Counter 加速列表计数
###### 一、背景
定义一个列表：       
```python
data = [x**2%1989 for x in range(2000000)]
```
<br><br>

###### 二、使用 for 循环计数
```python
%%time
values_count = {}
for i in data:
    i_cnt = values_count.get(i,0)
    values_count[i] = i_cnt + 1
print(values_count.get(4,0))
```
<br>

运行结果：         
```
CPU times: user 501 ms, sys: 2.81 ms, total: 504 ms
Wall time: 510 ms
```

<br><br>

###### 三、使用 Counter 计数
```python
%%time
from collections import Counter

values_count = Counter(data)
print(values_count.get(4,0))
```
<br>

运行结果：       
```
8044
CPU times: user 152 ms, sys: 1.06 ms, total: 154 ms
Wall time: 153 ms
```

<br><br>

## ChainMap 加速字典合并
###### 一、背景
定义四个字典：       
```python
dict_a = {i:i+1 for i in range(1,1000000,2)}
dict_b = {i:2*i+1 for i in range(1,1000000,3)}
dict_c = {i:3*i+1 for i in range(1,1000000,5)}
dict_d = {i:4*i+1 for i in range(1,1000000,7)}
```
<br><br>

###### 二、使用 dict.update 进行合并
```python
%%time
result = dict_a.copy()
result.update(dict_b)
result.update(dict_c)
result.update(dict_d)
print(result.get(9999,0))
```
<br>

运行结果：       
```
10000
CPU times: user 72.6 ms, sys: 17 ms, total: 89.6 ms
Wall time: 89.5 ms
```

<br><br>

###### 三、使用 ChainMap 进行合并
```python
%%time
from collections import ChainMap

chain = ChainMap(dict_a,dict_b,dict_c,dict_d)
print(chain.get(9999,0))
```
<br>

运行结果：        
```
10000
CPU times: user 451 µs, sys: 284 µs, total: 735 µs
Wall time: 1.14 ms
```

<br><br>

## Map 加速列表生成
###### 一、背景
&emsp;&emsp;用于生成一个没有 if 判断语句的列表。    
<br><br>

###### 二、使用列表推导式 
```python
%%time
result = [x**2 for x in range(1,1000000,3)]
```
<br>

运行结果：     
```
CPU times: user 90.9 ms, sys: 6.94 ms, total: 97.8 ms
Wall time: 97.7 ms
```

<br><br>

###### 三、使用 map 生成列表
```python
%%time
result = map(lambda x:x**2, range(1,1000000,3))
```
<br>

运行结果：          
```
CPU times: user 5 µs, sys: 1e+03 ns, total: 6 µs
Wall time: 8.11 µs
```

<br><br>

## Filter 加速列表生成
###### 一、背景
&emsp;&emsp;用于生成一个有 if 语句的列表。    

<br><br>

###### 二、使用列表推导式
```python
%%time
result = [x for x in range(1,1000000,3) if x%7 == 0]
```
<br>

运行速度：      
```
CPU times: user 19.7 ms, sys: 1.03 ms, total: 20.7 ms
Wall time: 21.5 ms
```

<br><br>

###### 三、使用 filter 生成列表
```python
%%time
result = filter(lambda x:x%7==0,range(1,1000000,3))
```
<br>

运行结果：     
```
CPU times: user 4 µs, sys: 0 ns, total: 4 µs
Wall time: 7.87 µs
```