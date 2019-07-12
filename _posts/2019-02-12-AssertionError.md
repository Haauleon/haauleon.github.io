---
layout: post
title: "自动化测试出现的异常"
subtitle: '那些年，自动化们一起追过的异常'
author: "Haauleon"
header-style: text
tags:
  - 异常
  - 自动化测试
  - python
---

&emsp;&emsp;今早运行了接口自动化测试用例，在输出的测试报告里面找到了几种比较常见的异常，想在此做个总结以及简单的分析一下出现这些异常的原因。记得第一次完整的写完某一版本的接口测试脚本后运行一路绿灯，总算松了口气，以为这样就完事了。然鹅，在下一次迭代发版时运行发现好几个亮红灯的，心慌但要学会自救，于是开始学着去看异常看日志。现在翅膀硬了，即使报错依然镇定自若。            




## AssertionError
异常名称：AssertionError         
异常描述：断言语句失败      
```python
AssertionError: False is not true
```        

出现原因：第一次运行正常，但是后续运行时才出现这种异常，99&#46;99&#37;是因为后端代码有bug。


## IndexError
异常名称：IndexError         
异常描述：序列中没有此索引&#40;index&#41;                    
```python
IndexError: list index out of range
```     

出现原因：一般这种返回列表数据为空的异常，绝大原因是后台数据为空，但也有可能是后端代码有bug。所以遇到这种异常第一件事要做的就是检查后台系统或者数据库有没有配数据，如果配了数据但是没返回就是后端代码有bug。


## KeyError
异常名称：KeyError         
异常描述：映射中没有这个键                   
```python
KeyError: 'listTime'
```

出现原因：意思就是说返回的字典里面没有这个键值对，毫无疑问，99&#46;99&#37;是因为后端代码有bug。


## 资源
[python异常](http://www.runoob.com/python/python-exceptions.html)