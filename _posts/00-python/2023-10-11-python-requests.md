---
layout:        post
title:         "爬虫 | requests 下载图片异常处理"
subtitle:      "HTTPSConnectionPool(host='...', port=443): Max retries exceeded with url"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
---

### 异常描述
&emsp;&emsp;在使用 requests 模块下载亚马逊的图片链接时，抛出了如下异常：     
`2023-10-11 03:56:58,413 [ThreadPoolExecutor-0_0:140300748936960] keepa - [ERROR] 下载文件接口请求异常: HTTPSConnectionPool(host='images-na.ssl-images-amazon.com', port=443): Max retries exceeded with url: /captcha/tinytuux/Captcha_xbothufyms.jpg (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f9a7069da60>: Failed to establish a new connection: [Errno 111] Connection refused'))`     

```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   KeepaCaptchaDownloadModel.py 
@Date    :   2023-08-24 17:17
@Function:   None

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2023-08-24 17:17         haauleon         1.0           None
"""
from request.rest_client import RestClient
from common.log import Logger
import random
import time


class KeepaCaptchaDownloadModel(RestClient):

    def __init__(self, api_root_url):
        super().__init__(api_root_url)

    def keepa_captcha_download(self, download_dir_path):
        """获取留评链接的内容"""
        for count in range(1, 100):
            try:
                res = self.get(download_url, stream=True, timeout=20, verify=False)
                if res.status_code == 200:
                    Logger.info("下载文件接口请求成功")
                    break
            except Exception as e:
                Logger.error(f"下载文件接口请求异常: {e}")
                Logger.warn(f"下载文件接口请求重试第{count}次")
                time.sleep(round(random.random(), 1))

        new_filename = 'captcha.jpg'
        file_path = download_dir_path + new_filename
        # print(file_path)
        with open(file_path, 'wb') as f:
            f.write(res.content)
        Logger.info(f'文件下载存放路径: {file_path}')
        return new_filename, file_path


keepa_captcha_download = KeepaCaptchaDownloadModel("")


if __name__ == '__main__':
    keepa_captcha_download.keepa_captcha_download('D:\\code\\yizhiyin-keepa\\files\\captcha\\', 'https://images-na.ssl-images-amazon.com/captcha/tinytuux/Captcha_pzdfuwjkyv.jpg')

```

<br>
<br>

### 异常处理
&emsp;&emsp;在发送请求是增加参数 `verify=False` 即可解决。      

```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   KeepaCaptchaDownloadModel.py 
@Date    :   2023-08-24 17:17
@Function:   None

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2023-08-24 17:17         haauleon         1.0           None
"""
from request.rest_client import RestClient
from common.log import Logger
import random
import time


class KeepaCaptchaDownloadModel(RestClient):

    def __init__(self, api_root_url):
        super().__init__(api_root_url)

    def keepa_captcha_download(self, download_dir_path, download_url):
        """获取留评链接的内容"""
        for count in range(1, 100):
            try:
                res = self.get(download_url, stream=True, timeout=20, verify=False)
                if res.status_code == 200:
                    Logger.info("下载文件接口请求成功")
                    break
            except Exception as e:
                Logger.error(f"下载文件接口请求异常: {e}")
                Logger.warn(f"下载文件接口请求重试第{count}次")
                time.sleep(round(random.random(), 1))

        new_filename = 'captcha.jpg'
        file_path = download_dir_path + new_filename
        # print(file_path)
        with open(file_path, 'wb') as f:
            f.write(res.content)
        Logger.info(f'文件下载存放路径: {file_path}')
        return new_filename, file_path


keepa_captcha_download = KeepaCaptchaDownloadModel("")


if __name__ == '__main__':
    keepa_captcha_download.keepa_captcha_download('D:\\code\\yizhiyin-keepa\\files\\captcha\\', 'https://images-na.ssl-images-amazon.com/captcha/tinytuux/Captcha_pzdfuwjkyv.jpg')

```

<br>
<br>

---

相关链接：    
[解决HTTPSConnectionPool(host=‘‘, port=443): Max retries exceeded with url: /api/container/ge](https://blog.csdn.net/m0_37772653/article/details/119874338)