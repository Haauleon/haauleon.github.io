---
layout:        post
title:         "Python3 | 关键字"
subtitle:      "列举了 3.7 版本所有的关键字及其定义"
date:          2021-05-14
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - Pythoneer
---

## 背景
&emsp;&emsp;Python 的关键字也称为保留字，是这个解释器里面已经定义好了的，具有特殊的含义。解释器也是程序，如果用户自定义的变量、函数、类等名称与保留字重名，那么解释器会提醒 `SyntaxError: invalid syntax`。       

&emsp;&emsp;查看当前 Python 版本的保留字，只需要在交互模式下输入以下代码：             
```python
import keyword
keyword.kwlist
```

运行结果：           
```
['False',
 'None',
 'True',
 'and',
 'as',
 'assert',
 'async',
 'await',
 'break',
 'class',
 'continue',
 'def',
 'del',
 'elif',
 'else',
 'except',
 'finally',
 'for',
 'from',
 'global',
 'if',
 'import',
 'in',
 'is',
 'lambda',
 'nonlocal',
 'not',
 'or',
 'pass',
 'raise',
 'return',
 'try',
 'while',
 'with',
 'yield']
```

<br>

&emsp;&emsp;我目前用的还是 3.7 版本，所以以上这些关键字都是 3.7 版本提供的。          

<br><br>

## 关键字
###### False
布尔值，表示假。等同于 0，与 True 相对。         
```python
test = False
print(test)
print(bool(test))
print(bool([]))
print(type(test))
```

运行结果：        
```
False
False
False
<class 'bool'>
```

<br><br>


###### None
定义 None 值，表示根本没有值。`0`, `False`, `””` 虽然是空，但不是 None。None 表示什么都没有，只有 `None = None`。       
```python
class Test:

    def __init__(self):
        self.a = None

test = Test()
print(test.a)
test.a = "是可爱的巧伦呀"
print(test.a)
```

运行结果：         
```
None
是可爱的巧伦呀
```

<br><br>


###### True
布尔值，表示真。等同于 1，与 False 相对。            

<br><br>


###### and
用于连接 2 条语句，如果都是 True 则为 True。      
```python
a = 6
if a > 1 and a < 10: 
    print("嗯呐！")
```

运行结果：        
```
嗯呐！
```

<br><br>


###### as
创建别名。        
```python
import os as a # 导入 os 后，为 os 创建别名为 a
print(a.getcwd())
```

运行结果：         
```
/Users/haauleon/xxx/xxx/xxx/xxx
```

<br><br>


###### assert
在调试代码时使用，如果给定的条件为 True 则继续执行。如果为 False，则会引起 AssertionError。         
```python
x = []

# 如果条件返回True，则什么也不会发生：
assert x == []

#如果条件返回 False，则会引发 AssertionError：
assert bool(x) 
```

运行结果：       
```
AssertionError                            Traceback (most recent call last)
~/xxx/xxx/xxx/xxx/test.py in <module>
      5 
      6 #如果条件返回 False，则会引发 AssertionError：
----> 7 assert bool(x)

AssertionError: 
```

<br><br>


###### async
被 async 修饰的函数或方法则被作为一个协程。        

<br><br>

###### await
被 await 修饰的语句作为一个异步操作。       

<br><br>


###### break
跳出当前的循环体。       
```python
for i in range(1,10):
    if i == 5:
        break # 从4之后的都不输出
    print(i)
```

运行结果：       
```
1
2
3
4
```

<br><br>


###### class
定义一个类。         
```python
class Test:

    def __init__(self):
        self.a = 1

test = Test()
print(test.a)
```

运行结果：          
```
1
```

<br><br>


###### continue
不执行循环剩余代码，直接跳循环的末尾语句。        
```python
for i in range(1, 10):
    if i == 5:
        continue # 不输出5
    print(i)
```

运行结果：          
```
1
2
3
4
6
7
8
9
```

<br><br>


###### def
定义一个函数。          
```python
def add(x, y):
    return x + y

print(add(3, 4))
```

运行结果：        
```
7
```

<br><br>


###### del
解除一个对象的定义，可以是类、变量、函数。             
```python
class Test:
     def __init__(self):
         self.a = 1

test = Test()
print(test.a)

del test
print(test.a)
```

运行结果：         
```
1
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
~/xxx/xxx/xxx/xxx/test.py in <module>
      7 
      8 del test
----> 9 print(test.a)

NameError: name 'test' is not defined
```

<br><br>


###### elif
对于 if 不满足的条件，可以做进一步判断。          

<br><br>

###### else
对于 if 和 elif 都不满足的条件进行执行。           

<br><br>

###### except
try 语句中遇到异常就执行 except。      
```python
try:
    print("1")
    raise Exception("异常")
    print("3")
except Exception as e:
    print("4", e)
    print("5")
print("6")
```

运行结果：        
```
1
4 异常
5
6
```

<br><br>


###### finally
`try-except` 代码段无论是否有异常，都会执行 finally。         
```python
try:
    print("1")
    raise Exception("异常")
    print("3")
except Exception as e:
    print("4", e)
    print("5")
finally:
    print("6")
print("7")
```

运行结果：         
```
1
4 异常
5
6
7
```

<br><br>


###### for
循环。       
```python
for i in range(5):
    print(i)
```

运行结果：        
```
0
1
2
3
4
```

<br><br>


###### from
从一个模块中导入特定的部分。                    
```python
from time import sleep
```

<br><br>


###### global
定义一个全局变量，可以在函数中定义。             
```python
def func():
    global a 
    a = 1

print(a)
```

运行结果：          
```
1
```

<br><br>


###### if
判断一个条件，成立则继续执行，不成立则跳到 elif 或 else 中。          

<br><br>


###### import
导入模块。        
```python
import time
```

<br><br>


###### in
```python
a = [1, 2, 3, 4, 5]
print(1 in a)
print(6 in a)
```

运行结果：         
```
True
False
```

<br><br>

###### is
测试两个变量是否引用同一对象。注意，判断的是两个变量引用同一个对象。如果只是值相同，则返回 False。               
```python
a = ["a","b","c"]
c = ["a","b","c"]
b = a
print(a is b) 
print(c is a)
print(c is b) 
```

运行结果：         
```
True
False
False
```

<br><br>


###### lambda
用于创建一个小型的行内匿名函数。      
```python
func = lambda x: x+1
print(func(4))
```

运行结果：         
```
5
```

<br><br>


###### nonlocal
在嵌套函数内部使用，表示当前的变量是上一层函数的。            
```python
def func1():
    a = 10
    def func2():
        nonlocal a # 如果不加 nonlocal，a 就会变为这个函数的局部变量
        a = 9
    func2()
    return a

def func3():
    b = 5
    def func4():
        b = 6
    func4()
    return b

print(func1())
print(func3)
```

运行结果：        
```
9
5
```

<br><br>


###### not
取反。如果为 False 则返回 True。         
```python
print(not True)
print(not 0)
print(not "a")
```

运行结果：        
```
False
True
False
```

<br><br>


###### or
用于连接 2 条语句，如果有一个为 True 则为 True。           
```python
a = 6
if a > 1 or a == 8: 
    print("嗯呐！")
```

运行结果：       
```
嗯呐！
```

<br><br>


###### pass
占位符，防止语法检查报错。          
```python
class Test:
    def func(self):
        pass

test = Test()
test.func()
```

运行结果：         
```

```

<br><br>


###### raise
用于引发一个错误。       
```python
if True:
    raise Exception("发生了一个异常")
```

运行结果：         
```
Exception                                 Traceback (most recent call last)
~/xxx/xxx/xxx/xxx/test.py in <module>
      1 if True:
----> 2     raise Exception("发生了一个异常")

Exception: 发生了一个异常
```

<br><br>


###### return
返回。表示当前函数执行完毕，return 下一行的代码会被忽略。           
```python
def func():
    print(1)
    print(2)
    return 3
    print(4) 

func()
```

运行结果：       
```
1
2
3
```

<br><br>


###### try
try 代码段一定先执行第一行语句，直到遇到异常。                          
```python
try:
    print("1")
```

运行结果：        
```
1
```

<br><br>


###### while
循环。         
```python
count = 3
while count:
    print("嘿嘿")
    count -= 1
print(count)
```

运行结果：         
```
嘿嘿
嘿嘿
嘿嘿
0
```

<br><br>


###### with
用于简化错误处理，即简化：`try-except-finlally`。                   
```python
with open("test.txt") as f:
    ff = f.read()
```

<br><br>


###### yield
生成器。被修饰的函数或者方法即作为一个生成器。