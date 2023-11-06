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
&emsp;&emsp;考虑到被驱动的 Chrome 浏览器版本是固定的不需要更新，所以驱动也不需要更新，解决方法就是在使用 `ChromeDriverManager(version="107.0.5304.62").install()` 来检查和安装最新驱动时，直接指定版本即可：    
```python
def start_driver():
    chrome_options = webdriver.ChromeOptions()
    # 禁止浏览器加载图片，提高运算速度
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    # ChromeDriverManager(version="107.0.5304.62") 增加版本号，解决网络问题
    driver = webdriver.Chrome(ChromeDriverManager(version="107.0.5304.62").install(), options=chrome_options)
    return driver

```

<br>
<br>

---

相关链接：   
[我无法使用ChromeDriverManager().install()安装ChromeDriverManager](https://www.5axxw.com/questions/content/25zj8m)