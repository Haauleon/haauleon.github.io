---
layout:        post
title:         "正则 | 提取指定范围的信息"
subtitle:      "python3 正则表达式快速提取并返回列表"
date:          2021-05-11
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
---

## 背景
&emsp;&emsp;禅道很多都是直接返回一个 html ，不是 Json 格式的话提取字符串的信息会比较麻烦。比如下面这个 html 字符串：          
```python
"""
<select name='assignedTo' id='assignedTo' class="form-control">
<option value='' selected='selected' title='' data-keys=' '></option>
<option value='chenqiaolun' title='C:陈巧伦' data-keys='c:chenqiaolun ccql'>C:陈巧伦</option>
<option value='huchongyang' title='H:胡重阳' data-keys='h:huzhongyang hhzy'>H:胡重阳</option>
<option value='jiangfenglang' title='J:蒋风浪' data-keys='j:jiangfenglang jjfl'>J:蒋风浪</option>
<option value='macheng' title='M:马成' data-keys='m:macheng mmc'>M:马成</option>
<option value='songbowen' title='S:宋博文' data-keys='s:songbowen ssbw'>S:宋博文</option>
<option value='xuliwei' title='X:许立伟' data-keys='x:xuliwei xxlw'>X:许立伟</option>
<option value='yesidi' title='Y:叶思迪' data-keys='y:yesidi yysd'>Y:叶思迪</option>
<option value='yinmanju' title='Y:尹满菊' data-keys='y:yinmanju yymj'>Y:尹满菊</option>
<option value='zhuangjunxin' title='Z:庄俊鑫' data-keys='z:zhuangjunxin zzjx'>Z:庄俊鑫</option>

"""
```

<br><br>

&emsp;&emsp;我只想要 `value=` 后面的值，于是又和正则表达式握了一次手，其实也只是简单的握了一次手。         

<br><br>

## 代码实现
1. 使用 re 正则表达式中的 compile 函数，在匹配内容的括号中写 `(.*?)`
    * 其中 `.*?` 代表非贪心算法，表示精准的配对
    * 在 `.*?` 的外面加个括号表示获取括号之间的信息
2. 在 `(.*?)` 两边加上原文本中要匹配信息两旁的信息
    * 例如要想获得字符串 `abcdefg` 中的 cd，就要在 `(.*?)` 里面分别加上 ab 和 efg
3. compile 中使用的第二个参数是 re.S，表示正则表达式会将这个字符串作为一个整体，包括 ”\n“，如果不使用 re.S 参数，则只在每一行内进行匹配，如果一行没有，就换下一行重新开始，不会跨行
4. compile() 函数返回的是一个匹配对象，单独使用无意义，需要和 `findall()` 函数搭配使用，返回的是一个列表


```python
# 要匹配的字符串对象
str_txt = """
<select name='assignedTo' id='assignedTo' class="form-control">
<option value='' selected='selected' title='' data-keys=' '></option>
<option value='chenqiaolun' title='C:陈巧伦' data-keys='c:chenqiaolun ccql'>C:陈巧伦</option>
<option value='huchongyang' title='H:胡重阳' data-keys='h:huzhongyang hhzy'>H:胡重阳</option>
<option value='jiangfenglang' title='J:蒋风浪' data-keys='j:jiangfenglang jjfl'>J:蒋风浪</option>
<option value='macheng' title='M:马成' data-keys='m:macheng mmc'>M:马成</option>
<option value='songbowen' title='S:宋博文' data-keys='s:songbowen ssbw'>S:宋博文</option>
<option value='xuliwei' title='X:许立伟' data-keys='x:xuliwei xxlw'>X:许立伟</option>
<option value='yesidi' title='Y:叶思迪' data-keys='y:yesidi yysd'>Y:叶思迪</option>
<option value='yinmanju' title='Y:尹满菊' data-keys='y:yinmanju yymj'>Y:尹满菊</option>
<option value='zhuangjunxin' title='Z:庄俊鑫' data-keys='z:zhuangjunxin zzjx'>Z:庄俊鑫</option>
</select>
          """
# print(str_txt)
comment = re.compile(r"value='(.*?)'",re.S)
comment1 = comment.findall(str_txt)
print(comment1)
```

<br><br>

运行结果：           
```
['', 'chenqiaolun', 'huchongyang', 'jiangfenglang', 'macheng', 'songbowen', 'xuliwei', 'yesidi', 'yinmanju', 'zhuangjunxin']
```