---
layout:        post
title:         "python3 | 计算 mp4 文件时长"
subtitle:      "批量计算指定目录下的 mp4 文件的时长，以秒为单位"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
  - Python
---

&emsp;&emsp;该脚本目前只写了个简易版，用于计算指定路径的目录下所有 mp4 文件的时长，且以秒为单位，四舍五入不保留小数点后的数字。适用于 windows 系统下 cmd 命令行执行。                

<br>

```python
import os
from moviepy.editor import VideoFileClip     # pip install moviepy

def get_mp4_time(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(root)
        # print(dirs)
        # print(files)
        for filename in files:
            # print(root + '\\' + filename)
            clip = VideoFileClip(root + '\\' + filename)
            file_time = clip.duration
            # print(type(file_time))
            print('文件名: {}\n文件时长: {:.0f}\n\n'.format(filename[:-4], file_time))
            # print(filename)

get_mp4_time("E:\BaiduNetdiskDownload\xxxxxxxxxxxxx")
```