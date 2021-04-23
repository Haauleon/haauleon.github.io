---
layout:        post
title:         "Python3 | 执行 shell 命令"
subtitle:      "用于在 python 脚本内通过管道来执行 shell 命令"
date:          2021-04-20
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
---

## 背景
&emsp;&emsp;在 python 脚本内执行 shell 命令，可以解放双手。     

<br><br>

## 使用技巧
###### 一、os.popen("command")
语法：       
```
os.popen("command")
```
<br>

实例：                    
```
import os

print("os.popen('ls'): {}".format(os.popen("ls")))
print("-" * 20)

pipeline = os.popen("ls")
print("pipeline: {}".format(pipeline)) 
print("-" * 20)

print("type(pipeline): {}".format(type(pipeline))) 
print("-" * 20)

print("pipeline.read(): {}".format(pipeline.read())) 
print("-" * 20)

print("type(pipeline.read()): {}".format(type(pipeline.read())))

```
<br>

运行结果：                                
```
os.popen('ls'): <os._wrap_close object at 0x7fb853f29550>
--------------------
pipeline: <os._wrap_close object at 0x7fb853f50350>
--------------------
type(pipeline): <class 'os._wrap_close'>
--------------------
pipeline.read(): online_notice.py
process_demo.py
saas-collection.json
saas-env-lssonline.json
saas-env-online.json
saas-env-test.json
saas-globals.json
saas_online_report.html
saas_test_report.html

--------------------
type(pipeline.read()): <class 'str'>
```
<br>

分析：os.popen() 无返回值，若需要返回值，需要实例化一个文件对象 pipeline = os.popen("command")，通过 pipeline.read() 方法读取文件内容。通常用于打开一个管道执行单个命令行。

<br><br>

###### 二、subprocess.call()
语法：       
```
subprocess.call("command", shell=True)
```
<br>

实例：                
```
import subprocess

subprocess.call("ls", shell=True)
```
<br>

运行结果：                            
```
0
```
<br>

分析：subprocess.call()有返回值，0为正常退出。跟 os.popen() 的场景一样，适用于打开一个管道执行单个命令行。        

<br><br>

###### 三、os.system()
语法：          
```
os.system("cd 指定的目录路径 && 执行的命令")
```
<br>

实例：                  
```
import os

os.system("cd ../ && ls")
```
<br>

运行结果：                     
```
0
```
<br>

分析：os.system(0 有返回值，0为正常退出。使用场景为在指定的目录下执行命令。