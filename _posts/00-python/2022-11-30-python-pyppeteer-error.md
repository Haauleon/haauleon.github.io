---
layout:        post
title:         "Python3 | pyppeteer 报错"
subtitle:      "pyppeteer.errors.PageError: net::ERR_SSL_VERSION_OR_CIPHER_MISMATCH at ..."
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - Windows
---

> 本篇所有操作均在基于 Python==3.8.10 且 pip==22.3.1 的环境下完成 

<br>
<br>


### 一、pyppeteer 执行报错
&emsp;&emsp;使用 pyppeteer 框架写的浏览器自动化脚本执行报错，报错信息如下：     
```
Traceback (most recent call last):
  File "C:/Users/Haauleon/AppData/Roaming/JetBrains/PyCharmCE2022.1/scratches/scratch_1.py", line 324, in <module>
    Run.exec_local()
  File "C:/Users/Haauleon/AppData/Roaming/JetBrains/PyCharmCE2022.1/scratches/scratch_1.py", line 317, in exec_local
    loop.run_until_complete(task)  # 完成事件循环，直到最后一个任务结束
  File "C:\Users\Haauleon\AppData\Local\Programs\Python\Python38\lib\asyncio\base_events.py", line 616, in run_until_complete
    return future.result()
  File "C:/Users/Haauleon/AppData/Roaming/JetBrains/PyCharmCE2022.1/scratches/scratch_1.py", line 257, in main
    await self.increase_more_pageviews()
  File "C:/Users/Haauleon/AppData/Roaming/JetBrains/PyCharmCE2022.1/scratches/scratch_1.py", line 247, in increase_more_pageviews
    await self.goto_page('https://macaoideas.ipim.gov.mo/home')  # 3.1MB
  File "C:/Users/Haauleon/AppData/Roaming/JetBrains/PyCharmCE2022.1/scratches/scratch_1.py", line 223, in goto_page
    await self.page.goto(page_url, timeout=0)
  File "C:\Users\Haauleon\AppData\Local\Programs\Python\Python38\lib\site-packages\pyppeteer\page.py", line 831, in goto
    raise PageError(result)
pyppeteer.errors.PageError: net::ERR_SSL_VERSION_OR_CIPHER_MISMATCH at https://macaoideas.ipim.gov.mo/home
Task was destroyed but it is pending!
task: <Task pending name='Task-47' coro=<wait() running at C:\Users\Haauleon\AppData\Local\Programs\Python\Python38\lib\asyncio\tasks.py:426> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x000002DE78D7CB50>()]> cb=[NavigatorWatcher.__init__.<locals>.<lambda>() at C:\Users\Haauleon\AppData\Local\Programs\Python\Python38\lib\site-packages\pyppeteer\navigator_watcher.py:54]>
```

<br>
<br>

### 二、报错分析
```
pyppeteer.errors.PageError: net::ERR_SSL_VERSION_OR_CIPHER_MISMATCH at https://macaoideas.ipim.gov.mo/home
```
&emsp;&emsp;报错提示指明了是被访问的网站 [https://macaoideas.ipim.gov.mo/home](https://macaoideas.ipim.gov.mo/home) 无法提供安全连接。访问网站时，浏览器会尝试与主机服务器建立连接，检查有效的SSL证书。如果浏览器在验证这些检查时遇到问题，则会产生 ERR_SSL_VERSION_OR_CIPHER_MISMATCH 错误。        

<br>
<br>

### 三、报错处理
#### 1、chromium flags 更新
&emsp;&emsp;由于 pyppeteer 框架在不指定浏览器时，默认使用的是 chromium 浏览器。该浏览器在第一次执行 pyppeteer 脚本时会自动下载安装，用户不需要手动下载。现在找到 chromium 浏览器存放的目录：     

1. Windows 系统下打开 Everything 软件，输入 chrome.exe 进行搜索        
2. 在搜索结果中，找到路径中包含 pyppeteer 的 chrome.exe 程序      
    ![](\img\in-post\post-python\2022-11-30-python-pyppeteer-error-1.jpg)
3. 双击打开 chrome.exe 程序，进入 chromium 浏览器主页      
4. 访问 [https://macaoideas.ipim.gov.mo/home](https://macaoideas.ipim.gov.mo/home)，访问失败      
    ![](\img\in-post\post-python\2022-11-30-python-pyppeteer-error-2.jpg)
5. 在浏览器地址栏输入 chrome://flags 回车后搜索 `TLS` 和 `QUIC` 并进行修改，修改项如下：    
    ```
    Experimental QUIC protocol: Disabled
    TLS 1.3: Enabled(Final)
    ```
    ![](\img\in-post\post-python\2022-11-30-python-pyppeteer-error-3.jpg)
6. 修改完成后重启 chromium 浏览器方可生效     
7. 重启后再次访问 [https://macaoideas.ipim.gov.mo/home](https://macaoideas.ipim.gov.mo/home)，访问成功      
    ![](\img\in-post\post-python\2022-11-30-python-pyppeteer-error-4.jpg)

<br>
<br>

#### 2、pyppeteer 设置浏览器
&emsp;&emsp;以上方法在手动打开 chromium 浏览器访问 [https://macaoideas.ipim.gov.mo/home](https://macaoideas.ipim.gov.mo/home) 时成功，但是在 pyppeteer 脚本执行去自动化访问网站的时候，发现还是无法访问该网站且报错信息不变，检查发现在执行脚本时所启动的 chromium 浏览器依然使用的是默认的 flags 配置，而不是刚刚已经更新过的。     

&emsp;&emsp;换条思路，使用稳定版的 chrome 浏览器去访问 [https://macaoideas.ipim.gov.mo/home](https://macaoideas.ipim.gov.mo/home)，发现访问成功。打开新的标签页访问 chrome://flags 检查 TLS 选项得到如下信息：             
```
Omit TLS client certificates if credential mode disallows

Strictly conform the Fetch spec to omit TLS client certificates if credential mode disallows. Without this flag enabled, Chrome will always try sending client certificates regardless of the credential mode. – Mac, Windows, Linux, ChromeOS, Android, Fuchsia, Lacros
```

&emsp;&emsp;所以，第二种方法就是将 pyppeteer 脚本中默认的 chromium 浏览器（开发版的 chrome）替换为指定的 chrome 浏览器（稳定版的 chrome），这样一来就可以解决自动化脚本执行的报错问题。      

&emsp;&emsp;查看 pyppeteer.launcher 文档，可通过增加设置项 `executablePath` 的方式指定浏览器的路径，文档内容如下：     
```
async def launch(options: dict = None, **kwargs: Any) -> Browser:
    """Start chrome process and return :class:`~pyppeteer.browser.Browser`.
    This function is a shortcut to :meth:`Launcher(options, **kwargs).launch`.
    Available options are:
    * ``ignoreHTTPSErrors`` (bool): Whether to ignore HTTPS errors. Defaults to
      ``False``.
    * ``headless`` (bool): Whether to run browser in headless mode. Defaults to
      ``True`` unless ``appMode`` or ``devtools`` options is ``True``.
    * ``executablePath`` (str): Path to a Chromium or Chrome executable to run
      instead of default bundled Chromium.
    ...
```

1. 查看稳定版 chrome.exe 的文件路径     
    进入浏览器主页，在地址栏输入 chrome://version，找到可执行文件路径并复制        
    ![](\img\in-post\post-python\2022-11-30-python-pyppeteer-error-5.jpg)
2. 更新 pyppeteer 脚本代码，增加 pyppeteer.launch 设置项          
    ```python
    ...
    ...

    async def _init(self):
    """初始化浏览器"""
    self.browser = await launch(
        {
            'executablePath': 'C:\Program Files\Google\Chrome\Application\chrome.exe',
            'headless': True,  # 浏览器是否启用无头模式
            'args': ['--disable-extensions',
                        '--hide-scrollbars',
                        '--disable-bundled-ppapi-flash',
                        '--mute-audio',
                        '--no-sandbox',
                        '--disable-setuid-sandbox',
                        '--disable-gpu',
                        '--disable-infobars',
                        '--proxy-server={}'.format(self.proxy)],
            'dumpio': True,  # 不添加会卡顿,
            'autoClose': True  # 在自动关闭浏览器的时候删除tmp文件
        }
    )

    ...
    ...
    ```
3. 重新执行脚本，执行成功，报错已经解决


<br>
<br>

相关链接：    
[开启 TLS 1.3 加密协议，极速 HTTPS 体验](https://www.cnblogs.com/upyun/p/8296404.html)      
[如何修复ERR SSL VERSION OR CIPHER MISMATCH](https://jingyan.baidu.com/article/9f7e7ec0c8647b6f28155495.html)     
[pyppeteer框架如何指定Chrome浏览器](https://blog.csdn.net/weixin_43343144/article/details/116242289)