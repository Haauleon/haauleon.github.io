---
layout:        post
title:         "Python3 | apscheduler + cron 实现定时执行作业"
subtitle:      "模拟读取并解析数据库的 cron 表达式后使用 apscheduler 模块实现定时任务"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 安装apscheduler
```
> pip install apscheduler==3.10.1
```

<br>
<br>

### 实现需求
&emsp;&emsp;模拟读取数据库的 cron 表达式，然后自己进行解析，将处理后的各个域值传递给 apscheduler 的 add_job() 方法，实现程序持久化定时执行的目的。代码如下：    

```python
# -*- coding: utf-8 -*-
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

# 模拟读取数据库的cron表达式
# <seconds:秒> <minutes:分> <hours:小时> <day_of_month:天> <month:月> <day_of_week:周> <year:年>
cron = '0/2 * * * * ?'
seconds, minutes, hours, day_of_month, month, day_of_week = tuple(cron.split(' '))
day_of_month = day_of_month if not day_of_month == '?' else None
day_of_week = day_of_week if not day_of_week == '?' else None


def rpa_job():
    # 模拟任务输出当前时间
    print('测试输出： ', datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

scheduler = BlockingScheduler()
scheduler.add_job(
    rpa_job,
    'cron',
    month=month,
    day=day_of_month,
    day_of_week=day_of_week,
    hour=hours,
    minute=minutes,
    second=seconds
)
scheduler.start()
```


结果输出如下：    
```
测试输出：  2023-07-14 15:22:12
测试输出：  2023-07-14 15:22:14
测试输出：  2023-07-14 15:22:16
测试输出：  2023-07-14 15:22:18
测试输出：  2023-07-14 15:22:20
测试输出：  2023-07-14 15:22:22
测试输出：  2023-07-14 15:22:24
测试输出：  2023-07-14 15:22:26
测试输出：  2023-07-14 15:22:28
测试输出：  2023-07-14 15:22:30
测试输出：  2023-07-14 15:22:32
测试输出：  2023-07-14 15:22:34
测试输出：  2023-07-14 15:22:36
测试输出：  2023-07-14 15:22:38
测试输出：  2023-07-14 15:22:40
测试输出：  2023-07-14 15:22:42
...
```

<br>
<br>

### 常用cron表达式例子

|表达式|解释|
|----|----|
|0/2 * * * * ?|表示每2秒执行任务|
|0 0/2 * * * ?|表示每2分钟执行任务|
|0 0 2 1 * ?|表示在每月的1日的凌晨2点调整任务|
|0 15 10 ? * MON-FRI|表示周一到周五每天上午10:15执行作业|
|0 15 10 ? 6L 2002-2006|表示2002-2006年的每个月的最后一个星期五上午10:15执行作|
|0 0 10,14,16 * * ?|每天上午10点，下午2点，4点|
|0 0/30 9-17 * * ?|朝九晚五工作时间内每半小时|
|0 0 12 ? * WED|表示每个星期三中午12点|
|0 0 12 * * ?|每天中午12点触发|
|0 15 10 ? * *|每天上午10:15触发|   
|0 15 10 * * ?|每天上午10:15触发|
|0 15 10 * * ?|每天上午10:15触发|
|0 15 10 * * ? 2005|2005年的每天上午10:15触发|
|0 * 14 * * ?|在每天下午2点到下午2:59期间的每1分钟触发|
|0 0/5 14 * * ?|在每天下午2点到下午2:55期间的每5分钟触发|
|0 0/5 14,18 * * ?|在每天下午2点到2:55期间和下午6点到6:55期间的每5分钟触发|
|0 0-5 14 * * ?|在每天下午2点到下午2:05期间的每1分钟触发|
|0 10,44 14 ? 3 WED|每年三月的星期三的下午2:10和2:44触发|
|0 15 10 ? * MON-FRI|周一至周五的上午10:15触发|
|0 15 10 15 * ?|每月15日上午10:15触发|
|0 15 10 L * ?|每月最后一日的上午10:15触发|
|0 15 10 ? * 6L|每月的最后一个星期五上午10:15触发|
|0 15 10 ? * 6L 2002-2005|2002年至2005年的每月的最后一个星期五上午10:15触发|
|0 15 10 ? * 6#3|每月的第三个星期五上午10:15触发|


<br>
<br>

---

相关链接：    
[Python 定时调度](https://blog.51cto.com/u_7174760/4014838)     
[APScheduler 使用指南](http://sinhub.cn/2018/11/apscheduler-user-guide/)      
[APScheduler如何将作业保存在数据库中？（Python）](https://www.cnpython.com/qa/326581)      
[APScheduler+MySQL实现定时任务及其持久化存储](https://www.jianshu.com/p/e36236c1df08)      
[APScheduler的cron触发器支持到秒级的cron表达式](https://blog.csdn.net/m0_47958289/article/details/116940934)   