---
layout:        post
title:         "谷歌 | 开源 google 翻译 api"
subtitle:      "有一些异常需要处理"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - 小而美脚本
---

> 参考 https://blog.csdn.net/linweidong/article/details/113866543

<br><br>

### 背景
&emsp;&emsp;他们说百度翻译不够地道，然后我就找到了官方的谷歌翻译，一看是收费的就放弃了，后来功夫不负有心人还是找到一个可用的且免费的 google 翻译 api。   

<br><br>

### 开源项目
项目地址：[https://github.com/Saravananslb/py-googletranslation](https://github.com/Saravananslb/py-googletranslation)        

&emsp;&emsp;这个开源项目要求依赖是  Python 3.6+ ，为了使用方便，安装了带 pip 管理工具下载 py-googletranslation。    
```
$ pip install pygoogletranslation==2.0.3
```

<br>

&emsp;&emsp;原来开源项目默认的 google.com 是访问不了的，要做下面修改，或直接找到下载代码，把 google.com 修改为 google.cn 。        
```python
>>> from googletrans import Translator
>>> translator = Translator(service_urls=[
      'translate.google.cn',   
    ])
```

<br><br>

### 代码实现
###### 文件翻译
```python
#!/usr/bin/python
import sys
import time
import os
def main():               
	from pygoogletranslation import Translator
	translator = Translator()
	count = 0
	with open('result.txt', 'w', encoding='gb18030') as df:
	    result = translator.bulktranslate('test.txt', dest="en")
	    df.write(result.text)

if __name__ == "__main__":
	main()
```

<br>

###### 文本翻译
```python
from googletrans import Translator

# 谷歌翻译配置
translator = Translator(service_urls=['translate.google.cn', ])
from pygoogletranslation import Translator

translator = Translator()
trans_text = translator.translate("晚安", dest='en').text
print(trans_text)
```