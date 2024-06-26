---
layout:        post
title:         "Python3 | f-string字符串格式化"
subtitle:      ""
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
tags:
    - Python
---

&emsp;&emsp;当要处理字符串列表等序列结构时，采用 `join()` 方式；拼接长度不超过 20 时，选用 `+` 号操作符方式；长度超过 20 的情况，高版本选用 `f-string`，低版本时看情况使用 `format()` 或 `join()` 方式。     

```python
# 每种%占位符都有特定意义，实际使用起来太麻烦了
print('%s %s' % ('Hello', 'world'))
# Hello world

# 使用key-value的方式对号入座既不会数错次序，又更直观可读
print('Hello {name1}! My name is {name2}.'.format(name1='World', name2='Python猫'))
# Hello World! My name is Python猫.

# 当拼接的最终字符串长度不超过20时，+号操作符的方式会比join等方式快得多，这与+号的使用次数无关
str_1 = 'Hello world！ '
str_2 = 'My name is Python猫.'
print(str_1 + str_2)
# Hello world！ My name is Python猫.

# 这种方法比较适用于连接序列对象中（例如列表）的元素，并设置统一的间隔符。当拼接长度超过20时，这种方式基本上是首选
str_list = ['Hello', 'world']
str_join1 = ' '.join(str_list)
print(str_join1)
# Hello world

# 特点是在字符串前加 f 标识，字符串中间则用花括号{}包裹其它字符串变量。处理长字符串的拼接时，速度与join()方法相当
name = 'world'
myname = 'python_cat'
words = f'Hello {name}. My name is {myname}.'
print(words)
# Hello world. My name is python_cat.
```