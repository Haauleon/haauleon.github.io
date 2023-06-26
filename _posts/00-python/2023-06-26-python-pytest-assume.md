---
layout:        post
title:         "Pytest | pytest-assume 插件"
subtitle:      "使用插件实现多重断言执行"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - Allure
    - Pytest
    - 单元测试框架
---

### 背景
&emsp;&emsp;使用 pytest 进行断言判断的时候，为了用例的精准性，经常会多个方面进行断言，比如如下：     
```python
# 断言1：断言响应的 http 的状态

# 断言2：断言响应返回的 code 值

# 断言3：断言响应返回的 json 中的 data 字段是否符合预期
```

&emsp;&emsp;如果使用原生 python 的 assert，就会遇到一个断言失败则全部失败的情况。比如说，断言1 结果为 Failed，那么断言2 和断言3 都不会被执行。      
&emsp;&emsp;我们希望断言2 和断言3 继续执行，这样我们能获取更多的断言结果来判断出接口哪里出了问题，能够更好地进行问题定位，这时候该本文主角出现了：pytest-assume 插件。      

<br>
<br>

### pytest-assume简介
&emsp;&emsp;一个可以允许 pytest 测试用例中执行多个失败的断言的插件（即上面断言1，断言2，断言3 都失败的情况下，三个断言都能被执行）。      

项目：[https://github.com/astraw38/pytest-assume](https://github.com/astraw38/pytest-assume)      

说明：（该插件源自 pytest-expect，并且做了一部分小的修改）           
1、支持 showlocals(即 pytest 命令行的 `-l` 参数，显示执行过程中的局部变量）    
2、可以全局使用，无需指定 fixtrue 装饰器。（即任意 test_xxx 函数中都能用）      
3、对断言输出做了一些格式上的美化      

<br>
<br>

### pytest-assume安装
```shell
# 根据python版本，可选择pip3或者pip
> sudo pip3(pip) install git+https://github.com/astraw38/pytest-assume.git
# 或者
> sudo pip3(pip) install pytest-assume
```

<br>
<br>

### 使用示例     
1、一个对比原生 assert 和 pytest-assume 的测试用例      
```python
#!/usr/bin/env python3
#!coding:utf-8
import pytest

@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    assert x == y  #如果这个断言失败，则后续都不会执行
    assert True
    assert False

@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_pytest_assume(x, y):
    pytest.assume(x == y) #即使这个断言失败，后续仍旧执行
    pytest.assume(True)
    pytest.assume(False)
```
输出：    
```shell
===================================================================================== test session starts =====================================================================================
platform darwin -- Python 3.8.2, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
rootdir: /Users/xxx/Desktop/pytest
plugins: assume-2.4.2, ordering-0.6

collected 6 items  # 这里执行了六个用例

test_demo.py FFF [100%]

========================================================================================== FAILURES ===========================================================================================
___________________________________________________________________________________ test_simple_assume[1-1] ___________________________________________________________________________________

x = 1, y = 1

@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
    def test_simple_assume(x, y):
        assert x == y
        assert True
> assert False  # 前两个断言成功，第三个断言失败了
E assert False

test_demo.py:9: AssertionError
___________________________________________________________________________________ test_simple_assume[1-0] ___________________________________________________________________________________

x = 1, y = 0

@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
> assert x == y  # 第一个断言失败了，后续断言不会被执行
E assert 1 == 0

test_demo.py:7: AssertionError
___________________________________________________________________________________ test_simple_assume[0-1] ___________________________________________________________________________________

x = 0, y = 1

@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
> assert x == y  # 第一个断言失败了，后续断言不会被执行
E assert 0 == 1 

test_demo.py:7: AssertionError
___________________________________________________________________________________ test_pytest_assume[1-1] ___________________________________________________________________________________

tp = <class 'pytest_assume.plugin.FailedAssumption'>, value = None, tb = None

def reraise(tp, value, tb=None):
    try:
        if value is None:
            value = tp()
        if value.__traceback__ is not tb:
> raise value.with_traceback(tb)
E pytest_assume.plugin.FailedAssumption:
E 1 Failed Assumptions:
E
E test_demo.py:15: AssumptionFailure
E >> pytest.assume(False)
E AssertionError: assert False  # 前两个断言成功，第三个断言失败了

/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages/six.py:702: FailedAssumption
---------------------------------------------------------------------------------- Captured stdout teardown -----------------------------------------------------------------------------------
F
___________________________________________________________________________________ test_pytest_assume[1-0] ___________________________________________________________________________________

tp = <class 'pytest_assume.plugin.FailedAssumption'>, value = None, tb = None

def reraise(tp, value, tb=None):
    try:
        if value is None:
            value = tp()
        if value.__traceback__ is not tb:
> raise value.with_traceback(tb)
E pytest_assume.plugin.FailedAssumption:
E 2 Failed Assumptions:
E
E test_demo.py:13: AssumptionFailure
E >> pytest.assume(x == y)  # 第一个断言失败，后续继续执行
E AssertionError: assert False
E
E test_demo.py:15: AssumptionFailure
E >> pytest.assume(False)
E AssertionError: assert False

/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages/six.py:702: FailedAssumption
---------------------------------------------------------------------------------- Captured stdout teardown -----------------------------------------------------------------------------------
F
___________________________________________________________________________________ test_pytest_assume[0-1] ___________________________________________________________________________________

tp = <class 'pytest_assume.plugin.FailedAssumption'>, value = None, tb = None

def reraise(tp, value, tb=None):
    try:
        if value is None:
            value = tp()
        if value.__traceback__ is not tb:
> raise value.with_traceback(tb)
E pytest_assume.plugin.FailedAssumption:
E 2 Failed Assumptions:
E
E test_demo.py:13: AssumptionFailure
E >> pytest.assume(x == y)  # 第一个断言失败，后续继续执行
E AssertionError: assert False
E
E test_demo.py:15: AssumptionFailure
E >> pytest.assume(False)
E AssertionError: assert False

/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages/six.py:702: FailedAssumption
---------------------------------------------------------------------------------- Captured stdout teardown -----------------------------------------------------------------------------------
F
=================================================================================== short test summary info ===================================================================================
FAILED test_demo.py::test_simple_assume[1-1] - assert False
FAILED test_demo.py::test_simple_assume[1-0] - assert 1 == 0
FAILED test_demo.py::test_simple_assume[0-1] - assert 0 == 1
FAILED test_demo.py::test_pytest_assume[1-1] - pytest_assume.plugin.FailedAssumption:
FAILED test_demo.py::test_pytest_assume[1-0] - pytest_assume.plugin.FailedAssumption:
FAILED test_demo.py::test_pytest_assume[0-1] - pytest_assume.plugin.FailedAssumption:
====================================================================================== 6 failed in 0.19s ======================================================================================
```

这里我们可以看出二者的区别了，执行差异如下：     

|断言类型|1, 1|1, 0|0, 1|结论|
|---|---|---|---|---|
|assert|断言3 失败|断言1 失败，<br>断言2 和断言3 不执行|断言1 失败，断言2 和断言3 不执行|assert 遇到断言失败则停下|
|pytest.assume|断言3 失败|断言1 失败，<br>断言2 和断言3 继续执行|断言1 失败，断言2 和断言3 继续执行|pytest.assume 无论断言结果失败与否，全部执行|

<br>
<br>

2、 通过上下文管理器 with 使用 pytest-assume     
```python
#!/usr/bin/env python3
#!coding:utf-8
import pytest
# from pytest import assume
from pytest_assume.plugin import assume

@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    #使用上下文管理器的好处是不用显示去try和finally捕获异常，建议使用这种写法，简洁有效。
    with assume: assert x == y
    with assume: assert True
    with assume: assert False
```

主要注意的是，如果上下文管理器里面包含多个断言，则只有第一个会被执行，如：    
```python
#!/usr/bin/env python3
#!coding:utf-8
import pytest
# from pytest import assume
from pytest_assume.plugin import assume
    
@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume(x, y):
    #使用上下文管理器的好处是不用显示去try和finally捕获异常，建议使用这种写法，简洁有效。
    with assume: 
        #只有第一个断言会被执行！
        assert x == y
        assert True
        assert False
```

<br>
<br>

---

相关链接：   
[pytest-assume插件（全网最详细解释）：多重断言执行](https://blog.csdn.net/weixin_50829653/article/details/113179401)        
[pytest assume无法导入：解决ImportError: cannot import name ‘assume‘ from ‘pytest‘问题](https://blog.csdn.net/tianshuiyimo/article/details/116519264)