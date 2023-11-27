---
layout:        post
title:         "Debian | Ubuntu/Debian Server 系统安装/升级/删除 Google Chrome"
subtitle:      "下载、安装旧版的 chrome 浏览器和 chromedriver 用于无头模式下运行 selenium 爬虫程序"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - 操作系统
    - Ubuntu
    - Linux
    - Debian
    - 爬虫
---


### 一、背景
&emsp;&emsp;目前有如下需求，在 Debian 服务器上搭建一个用于执行 selenium 自动化爬虫的程序，而程序的执行依赖<mark>google chrome 浏览器</mark>和<mark>chromedriver 驱动</mark>的支持。截止至今日 2023 年 8 月 28 日，chromedriver 的版本只更新到 114，不支持最新 116 版本的 chrome 浏览器。因此，需要下载旧版的 chrome 浏览器和与之相匹配的 chromedriver 驱动版本。      

<br>
<br>

### 二、下载和安装
当前使用的是基于 Linux 的 5.10.0-16-amd64 #1 SMP Debian 5.10.127-1 (2022-06-30) x86_64 的 Debian 服务器。     

<br>

#### 1、下载安装旧版的chrome浏览器
目前网上的方法是直接执行以下命令用于下载最新版本的 chrome 浏览器，但是 chromedriver 驱动的最新版本还停留在 114 ，直接导致 chrome 浏览器版本和 chromedriver 版本不匹配：             
```bash
> wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

（1）下载旧版的 chrome 浏览器         
因此，请使用以下离线方式下载旧版的 chrome 浏览器的 deb 安装包：      
链接：https://pan.baidu.com/s/1KpWuS-l57pBIwguic57lTQ?pwd=x4ez                
提取码：x4ez            

（2）解压文件并上传至服务器            
解压后将整个目录 google-chrome-stable_deb_rpm_107.0.5304.122 使用 FileZilla 上传到服务器                                 

（3）进入 google-chrome-stable_deb_rpm_107.0.5304.122 目录            
```bash
> cd google-chrome-stable_deb_rpm_107.0.5304.122     
> ls -al 
总用量 185692
drwxr-xr-x  2 root root     4096  8月 28 15:13 .
drwxr-xr-x 17 root root     4096  8月 28 15:17 ..
-rw-r--r--  1 root root 93329504  8月 28 15:13 google-chrome-stable_current_amd64.deb
-rw-r--r--  1 root root 96799808  8月 28 15:13 google-chrome-stable_current_x86_64.rpm
```

（4）使用以下命令行进行安装      
```bash
> sudo dpkg -i --force-depends google-chrome-stable_current_amd64.deb
> apt --fix-broken install
```

（5）检查 chrome 浏览器版本      
```bash
> google-chrome --version
Google Chrome 107.0.5304.121
```

<br>
<br>

#### 2、下载安装chromedriver驱动
下载的驱动版本需要与 chrome 浏览器版本保持一致。     

（1）使用以下命令行进行下载安装     
```bash
> wget https://chromedriver.storage.googleapis.com/107.0.5304.62/chromedriver_linux64.zip
> unzip chromedriver_linux64.zip
> cp chromedriver /usr/bin/
```

（2）检查 chromedriver 驱动版本     
```bash
> chromedriver --version
ChromeDriver 107.0.5304.62 (1eec40d3a5764881c92085aaee66d25075c159aa-refs/branch-heads/5304@{#942})
```

<br>
<br>

#### 3、设置无头模式和无沙箱
```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# 消除 Chrome 正受到自动测试软件的控制提示
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# 设置无头浏览器隐式访问
chrome_options.add_argument('--headless')
# "--no-sandbox" 参数是让 Chrome 在 root 权限下跑
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("www.baidu.com")
driver.quit()
```

<br>
<br>

#### 4、解决urllib3报错
执行 selenium 爬虫脚本后报错信息如下：     
```bash
[WDM] - Current google-chrome version is 107.0.5304
[WDM] - Get LATEST driver version for 107.0.5304
[WDM] - Driver [/root/.wdm/drivers/chromedriver/linux64/107.0.5304.62/chromedriver] found in cache
Traceback (most recent call last):
  File "run.py", line 38, in <module>
    job.goto_comment_page(
  File "/home/ejet/Spider/yizhiyin-keepa/job/job_keepa_comment_get.py", line 57, in goto_comment_page
    self.driver_start()
  File "/home/ejet/Spider/yizhiyin-keepa/job/job_base.py", line 42, in driver_start
    self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/selenium/webdriver/chrome/webdriver.py", line 76, in __init__
    RemoteWebDriver.__init__(
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 157, in __init__
    self.start_session(capabilities, browser_profile)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 252, in start_session
    response = self.execute(Command.NEW_SESSION, parameters)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 319, in execute
    response = self.command_executor.execute(driver_command, params)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/selenium/webdriver/remote/remote_connection.py", line 374, in execute
    return self._request(command_info[0], url, body=data)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/selenium/webdriver/remote/remote_connection.py", line 397, in _request
    resp = self._conn.request(method, url, body=body, headers=headers)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/urllib3/_request_methods.py", line 118, in request
    return self.request_encode_body(
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/urllib3/_request_methods.py", line 217, in request_encode_body
    return self.urlopen(method, url, **extra_kw)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/urllib3/poolmanager.py", line 432, in urlopen
    conn = self.connection_from_host(u.host, port=u.port, scheme=u.scheme)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/urllib3/poolmanager.py", line 303, in connection_from_host
    return self.connection_from_context(request_context)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/urllib3/poolmanager.py", line 328, in connection_from_context
    return self.connection_from_pool_key(pool_key, request_context=request_context)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/urllib3/poolmanager.py", line 351, in connection_from_pool_key
    pool = self._new_pool(scheme, host, port, request_context=request_context)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/urllib3/poolmanager.py", line 265, in _new_pool
    return pool_cls(host, port, **request_context)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/urllib3/connectionpool.py", line 196, in __init__
    timeout = Timeout.from_float(timeout)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/urllib3/util/timeout.py", line 190, in from_float
    return Timeout(read=timeout, connect=timeout)
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/urllib3/util/timeout.py", line 119, in __init__
    self._connect = self._validate_timeout(connect, "connect")
  File "/home/ejet/Spider/yizhiyin-keepa/venv/lib/python3.8/site-packages/urllib3/util/timeout.py", line 156, in _validate_timeout
    raise ValueError(
ValueError: Timeout value connect was <object object at 0x7fecd4755090>, but it must be an int, float or None.
```

解决办法：把 urllib3 版本降级到 1.26.2 后，错误全部消失。             
```bash
> pip show urllib3
> pip uninstall urllib3
> pip install urllib3==1.26.2
```

<br>
<br>

#### 5、卸载chrome浏览器
```bash
> apt-get purge google-chrome-stable
> apt-get autoremove
```

<br>
<br>

---

相关链接：     
[Debian9安装旧版Chrome](https://codeleading.com/article/503896546/#google_vignette)        
[立即下载 chrome_linux64_stable_107.0.5304.122](https://www.chromedownloads.net/chrome64linux-stable/1295.html)               
[Ubuntu/Debian Server 系统安装/升级/删除Google Chrome](https://pylist.com/topic/230.html)                   
[Python中使用Selenium遇到ValueError: Timeout value connect错误解决方法](https://www.iotword.com/13889.html)