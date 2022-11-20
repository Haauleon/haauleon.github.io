---
layout:        post
title:         "python3 | 合并多个 json 文件"
subtitle:      ""
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
  - Python
---

&emsp;&emsp;该脚本用于合并当前目录下的所有以 json 结尾的文件内容，并生成一个新的 json 文件。                      

<br>

```python
import os, json
# import pandas as pd

path_to_json = './'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
# print(json_files)  # for me this prints ['foo.json']

json.dump([json.load(open(f)) for f in json_files], open("./tests.json", 'w'))

with open("./tests.json") as f:
    data = json.load(f)
    print(data)
```