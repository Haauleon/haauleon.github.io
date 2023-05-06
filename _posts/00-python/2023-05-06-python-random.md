---
layout:        post
title:         "Python3 | 使用 random 生成随机数"
subtitle:      "使用 Python3 中的 random 库生成随机数、随机小数、随机序列、随机字符串以及扑克洗牌等方法"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 一、生成随机浮点数或小数
1、生成 0-1 之间的浮点数    
```python
import random
rnd = random.random()
print(rnd)
```

输出   
```
0.4116634571675989
```

<br>

2、生成 0-1 之间的浮点数，2位精度     
```python
rnd = round(random.random(),2)
print(rnd)
```

输出    
```
0.86
```

<br>

3、生成 `[1,100]` 之间的浮点数；       
```python
rnd = round(random.uniform(1, 100),2)
print(rnd)
```

<br>

4、生成 `[1,100]` 之间的浮点数，2位精度     
```python
rnd = round(random.uniform(1, 100),2)
print(rnd)
```

输出   
```
81.31
```

<br>
<br>

### 二、生成整数、奇数、偶数
1、生成 `[1,100]` 之间的整数     
```python
rnd = random.randint(1, 100)
print(rnd)
```

输出     
```
79
```

<br>

2、生成 `[1,100]` 之间的整数，加百分号     
```python
rnd = str(random.randint(1, 100)) + "%"
print(rnd)
```

输出    
```
87%
```

<br>

3、生成 `[1,100]` 之间的奇数   
```python
rnd = random.randrange(1, 100, 2)
print(rnd)
```

输出    
```
93
```

<br>

4、生成 `[2,100]` 之间的偶数   
```python
rnd = random.randrange(2, 100, 2)
print(rnd)
```

输出    
```
26
```

<br>
<br>

### 三、序列中随机取元素
1、从序列中随机取一个元素     
```python
rnd = random.choice(['剪刀', '石头', '布'])
print(rnd)
```

输出   
```
剪刀
```

<br>
<br>

### 四、生成随机字符串
1、生成字母数字组成的32位密钥，来源 比特量化      
```python
rnd = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',32))
print(rnd)
```

输出
```
43bFuQln6fkGjmH1OCE9aweLz08WTsIA
```

<br>
<br>

### 五、扑克洗牌
1、扑克洗牌，来源 比特量化     
```python
poker = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
random.shuffle(poker)
print(poker)
```

输出    
```
['9', 'A', '10', 'K', 'Q', '3', '6', 'J', '4', '7', '5', '8', '2']
```

<br>
<br>

---

相关链接：    
[Python3使用random生成随机数](https://zhuanlan.zhihu.com/p/499743218)