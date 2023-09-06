---
layout:        post
title:         "Python3 | SqlServer 查询重复数据"
subtitle:      "SqlServer 中如何查询重复数据"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - SqlServer
    - 数据库
---

### 查询数据库表中字段重复的记录
```
SqlServer查询重复数据

1.查询单列重复：
select * from test
where name in (select name from test
group by name
having count(name) > 1
)



2.查询多列重复：
SELECT a.* FROM test a,
(
SELECT name,code FROM test
GROUP BY name,code
HAVING COUNT(1)>1
) AS b
WHERE a.name=b.name AND a.code=b.code
```