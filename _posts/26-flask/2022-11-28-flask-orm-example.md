---
layout:        post
title:         "Flask Web | 使用 ORM"
subtitle:      "ORM 是基于 SQLAlchemy 表达式语言的"
author:        "Haauleon"
header-img:    "img/in-post/post-flask/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Flask
    - Python
    - Web开发
    - 数据库
    - ORM
    - SQLAlchemy
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、使用 ORM
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     


&emsp;&emsp;ORM 是基于 SQLAlchemy 表达式语言的，如下代码示例：     
```python
# coding=utf-8
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker

from consts import DB_URI    # 导入数据库连接配置

eng = create_engine(DB_URI)  # 配置数据库
Base = declarative_base()    # 构造基类


class User(Base):
    """定义的 User 类会生成一张表，__tablename__ 的值就是表名"""

    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'),
                primary_key=True, autoincrement=True)   # Sequence`object 表示数据库序列的名称和配置参数。
    name = Column(String(50))


Base.metadata.drop_all(bind=eng)    # 删除全部表（实际工作时不要这样用）
Base.metadata.create_all(bind=eng)  # 创建多个表


# 通过 sessionmaker 创建一个会话与数据库建立连接，会话提供了事务控制的支持
Session = sessionmaker(bind=eng)
session = Session()

"""
session.add_all() 可以将给定的模型实例对象的集合加入到会话中

因为模型实例对象本身独立存在，若想要其修改（创建）生效，需要将它们加入某个会话；
若不想生效则去掉由 session 管理的实例对象
"""
session.add_all([User(name=username)
                 for username in ('xiaoming', 'wanglang', 'lilei')])

session.commit()  # 修改被提交到数据库
# session.rollback  # 回滚变更


def get_result(rs):
    print '-' * 20
    for user in rs:
        print user.name


# 示例一、查询表 users 中全部的记录
rs = session.query(User).all()
get_result(rs)
# 示例二、查询 id 包含 [2, ] 的记录，此处查询 id=2。若为 [2, 3, 4] 则查询 id=2,id=3,id=4 的记录
rs = session.query(User).filter(User.id.in_([2, ]))
get_result(rs)
# 示例三、查询 id>2 and id<4 的记录
rs = session.query(User).filter(and_(User.id > 2, User.id < 4))
get_result(rs)
# 示例四、查询 id=2 or id=4 的记录
rs = session.query(User).filter(or_(User.id == 2, User.id == 4))
get_result(rs)
# 示例五、模糊查询 like
rs = session.query(User).filter(User.name.like('%min%'))
get_result(rs)
# 示例六、查询 name='xiaoming' 的记录
user = session.query(User).filter_by(name='xiaoming').first()
get_result([user])
```

<br>

#### 1、条件查询语句示例   
&emsp;&emsp;如上代码所示，使用 create_engine() 配置数据库，使用 sessionmaker() 创建会话与数据库建立连接
```python
# 示例一、查询表 users 中全部的记录
rs = session.query(User).all()
get_result(rs)
# 示例二、查询 id 包含 [2, ] 的记录，此处查询 id=2。若为 [2, 3, 4] 则查询 id=2,id=3,id=4 的记录
rs = session.query(User).filter(User.id.in_([2, ]))
get_result(rs)
# 示例三、查询 id>2 and id<4 的记录
rs = session.query(User).filter(and_(User.id > 2, User.id < 4))
get_result(rs)
# 示例四、查询 id=2 or id=4 的记录
rs = session.query(User).filter(or_(User.id == 2, User.id == 4))
get_result(rs)
# 示例五、模糊查询 like
rs = session.query(User).filter(User.name.like('%min%'))
get_result(rs)
# 示例六、查询 name='xiaoming' 的记录
user = session.query(User).filter_by(name='xiaoming').first()
get_result([user])
```

查询结果如下：     
```
--------------------
xiaoming
wanglang
lilei
--------------------
wanglang
--------------------
lilei
--------------------
wanglang
--------------------
xiaoming
--------------------
xiaoming
```