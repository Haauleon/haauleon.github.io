---
layout:        post
title:         "Python3 | 单线程异步协程"
subtitle:      "asyncio + pyppeteer 实现单线程多任务异步爬虫"
date:          2021-04-22
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - 爬虫
---


## 背景
&emsp;&emsp;接盘了其中一个异步爬虫项目，看了下，在被 async 修饰的协程 main() 中加了一行 `time.sleep(30)` 这样的非异步操作代码，导致异步失效，程序运行总耗时太长。我看了别人的协程示例后，把代码改了，用 `await asyncio.sleep(30)` 去代替原来的 `time.sleep(30)`，然后在主程序中定义了一个任务列表 tasks， 用来放置多个任务对象，然后执行 `loop.run_until_complete(asyncio.wait(tasks))` 将多个任务对象对应的列表 tasks 注册到事件循环中，解决了异步失效的问题。另外，还增加了自动关闭浏览器时删除 tmp 文件的参数。                                
&emsp;&emsp;但是我发现了 pyppeteer 有个问题，不知道是不是 bug，就是如果我的 urls 列表的长度超过 2，那么程序在同时打开 3 个浏览器窗口时，偶尔会有一个或两个窗口的标签页未加载 url，真的很奇怪，我试了很多种办法都无法解决，打算优化成单个窗口打开多个标签页试试能不能解决。        

<br><br>

## 代码
###### 一、旧代码
```python
# -*- coding: utf-8 -*-#
# Description:  
# Author:       ribbog77
# Date:         2020/2/18
import random
import time

import asyncio
import pyppeteer
import requests


class SpiderGoogle(object):
    """
    异步类
    """
    pyppeteer.DEBUG = True
    page = None
    item_list = list()
    # proxy = None

    def __init__(self):
        # self.proxy = proxy
        pass

    async def _init(self):
        """
        初始化浏览器,获取代理ip
        :return:
        """
        browser = await pyppeteer.launch(
            {
                'headless': True,  # 浏览器是否启用无头模式
                'args': ['--disable-extensions',
                         '--hide-scrollbars',
                         '--disable-bundled-ppapi-flash',
                         '--mute-audio',
                         '--no-sandbox',
                         '--disable-setuid-sandbox',
                         '--disable-gpu',
                         '--disable-infobars',
                ],
                'dumpio': True  # 不添加会卡顿

            }
        )
        # 在浏览器创建新页面
        self.page = await browser.newPage()
        # 设置浏览器头部
        await self.page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ')
        # 设置浏览器大小(如果设置了无头浏览器就把这里屏蔽掉)
        # await self.page.setViewport({'width': 1000, 'height': 1000})

    async def _insert_js(self):
        """
        注入js
        :return:
        """
        await self.page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')  # 本页刷新后值不变

    async def main(self):
        await self._init()
        await self._insert_js()
        await self.page.goto('https://www.cnblogs.com/', timeout=0) # 3.1MB
        time.sleep(5)
        await self.page.goto('https://www.csdn.net/', timeout=0) # 1.8MB
        time.sleep(5)
        await self.page.close()


if __name__ == '__main__':
    start = time.time()
    google = SpiderGoogle()
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(google.main())
    loop.run_until_complete(task)
    print('总耗时：',time.time()-start)  
```

<br>

运行结果：                      
```
总耗时： 16.083781003952026

```

<br><br>

###### 二、多任务协程代码（更新后）
```python
# -*- coding: utf-8 -*-#
# Description:  
# Author:       ribbog77
# Date:         2020/2/18
import random
import time

import asyncio
import pyppeteer
import requests

urls = [
    'https://www.cnblogs.com/',
    'https://www.csdn.net/',
]

tasks = [] # 任务列表，放置多个任务对象


class SpiderGoogle(object):
    """
    异步类
    """
    async def _init(self):
        """
        初始化浏览器,获取代理ip
        :return:
        """
        browser = await pyppeteer.launch(
            {
                'headless': True,  # 浏览器是否启用无头模式
                'args': ['--disable-extensions',
                         '--hide-scrollbars',
                         '--disable-bundled-ppapi-flash',
                         '--mute-audio',
                         '--no-sandbox',
                         '--disable-setuid-sandbox',
                         '--disable-gpu',
                         '--disable-infobars',
                         '--window-size=1366,850',
                ],
                'dumpio': True,   # 不添加会卡顿,
                'autoClose': True # 在自动关闭浏览器的时候删除tmp文件

            }
        )
        # 在浏览器创建新页面
        self.page = await browser.newPage()
        # 设置浏览器头部
        await self.page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ')
        # 设置浏览器大小(如果设置了无头浏览器就把这里屏蔽掉)
        # await self.page.setViewport({'width': 1366, 'height': 768})
    
    async def main(self, url):
        await self._init()
        await self.page.goto(url, timeout=0)
        await asyncio.sleep(5)
        
    async def close_page(self):
        await self.page.close()


def run():
    for url in urls:
        print(url)
        task = asyncio.ensure_future(google.main(url))
        tasks.append(task)


if __name__ == '__main__':
    start = time.time()
    google = SpiderGoogle()
    loop = asyncio.get_event_loop()
    run()
    loop.run_until_complete(asyncio.wait(tasks))   #将多个任务对象对应的列表注册到事件循环中
    print('总耗时：', time.time()-start)
```

<br>

运行结果：                    
```
https://www.cnblogs.com/
https://www.csdn.net/
总耗时： 7.385887861251831

```

<br><br>

## 结论
&emsp;&emsp;pyppeteer 本身就支持异步，不过我还不熟练，总感觉坑很多。参考：[高性能的异步爬虫](https://www.cnblogs.com/pythonz/p/10933838.html)