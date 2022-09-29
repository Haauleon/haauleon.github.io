---
layout:        post
title:         "Python3 | 函数式编程"
subtitle:      "map、filter 的使用"
date:          2021-05-13
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - Pythoneer
---

## 背景
&emsp;&emsp;在 Python 的函数式编程中的 map() 和 filter() 函数，均可用 for 循环来实现，那么为什么还需要 map() 和 filter() 函数呢？主要是因为 Python 的 for 命令效率不高且复杂，而 map() 和 filter() 更为高效和简洁，map() 和 filter() 的循环速度比 Python 内置的 for 或 while 循环要快得多，其执行速度相当于 C 语言。       

<br>

```python
%%time
# 使用 for 循环
def demo_for():
    x = [x for x in range(100000)]
    y = [y for y in range(100000)]
    result = []
    for i in range(100000):
        result.append(x[i] + y[i])
    return result
    
demo_for()
```

运行结果：       
```
CPU times: user 23.3 ms, sys: 4.29 ms, total: 27.5 ms
Wall time: 28 ms
[0,
 2,
 ...]
```

<br><br>

```python
%%time
# 使用 map 函数
def demo_map():
    a = map(lambda x, y: x + y, range(100000), range(100000))
    return list(a)

demo_map()
```

运行结果：           
```
CPU times: user 12.9 ms, sys: 1.09 ms, total: 14 ms
Wall time: 15 ms
[0,
 2,
 ...]
```

<br>

&emsp;&emsp;在以上的十万个元素的对比计算中，demo_map 的执行效率比 demo_for 的高出差不多 2 倍。      

<br><br>


## python 函数式编程
&emsp;&emsp;python 中的 map() 和 filter() 函数均是应用于序列的内置函数，分别对序列进行遍历和过滤操作，这两个内置函数在实际使用过程中经常跟 lambda 关键字联合使用。        

<br>

###### 一、lambda 函数
lambda 的 Python3.x API文档       
> lambda       
> An anonymous inline function consisting of a single expression which is evaluated when the function is called. The syntax to create a lambda function is lambda [arguments]: expression

<br>

由文档可知，lambda 函数是匿名行内函数，其语法为 `lambda [arguments]: expression`，比如：          
```python
f = lambda x, y : x * y #定义了函数f(x, y) = x * y
```   

其非匿名函数表达如下：         
```python
def f(x, y):
    return x * y
```

<br><br>


###### 二、map 函数
map() 函数的 Python3.x API文档            
> map(function, iterable, ...)         
> Return an iterator that applies function to every item of iterable, yielding the results. If additional iterable arguments are passed, function must take that many arguments and is applied to the items from all iterables in parallel. With multiple iterables, the iterator stops when the shortest iterable is exhausted. For cases where the function inputs are already arranged into argument tuples, see itertools.starmap().

<br>

&emsp;&emsp;map() 函数的输入是一个函数 function 以及一个或多个可迭代的集合 iterable，在 Python 2.x 中 map() 函数的输出是一个集合，Python 3.x 中 输出的是一个迭代器。map() 函数主要功能为对 iterable中 的每个元素都进行 function 函数操作，并将所有的返回结果放到集合或迭代器中。function 如果是 None，则其作用等同于 zip()。           
```python
%%time
a = map(lambda x,y : x * y, [1,2,3], [4,6])
b = list(a)
print(b)
```

运行结果：           
```
[4, 12]
CPU times: user 127 µs, sys: 67 µs, total: 194 µs
Wall time: 161 µs
```

<br><br>


###### 三、filter 函数
filter() 函数的 Python3.x API文档              
> filter(function, iterable)               
> Construct an iterator from those elements of iterable for which function returns true. iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed. Note that filter(function, iterable) is equivalent to the generator expression (item for item in iterable if function(item)) if function is not Noneand (item for item in iterable if item) if function is None.              
> See itertools.filterfalse() for the complementary function that returns elements of iterable for which function returns false.   

<br>

&emsp;&emsp;filter() 函数的输入为一个函数 function 和一个可迭代的集合 iterable，在 Python 2.x 中 filter() 函数的输出是一个集合，Python 3.x 中输出的是一个 filter 类。顾名思义，filter() 函数主要是对指定可迭代集合进行过滤，筛选出集合中符合条件的元素。比如：                
```python
%%time
a = filter(lambda x: 3 < x < 6, range(10))
print(a)
b = list(a)
print(b)
```

运行结果：         
```
<filter object at 0x7fdab10bdfd0>
[4, 5]
CPU times: user 274 µs, sys: 212 µs, total: 486 µs
Wall time: 392 µs
```