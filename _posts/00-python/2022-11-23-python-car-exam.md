---
layout:        post
title:         "Python3 | 汉字转语音播报"
subtitle:      "实现科目三灯光模拟考试语音播报，控制台输入并打分"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---

> 本篇所有操作均在基于 Python==3.8.10 且 pip==22.3.1 的环境下完成 

<br>
<br>

### 一、语音播报
#### 1、安装第三方包
```
> pip3 install pyttsx3
> pip3 show pyttsx3
Name: pyttsx3
Version: 2.90
Summary: Text to Speech (TTS) library for Python 2 and 3. Works without internet connection or delay. Supports multiple TTS engines, including Sapi5, nsss, and espeak.
Home-page: https://github.com/nateshmbhat/pyttsx3
Author: Natesh M Bhat
Author-email: nateshmbhatofficial@gmail.com
License: UNKNOWN
Location: 
Requires: comtypes, pypiwin32, pywin32
Required-by:
```

<br>
<br>

### 二、功能实现
#### 1、科三语音播报实现
&emsp;&emsp;脚本实现了科三模拟灯光试题随机播报并进行输入打分的功能。      
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   car_3.py 
@Date    :   2022/11/23 10:23
@Function:   汉字转语音

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2022/11/23 10:23      haauleon         1.0           科三模拟灯光考试
"""
import pyttsx3
import time
import random

# 配置问题列表
questions_list = [
    '请打开前照灯',
    '进入照明良好道路',
    '夜间与机动车会车',
    '同方向近距离跟车行驶',
    '夜间经过有信号灯路口',
    '进入照明不良道路',
    '夜间通过急弯',
    '夜间通过拱桥',
    '夜间通过坡路',
    '夜间超越前方车辆',
    '夜间在路边临时停车',
]


class DrivingTest:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.questions_list = questions_list

    def say(self, text):
        """文字转语音播报"""
        self.engine.say(text)
        self.engine.runAndWait()
        time.sleep(2)  # 自己练习的时候可以调快一点

    def stop(self):
        self.engine.stop()

    @staticmethod
    def get_question(questions):
        """随机选取科三模拟灯光题目"""
        return random.choice(questions)

    def start_exam(self):
        """开始考试"""
        self.say('下面将进行模拟夜间行驶灯光的考试，请在5秒内做出相应的灯光操作')
        for _ in range(5):
            question = self.get_question(self.questions_list)
            self.say(question)
            user_input = input('请输入操作: ')
            if not DrivingScore.find_answer(question, user_input):
                self.say('考试结束，成绩不合格')
                break
            self.questions_list.remove(question)
        self.say('模拟夜间考试完成，请关闭所有灯光')
        self.stop()


class DrivingScore:
    """配置问题答案"""

    @staticmethod
    def find_answer(question: str, user_input: str) -> bool:
        """找到问题答案"""
        is_correct = True
        answer = {
            '请打开前照灯': '近光灯',
            '进入照明良好道路': '近光灯',
            '夜间与机动车会车': '近光灯',
            '同方向近距离跟车行驶': '近光灯',
            '夜间经过有信号灯路口': '近光灯',
            '进入照明不良道路': '远光灯',
            '夜间通过急弯': '远近交替',
            '夜间通过拱桥': '远近交替',
            '夜间通过坡路': '远近交替',
            '夜间超越前方车辆': '远近交替',
            '夜间在路边临时停车': '示宽灯',
        }
        if user_input != answer[question]:
            is_correct = False
        return is_correct


if __name__ == '__main__':
    t = DrivingTest()
    t.start_exam()
```

实现效果如下：    
```
> python car_3.py
请输入操作: 远近交替
请输入操作: 示宽灯
请输入操作: 远光灯
请输入操作: 远近交替
请输入操作: 远近交替
```

<br>
<br>

#### 2、增加倒计时装饰器
&emsp;&emsp;在上一个版本中增加了语音倒计时功能，也就是增加了一个语音倒计时装饰器，装饰在需要控制台输入的地方。     
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   car_3.py 
@Date    :   2022/11/23 10:23
@Function:   汉字转语音

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2022/11/23 10:23      haauleon         1.0           科三模拟灯光考试
"""
import pyttsx3
import time
import random

questions_list = [
    '请打开前照灯',
    '进入照明良好道路',
    '夜间与机动车会车',
    '同方向近距离跟车行驶',
    '夜间经过有信号灯路口',
    '进入照明不良道路',
    '夜间通过急弯',
    '夜间通过拱桥',
    '夜间通过坡路',
    '夜间超越前方车辆',
    '夜间在路边临时停车',
]

site_list = {
    '起步': '请起步，继续完成考试',
    '超车': '请超越前方车辆',
    '会车': '会车',
    '靠边停车': '请靠边停车',
    '人行横道': '通过人行横道',
    '公交车站': '通过公交车站',
    '路口左转': '前方路口左转',
    '学校区域': '通过学校区域',
    '掉头': '前方选择合适地点掉头',
    '路口右转': '前方路口右转',
    '变更车道': '前方请变更车道',
    '直线行驶': '请保持直线行驶',
    '路口直行': '前方路口直行',
    '终点': '终点',
}


def countdown(func):
    """异步5秒倒计时装饰器"""
    def wrapper(*args, **kwargs):
        # func(*args, **kwargs)
        speech = pyttsx3.init()
        for i in range(1, 6).__reversed__():
            speech.say(str(i))
            speech.runAndWait()
            time.sleep(1)
        func(*args, **kwargs)
        speech.runAndWait()
        speech.stop()

    return wrapper


class DrivingTest:

    def __init__(self):
        self.user_input = None
        self.engine = pyttsx3.init()
        self.questions_list = questions_list
        self.site_list = site_list

    def say(self, text):
        """文字转语音播报"""
        self.engine.say(text)
        self.engine.runAndWait()
        # time.sleep(5)

    def stop(self):
        self.engine.stop()

    @staticmethod
    def get_question(questions):
        """随机选取科三模拟灯光题目"""
        return random.choice(questions)

    @countdown
    def get_user_input(self):
        """答题倒计时"""
        self.user_input = input()

    def start_exam(self):
        """开始考试"""
        self.say('下面将进行模拟夜间行驶灯光的考试，请在5秒内做出相应的灯光操作')
        for _ in range(5):
            question = self.get_question(self.questions_list)
            self.say(question)
            self.get_user_input()
            if not DrivingScore.find_answer(question, self.user_input):
                self.say('考试结束，成绩不合格')
                break
            self.questions_list.remove(question)
        self.say('模拟夜间考试完成，请关闭所有灯光')
        # self.stop()


class DrivingScore:

    @staticmethod
    def find_answer(question: str, user_input: str) -> bool:
        """找到问题答案"""
        is_correct = True
        answer = {
            '请打开前照灯': '近光灯',
            '进入照明良好道路': '近光灯',
            '夜间与机动车会车': '近光灯',
            '同方向近距离跟车行驶': '近光灯',
            '夜间经过有信号灯路口': '近光灯',
            '进入照明不良道路': '远光灯',
            '夜间通过急弯': '远近交替',
            '夜间通过拱桥': '远近交替',
            '夜间通过坡路': '远近交替',
            '夜间超越前方车辆': '远近交替',
            '夜间在路边临时停车': '示宽灯',
        }
        if user_input != answer[question]:
            is_correct = False
        return is_correct


if __name__ == '__main__':
    t = DrivingTest()
    t.start_exam()
    t.stop()
```