---
layout:        post
title:         "Python3 | JSON 和字符串之间的转换与读写"
subtitle:      "字典与json间、列表与json间、字符串与json间的转换以及字典或列表读写到json文件等"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 一、字典（JSON 对象）与JSON字符串的转换
#### 1.字典转JSON字符串
```python
import json

student = {"name": "张三", "age": 18, "gender": "男"}
# 将字典转成json字符串
jsonStr = json.dumps(student, ensure_ascii=False)
print(type(jsonStr))

```

输出结果：   
```bash
<class 'str'>
```

<br>
<br>

#### 2.JSON字符串转字典
```python
import json

studentStr = '{"name": "张三", "age": 18, "gender": "男"}'
# 将字符串转成字典
jsonDict = json.loads(studentStr)
print(type(jsonDict))

```

输出结果：   
```bash
<class 'dict'>
```

<br>
<br>

### 二、列表（JSON 数组）与JSON字符串的转换
#### 1.列表转JSON字符串
```python
import json

students = [{"name": "张三", "age": 18, "gender": "男"},{"name": "刘霜", "age": 19, "gender": "女"}]
# 将列表转成json字符串
jsonStr = json.dumps(students, ensure_ascii=False)
print(type(jsonStr))

```

输出结果：   
```bash
<class 'str'>
```

<br>
<br>

#### 2.JSON字符串转列表
```python
import json

studentsStr = '[{"name": "张三", "age": 18, "gender": "男"}, {"name": "刘霜", "age": 19, "gender": "女"}]'
# 将字符串转成列表
jsonList = json.loads(studentsStr)
print(type(jsonList))

```

输出结果：    
```bash
<class 'list'>
```

<br>
<br>

### 三、格式化JSON字符串输出
对于 JSON 字符串，有时候我们不想那么紧凑的打印输出，而是想要根据层级缩进格式化的输出，可以在 `json.dumps()` 方法里加入 `indent` 参数，比如 `indent=2` 每层就会缩进两个空格。     
```python
import json

students = [{"name": "张三", "age": 18, "gender": "男"}, {"name": "刘霜", "age": 19, "gender": "女"}]
# 将列表转成json字符串，并使用 indent=2 每层缩进两个空格
jsonStr = json.dumps(students, ensure_ascii=False, indent=2)
print(jsonStr)

```

输出结果：     
```bash
[
  {
    "name": "张三",
    "age": 18,
    "gender": "男"
  },
  {
    "name": "刘霜",
    "age": 19,
    "gender": "女"
  }
]
```

<br>
<br>

### 四、字典或列表读写到JSON文件
#### 1.写入josn文件
以列表为例      
```python
import json

students = [{"name": "张三", "age": 18, "gender": "男"}, {"name": "刘霜", "age": 19, "gender": "女"}]
with open('F:\pythonTest\myfile.json', 'w', encoding='utf8') as json_file:
    json.dump(students, json_file, ensure_ascii=False, indent=2)

```

<br>
<br>

#### 2.读取josn文件
使用 `json.load` 读取 json 文件，如果文件中是 json 数组读取出来 students 是列表，如果是 json 对象读取出来 students 是字典。             
```python
import json

#如果文件中是json数组读取出来students是列表，如果是json对象读取出来students是字典
with open("F:\pythonTest\myfile.json", "r", encoding='utf-8') as f:
    students = json.load(f)

```

<br>
<br>

### 五、总结

|方法|作用|
|---|---|
|json.dumps()|将python对象编码成Json字符串|
|json.loads()|将Json字符串解码成python对象|
|json.dump()|将python中的对象转化成json储存到文件中|
|json.load()|将文件中的json的格式转化成python对象提取出来|

使用技巧：         
1、要将 python 中的对象（如字典、列表）转换成 json 字符串，使用 json 模块的 json.dumps() 方法。            
2、要将 python 中的对象（如字典、列表）写入文件，使用 json 模块的 json.dump() 方法。              
3、要将 JSON 字符串转成 python 中的对象（如字典、列表），使用 json 模块的 json.loads() 方法。               
4、要将 JSON 文件读取为 python 中的对象（如字典、列表），使用 json 模块的 json.load() 方法。               
5、ensure_ascii 与 indent 参数                 
（1）ensure_ascii=False ：如果字典或列表里有中文，不使用 ensure_ascii=False 参数的话 转化为 JSON 的字符串的时候会被转义为 `\u5f20\u4e09` 这样的字符 （即所有非 ASCII 字符都会被转义），所以上面的示例代码里都加了 ensure_ascii=False 来让中文不转义让它正常显示。如果你的字典或列表里没有中文没有非 ASCII 字符，在使用 json.dumps() 方法转成 JSON 字符串的时候可以不用加 ensure_ascii=False。                         
（2）indent=n ：在字典或列表要转成 JSON 字符串转成字符串的时候，如果不想那么紧凑的打印 JSON 字符串，可以加入 indent=n 来格式化缩进 JSON 字符串，其中 n 是每层缩进的空格数。               

<br>
<br>

---

相关链接：   
[Python中JSON字符串转换与读写](https://blog.csdn.net/qq_33697094/article/details/131328465)