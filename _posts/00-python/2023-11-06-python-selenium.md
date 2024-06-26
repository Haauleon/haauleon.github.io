---
layout:        post
title:         "爬虫 | ChromeDriverManager().install()异常处理"
subtitle:      "使用ChromeDriverManager().install()安装ChromeDriverManager失败"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 异常分析
&emsp;&emsp;最近的爬虫项目使用到了 selenium 模块来驱动浏览器进行爬虫，但是今天在公司的服务器上去执行的时候，因为网络的原因，使用 `ChromeDriverManager().install()` 检查并安装最新版本驱动的时候抛出了以下异常：    
```bash
http: error: ConnectionError: HTTPSConnectionPool(
host='chromedriver.storage.googleapis.com', port=443): Max retries exceeded with url: /LATEST_RELEASE_107.0.5304 
(Caused by NewConnectionError( '<urllib3.connection.HTTPSConnection object at 0x7fd46be37730>: Failed to 
establish a new connection: [Errno 101] Network is unreachable')) while doing a GET request to URL: 
https://chromedriver.storage.googleapis.com/LATEST_RELEASE_107.0.5304
```

&emsp;&emsp;我在我自己的电脑本地直接去访问 [https://chromedriver.storage.googleapis.com/LATEST_RELEASE_107.0.5304](https://chromedriver.storage.googleapis.com/LATEST_RELEASE_107.0.5304) 是没问题的，但是服务器就一直访问异常。     

<br>
<br>

### 异常处理
&emsp;&emsp;家人们谁懂啊，公司的网络无法访问[http://chromedriver.storage.googleapis.com/index.html](http://chromedriver.storage.googleapis.com/index.html)。考虑到被驱动的 Chrome 浏览器版本是固定的不需要更新，所以驱动也不需要更新，解决方法就是直接指定本地已有的驱动版本和驱动存放的目录即可。以下是 107.0.5304.62 版本的驱动 `chromedriver_linux64.zip` 存放的绝对路径 `src/driver/107.0.5304.62`：    
```bash
.
|-- Dockerfile
|-- README.md
|-- cache
|-- chatgpt_t.py
|-- common
|-- config
|   |-- __init__.py
|   `-- setting.ini
|-- db_model
|-- deploy.yaml
|-- files
|-- job
|-- logs
|-- model
|-- request
|-- requirements.txt
|-- response
|-- run_amazan_dog_spider.py
|-- run_amazon_product_spider.py
|-- run_keepa_spider.py
|-- sources.list
|-- src
|   |-- driver
|   |   |-- 107.0.5304.62
|   |   |   |-- chromedriver
|   |   |   |-- chromedriver_linux64.zip
|   |   |   |-- drivers
|   |   |   |   `-- chromedriver
|   |   |   |       `-- linux64
|   |   |   |           `-- 107.0.5304.62
|   |   |   |               |-- chromedriver
|   |   |   |               `-- driver.zip
|   |   |   `-- drivers.json
|   |   |-- 114.0.5735.90
|   |   |   `-- chromedriver_linux64.zip
|   |   |-- drivers
|   |   |   `-- chromedriver
|   |   |       `-- linux64
|   |   |           |-- 107.0.5304.62
|   |   |           |   |-- chromedriver
|   |   |           |   `-- driver.zip
|   |   |           `-- 114.0.5735.90
|   |   |               |-- LICENSE.chromedriver
|   |   |               |-- chromedriver
|   |   |               `-- driver.zip
|   |   `-- drivers.json
|   `-- google-chrome-stable_deb_rpm_107.0.5304.122
|       |-- google-chrome-stable_current_amd64.deb
|       `-- google-chrome-stable_current_x86_64.rpm
|-- task
|   |-- __init__.py
|   `-- keepa_comment_get.py
|-- url_t.py
`-- utils

43 directories, 228 files

```

<br>

#### Linux系统
实现方法：            
（1）将文件 `chromedriver_linux64.zip` 放在目录 `src/driver/107.0.5304.62` 下      
（2）进入该目录：            
```bash
> cd src/driver/107.0.5304.62
```
（3）解压该文件：    
```bash
> unzip chromedriver_linux64.zip
```
（4）拷贝到 bin 目录下：            
```bash
> cp chromedriver /usr/bin/
```
（5）在代码中指定该驱动的版本号和存放的绝对路径：              
```python
import os


_SLASH = os.sep
# chromedriver存放的绝对路径（在项目中存放的位置）
driver_path = os.path.join(root_path, 'src' + _SLASH + 'driver' + _SLASH + '107.0.5304.62' + _SLASH + 'chromedriver')


def start_driver():
    chrome_options = webdriver.ChromeOptions()
    # 禁止浏览器加载图片，提高运算速度
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    # 服务器运行方式一：将chromedriver拷贝到/usr/bin下
    # driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)
    # 服务器运行方式二：指定chromedriver在项目中存放的位置
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    return driver

```

<br>

&emsp;&emsp;最后执行就会提示从缓存中加载已有的驱动：      
```bash
[WDM] - Current google-chrome version is 107.0.5304
[WDM] - Driver [/home/xxx/Spider/keepa-test/src/driver//drivers/chromedriver/linux64/107.0.5304.62/chromedriver] found in cache

[WDM] - Current google-chrome version is 107.0.5304
[WDM] - Driver [/home/xxx/Spider/keepa-test/src/driver//drivers/chromedriver/linux64/107.0.5304.62/chromedriver] found in cache

[WDM] - Current google-chrome version is 107.0.5304
[WDM] - Driver [/home/xxx/Spider/keepa-test/src/driver//drivers/chromedriver/linux64/107.0.5304.62/chromedriver] found in cache

[WDM] - Current google-chrome version is 107.0.5304
[WDM] - Driver [/home/xxx/Spider/keepa-test/src/driver//drivers/chromedriver/linux64/107.0.5304.62/chromedriver] found in cache

[WDM] - Current google-chrome version is 107.0.5304
[WDM] - Driver [/home/xxx/Spider/keepa-test/src/driver//drivers/chromedriver/linux64/107.0.5304.62/chromedriver] found in cache

.......
```

<br>
<br>

#### windows系统
在代码中指定该驱动的版本号和存放的绝对路径：               
```python
import os


_SLASH = os.sep
# chromedriver.exe存放的绝对路径（在项目中存放的位置）
driver_path = os.path.join(root_path, 'src' + _SLASH + 'driver' + _SLASH + '107.0.5304.62' + _SLASH + 'chromedriver.exe')


def start_driver():
    chrome_options = webdriver.ChromeOptions()
    # 禁止浏览器加载图片，提高运算速度
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    # windows系统运行方式一：如果能正常访问网络，就直接使用ChromeDriverManager进行安装
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    # windows系统运行方式二：指定chromedriver在项目中存放的位置（公司网络垃圾就使用以下代码）
    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    return driver

```

<br>
<br>

---

相关链接：              
[Web自动化框架selenium的介绍与使用](http://code.newban.cn/292.html)         
[“Webdrivers”可执行文件可能具有错误的权限。请看https://sites.google.com/a/chromium.org/chromedriver/home](https://www.cnpython.com/qa/1283323)                
[我无法使用ChromeDriverManager().install()安装ChromeDriverManager](https://www.5axxw.com/questions/content/25zj8m)            
[当webdriver遇到“' executable may have wrong permissions. ”](https://www.jianshu.com/p/109aa204f58d)