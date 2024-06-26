---
layout:        post
title:         "爬虫 | selenium 与多线程的完美结合"
subtitle:      "使用 Selenium + threading 或 Selenium + ThreadPoolExecutor 实现多线程/线程池"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 一、前言
使用 Selenium 创建多个浏览器，这在自动化操作中非常常见。而在 Python中，使用 Selenium + threading 或 Selenium + ThreadPoolExecutor 都是很好的实现方法。               

应用场景：             
1、创建多个浏览器用于测试或者数据采集                    
2、使用 Selenium 控制本地安装的 chrome 浏览器去做一些操作                
3、......          


文章提供了 Selenium + threading 和 Selenium + ThreadPoolExecutor 结合的代码模板，拿来即用。                      

<br>
<br>

### 二、知识点  
下面两个都是 Python 内置模块，无需手动安装~            

|作用|链接|
|----|---|
|<mark>threading</mark> 用于实现多线程|https://docs.python.org/zh-cn/3/library/threading.html|
|<mark>concurrent.futures.ThreadPoolExecutor</mark> 使用线程池来异步执行调用|https://docs.python.org/zh-cn/3/library/concurrent.futures.html|

<br>

#### 1、导入模块
```python
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

```

<br>
<br>

### 三、多线程还是线程池？

> 在Selenium中，使用 多线程 或者是 线程池，差别并不大。主要都是网络I/O的操作。       

在使用 `ThreadPoolExecutor` 的情况下，任务将被分配到不同的线程中执行，从而提高并发处理能力。与使用 `threading` 模块相比，使用 `ThreadPoolExecutor` 有以下优势:              
1、更高的并发处理能力：线程池 可以动态地调整线程数量，以适应任务的数量和处理要求，从而提高并发处理能力。               
2、更好的性能：线程池 可以根据任务的类型和大小动态地调整线程数量，从而提高性能和效率。                
3、......              

总之，使用<mark>线程池</mark>可以提高并发处理能力，更易于管理，并且可以提供更好的性能和效率。             
但是选择多线程，效果也不差。               
所以使用哪个都不必纠结，哪个代码量更少就选哪个自然是最好的。             

<br>
<br>

### 四、多个浏览器
Selenium 自动化中需要多个浏览器，属于是非常常见的操作了。不管是用于自动化测试、还是爬虫数据采集，这都是个可行的方法。                
这里示例的代码中，<mark>线程池的运行时候只有多线程的一半！！！</mark>                

<br>

#### 1、多线程与多浏览器

> 这份代码的应用场景会广一些，后续复用修改一下 browser_thread 函数的逻辑就可以了。       

这里模拟相对复杂的操作，在创建的浏览器中新打开一个标签页，用于访问指定的网站。然后切换到新打开的标签页，进行截图。                      

代码释义：             
（1）定义一个名为 start_browser 的函数，用于创建 webdriver.Chrome 对象。                
（2）定义一个名为 browser_thread 的函数，接受一个 webdriver.Chrome 对象和一个整数作为参数，用于打开指定网页并截图。切换到最后一个窗口，然后截图。            
（3）main 函数创建了 5 个浏览器，5 个线程，执行上面的操作，然后等待所有线程执行完毕。                  
```python
# -*- coding: utf-8 -*-
# Name:         multi_thread.py
# Author:       小菜
# Date:         2023/6/1 20:00
# Description:


import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager


def start_browser():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver


def browser_thread(driver: webdriver.Chrome, idx: int):
    url_list = ['https://www.csdn.net/', 'https://www.baidu.com',
                'https://music.163.com/', 'https://y.qq.com/', 'https://cn.vuejs.org/']

    try:
        driver.execute_script(f"window.open('{url_list[idx]}')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.save_screenshot(f'{idx}.png')
        return True
    except Exception:
        return False


def main():
    for idx in range(5):
        driver = start_browser()
        threading.Thread(target=browser_thread, args=(driver, idx)).start()

    # 等待所有线程执行完毕
    for thread in threading.enumerate():
        if thread is not threading.current_thread():
            thread.join()


if __name__ == "__main__":
    main()

```

运行结果：         
运行时长在 9.28 秒（速度与网络环境有很大关系，木桶效应，取决于最后运行完成的浏览器。看到程序运行完成后，多出了 5 张截图。                      
![](\img\in-post\post-python\2023-08-31-python-selenium-thread-1.gif)     

<br>
<br>

#### 2、线程池与多浏览器

> 这份代码与 多线程与 多浏览器 的操作基本一致。速度上却比多线程节省了一半。      


```python
# -*- coding: utf-8 -*-
# Name:         demo2.py
# Author:       小菜
# Date:         2023/6/1 20:00
# Description:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor, as_completed

MAX_WORKERS = 5
service = ChromeService(ChromeDriverManager().install())


def start_browser():
    driver = webdriver.Chrome(service=service)
    return driver


def browser_task(driver: webdriver.Chrome, idx: int):
    url_list = ['https://www.csdn.net/', 'https://www.baidu.com',
                'https://music.163.com/', 'https://y.qq.com/', 'https://cn.vuejs.org/']

    try:
        driver.execute_script(f"window.open('{url_list[idx]}')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.save_screenshot(f'{idx}.png')
        return True
    except Exception:
        return False


def main():
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    ths = list()
    for idx in range(5):
        driver = start_browser()
        th = executor.submit(browser_task, driver, idx=idx)
        ths.append(th)

    # 获取结果
    for future in as_completed(ths):
        print(future.result())


if __name__ == "__main__":
    main()

```

运行结果：                  
运行时长在 4.5 秒（运行效果图不是很匹配，但确实是比多线程快很多。看到程序运行完成后，多出了 5 张截图。               
![](\img\in-post\post-python\2023-08-31-python-selenium-thread-2.gif)     

<br>
<br>

### 五、多个标签页

> 这个的应用场景有点意思。     


这里的操作与上面的多个浏览器其实是差不多的。区别在于：上面打开多个浏览器，这里打开多个标签页。所以这个需要考量一个问题：<mark>资源争夺</mark>。于是这里用上了 `threading.Lock` 锁，用以保护资源线程安全。            

<br>

#### 1、多线程与多标签页
```python
# -*- coding: utf-8 -*-
# Name:         demo2.py
# Author:       小菜
# Date:         2023/6/1 20:00
# Description:

import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(ChromeDriverManager().install())
lock = threading.Lock()


def start_browser():
    driver = webdriver.Chrome(service=service)
    return driver


def browser_thread(driver: webdriver.Chrome, idx: int):
    url_list = ['https://www.csdn.net/', 'https://www.baidu.com',
                'https://music.163.com/', 'https://y.qq.com/', 'https://cn.vuejs.org/']
    try:
        lock.acquire()
        driver.execute_script(f"window.open('{url_list[idx]}')")
        driver.switch_to.window(driver.window_handles[idx + 1])
        driver.save_screenshot(f'{idx}.png')
        return True
    except Exception:
        return False
    finally:
        lock.release()


def main():
    driver = start_browser()
    for idx in range(5):
        threading.Thread(target=browser_thread, args=(driver, idx)).start()

    # 等待所有线程执行完毕
    for thread in threading.enumerate():
        if thread is not threading.current_thread():
            thread.join()


if __name__ == "__main__":
    main()

```

运行结果：      
![](\img\in-post\post-python\2023-08-31-python-selenium-thread-3.gif)              
 
<br>
<br>

#### 2、线程池与多标签页
```python
# -*- coding: utf-8 -*-
# Name:         thread_pool.py
# Author:       小菜
# Date:         2023/6/1 20:00
# Description:

import time
import threading

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from concurrent.futures import ThreadPoolExecutor, as_completed

MAX_WORKERS = 5
service = ChromeService(ChromeDriverManager().install())
lock = threading.Lock()


def start_browser():
    driver = webdriver.Chrome(service=service)
    return driver


def browser_task(driver: webdriver.Chrome, idx: int):
    url_list = ['https://www.csdn.net/', 'https://www.baidu.com',
                'https://music.163.com/', 'https://y.qq.com/', 'https://cn.vuejs.org/']

    try:
        lock.acquire()
        driver.execute_script(f"window.open('{url_list[idx]}')")
        driver.switch_to.window(driver.window_handles[idx + 1])
        driver.save_screenshot(f'{idx}.png')
        return True
    except Exception:
        return False
    finally:
        lock.release()


def main():
    driver = start_browser()
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)
    ths = list()
    for idx in range(5):
        th = executor.submit(browser_task, driver, idx=idx)
        ths.append(th)

    # 获取结果
    for future in as_completed(ths):
        print(future.result())


if __name__ == "__main__":
    st = time.time()
    main()
    et = time.time()
    print(et - st)

```

<br>
<br>

### 六、总结
本文章介绍了 Selenium + threading 和 Selenium + ThreadPoolExecutor 来创建多个浏览器或多个标签页的操作。<mark>文中示例的代码比较简单，所以线程池比多线程运行的更加快</mark>。但在实际的使用过程中，可以根据自己的喜好去选择线程池还是多线程。

<br>
<br>

---

相关链接：    
[【Selenium】提高测试&爬虫效率：Selenium与多线程的完美结合](https://blog.csdn.net/weixin_45081575/article/details/130948409)