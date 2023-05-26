---
layout:        post
title:         "Python3 | python 删除文件夹和文件"
subtitle:      "三种删除方法"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 一、三种删除方法
python 删除文件和文件夹主要用到 os 模块和 shutil 模块，针对文件夹和文件的删除，有几种情况。       

```python
import shutil
import os
from pathlib import Path

# 第一种：删除一个文件夹，无论里面是否有文件或文件夹
# (不支持文件，文件夹不存在会报错)
def del_files0(dir_path):
    shutil.rmtree(dir_path)

# 第二种 递归删除dir_path目标文件夹下所有文件，以及各级子文件夹下文件，保留各级空文件夹
# (支持文件，文件夹不存在不报错)
def del_files(dir_path):
    if os.path.isfile(dir_path):
        try:
            os.remove(dir_path) # 这个可以删除单个文件，不能删除文件夹
        except BaseException as e:
            print(e)
    elif os.path.isdir(dir_path):
        file_lis = os.listdir(dir_path)
        for file_name in file_lis:
            # if file_name != 'wibot.log':
            tf = os.path.join(dir_path, file_name)
            del_files(tf)
    print('ok')

# 第三种： 删除dir_path目标文件夹下所有内容，保留dir_path文件夹
# (不支持文件，文件夹不存在会报错)
def del_files2(dir_path):
    # os.walk会得到dir_path下各个后代文件夹和其中的文件的三元组列表，顺序自内而外排列，
    # 如 log下有111文件夹，111下有222文件夹：[('D:\\log\\111\\222', [], ['22.py']), ('D:\\log\\111', ['222'], ['11.py']), ('D:\\log', ['111'], ['00.py'])]
    for root, dirs, files in os.walk(dir_path, topdown=False):
        print(root) # 各级文件夹绝对路径
        print(dirs) # root下一级文件夹名称列表，如 ['文件夹1','文件夹2']
        print(files)  # root下文件名列表，如 ['文件1','文件2']
        # 第一步：删除文件
        for name in files:
            os.remove(os.path.join(root, name))  # 删除文件
        # 第二步：删除空文件夹
        for name in dirs:
            os.rmdir(os.path.join(root, name)) # 删除一个空目录


if __name__ == '__main__':
    dir_path = Path('./log').absolute()
    del_files2(dir_path)
```

<br>
<br>

### 二、删除失败情况 
`PermissionError: [WinError 5] 拒绝访问`           

删除某些文件夹或者文件，比如 git 仓库的时候，会报错，显示 `PermissionError: [WinError 5]` 拒绝访问。         

<br>

方法：   
1、给 python 权限        
这是因为没有权限      

2、删除改为更名        
我感觉给与权限还需要修改这修改那的很麻烦，直接放弃删除操作，替换为更改文件夹名字操作：      
```python
import random,os

dir_path = os.getcwd()  # 当前目录绝对路径D:\git_helper
print('当前目录绝对路径:', str(random.random())[-5:])
os.rename(src='../weebot_wxbot', dst=f'../weebot_wxbot{str(random.random())[-5:]}')
```

<br>
<br>

---

相关链接：   
[python 删除文件夹和文件【转】](https://blog.csdn.net/a1579990149wqh/article/details/124953746)