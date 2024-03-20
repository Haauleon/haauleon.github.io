---
layout:        post
title:         "Python3 | apscheduler 设置 misfire_grace_time"
subtitle:      "解决因服务器资源不足而导致任务错过了执行时间，通过该参数设置任务运行前的延迟秒数"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 背景
&emsp;&emsp;目前运维同事给我的服务器部署了 4 个爬虫项目，这些爬虫项目均使用了 apscheduler 模块实现定时调度任务。但是最近发现，一到周末，这些爬虫到点后居然不运行了，还抛出了以下异常提示：   
```bash
Run time of job "login (trigger: interval[0:10:00], next run at: 2021-04-22 18:39:54 CST)" was missed by 0:00:02.547804
```

&emsp;&emsp;意味着在设置的时间点，任务并没有运行起来，一检查发现，服务器一到周末就很卡，运维同事说是因为 CPU 不够了，内存也不够了。

<br>
<br>

### 目标
&emsp;&emsp;看提示 `was missed by 0:00:02.547804`，大概就是当时服务器卡了一会儿，卡了两秒，所以没资源执行任务了。所以，为了解决这个问题，引入了参数 misfire_grace_time，当任务被唤起时，如果在 misfire_grace_time 时间差内，依然运行。不设置时默认为1。这里需要设置大于 2 秒即可，为了保险点，我设置了 10 分钟。     

<br>
<br>

### 使用
```python
from apscheduler.schedulers.blocking import BlockingScheduler

def my_job():
    print("The job executed.")

scheduler = BlockingScheduler()
scheduler.add_job(my_job, 'interval', seconds=5, misfire_grace_time=600)
scheduler.start()
```

或者：    
```python
from apscheduler.schedulers.blocking import BlockingScheduler

@scheduler.scheduled_job("cron", day_of_week='*', hour='0', minute='0', second='0', misfire_grace_time=600)
def my_job():
    print("The job executed.")

scheduler = BlockingScheduler()
scheduler.start()
```

<br>
<br>

---

相关链接：    
[APscheduler报错Run time of job "xxx" was missed by xxx 解决方案](https://www.jianshu.com/p/f01be9eaf86f)