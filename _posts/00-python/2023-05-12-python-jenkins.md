---
layout:        post
title:         "环境搭建 | pip install jenkins 异常解决"
subtitle:      "Microsoft Visual C++ 14.0 or greater is required. Get it with Microsoft C++ Build Tools"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

### 异常
```
> pip install jenkins==1.0.2 -U -i https://pypi.douban.com/simple
Looking in indexes: https://pypi.douban.com/simple
Collecting jenkins==1.0.2
  Using cached https://pypi.doubanio.com/packages/2c/dd/b65fd97de6c3a4aa74d1a92760291b7cd30d84e9729254c6e4cc376cc360/jenkins-1.0.2.tar.gz (8.2 kB)
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: jenkins
  Building wheel for jenkins (setup.py) ... error
  error: subprocess-exited-with-error

  × python setup.py bdist_wheel did not run successfully.
  │ exit code: 1
  ╰─> [1 lines of output]
      error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for jenkins
  Running setup.py clean for jenkins
Failed to build jenkins
ERROR: Could not build wheels for jenkins, which is required to install pyproject.toml-based projects
```

<br>
<br>

### 原因
#### 报错信息翻译    
错误：需要 Microsoft Visual C++14.0 或更高版本。使用 “Microsoft C++构建工具” 获取：https://visualstudio.microsoft.com/visual-cpp-build-tools/       
注意：此错误源于子流程，可能不是 pip 的问题。      

错误：旧版安装失败     
×在尝试安装程序包时遇到错误。     

╰─> jpype1      

注意：这是上述软件包的问题，而不是 pip。    
提示：请参阅上面的故障输出。        

<br>

#### 报错原因
想要 pyhanlp 安装需要先安装 Jpype（Jpype 是使用 Python 调用 Java 的工具包）和 安装 Microsoft C++ 生成工具 - Visual Studio        

<br>
<br>

### 解决方法     
#### 安装 jdk8
1、确认 jdk 已安装，否则安装 jdk（注意：安装 JDK 时，注意添加系统变量和环境变量）        
下载链接：[https://www.oracle.com/technetwork/java/javase/downloads/index.html](https://www.oracle.com/technetwork/java/javase/downloads/index.html)        

<br>

#### 安装 Jpype
1、安装 Jpype（Jpype 是使用 Python 调用 Java 的工具包）        
下载链接：[https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype](https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype)       

<br>

2、Jpype 版本要注意下载版本和你的 python 版本需要一致。      
![](https://img-blog.csdnimg.cn/e5ca90a046ef4e92882a7171084e1157.png)      

<br>

3、下载完成后 cd 切换到文件路径下，pip install +下载的文件名，即可安装       
```
pip install JPype1-1.4.0-cp38-cp38-win_amd64.whl
```
![](https://img-blog.csdnimg.cn/a640b8e3fba7472fb5e6d1c34a54e579.png)

<br>

#### 安装 Visual Studio
1、安装 Microsoft C++ 生成工具 - Visual Studio      
下载链接：[https://visualstudio.microsoft.com/zh-hans/visual-cpp-build-tools/](https://visualstudio.microsoft.com/zh-hans/visual-cpp-build-tools/)      
![](https://img-blog.csdnimg.cn/bc4728f8f3d54d9f9e43aa33e8ad47a9.png)    

<br>

2、勾选使用 c++ 的桌面开发      
![](https://img-blog.csdnimg.cn/5203fed1f80c41eba257ad1ea7740c54.png)     

<br>

3、等待下载安装成功     
![](https://img-blog.csdnimg.cn/65095b51775e4d7b8c18e89d0353ab3b.png)     

<br>

#### 重新执行 pip install 命令

