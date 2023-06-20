---
layout:        post
title:         "Pytest | Pytest 失败重跑"
subtitle:      "使用插件实现自定义重跑次数和重跑间隔"
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



### 一、背景
在编写自动化测试用例的时候，我们常遇到一个这样的问题：     
&emsp;&emsp;测试环境不稳定偶发接口超时（和服务无关，纯粹是环境问题），然后执行自动化 case 也因此偶发失败。比如同一个 case 跑五次，其中有两次失败，另外三次都是成功的，这种偶发性的环境问题就需要我们手动重跑（还不一定能够通过）。有没有一个比较好的机制，保证 case 能够尽最大努力通过测试呢？       

这里我们介绍 pytest 的一个失败重跑插件：`pytest-rerunfailures`    

<br>
<br>

### 二、介绍
`pytest-rerunfailures` 是一个通过重跑机制来消除不稳定失败的 pytest 插件。         

项目地址：[https://github.com/pytest-dev/pytest-rerunfailures](https://github.com/pytest-dev/pytest-rerunfailures)

<br>
<br>

### 三、安装
安装&运行要求：      
```
Python 3.6~3.9, or PyPy3
pytest 5.0+
```
安装插件：
```
> pip install pytest-rerunfailures==10.1
```

<br>
<br>

### 四、使用pytest-rerunfailures
使用方式有两种：    
- 命令行参数
- 装饰器方式

<br>

#### 1、命令行参数模式
case：test_demo.py      
```python
#!/usr/bin/env python3
#!coding:utf-8
import pytest
import random
 
def test_simple_assume():
    #每次case运行的值为1或者2，具有随机性
    r = random.randint(1,2)
    assert r == 1
```
如果我们直接运行 `pytest test_demo.py`，那么每次运行的结果会具有一定随机性（可能成功也可能失败）。      
如果使用 pytest-rerunfailures 指定执行多次，只要执行次数足够多，那么遇到结果成功的机会就会更多。       

<br>

（1）示例一：指定失败重跑最大次数为10        
```
> pytest --reruns 10
```
如下图，我们看到一共跑了两次，第一次结果失败，所以重跑了第二次，最终结果用 `R` 标注。（如果跑一次就成功，结果应该是 `.`)      
![](\img\in-post\post-python\2023-06-20-python-pytest-1.png)     

<br>

（2）示例二：指定失败重跑最大次数为10，重跑间隔为1秒     
```
> pytest --reruns 10 --reruns-delay 1
```
如下图，一共重跑了两次，重跑两次的执行时间为2.1秒，上图中一次只需要0.07秒，这里多出的两秒就是因为 `--reruns-delay` 指定的重跑间隔为1秒。    
![](\img\in-post\post-python\2023-06-20-python-pytest-2.png)     

<br>

（3）通过表达式指定失败重跑      
test_demo.py 解释：    
- test_assert_error 随机抛出 AssertionError    
- test_value_error 随机抛出 ValueError

```python
!/usr/bin/env python3
#!coding:utf-8
import pytest
import random
 
def test_assert_error():
    r = random.randint(1,2)
    with pytest.raises(AssertionError):
        #这里如果不使用pytest.raises显式抛出AssertionError异常，pytest-rerunfailures无法捕获到assert r == 1，应该是该插件的bug。
        assert r == 1
 
def test_value_error():
    r = random.randint(1,2)
    if r == 1:
        s = int('www')
```
执行以下命令行，其中多个 `--only-rerun` 之间是或的关系。          
```
> pytest --reruns 10 --only-rerun AssertionError --only-rerun ValueError test_demo.py -v
```
如下图，遇到 AssertionError 和 ValueError 的情况下都被重跑了。     
![](\img\in-post\post-python\2023-06-20-python-pytest-3.png)     


<br>
<br>

#### 2、装饰器模式
case: test_demo.py       
- test_assert_error 随机抛出 AssertionError，最多失败重跑五次
- test_value_error 随机抛出 ValueError，最多失败重跑五次，失败重跑间隔为2秒
- test_value_error_condition 最多失败重跑五次，仅当系统为 win32 系统才重跑

```python
#!/usr/bin/env python3
#!coding:utf-8
import pytest
import random
import sys
 
#这个最多失败重跑五次
@pytest.mark.flaky(reruns=5)
def test_assert_error():
    r = random.randint(1,2)
    #raise AssertionError("ERR")
    with pytest.raises(AssertionError):
        assert r == 1
#这个最多失败重跑五次 
@pytest.mark.flaky(reruns=5, reruns_delay=2) 
def test_value_error(): 
　　r = random.randint(1,2) 
　　if r == 1: 
　　　　s = int('nick') 
#官网的这个例子有问题，如果拿mac或者linux机器跑也会有重试（condition中指定的是win32平台才会触发重跑机制）
@pytest.mark.flaky(reruns=5, condition=not sys.platform.startswith("win32")) 
def test_value_error_condition(): 
　　r = random.randint(1,2) 
　　　　if r == 1: 
　　　　　　s = int('nick')
```

执行：`> pytest -v`      
![](\img\in-post\post-python\2023-06-20-python-pytest-4.png)         

&emsp;&emsp;这里前面两个 testcase 都有过失败重跑，但是第三个也重跑了（作者原意是 condition 为 False 情况下不会重跑），这里是有 bug 的，即 condition 是无效的。      
&emsp;&emsp;去查看项目源码，果然发现这里有些问题，是否不重跑的函数里面用的是 or，即最后一个 not condition 只是不重跑的条件之一，如果前面满足重跑，则 condition 这个参数可以被忽略掉。      
![](\img\in-post\post-python\2023-06-20-python-pytest-5.png)      

<br>
<br>

### 五、兼容性
- 不可以与类，模块还有包级别的 fixture 装饰器一起使用： `@pytest.fixture()` 
- 该插件与 `pytest-xdis`t 的 `--looponfail` 标志不兼容
- 该插件在使用 pdb 调试时候会有不兼容性     

最后总结，这个插件虽然还用，但是坑还是不少，建议主要使用失败重试次数和重试间隔的功能即可。 

<br>
<br>

### 六、allure测试报告上的效果
在运行结果不稳定的测试用例加上失败重跑，重跑次数为3，重跑间隔为2秒：       
```python
    @pytest.mark.usefixtures("global_step")
    @pytest.mark.usefixtures("kill_driver")
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    @allure.title('销售-营销数据分析-业绩分布页面-报表搜索成功')
    def test_amazondistributionview_search_success(self, global_step):
        PageLogin(global_step).get_login()
        PageLogin(global_step).input_username(keyword=username)
        PageLogin(global_step).input_password(keyword=password)
        PageLogin(global_step).click_login_button()
        time.sleep(3)
        PageAmazonDistributionView(global_step).get_amazondistributionview()
        PageAmazonDistributionView(global_step).click_date_select_button()
        PageAmazonDistributionView(global_step).click_pre_month()
        PageAmazonDistributionView(global_step).click_search_button()
        time.sleep(5)
        PageAmazonDistributionView(global_step).assert_order_total(assert_value='订单量汇总：413,718')
```

测试报告上的显示效果如下：    
![](\img\in-post\post-python\2023-06-20-python-pytest-6.png) 


<br>
<br>

---

相关链接：   
[Pytest失败重跑](https://blog.csdn.net/fish_study_csdn/article/details/125999090)