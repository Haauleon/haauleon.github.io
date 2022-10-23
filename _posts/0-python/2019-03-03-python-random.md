---
layout:        post
title:         "Python3 | 随机数模块 random"
subtitle:      "列举了使用 random 模块的所有的场景"
date:          2017-11-09
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
---




## random 随机数模块

|  方法   |  说明   |
| --- | --- |
|  random.random()   |  生成一个0到1的随机符点数   |
| random.uniform(a, b)  |  生成一个指定范围内的随机浮点数 |
| random.randint(a, b) |  生成一个指定范围内的随机整形数|
|  random.randrange(\[start\], stop\[, step\])  |  从一个按指定基数递增的序列中随机选取一个数 |
|  random.choice(sequence)  |  从指定序列中随机获取一个元素 |
| random.shuffle(x[, random]) | 打乱指定列表的元素|
| random.sample(sequence, k) | 从指定序列中随机获取指定长度的切片|

<br><br>

###### random.random
描述: 生成一个范围在`[0, 1]`的随机浮点数。                    

语法: `random.random()`         

参数:                      
* 无                   

返回值: 返回一个 0 到 1 的随机符点数。                       

<br>

实例:                    
```
>>> import random
>>> random.random()
0.1456303839809635
>>> print("{:.2f}".format(random.random()))
0.76
```
<br><br>

###### random.uniform
描述: 生成一个指定范围`[a, b]`内的随机符点数。                  

语法: `random.uniform(a, b)`                 

参数:                       
* a — 浮点数的下／上限
* b — 浮点数的上／下限                      

返回值: 返回一个指定范围`[a, b]`内的随机符点数。                    

<br>

**实例**
```
>>> import random
>>> # a < b
>>> random.uniform(5, 8)
7.2870590618030935
>>> # a > b
>>> random.uniform(8, 5)
7.03271135071411
>>> # a == b
>>> random.uniform(5, 5)
5.0
>>> print("{:.2f}".format(random.uniform(5, 8)))
6.53
```
<br><br>

###### random.randint
描述: 生成一个指定范围`[a, b]`内的随机整形数。                        

语法: `random.randint(a, b)`                

参数:                            
* a — 整形数的下限
* b — 整形数的上限（b >= a，否则抛出异常）                      

返回值: 返回一个指定范围`[a, b]`内的随机整形数。                        

<br>

实例:                          
```
>>> import random
>>> # a < b
>>> random.randint(10, 20)
19
>>> # a == b
>>> random.randint(10, 10)
10
>>> # a > b 抛出异常
>>> random.randint(20, 10)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    random.randint(20, 10)
  File "C:\python37\lib\random.py", line 222, in randint
    return self.randrange(a, b+1)
  File "C:\python37\lib\random.py", line 200, in randrange
    raise ValueError("empty range for randrange() (%d,%d, %d)" % (istart, istop, width))
ValueError: empty range for randrange() (20,11, -9)
```
<br><br>

###### random.randrange
描述: 根据步长在指定范围的整形数序列中获取一个随机元素。                     

语法: `random.randrange([start], stop[, step])`                      

参数:                
* start — 序列的开始值，可选填。默认为0
* stop — 序列的结束值，必输项
* step — 步长，可选填。默认为1                       

返回值: 返回列表的一个随机元素。                      

<br>

实例:                        
```
>>> import random
>>> # 范围在 [1, 5) ，步长为2。即从序列 [1, 3] 中随机获取一个元素
>>> random.randrange(1, 5, 2)
3
>>> # 范围在 [1, 5) ，步长为1。即从序列 [1, 2, 3, 4] 中随机获取一个元素
>>> random.randrange(1, 5)
1
>>> # 范围在 [0, 5) ，步长为2。即从序列 [0, 1, 2, 3, 4] 中随机获取一个元素
>>> random.randrange(5)
2
```
<br><br>

###### random.choice
描述: 从序列中获取一个随机元素。                  

语法: `random.choice(sequence)`                           
 
参数:                         
* sequence — 序列                    

返回值: 返回序列的一个随机元素。                         

<br>

实例:                             
```
>>> import random
>>> # 获取列表的一个随机元素
>>> random.choice(["可爱的", "迷人的", "温柔的"])
'迷人的'
>>> random.choice(range(1, 10))
4
>>> # 获取字符串的一个随机字符
>>> random.choice("可爱的迷人的温柔的")
'人'
>>> # 获取元组的一个随机元素
>>> random.choice(("可爱的", "迷人的", "温柔的"))
'迷人的'
```
<br><br>

###### random.shuffle
描述: 将一个列表中的元素打乱，即改变原有的列表。                       

语法: `random.shuffle(x[, random])`                       

参数:                    
* x — 列表                 

返回值: 无。                         

<br>

实例:                           
```
>>> import random
>>> daily = [1, 2, 3, 4, 5]
>>> random.shuffle(daily)
>>> daily
[1, 3, 2, 5, 4]
```
<br><br>

###### random.sample
描述: 从指定序列中随机获取指定长度的切片，不会修改原有序列。                         

语法: `random.sample(sequence, k)`                       

参数:                       
* sequence — 序列
* k — 切片的长度                 

返回值: 返回一个新的随机的切片序列。                         

<br>

实例:                             
```
>>> import random
>>> daily = [1, 2, 3, 4, 5]
>>> random.sample(daily, 3)
[4, 2, 3]
>>> daily
[1, 2, 3, 4, 5]
```
<br><br>

## 应用场景

###### 随机整数
```
>>> import random  
>>> random.randint(0,99)  
21
```
<br><br>

###### 随机选取0到100间的偶数    
```
>>> import random  
>>> random.randrange(0, 101, 2)  
42
```
<br><br>

###### 随机浮点数
```
>>> import random  
>>> random.random()  
0.85415370477785668  
>>> random.uniform(1, 10)  
5.4221167969800881
```
<br><br>

###### 随机字符
```
>>> import random  
>>> random.choice('abcdefg&#%^\*f')  
'd'
```
<br><br>

###### 多个字符中选取特定数量的随机字符
```
>>> import random  
>>> random.sample('abcdefghij', 3)  
['a', 'd', 'b'\]
```
<br><br>

###### 多个字符中选取特定数量的随机字符组成新字符串
```
>>> import random  
>>> import string  
>>> string.join( random.sample(\['a','b','c','d','e','f','g','h','i','j'\], 3) ).replace(" ","")  
'fih'
```
<br><br>

###### 随机选取字符串
```
>>> import random  
>>> random.choice ( \['apple', 'pear', 'peach', 'orange', 'lemon'\] )  
'lemon'
```
<br><br>

###### 洗牌
```
>>> import random  
>>> items = \[1, 2, 3, 4, 5, 6\]  
>>> random.shuffle(items)  
>>> items  
[3, 2, 5, 6, 4, 1\]
```