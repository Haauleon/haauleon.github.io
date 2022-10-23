---
layout:        post
title:         "python3 | 获取类中除内置方法外的所有方法名"
subtitle:      ""
date:          2021-09-16
author:        "Others"
header-style:  text
catalog:       true
tags:
  - Python
---

&emsp;&emsp;最近工作遇到了点小麻烦，原本的结构不满足于现有需求了，但是又不想改变原有的结构，所以重新写了一个类。但是有个问题，我想获取类中所有自定义方法的列表长度，走投无路搜了百度发现以下的方法可以解决这个问题。           

<br>

```python
class Menu:

    def __init__(self):
        pass

    def updateProject(self):
        pass

    def restartProject(self):
        pass

    def restartTomcat(self):
        pass

    def stopTomcat(self):
        pass

    def startTomcat(self):
        pass

    def methods(self):
        return(list(filter(lambda m: not m.startswith("__") and not m.endswith("__") and callable(getattr(self, m)), dir(self))))

if __name__ == '__main__':
    print(Menu().methods()) 
    # ['methods', 'restartProject', 'restartTomcat', 'startTomcat', 'stopTomcat', 'updateProject']
```