---
layout:        post
title:         "Python3 | 列表推导式和生成器表达式"
subtitle:      "实现遍历字典每个键，判断该键是否被包含于某个字符串变量中，有则返回键对应的值"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 生成器表达式    
```python
aaa = {'ACP': 25, '包逆算': 30, '快递': 7}
a = '海运ACP25'
next((aaa[k] for k in aaa if re.search(k, a)), None)
# 返回 25
```
&emsp;&emsp;这行代码是 Python中 的一个表达式，‌它使用了生成器表达式（‌generator expression）‌和 `next()` 函数。‌这个表达式的目的是在字典 aaa 中查找与字符串a匹配的键，‌并返回对应的值。‌如果找不到匹配的键，‌则返回 None。‌    
解析这个表达式：‌
1. `aaa`：‌这是一个可迭代对象，‌通常是一个列表或元组，‌包含了要在字典 d 中查找的键。‌      
2. `re.search(k, a)`：‌这是使用正则表达式模块 re 来检查字符串a中是否包含子串 k。‌如果 a 中包含 k，‌`re.search()` 将返回一个匹配对象；‌否则，‌返回 None。‌       
3. `(aaa[k] for k in aaa if re.search(k, a))`：‌这是一个生成器表达式，‌它遍历 aaa中 的每个元素 k，‌检查 a 是否包含 k。‌如果包含，‌就生成字典 d 中对应键 k 的值。‌       
4. `next(..., None)`：‌`next()` 函数用于从生成器中获取下一个元素。‌如果生成器为空（‌即没有找到匹配的键）‌，‌则返回 None。‌        

&emsp;&emsp;综上所述，‌这个表达式的功能是：‌在字典 d 中查找一个键，‌这个键必须是字符串 a 的子串，‌并且这个键必须在列表 aaa 中。‌如果找到了这样的键，‌就返回它对应的值；‌如果没有找到，‌就返回 None。‌     

<br>
<br>

### 列表推导式
```python
aaa = {'ACP': 25, '包逆算': 30, '快递': 7}
a = '海运ACP25'
[aaa[k] for k in aaa if re.search(k, a)]
# 返回 [25]
```
&emsp;&emsp;该列表推导式的功能是：创建一个列表，其中包含所有与字符串 a 匹配的键对应的值，如果 aaa 中没有任何键与 a 匹配，‌则返回一个空列表。‌        

类似的有：     
```python
a = '海运ACP25'
bool([i for i in ['ACP', '包逆算', '快递'] if (i in a)])
# 返回 True
```

<br>
<br>

### 两者区别
`[aaa[k] for k in aaa if re.search(k, a)]` 和 `next((aaa[k] for k in aaa if re.search(k, a)), None)` 这两个表达式在功能上有明显的区别：‌       
1. 返回类型：‌       
- `[d[k] for k in aaa if re.search(k, a)]`：‌这是一个列表推导式，‌它返回一个列表。‌如果 aaa 中有多个键 k 满足 `re.search(k, a)` 为真，‌那么这个列表将包含所有这些键对应的字典 aaa 中的值。‌      
- `next((d[k] for k in aaa if re.search(k, a)), None)`：‌这是一个使用 `next()` 函数的生成器表达式，‌它返回单个值。‌`next()` 函数尝试从生成器中获取下一个元素。‌如果生成器为空（‌即没有找到满足条件的键 k）‌，‌则返回 None。‌        
2. 用途：‌       
- 列表推导式通常用于你需要一个包含所有满足条件元素的列表时。‌       
- `next()` 函数通常用于你只需要找到第一个满足条件的元素时。‌             
3. 性能：‌         
- 列表推导式会遍历整个 aaa，‌并构建一个包含所有满足条件元素的列表。‌这可能会消耗更多的内存和时间，‌特别是当 aaa 很大且有很多满足条件的元素时。‌         
- `next()` 函数在找到第一个满足条件的元素时就会停止遍历，‌因此它通常比列表推导式更快，‌特别是当你只需要找到第一个匹配项时。‌           
4. 使用场景：‌             
- 如果你需要所有匹配项，‌应该使用列表推导式。‌             
- 如果你只需要第一个匹配项，‌或者对性能有较高要求，‌应该使用 `next()` 函数。‌      
