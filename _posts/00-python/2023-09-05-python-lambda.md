---
layout:        post
title:         "Python3 | 高阶函数的基本使用方法"
subtitle:      "Python 最频繁使用的 4 个函数：lambda、 map、filter 和 reduce"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 一、Lambda 函数简介
&emsp;&emsp;Lambda 函数也被称为<mark>匿名(没有名称)函数</mark>，它直接接受参数的数量以及使用该参数执行的条件或操作，该参数以冒号分隔，并返回最终结果。为了在大型代码库上编写代码时执行一项小任务，或者在函数中执行一项小任务，便在正常过程中使用 lambda 函数。         
```text
lambda argument_list:expersion
```

1、`​​argument_list`​​​ 是参数列表，它的结构与​​ Python​​​ 中函数(​​function​​)的参数列表是一样的              
```text
a, b
a = 1, b = 2
*args
**kwargs
a, b = 1, *args
空
....
```

2、`​​expression`​​​ 是一个关于参数的表达式，表达式中出现的参数需要在​​ argument_list​​ 中有定义，并且表达式只能是单行的                
```text
1
None
a + b
sum(a)
a if a is not None else 'NULL'
[i for i in range(10)]
...
```

<br>
<br>

### 二、普通函数和Lambda函数的区别
1、没有名称         
Lambda 函数没有名称，而普通操作有一个合适的名称。             

2、Lambda 函数没有返回值            
使用​​ `def​​` 关键字构建的普通函数返回值或序列数据类型，但在 Lambda 函数中返回一个完整的过程。假设我们想要检查数字是偶数还是奇数，使用 lambda 函数语法类似于下面的代码片段。           
```python
b = lambda x: "Even" if x%2==0 else "Odd"
print(b(9))  # Odd
```

3、函数只在一行中          
Lambda 函数只在一行中编写和创建，而在普通函数的中使用缩进            

4、不用于代码重用           
Lambda 函数不能用于代码重用，或者不能在任何其他文件中导入这个函数。相反，普通函数用于代码重用，可以在外部文件中使用。                

<br>
<br>

### 三、为什么要使用Lambda函数?
&emsp;&emsp;一般情况下，我们不使用 Lambda 函数，而是<mark>将其与高阶函数一起使用</mark>。高阶函数是一种需要多个函数来完成任务的函数，或者当一个函数返回任何另一个函数时，可以选择使用 Lambda 函数。          

<br>
<br>

### 四、什么是高阶函数?
通过一个例子来理解高阶函数。假设有一个整数列表，必须返回三个输出。                
1、一个列表中所有偶数的和                
2、一个列表中所有奇数的和             
3、一个所有能被三整除的数的和                

&emsp;&emsp;首先假设用普通函数来处理这个问题。在这种情况下，将声明三个不同的变量来存储各个任务，并使用一个 `for` 循环处理并返回结果三个变量。该方法常规可正常运行。             
&emsp;&emsp;现在使用 Lambda 函数来解决这个问题，那么可以用三个不同的 Lambda 函数来检查一个待检验数是否是偶数，奇数，还是能被三整除，然后在结果中加上一个数。                  
```python
def return_sum(func, lst):
    result = 0
    for i in lst:
        if func(i):
            result = result + i
    return result


lst = [11, 14, 21, 56, 78, 45, 29, 28]
x = lambda a: a%2 == 0
y = lambda a: a%2 != 0
z = lambda a: a%3 == 0
print(return_sum(x, lst))  # 176
print(return_sum(y, lst))  # 106
print(return_sum(z, lst))  # 144
```

&emsp;&emsp;这里创建了一个高阶函数，其中将 Lambda 函数作为一个部分传递给普通函数。其实这种类型的代码在互联网上随处可见。然而很多人在使用 Python 时都会忽略这个函数，或者只是偶尔使用它，但其实这些函数真的非常方便，同时也可以节省更多的代码行。接下来我们一起看看这些高阶函数。               

<br>
<br>

### 五、Python内置高阶函数
#### 1、Map函数
`map()` 会根据提供的函数对指定序列做映射。          

&emsp;&emsp;Map 函数是一个接受两个参数的函数。第一个参数 function 以参数序列中的每一个元素调用 function 函数，第二个是任何可迭代的序列数据类型。返回包含每次 function 函数返回值的新列表。             
```text
map(function, iterable, ...)
```

&emsp;&emsp;Map 函数将定义在迭代器对象中的某种类型的操作。假设我们要将数组元素进行平方运算，即将一个数组的每个元素的平方映射到另一个产生所需结果的数组。               
```python
arr = [2,4,6,8]
arr = list(map(lambda x: x*x, arr))
print(arr)  # [4, 16, 36, 64]
```

&emsp;&emsp;我们可以以不同的方式使用 Map 函数。假设有一个包含名称、地址等详细信息的字典列表，目标是生成一个包含所有名称的新列表。                 
```python
students = [
    {
        "name": "John Doe",
        "father name": "Robert Doe",
        "Address": "123 Hall street"
    },
    {
        "name": "Rahul Garg",
        "father name": "Kamal Garg",
        "Address": "3-Upper-Street corner"
    },
    {
        "name": "Angela Steven",
        "father name": "Jabob steven",
        "Address": "Unknown"
    }
]

print(list(map(lambda student: student['name'], students)))
# ['John Doe', 'Rahul Garg', 'Angela Steven']
```

上述操作通常出现在从数据库或网络抓取获取数据等场景中。          

<br>
<br>

#### 2、Filter函数
&emsp;&emsp;Filter 函数根据给定的特定条件过滤掉数据。即在函数中设定过滤条件，迭代元素，保留返回值为 True 的元素。Map 函数对每个元素进行操作，而 filter 函数仅输出满足特定要求的元素。              

假设有一个水果名称列表，任务是只输出那些名称中包含字符 ​​`'g'` ​​的名称。           
```python
fruits = ['mango', 'apple', 'orange', 'cherry', 'grapes']
print(list(filter(lambda fruit: 'g' in fruit, fruits)))
# ['mango', 'orange', 'grapes']
```

返回一个迭代器，为那些函数或项为真的可迭代项。如果函数为 None，则返回为真的项。            
```text
filter(function or None, iterable) --> filter object
```

<br>
<br>

#### 3、Reduce函数
&emsp;&emsp;这个函数比较特别，不是 Python 的内置函数，需要通过​​ `from functools import reduce`​​ 导入。Reduce 从序列数据结构返回单个输出值，它通过应用一个给定的函数来减少元素。           
```text
reduce(function, sequence[, initial]) -> value
```

&emsp;&emsp;将包含两个参数的函数(​​function​​​)累计应用于序列(​​sequence​​​)的项，从左到右，从而将序列 ​​reduce​​ 至单个值。如果存在 ​​initial​​，则将其放在项目之前的序列，并作为默认值时序列是空的。      

假设有一个整数列表，并求得所有元素的总和。且使用 reduce 函数而不是使用 `for` 循环来处理此问题。            
```python
from functools import reduce
lst = [2,4,6,8,10]
print(reduce(lambda x, y: x+y, lst))  # 30
```

还可以使用 reduce 函数而不是for循环从列表中找到最大或最小的元素。             
```python
from functools import reduce

lst = [2,4,6,8]
# 找到最大元素
print(reduce(lambda x, y: x if x>y else y, lst))  # 8
# 找到最小元素
print(reduce(lambda x, y: x if x<y else y, lst))  # 2
```

<br>
<br>

### 六、高阶函数的替代方法
#### 1、列表推导式
&emsp;&emsp;其实列表推导式只是一个 for 循环，用于添加新列表中的每一项，以从现有索引或一组元素创建一个新列表。之前使用 map、filter 和 reduce 完成的工作也可以使用列表推导式完成。然而，相比于使用 Map 和 filter 函数，很多人更喜欢使用列表推导式，也许是因为它更容易应用和记忆。            

&emsp;&emsp;同样使用列表推导式将数组中每个元素进行平方运算，水果的例子也可以使用列表推导式来解决。              
```python
arr = [2,4,6,8]
arr = [i**2 for i in arr]
print(arr)  # [4, 16, 36, 64]

fruits = ['mango', 'apple', 'orange', 'cherry', 'grapes']
fruit_result = [fruit for fruit in fruits if 'g' in fruit]
print(fruit_result)  # ['mango', 'orange', 'grapes']
```

<br>
<br>

#### 2、字典推导式
&emsp;&emsp;与列表推导式一样，使用字典推导式从现有的字典创建一个新字典。还可以从列表创建字典。           

&emsp;&emsp;假设有一个整数列表，需要创建一个字典，其中键是列表中的每个元素，值是列表中的每个元素的平方。                
```python
lst = [2,4,6,8]
D1 = {item:item**2 for item in lst}
print(D1)  # {2: 4, 4: 16, 6: 36, 8: 64}

# 创建一个只包含奇数元素的字典
arr = [1,2,3,4,5,6,7,8]
D2 = {item: item**2 for item in arr if item %2 != 0}
print(D2)  # {1: 1, 3: 9, 5: 25, 7: 49}
```

<br>
<br>

### 七、一个简单应用
#### 如何快速找到多个字典的公共键
（1）方法一           
```python
dl = [d1, d2, d3] # d1, d2, d3为字典，目标找到所有字典的公共键
[k for k in dl[0] if all(map(lambda d: k in d, dl[1:]))]
```

例           
```python
dl = [{1:'life', 2: 'is'}, 
      {1:'short', 3: 'i'}, 
      {1: 'use', 4: 'python'}]
[k for k in dl[0] if all(map(lambda d: k in d, dl[1:]))]
# 1
```

解析         
```python
# 列表表达式遍历dl中第一个字典中的键
[k for k in dl[0]]
# [1, 2]

# lambda 匿名函数判断字典中的键，即k值是否在其余字典中
list(map(lambda d: 1 in d, dl[1:]))
# [True, True]
list(map(lambda d: 2 in d, dl[1:]))
#[False, False]

# 列表表达式条件为上述结果([True, True])全为True,则输出对应的k值
#1
```

<br>
<br>

（2）方法二             
```python
# 利用集合（set）的交集操作
from functools import reduce
# reduce(lambda a, b: a*b, range(1,11)) # 10!
reduce(lambda a, b: a & b, map(dict.keys, dl))
```

<br>
<br>

---

相关链接：    
[Python 最频繁使用的4个函数：lambda、 map、filter 和 reduce](https://blog.51cto.com/u_11215354/5220481)                
[lambda的应用：做加法计算，做判断功能，做字典排序](https://blog.csdn.net/qq_56680511/article/details/125463220)