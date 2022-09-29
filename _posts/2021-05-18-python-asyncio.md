---
layout:        post
title:         "Python3 | asyncio 的应用"
subtitle:      "asyncio 的使用方式和使用场景是什么？"
date:          2021-05-18
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - Pythoneer
---

## asyncio
asyncio 官方文档说明：            

> asyncio is a library to write concurrent code using the async/await syntax.           

> asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.        

&emsp;&emsp;asyncio 是一个使用 async / await 语法编写并发代码的库。用作多个 Python 异步框架的基础，这些框架提供了高性能的网络和 Web 服务器，数据库连接库，分布式任务队列等。             

<br><br>

## 使用场景
###### 一、分布式任务队列       
python 的协程:
1. Python 对协程的支持是通过 generator 实现的。                  
2. 协程是由程序自身控制的程序间的切换。             

<br>

asyncio 协程库:
1. 通过 async 关键字定义一个协程（coroutine），协程也是一种对象。协程不能直接运行，需要把协程加入到事件循环（loop）。              
2. 所谓 task 对象是 Future 类的子类。保存了协程运行后的状态，用于未来获取协程的结果。                    
3. future： 代表将来执行或没有执行的任务的结果。它和 task 上没有本质的区别。             
4. async/await async 定义一个协程，await 用于挂起阻塞的异步调用接口。              
5. aiohttp 异步 web 请求库。               
6. aiomysql 异步数据库连接库。               
 
```python
import asyncio
import time
import aiohttp

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    async with aiohttp.ClientSession() as session:
        async with session.get('http://www.baidu.com') as resp:
            print(resp.status)
    return 'Done after {}s'.format(x)

async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        # 创建 task 的另一种方式!
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    # as_completed 返回一个迭代对象
    for task in asyncio.as_completed(tasks):
        # await 表明 如果遇到阻塞就切换其他的 task
        result = await task
        print('Task ret: {}'.format(result))

def callback(t, future):
    print(t)
start = now()

# 开启一个无限的循环，程序员会把一些函数注册到事件循环上。
# 当满足事件发生的时候(本次是遇到阻塞)，调用相应的协程函数
loop = asyncio.get_event_loop()

# 将协程变成 task
task = loop.create_task(main())
# 获取 task 状态
print(task.result)

import functools
# 偏函数注册回调参数!
task.add_done_callback(functools.partial(callback, 2))
# task 注册到 循环之中
loop.run_until_complete(task)

# 将协程函数注册到循环之中(一步到达),等于前两步骤
# loop.run_until_complete(main())
print('TIME: ', now() - start) # 是同步的 1/3 时间消耗
```

运行结果：         
```
<built-in method result of _asyncio.Task object at 0x7ff994c2c9f0>
Waiting:  1
Waiting:  2
Waiting:  4
200
Task ret: Done after 2s
200
Task ret: Done after 4s
200
Task ret: Done after 1s
2
TIME:  0.0722041130065918
```

<br><br>

###### 二、数据库连接库
异步操作 mysql 连接: asyncio + sqlalchemy              
1. 创建一个全局的连接池，每个HTTP请求都可以从连接池中直接获取数据库连接。                
2. 使用连接池的好处是不必频繁地打开和关闭数据库连接。                   

```python
import aiomysql
import asyncio

async def select(loop, sql, pool):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql)
            r = await cur.fetchone()
            print(r)

async def insert(loop, sql, pool):
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(sql)
            await conn.commit()

async def main(loop):
    pool = await aiomysql.create_pool(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        password = '123456',
        db = 'test',
        loop = loop)
    c1 = select(loop=loop, sql='select * from minifw limit 1', pool=pool)
    c2 = insert(loop=loop, sql="insert into minifw (name) values ('hello')", pool=pool)

    tasks = [asyncio.ensure_future(c1), asyncio.ensure_future(c2)]
    return await asyncio.gather(*tasks)


if __name__ == '__main__':
    cur_loop = asyncio.get_event_loop()
    cur_loop.run_until_complete(main(cur_loop))
```

<br><br>

## 使用方式
###### 一、定义协程并创建 tasks
1. 通过 async 关键字定义一个协程（coroutine）,当然协程不能直接运行，需要将协程加入到事件循环 loop 中。            
2. asyncio.get_event_loop：创建一个事件循环，然后使用 run_until_complete 将协程注册到事件循环，并启动事件循环。             
3. 协程对象不能直接运行，在注册事件循环的时候，其实是 run_until_complete 方法将协程包装成为了一个任务（task）对象。            
4. task 对象是 Future 类的子类，保存了协程运行后的状态，用于未来获取协程的结果。

<br>

定义一个协程并创建 tasks:            
```python
import asyncio
import time

# 通过 async 关键字定义一个协程，当然协程不能直接运行，需要将协程加入到事件循环 loop 中
async def do_some_work(x):
    print("waiting:", x)

start = time.time()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()        # asyncio.get_event_loop：创建一个事件循环

# 通过 loop.create_task(coroutine) 创建 task，同样的可以通过 asyncio.ensure_future(coroutine) 创建 task
task = loop.create_task(coroutine)     # 创建任务, 不立即执行
loop.run_until_complete(task)          # 使用run_until_complete将协程注册到事件循环，并启动事件循环
print("Time:",time.time() - start)
```

运行结果：          
```
waiting: 2
Time: 0.00032591819763183594
```

<br><br>

###### 二、绑定回调
&emsp;&emsp;绑定回调。在 task 执行完成的时候可以获取执行的结果，回调的最后一个参数是 future 对象，通过该对象可以获取协程返回值。           

asyncio 绑定回调:        
```python
import asyncio
import time

# 通过async关键字定义一个协程,当然协程不能直接运行，需要将协程加入到事件循环loop中
async def do_some_work(x):
    print("waiting:", x)
    return "Done after {}s".format(x)

def callback(future):
    print("callback:",future.result())

start = time.time()

coroutine = do_some_work(2)
loop = asyncio.get_event_loop()        # asyncio.get_event_loop：创建一个事件循环

# 通过 loop.create_task(coroutine) 创建 task，同样的可以通过 asyncio.ensure_future(coroutine) 创建 task
task = loop.create_task(coroutine)     # 创建任务, 不立即执行
# task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)

# 绑定回调，在task执行完成的时候可以获取执行的结果
loop.run_until_complete(task)          # 使用 run_until_complete 将协程注册到事件循环，并启动事件循环
print("Time:",time.time() - start)
```

运行结果：         
```
waiting: 2
callback: Done after 2s
Time: 0.00039696693420410156
```

<br><br>

###### 三、阻塞和 await
1. 使用 async 可以定义协程对象，使用 await 可以针对耗时的操作进行挂起，就像生成器里的 yield 一样，函数让出控制权。               
2. 协程遇到 await，事件循环将会挂起该协程，执行别的协程，直到其他的协程也挂起或者执行完毕，再进行下一个协程的执行。          
3. 耗时的操作一般是一些 IO 操作，例如网络请求，文件读取等。             
4. 使用 asyncio.sleep 函数来模拟 IO 操作。协程的目的也是让这些 IO 操作异步化。          

<br>

（1）普通串行花费 7 秒:          
```python
import time

def do_some_work(t):
    time.sleep(t)
    print('用了%s秒' %t)

start = time.time()
coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)
print(time.time()-start)
```

运行结果：        
```
用了1秒
用了2秒
用了4秒
7.004793882369995
```

<br>

（2）使用协程并发执行只花费 4 秒:             
```python
import asyncio
import time

async def do_some_work(x):
    print("Waiting:",x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)

start = time.time()

coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print("Task ret:",task.result())

print("Time:",time.time() - start)
```

运行结果：            
```
Waiting: 1
Waiting: 2
Waiting: 4
Task ret: Done after 1s
Task ret: Done after 2s
Task ret: Done after 4s
Time: 4.0017218589782715
```

<br><br>

###### 四、协程嵌套
1. 使用 async 可以定义协程，协程用于耗时的 io 操作，也可以封装更多的 io 操作过程。          
2. 嵌套的协程，即一个协程中 await 了另外一个协程，如此连接起来。           

<br>

（1）协程嵌套 -- 普通写法:           
```python
import asyncio
import time
import asyncio

async def do_some_work(x):
    print("waiting:",x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)

async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    dones, pendings = await asyncio.wait(tasks)
    for task in dones:
        print("Task ret:", task.result())

    # results = await asyncio.gather(*tasks)
    # for result in results:
    #     print("Task ret:",result)


start = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("Time:", time.time() - start)
```

运行结果：         
```
waiting: 1
waiting: 2
waiting: 4
Task ret: Done after 4s
Task ret: Done after 1s
Task ret: Done after 2s
Time: 4.003580093383789
```

<br>

（2）协程嵌套 -- 使用 asyncio.wait 方式挂起协程:            
```python
import asyncio
import time

async def do_some_work(x):
    print("waiting:",x)
    await asyncio.sleep(x)
    return "Done after {}s".format(x)

async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
    return await asyncio.wait(tasks)

start = time.time()

loop = asyncio.get_event_loop()
done,pending = loop.run_until_complete(main())
for task in done:
    print("Task ret:",task.result())

print("Time:", time.time() - start)
```

运行结果：         
```
waiting: 1
waiting: 2
waiting: 4
Task ret: Done after 4s
Task ret: Done after 1s
Task ret: Done after 2s
Time: 4.0029308795928955
```

<br>

（3）协程嵌套 -- 使用列表推导式简写:          
```python
import time
import asyncio

async def job(t):            # 使用 async 关键字将一个函数定义为协程
    await asyncio.sleep(t)   # 等待 t 秒, 期间切换执行其他任务
    print('用了%s秒' % t)

async def main(loop):           # 使用 async 关键字将一个函数定义为协程
    tasks = [loop.create_task(job(t)) for t in range(1,3)]  # 创建任务, 不立即执行
    await asyncio.wait(tasks)   # 执行并等待所有任务完成

start = time.time()
loop = asyncio.get_event_loop()      # 创建一个事件loop
loop.run_until_complete(main(loop))  # 将事件加入到事件循环loop
loop.close()                         # 关闭 loop

print(time.time()-start)
```

运行结果：      
```
用了1秒
用了2秒
2.0037617683410645
```