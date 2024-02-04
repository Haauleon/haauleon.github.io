---
layout:        post
title:         "Python3 | apscheduler 添加调度任务"
subtitle:      "cron实现周期性触发，date实现指定时间点一次触发"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 添加调度任务
&emsp;&emsp;使用 `BlockingScheduler()` 新建一个调度器在当前进程的主线程中运行，会阻塞当前线程。该调度器一般用的比较多，可以看到当前调度任务运行的输出结果，推荐使用。      

<br>

#### date
使用 `date` 触发器可实现指定时间点，为一次触发。如下示例：在2024年2月4日15时8分0秒执行一次。            
```python
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from common.log import Logger

scheduler = BlockingScheduler()


@scheduler.scheduled_job('date', run_date=datetime.datetime(2024, 2, 4, 15, 8, 0))
def main():
    for _ in range(5):
        try:
            print("This script is running!")
            break
        except Exception as e:
            Logger.error(e)


if __name__ == '__main__':
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

```

<br>
<br>

#### cron
使用 `cron` 触发器可实现周期性执行。如下示例：每周日凌晨0点0分0秒执行。     
```python
from apscheduler.schedulers.blocking import BlockingScheduler
from common.log import Logger

scheduler = BlockingScheduler()


@scheduler.scheduled_job("cron", day_of_week='SUN', hour='0', minute='0', second='0')
def main():
    for _ in range(5):
        try:
            print("This script is running!")
            break
        except Exception as e:
            Logger.error(e)


if __name__ == '__main__':
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()

```

<br>
<br>

---

相关链接：    
[一文详解Python定时任务触发](https://www.jb51.net/article/279789.htm)