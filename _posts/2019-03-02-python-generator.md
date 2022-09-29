---
layout:        post
title:         "Python3 | 生成器 generator"
subtitle:      "如何使用生成器中的 yield 关键字？"
date:          2017-11-07
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
---

## 生成列表的方式
###### 方式一 普通的方式
```python
gen = []
for i in range(1, 6):
    if i >= 3:
        gen.append(i)
print(gen) # [3, 4, 5]
```

<br><br>

###### 方式二 列表推导式
```python
gen = [i for i in range(1, 6) if i >=3]
print(gen) # [3, 4, 5]
```

<br><br>

## 理解生成器中
###### 一、yield 关键字的作用
&emsp;&emsp;生成器中的 yield 关键字能把一个函数变成一个生成器 generator ，与 return 不同，yield 在函数中返回值的时会保存函数的状态，使下一次调用函数时会从 yield 的下一条语句处开始执行。若要获得下一个值，仅需要调用 next() 方法即可。生成器 generator 总是生成值，一般是迭代的序列。

```python
def gen():
    # 函数中只要出现 yield 关键字，则这个函数就变成一个生成器 generator
    yield i

print(type(gen())) # <class 'generator'>
g = gen()
print(type(g)) # <class 'generator'>
```
<br><br>

###### 二、使用 yield 关键字的好处
&emsp;&emsp;想要生成一个列表，假如这个列表的存储空间很大，而又只想访问列表前几个元素，那个 yield 这个关键字就能实现一边循环一边计算的机制，节省存储空间又提高运行效率。

<br><br>

## 生产者和消费者的问题
###### 一、需求描述
&emsp;&emsp;现在我们要让生产者发送 1, 2, 3, 4, 5 给消费者，消费者接受数字同时返回状态给生产者，而消费者只需要 3, 4, 5 就行了，所以当数字等于 3 时将返回一个错误的状态。最终我们需要由主程序来监控生产者-消费者的过程状态，调度结束程序。 

<br><br>

###### 二、不使用生成器
```python
def consumer(producer):
    return [status for status in producer if status >=3]

def producer():
    return [n for n in range(1, 6)]

if __name__ == '__main__':
    p = producer()
    c = consumer(p)
    print(c) # [3, 4, 5]
```

分析：这样的做法很简单，但是弊端也很明显。我每一次去调用 producer() 和 consumer() 这两个函数时，都要耗费大量时间去循环做重复的事情。并且无法通过主程序来监控生产者-消费者的过程状态。
<br><br>

###### 三、使用生成器
```python
def consumer():
    status = True
    while True:
        # 将 status 返回给调度它的主程序
        n = yield status
        print("拿到了{}!".format(n))
        if n == 3:
            status = False

def producer(consumer):
    n = 5
    while n > 0:
        yield consumer.send(n)
        n -= 1

if __name__ == '__main__':
    c = consumer()
    # print(type(c)) # <class 'generator'>
    # print("c = {}".format(c)) # c = <generator object consumer at 0x7fa6a7694c50>
    c.send(None) 
    p = producer(c) # 传入了消费者的生成器，让 producer 跟 consumer 进行通信
    for status in p:
        if status == False:
            print("我只要3,4,5就行啦")
            break
    print("程序结束")
```
<br>

运行结果：                         
```
我拿到了5!
我拿到了4!
我拿到了3!
我只要3,4,5就行啦
程序结束
```
<br>

分析：                          
从主程序 `if __name__ == '__main__': ` 开始看：                             
```python
if __name__ == '__main__':
    c = consumer()
    c.send(None) 
    p = producer(c) 
    for status in p:
        if status == False:
            print("我只要3,4,5就行啦")
            break
    print("程序结束")
```
<br>

&emsp;&emsp;第一条语句 `c = consumer()`，因为 consumer 函数中存在 yield 关键字，python 会把它当成一个生成器 generator。因此在运行这条语句后，python 并不会像执行函数一样，而是返回了一个 generator object。即语句` print("c = {}".format(c)) ` 的执行结果是 ` c = <generator object consumer at 0x7fa6a7694c50>`。                                
<br>

&emsp;&emsp;第二条语句 `c.send(None)`，这条语句的作用是将生成器 consumer 中的语句推进到第一个 yield 语句出现的位置即 `yield status`。在 consumer 中，`status = True` 和 `while True:` 都已经被执行了，此时程序停留在n = yield status的位置（注意：此时这条语句还没有被执行）。                          
<br>

&emsp;&emsp;第三条语句 `c.send(None)`，漏写这一句，程序直接报错 `TypeError: can't send non-None value to a just-started generator`。               
<br>

&emsp;&emsp;第四条语句 `p = producer(c)`，producer 也是一个生成器，所以 p 是一个生成器对象。这里传入了消费者生成器consumer ，以此来让生产者 producer 和消费者 consumer 进行通信。                       
<br>

&emsp;&emsp;第五条语句 `for status in p:`，这条语句会循环地运行 producer 和获取它 yield 回来的消费者状态 status。                    
<br><br>

```python
def consumer():
    status = True
    while True:
        n = yield status
        print("拿到了{}!".format(n))
        if n == 3:
            status = False

def producer(consumer):
    n = 5
    while n > 0:
        yield consumer.send(n)
        n -= 1
```
<br>

分析 ：producer 中的语句 `yield consumer.send(n)`                                     
&emsp;&emsp;生产者 producer 调用 `consumer.send(n)`，把 n 的值发送给 consumer。在 consumer 的语句 `n = yield status` 中， n 拿到的是 producer 发送的数字，同时返回 consumser 中用 yield 的变量 status 给 producer，然后 producer 马上将 status 返回给调度它的主程序，主程序 `for status in p:`获取 status 的值，判断若为 false 则终止循环，结束程序。

<br><br>

###### 四、generator.send(args)
&emsp;&emsp;`generator.send(n)` 的作用是：将 args 发送到生成器 generator 中的 yield 关键字处，同时返回 generator 中 yield 的变量（结果）。

