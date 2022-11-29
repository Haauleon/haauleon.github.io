---
layout:        post
title:         "Flask Web | SQLAlchemy 数据库关联"
subtitle:      "使用外键进行多表关联，保证数据一致性和实现一些级联操作"
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
    - MySQL
---

> 本篇所有操作均在基于 Ubuntu 16.04 LTS 的虚拟机下完成，且使用 Vagrant 来操作虚拟机系统，虚拟机系统 VirtualBox Version: 7.0 

<br>
<br>

### 一、数据库关联
环境准备：     
Python 2.7.11+      
pip==9.0.3     
flask==0.11.1   
httpie==0.9.4     

&emsp;&emsp;InnoDB 类型的表可以使用外键进行多表关联，保证数据的一致性和实现一些级联操作。         
```python
# coding=utf-8
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

from consts import DB_URI

eng = create_engine(DB_URI)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(128), nullable=False)
    # 使用 ForeignKey 外键关联 users 表的 id，所以 address.user_id 其实就是 users.id，而 address 表不需要独立存储一份 user_id 数据
    user_id = Column(Integer, ForeignKey('users.id'))
    # user 字段关联到 User 模型类
    user = relationship('User', back_populates='addresses')


# User.addresses 字段需要放在 Address 模型类定义之后
User.addresses = relationship('Address', order_by=Address.id,
                              back_populates='user')


Base.metadata.drop_all(bind=eng)
Base.metadata.create_all(bind=eng)

Session = sessionmaker(bind=eng)
session = Session()

user = User(name='xiaoming')

user.addresses = [Address(email_address='a@gmail.com', user_id=user.id),
                  Address(email_address='b@gmail.com', user_id=user.id)]
session.add(user)
session.commit()
```

&emsp;&emsp;通过 `> ipython -i` 来执行上面的脚本并继续验证：     
```
(venv) ❯ ipython --no-banner -i chapter3/section3/rel_sql.py

In [1]: for u, a in session.query(User, Address).\
   ...: filter(User.id==Address.user_id).\
   ...: filter(Address.email_address=='b@gmail.com').\
   ...: all():
   ...:     print 'User ID: {}'.format(u.id)
   ...:     print 'Email Address: {}'.format(a.email_address)
   ...:
User ID: 1
Email Address: b@gmail.com

In [2]: session.query(Address).join(User).filter(Address.id.in_([2,])).all()[0].email_address
Out[2]: 'b@gmail.com'

In [3]: session.query(User).join(Address).filter(Address.email_address=='a@gmail.com').one().name
Out[3]: 'xiaoming'
``` 

<br>

&emsp;&emsp;虽然使用外键可以降低开发成本，减少数据量，但是在 **用户量大、并发度高** 的时候，不推荐使用外键来关联，数据的一致性和完整性问题可以通过 **事务** 来保证。