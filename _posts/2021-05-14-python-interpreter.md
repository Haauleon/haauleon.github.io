---
layout:        post
title:         "Python3 | 常见的解释器"
subtitle:      "用的最多的是 CPython 和 IPython"
date:          2021-05-14
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - Pythoneer
---

## 背景
&emsp;&emsp;Python 是一门解释性语言，也是就需要依赖解释器去运行。换句话说，一个 `xxx.py` 文件需要 Python 解释器去执行。       

&emsp;&emsp;目前用的最多的是 CPtyhon 和 IPython。CPtyhon 解释器在命令行下执行文件，而 IPython 解释器我是在 VSCode 里面装的一个插件，每次想要在交互式窗口执行文件时就自动启动一个 Jupyter 服务器用来调试代码，Jupyter 还有一个好处就是计算代码运行时间只需要在代码段上方加上 `%%time` 即可。          

<br><br>

## Python 解释器
###### 一、CPython（应用最广）
&emsp;&emsp;其实大部分人开始学习 python 的时候都是用的 CPtyhon 解释器，因为很多课程都会直接告诉你要去 Python 官方网站（[https://www.python.org/](https://www.python.org/)）去下载对应的 Python 版本，也就直接获得了一个官方版本的 CPtyhon 解释器。这个解释器是用 C 语言开发的，所以叫 CPtyhon。使用 CPtyhon 解释器的方式很简单，写好一个 py 文件，直接在终端使用命令行 `$ python3 xxx.py` 即可启动 CPtyhon 解释器。还有一种方式就是打开自带的 IDLE，像这种以 `>>>` 开头的提示符就是 CPtyhon 解释器，我还经常拿来当计算器。                

<br><br>

###### 二、IPython（交互神器）
&emsp;&emsp;IPython 解释器，我个人蛮喜欢用的，因为我经常用 VSCode 写代码，刚好它的插件支持 Jupyter ，我干脆就安装了。一般用来交互式地调试代码，而且它计算代码执行时间也非常简单，只需要在第一行写上 `%%time` 即可。拿来当计算器也挺时髦的，反正所有的解释器都躲不过被我当计算器的命运。           

&emsp;&emsp;除了在 VSCode 里面调试代码，其实更多人是去 IPython 官网（[https://ipython.org/](https://ipython.org/)）下载的，文档地址在 [https://jupyter.readthedocs.io/en/latest/install.html](https://jupyter.readthedocs.io/en/latest/install.html)。       

&emsp;&emsp;说白了就是一种交互式解释器，用 `In [序号]:` 作为提示符。             

<br><br>

###### 三、PyPy（速度最快）
&emsp;&emsp;PyPy 是另一个 Python 解释器，它的目标是执行速度。PyPy 采用 JIT 技术，对 Python 代码进行动态编译（注意不是解释），所以可以显著提高 Python 代码的执行速度。               

&emsp;&emsp;绝大部分 Python 代码都可以在 PyPy 下运行，但是 PyPy 和 CPython 有一些不同，这就导致相同的 Python 代码在两种解释器下执行可能会有不同的结果。如果代码要放到 PyPy 下执行，就需要了解 [PyPy 和 CPython 的不同点](http://pypy.readthedocs.org/en/latest/cpython_differences.html)。            

&emsp;&emsp;PyPy 解释器的官方下载地址：[https://www.pypy.org/](https://www.pypy.org/)。文档地址：[https://doc.pypy.org/en/latest/](https://doc.pypy.org/en/latest/)。        

<br><br>

###### 四、Jython
&emsp;&emsp;Jython 是运行在 Java 平台上的 Python 解释器，可以直接把 Python 代码编译成 Java 字节码执行。没用过，不评价。           

&emsp;&emsp;Jython 解释器的官方下载地址：[https://www.jython.org/](https://www.jython.org/)。           

<br><br>

###### 五、IronPython
&emsp;&emsp;IronPython 和 Jython 类似，只不过 IronPython 是运行在微软 .Net 平台上的 Python 解释器，可以直接把 Python 代码编译成 .Net 的字节码。没用过，不评价。        

&emsp;&emsp;IronPython 解释器的官方下载地址：[https://ironpython.net/](https://ironpython.net/)。

<br><br>

## 结论
&emsp;&emsp;Python 的解释器很多，但使用最广泛的还是 CPython。如果要和 Java 或 .Net 平台交互，最好的办法不是用 Jython 或 IronPython，而是通过网络调用来交互，确保各程序之间的独立性。