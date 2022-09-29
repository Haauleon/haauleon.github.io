---
layout:        post
title:         "Python3 | API 自动化测试"
subtitle:      "基于 unittest + requests + utx 的接口自动化"
date:          2021-04-30
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - API 测试
    - Python
---

## 背景
&emsp;&emsp;utx 这个项目扩展了 python 的单元测试框架 unittest 的功能，解决了 unittest 框架默认用例执行顺序是按照 ascii 编码的用例函数名称来执行的。关于函数名称这一块真的挺头疼的，因为必须要按照 ascii 码去设计用例名称。这个项目的起因就是为了解决这个问题，同时还增加了用例标签功能，以及使用了数据驱动，日志封装等等都很值得借鉴。        
&emsp;&emsp;这个宝藏项目其实早在 2019 年我就发现了，也不知道一直都没火，最近又发现的一个宝藏项目 seldom 也借鉴了 utx 项目的部分功能。utx 这个项目在 2019 年后就没有迭代了，不知道作者后面还会不会有新的功能更新，总之，真的很感谢每一位愿意在 github 上贡献源码的人，为后来的人指明了一条道路，同时也提了一些好的想法。         

<br><br>

## 项目结构
```
192:utx haauleon$ tree
.
├── __init__.py
├── core.py
├── log.py
├── report
│   ├── __init__.py
│   ├── style_1.py
│   └── style_2.py
├── runner.py
├── setting.py
└── tag.py

2 directories, 15 files
192:utx haauleon$ 
```
<br>

###### core.py
`core.py` 该模块为项目的主模块，定义了数据驱动，用例添加标签，用例执行顺序等功能。      

1.解决用例名称执行顺序问题      
```python
# utx/core.py

def run_case(case_class, case_name: str):
    setting.execute_interval = 0.3
    r = re.compile(case_name.replace("test_", "test(_\d+)?_"))
    suite = unittest.TestSuite()
    for i in unittest.TestLoader().loadTestsFromTestCase(case_class):
        if r.match(getattr(i, "_testMethodName")):
            suite.addTest(i)
    unittest.TextTestRunner(verbosity=0).run(suite)
```

<br>

2.给用例添加