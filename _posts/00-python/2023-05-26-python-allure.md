---
layout:        post
title:         "Pytest | allure 测试报告"
subtitle:      "allure 测试报告框架的使用教程"
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

> 本篇文章带来allure测试报告框架的使用教程，这个allure报告目前发现是市面上最精美的测试报告之一了，功能非常的多吗，也非常的好看，值得一试！

<br>
<br>

### 一、介绍
allure 官网 ：[http://allure.qatools.ru/](http://allure.qatools.ru/)     

![](\img\in-post\post-python\2023-05-26-python-allure-1.png)      

安装包下载地址：[https://github.com/allure-framework/allure2/releases](https://github.com/allure-framework/allure2/releases)      

<br>

#### allure
&emsp;&emsp;allure 是一个轻量级、灵活的、支持多语言的测试报告工具，基于 java 语言开发，支持 java,python,javascript,ruby,php 等多种语言，同时拥有 jenkins 的相关插件支持，可以很好的运用到持续集成中。     

<br>
<br>

### 二、allure工具环境配置
在使用 allure 之前，我们必须先要安装 java jdk 环境（本篇文章不介绍，请自行百度）和 allure 环境。      

<br>

#### allure下载
下载地址：[https://github.com/allure-framework/allure2/releases](https://github.com/allure-framework/allure2/releases)       

1、我们直接下载 allure.zip 即可：     
![](\img\in-post\post-python\2023-05-26-python-allure-2.png)       

2、下载好之后进行解压 ，我们需要给其配置环境变量（Mac版本，Windows类似），解压之后如下：     
![](\img\in-post\post-python\2023-05-26-python-allure-3.png)       

3、我们注意这个 bin 目录，需要把这个路径配置到环境变量中，也就是我们的 bash_profile 文件，首先我们打开 bash_profile：     
```
vim ~/.bash_profile
```

4、接着使用 vim 的输入模式，加上一行代码：     
![](\img\in-post\post-python\2023-05-26-python-allure-4.png)      

5、接着使用 `:wq` 保存一下文件，并且使用下面的命令使其生效：      
```
source ~/.bash_profile
```

6、那么现在我们可以确认一下allure环境是否配置好了，输入 allure 看看：
![](\img\in-post\post-python\2023-05-26-python-allure-5.png)       

7、如果出现和上面一样的提示，那么恭喜，此时 allure 环境已经配置完毕了。

<br>
<br>

### 三、allure-pytest 生成测试结果    
allure-pytest 是 pytest 的第三方插件，为了支持 allure 实现的一个插件，他可以帮助我们保存用例的执行结果，供 allure 使用。     


1、安装：         
```
pip install allure-pytest
```

2、安装完成了之后，我们使用 `pytest -h` 命令查看一下，会多出一些命令选项：     
![](\img\in-post\post-python\2023-05-26-python-allure-6.png)      

3、在使用pytest执行测试用例的时候，使用命令：     
```
pytest --alluredir=./allure-results
```

4、当然在此之前，我们还要有测试用例：    
```python
import pytest


def test_001():
    print('test_001')

def test_002():
    print('test_002')

def test_003():
    print('test_003')

def test_004():
    print('test_004')
```

5、运行命令后，可以发现当前目录下多了一个 allure-results 文件夹：       
![](\img\in-post\post-python\2023-05-26-python-allure-7.png)       

6、这里面大概存的就是一些测试的结果数据，有了数据后，我们就可以利用 allure 来生成测试报告。    

<br>
<br>

### 四、allure生成静态测试报告 
1、在有了上面的测试数据后，很简单，我们只需要一条命令就可以生成测试报告了：       
```
 allure generate ./allure-results/ -o ./allure-report/ --clean
```

2、generate 后面跟测试结果数据的目录，-o 跟输出测试报告的目录，--clean 代表每次清空报告数据重新生成。       
运行完后 ，发现目录下又多了一个文件夹：       
![](\img\in-post\post-python\2023-05-26-python-allure-8.png)       

3、可以看到，和 pytest-html 一样 ，它也拥有很多的这个样式文件，同时，他还有其他的一些比如说存储数据的文件夹data，存储历史记录的 history 等等，功能非常的多，并且东西也非常的多。我们尝试打开一些 index.html 试试看：     
![](\img\in-post\post-python\2023-05-26-python-allure-9.png)          

4、可以看到现在测试报告已经完美生成了，我们可以查看一下具体的执行记录：    
![](\img\in-post\post-python\2023-05-26-python-allure-10.png)     

<br>
<br>

### 五、allure在线报告   
如果你不想生成大量的静态测试报告资源，或者想在局域网上把测试报告共享给其他人看，那么 allure 也提供了在线的测试报告，我们需要使用如下命令：     
```
allure serve ./allure-results  
```

命令行启动后，会自动打开浏览器：    
![](\img\in-post\post-python\2023-05-26-python-allure-11.png)     

<br>
<br>

---

相关链接：   
[pytest系列——精美的测试报告allure](https://www.modb.pro/db/105194)