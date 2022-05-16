---
layout:        post
title:         "爬虫 | requests 模块下载图片"
subtitle:      "通过 requests 请求文件链接，将文件下载至本地"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 爬虫
    - Python
    - API 测试
---

参考：[https://www.cnblogs.com/caoyinshan/p/12072847.html](https://www.cnblogs.com/caoyinshan/p/12072847.html)

### 代码设计
```python
import requests
import os


class ConfigHandler:
    _SLASH = os.sep

    # 项目路径
    root_path = os.path.dirname(os.path.abspath(__file__))
    # 图片路径
    img_path = os.path.join(root_path, 'img' + _SLASH)


class IMGHandler:

    @staticmethod
    def download_img(img_url):
        res = requests.get(img_url, stream=True)
        if res.status_code == 200:
            file_path = ConfigHandler.img_path + img_url.rsplit('/', 1)[-1]
            print(file_path)
            with open(file_path, 'wb') as f:
                f.write(res.content)


if __name__ == '__main__':
    IMGHandler.download_img('https://img.alicdn.com/imgextra/i4/2204820661060/O1CN01YGnn5C1JhWX2heNVv_!!2204820661060'
                            '-0-beehive-scenes.jpg')

```