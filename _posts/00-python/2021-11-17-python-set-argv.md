---
layout:        post
title:         "python3 | 自定义命令行参数"
subtitle:      "命令行自定义参数以及处理命令行参数"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
  - Python
---

&emsp;&emsp;自定义命令行参数，用于在命令行窗口中执行程序时附加参数。处理命令行参数，用于获取命令行窗口中输入的参数。                 

<br>

```python
'''
自定义命令行参数
'''
import argparse

# 添加命令行解析器
parser = argparse.ArgumentParser() 
# default=1,help="命令行说明信息"  自定义命令行参数标志 
parser.add_argument("--fn", type=str)
# 解析命令行参数
args, unparsed = parser.parse_known_args() 
# 访问解析后的命令行参数
threadnum = args.tn   
# 打印参数
print(threadnum)  
# 打印参数类型 
print(type(threadnum))
# 命令行输入: python test.py collection.json
 


'''
处理命令行参数
'''
import sys  

# sys.argv 的类型为  <class 'list'>
print ('参数个数为:', len(sys.argv), '个参数。') 
# ['argv1.py', '1', '2', '3'] 命令行输入的均被解析为字符串  
# sys.argv为列表，可行访问命令参数  
print ('参数列表:', str(sys.argv))  
# 如命令行输入：python test.py 1234 5678   
# 那么sys.argv[0]=test.py  sys.argv[1]="1234"   sys.argv[2]="5678" 
# 从第二个参数开始才是我们输入的参数
```