---
layout:        post
title:         "Python3 | SqlServer 插入单引号"
subtitle:      "SqlServer 中如何向数据库插入带有单引号（'）的字符串"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
    - SqlServer
    - 数据库
---


### SqlServer 插入单引号
相关链接：    
[SqlServer如何向数据库插入带有单引号（'）的字符串](https://www.bbsmax.com/A/gVdnljNXJW/)    

<br>
<br>

在 SqlServer 中执行如下 SQL 语句会抛出异常
```
UPDATE tablename SET Country='US',Province='MO',City='Lee's Summit',Address1='',Address2='',Address3='',PostCode='64086',Telephone='',isSpider='1' WHERE ClientOrderCode='xxx'
```

```
UPDATE tablename SET Country='US',Province='MO',City='Lee's Summit',Address1='',Address2='',Address3='',PostCode='64086',Telephone='',isSpider='1' WHERE ClientOrderCode='xxx'
> Msg 102, Level 15, State 1, Server DataServer002, Procedure , Line 0
“s”附近有语法错误。
> Msg 105, Level 15, State 1, Server DataServer002, Procedure , Line 0
字符串 '' 后的引号不完整。
> [42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]“s”附近有语法错误。 (102)
[42000] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]字符串 '' 后的引号不完整。 (105)
```

<br>

原因：    
`'Lee's Summit'` 中的单引号 `'s` 导致了异常。正确的 SqlServer 语法如下：   
```
UPDATE tablename SET Country='US',Province='MO',City='Lee''s Summit',Address1='',Address2='',Address3='',PostCode='64086',Telephone='',isSpider='1' WHERE ClientOrderCode='xxx'
```

<br>

解决方法：   
```python
str.replace("'", "''")   # 将单引号 ' 替换成两个单引号 '' 就可以解决 
```