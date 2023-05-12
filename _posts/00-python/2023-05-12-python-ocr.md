---
layout:        post
title:         "Python3 | Web UI 自动化项目使用图像识别"
subtitle:      "通过运行前后的图像识别自动校对，找出图像差异，免去人工校验截图"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 图像识别
---

### 一、前言
&emsp;&emsp;图像识别 ocr 在自动化测试项目中的应用包括程序运行前后的图像自动识别校对。大致思路是，先录制一组正确的 UI 自动化截图，然后在回归测试时将运行后的截图与之前正确的截图进行对比，找出两次运行的差异，从而判断回归测试有无问题。该功能的加入，免去了运行后人工校验截图，使得测试工程师把注意力放在业务流程上。     

<br>
<br>

### 二、环境搭建
环境搭建：   
```
Python 3.8.10      
pip 21.1.1      
java version "1.8.0_181"       
```

项目依赖的 python 模块：      
```
$ pip install imutils==0.5.4
$ pip install scikit-image==0.20.0
$ pip install numpy==1.24.2
$ pip install ddddocr==1.4.7
```

<br>

#### 1、其他事宜
`scikit-image==0.20.0` 为高版本，如若要安装老版本，可以使用以下方法安装：    
```
$ pip install scikit-image==0.15.0 -U -i https://pypi.tuna.tsinghua.edu.cn/simple
```

详见：[https://pypi.tuna.tsinghua.edu.cn/simple/scikit-image/](https://pypi.tuna.tsinghua.edu.cn/simple/scikit-image/)      

<br>

#### 2、报错处理
```python
from skimage.measure import compare_ssim
```

报错信息：    
```
cannot import name 'compare_ssim' from 'skimage.measure'
```

解决方法：   
```
原语句 from skimage.measure import compare_ssim
替换成 from skimage.metrics import structural_similarity as compare_ssim
```

<br>

参考链接：    
[cannot import name ‘compare_ssim‘ from ‘skimage.measure‘](https://blog.csdn.net/weixin_43334838/article/details/118481019)       
[ImportError: cannot import name ‘compare_ssim‘ from ‘skimage.measure‘解决办法](https://blog.csdn.net/mathematican/article/details/123005581)      
[scikit-image 0.18.0版本计算PSNR、SSIM、MSE(Python代码)](https://www.ngui.cc/article/show-118476.html?action=onClick)       

<br>
<br>

### 三、代码实现
#### 1、项目结构       
```
web_auto_test
    - case1
        - ocr_py.py
        - test_base.png
        - test_running.png
    - Dingtalk_11111.jpg
    - Dingtalk_22222.jpg
```

<br>

#### 2、代码展示   
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   ocr_py.py 
@Date    :   2023/5/12 11:42
@Function:   None

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2023/5/12 11:42         haauleon         1.0           None
"""
import imutils
# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity as compare_ssim
import cv2
import numpy as np


class MarkDiffImg:
    @staticmethod
    def cv_imread(file_path):
        """
        读取图片（解决路径中含有中文无法读取的问题），一般是直接cv2.imread(filea_path)
        :param file_path:图片的路径
        :return:
        """
        cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
        return cv_img

    def mark_diff_img(self, result, basesnapshot_png, runningsnapshot_png, DiffSnapshot_Dir, casename, name):
        """
        对比图片并标出差异，保存差异图片
        :param basesnapshot_png:
        :param runningsnapshot_png:
        :param DiffSnapshot_Dir:
        :param casename:
        :param name:
        :return:
        """
        # 加载两张图片并将他们转换为灰度：
        image_a = self.cv_imread(basesnapshot_png)
        image_b = self.cv_imread(runningsnapshot_png)
        gray_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
        gray_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)

        # 计算两个灰度图像之间的结构相似度指数：
        (score, diff) = compare_ssim(gray_a, gray_b, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM:{}".format(score))

        # 找到不同点的轮廓以致于我们可以在被标识为“不同”的区域周围放置矩形：
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        # 找到一系列区域，在区域周围放置矩形：
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image_a, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.rectangle(image_b, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 基础快照标出与运行时快照的差异 图片
        diffsnapshot_png_a = DiffSnapshot_Dir + casename + '\\' + name + '_base.png'
        # 运行时快照标出与基础快照的差异 图片
        diffsnapshot_png_b = DiffSnapshot_Dir + casename + '\\' + name + '_running.png'
        # 保存差异图片
        cv2.imencode('.jpg', image_a)[1].tofile(diffsnapshot_png_a)
        cv2.imencode('.jpg', image_b)[1].tofile(diffsnapshot_png_b)
        result["对比快照-基础快照路径"] = diffsnapshot_png_a
        result["对比快照-运行时快照路径"] = diffsnapshot_png_b

        return result



class Result:

    def __init__(self):
        pass


result = Result()
diff = MarkDiffImg()
diff.mark_diff_img(
    result=result.__dict__,
    basesnapshot_png='D:\code\web_auto_test\Dingtalk_11111.jpg',
    runningsnapshot_png='D:\code\web_auto_test\Dingtalk_22222.jpg',
    DiffSnapshot_Dir='D:\code\web_auto_test\\',
    casename='case1',
    name='test'
)
```

<br>
<br>

---

相关链接：    
[opencv教程-图像基本操作](https://baijiahao.baidu.com/s?id=1679069586952135056&wfr=spider&for=pc)      
[python+appium自动化测试-openCV判断图片的相似度](https://juejin.cn/post/6950230148952096781)      
[python+appium自动化测试-openCV判断图片的相似度](https://zhuanlan.zhihu.com/p/376262582)       
[【python+selenium自动化】图像识别技术在UI自动化测试中的实际运用](https://blog.csdn.net/garyyoung123/article/details/127895965)