---
layout:        post
title:         "Python3 | SQLAlchemy学习"
subtitle:      "SQLAlchemy是一个基于Python实现的ORM框架"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - SQLAlchemy
---


### 一、SQLAlchemy简介
&emsp;&emsp;SQLAlchemy 是一个基于 Python 实现的 ORM 框架。该框架建立在 DB API之上，使用关系对象映射进行数据库操作，简言之便是：<mark>将类和对象转换成SQL，然后使用数据 API 执行 SQL 并获取执行结果</mark>。    

<br>

#### 1、与Django中models的区别
&emsp;&emsp;很多小伙伴说 SQLAlchemy 不如 Django 的 models 好用，这里我们需要知道。Models 其实只是配置和使用比较简单，毕竟是 Django 自带的 ORM 框架，但是兼容性远不如 SQLAchemy，真正算得上全面的 ORM 框架必然是 SQLAlchemy。               
&emsp;&emsp;无论使用什么 ORM 框架，其实都是为了方便不熟练数据库使用的同学，最推荐的还是使用原生的 SQL 语句，也建议大家攻克 SQL 难关。          

<br>
<br>

#### 2、SQLAlchemy组成
组成部分：          

|组成|释义|
|---|---|
|Engine|框架的引擎|
|Connection Pooling|数据库连接池|
|Dialect|选择连接数据库的DB API种类|
|Schema/Types|架构和类型|
|SQL Exprression Language|SQL表达式语言|

&emsp;&emsp;SQLAlchemy 本身无法操作数据库，其必须以来 pymsql 等第三方插件，Dialect 用于和数据 API 进行交流，根据配置文件的不同调用不同的数据库 API，从而实现对数据库的操作，如：             
```text
MySQL-Python
    mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
    
pymysql
    mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
    
MySQL-Connector
    mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
    
cx_Oracle
    oracle+cx_oracle://user:pass@host:port/dbname[?key=value&key=value...]
    
更多：http://docs.sqlalchemy.org/en/latest/dialects/index.html
```

<br>
<br>

### 二、SQLAlchemy使用
#### 1、执行原生sql语句
**通过 SQLAlchemy 执行原生的 sql 语句**           

（1）方式一：      
```python
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:123@127.0.0.1:3306/sqlalchemy01?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

def task():
    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute(
        "select * from t1"
    )
    result = cursor.fetchall()
    print(">>>",result)
    cursor.close()
    conn.close()

task()
```

（2）方式二：       
```python
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/sqlalchemy01", max_overflow=0, pool_size=5)


def task():
    conn = engine.connect()
    with conn:
        cur = conn.execute(
            "select * from t1"
        )
        result = cur.fetchall()
        print(result)
        
task()
```

（3）方式三：      
```python
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/sqlalchemy01", max_overflow=0, pool_size=5)


def task():
    cur = engine.execute("select * from t1")
    result = cur.fetchall()
    cur.close()
    print(result)

task()
```

<br>
<br>

#### 2、数据表的操作
**通过 SQLAlchemy 来创建表和删除表**     

```python
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

# 建立基础类 R关系 M映射 类
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'  # 指定创建的表名

    # 写字段
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    email = Column(String(32), unique=True)
    # ctime = Column(DateTime, default=datetime.datetime.now)
    # extra = Column(Text, nullable=True)

    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),  # 设置位移约束
        Index('ix_id_name', 'name', 'email'),  # 设置索引
    )


# 创建数据库的引擎
engine = create_engine(
    "mysql+pymysql://root:123@127.0.0.1:3306/sqlalchemy01?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

# 检索所有继承Base的Object并在 engine 指向的数据库中创建所有的表
Base.metadata.create_all(engine)

# 删除所有的数据库表
Base.metadata.drop_all(engine)
```

（1）单表创建示例                 
```python
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

# 建立基础类 R关系 M映射 类
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'  # 指定创建的表名

    # 写字段
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=False)
    email = Column(String(32), unique=True)
    # ctime = Column(DateTime, default=datetime.datetime.now)
    # extra = Column(Text, nullable=True)

    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),  # 设置位移约束
        Index('ix_id_name', 'name', 'email'),  # 设置索引
    )


# 创建数据库的引擎
engine = create_engine(
    "mysql+pymysql://root:123@127.0.0.1:3306/sqlalchemy01?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

# 检索所有继承Base的Object并在 engine 指向的数据库中创建所有的表
Base.metadata.create_all(engine)

# 删除所有的数据库表
Base.metadata.drop_all(engine)
```

（2）一对多示例              
```python
# ########## 一对多示例 ##########
class School(Base):
    __tablename__ = "school"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    school_id = Column(Integer, ForeignKey("school.id"))  # 多对一关系存储列

    # 与生成表结构无关，仅用于查询方便
    school = relationship("School", backref='student')

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy01?charset=utf8")

# 检索所有继承 Model 的Object 并在 engine 指向的数据库中创建 所有的表
Model.metadata.create_all(engine)
```

（3）多对多表结构创建            
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Girls(Model):
    __tablename__ = "girl"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    # relationship
    g2b = relationship("Boys", backref="b2g", secondary="hotel")


class Boys(Model):
    __tablename__ = "boy"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)


class Hotels(Model):
    __tablename__ = "hotel"
    id = Column(Integer, primary_key=True)
    boy_id = Column(Integer, ForeignKey("boy.id"))
    girl_id = Column(Integer, ForeignKey("girl.id"))

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/sqlalchemy01?charset=utf8")

# 检索所有继承 Model 的Object 并在 engine 指向的数据库中创建 所有的表
Model.metadata.create_all(engine)
```

（4）定义函数来创建和删除表                  
```python
def init_db():
    """
    根据类创建数据库表
    :return:
    """
    engine = create_engine(
        "mysql+pymysql://root:123@127.0.0.1:3306/s6?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.create_all(engine)


def drop_db():
    """
    根据类删除数据库表
    :return:
    """
    engine = create_engine(
        "mysql+pymysql://root:123@127.0.0.1:3306/s6?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.drop_all(engine)


if __name__ == '__main__':
    drop_db()
    init_db()
```

<br>
<br>

#### 3、记录的增删改查
**数据库记录操作的两种方式**              

```python
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Users

engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/s6", max_overflow=0, pool_size=5)
############方式一#############
Session = sessionmaker(bind=engine)

# 每次执行数据库操作时，都需要创建一个session
session = Session()

# ############# 执行ORM操作 #############
obj1 = Users(name="alex1")
session.add(obj1)

# 提交事务
session.commit()
# 关闭session
session.close()

###########方式二###########
# 方式二：支持线程安全，为每个线程创建一个session
#               - threading.Local
#               - 唯一标识
# ScopedSession对象
#       self.registry(), 加括号 创建session
#       self.registry(), 加括号 创建session
#       self.registry(), 加括号 创建session
from greenlet import getcurrent as get_ident

Session = sessionmaker(bind=engine)
session = scoped_session(Session, get_ident)
# session.add
# 操作
session.remove()
```

（1）单表的增删改查              
```python
from day101_sqlAlchemy.SQLAlchemy02_create_table_single import engine,Users
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)  # 新建数据库的查询窗口
db_session = Session()  # 打开查询窗口

# 增加单条数据
# u = Users(name="ryxiong")  # 新建insert语句 insert into
# db_session.add(u)  # 将insert语句移动到 db_session 查询窗口
# db_session.commit()  # 执行查询窗口中的所有语句
# db_session.close()  # 关闭查询窗口

# 增加多条数据
# u_list = [Users(name="egon"),Users(name="alex")]
# db_session.add_all(u_list)  # 添加多条数据
# db_session.commit()
# db_session.close()


# 查询数据
# res = db_session.query(Users).all()  # 查询所有数据
# for user in res:
#     print(user.id,user.name)

# res = db_session.query(Users).first()  # 查询符合条件的第一条数据
# print(res.id,res.name)  # 3 alex

# 并列条件查询
# res = db_session.query(Users).filter(Users.id<3,Users.name=="ryxiong").all()
# for user in res:
#     print(user.id,user.name)  # 1 ryxiong

# res = db_session.query(Users).filter(Users.id<3,Users.name=="ryxiong").first()
# print(res.id,res.name)  # 1 ryxiong


# 修改数据
# db_session.query(Users).filter(Users.id==2).update({"name":"Egon"})
# db_session.commit()

# 删除数据
db_session.query(Users).filter(Users.id==3).delete()
db_session.commit()
```

（2）一对多的增删改查            
```python
from day101_sqlAlchemy.SQLAlchemy03_create_table_foreignKey import engine,Student,School
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)  # 新建数据库的查询窗口
db_session = Session()  # 打开查询窗口

# 增加一条数据
# school = School(name="新东方")
# db_session.add(school)
# db_session.commit()

# 在添加学生
# school_fir = db_session.query(School).filter(School.name=="新东方").first()
#
# student = Student(name="ryxiong",school_id=school_fir.id)
# db_session.add(student)
# db_session.commit()

# 1.添加数据 relationship 正向添加数据
# stu = Student(name="alex",school=School(name="蓝翔"))
# db_session.add(stu)
# db_session.commit()

# 2.添加数据relationship 反向添加数据
# sch = School(name="蓝翔")
# sch.student = [
#     Student(name="egon"),
#     Student(name="wusir")
# ]
# db_session.add(sch)
# db_session.commit()


# 查询
# 1.relationship正向查询
res = db_session.query(Student).all()
for stu in res:
    print(stu.id,stu.name,stu.school.name)

# 2.relationship反向查询
res = db_session.query(School).all()
for sch in res:
    for stu in sch.student:
        print(sch.name,stu.id,stu.name)
```

（3）多对多查询             
```python
from day101_sqlAlchemy.SQLAlchemy04_create_table_M2M import engine,Boys,Girls
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)  # 新建数据库的查询窗口
db_session = Session()  # 打开查询窗口

# 添加数据
# 1.relationship正向添加
# girl = Girls(name="Nancy",boy=[Boys(name="ryxiong"),Boys(name="alex")])
# db_session.add(girl)
# db_session.commit()

# 2.relationship反向添加
# boy = Boys(name="egon")
# boy.girl = [
#     Girls(name="罗玉凤"),
#     Girls(name="朱利安"),
# ]
#
# db_session.add(boy)
# db_session.commit()

# 查询数据

# 1.relationship 正向查询

res = db_session.query(Girls).all()
for girl in res:
    for boy in girl.boy:
        print(girl.name,boy.name)

# 2.relationship 反向查询
res = db_session.query(Boys).all()
for boy in res:
    for girl in boy.girl:
        print(boy.name,girl.name)
```

<br>
<br>

#### 4、记录的高级查询              
```python
from day101_sqlAlchemy.SQLAlchemy02_create_table_single import engine,Users
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_,or_

Session = sessionmaker(engine)  # 新建数据库的查询窗口
db_session = Session()  # 打开查询窗口

# 逻辑条件查询 and/or
# ret1 = db_session.query(Users).filter(and_(Users.id<3,Users.name=="ryxiong")).all()
# print(ret1)
# ret2 = db_session.query(Users).filter(or_(Users.id<2,Users.name=="egon")).all()
# print(ret2)
#
# ret3 = db_session.query(Users).filter(
#     or_(
#         and_(Users.id==1,Users.name=="ryxiong"),
#         and_(Users.id==2,Users.name=="egon")
#     )
# ).all()
# print(ret3)


# 查询所有数据排序
# ret = db_session.query(Users).order_by(Users.id.asc()).all()  # 按照id升序排列
#
# print(ret)


# 查询数据，指定查询数据列，加入别名
# ret = db_session.query(Users.name.label("username"),Users.id).first()
#
# print(ret)  # ('alex', 3)
# print(ret.id,ret.username)  # 3 alex

# 表达式筛选条件
# user_list = db_session.query(Users).filter(Users.name=="ryxiong").all()
# user_list1 = db_session.query(Users).filter_by(name="ryxiong").all()
# for user in user_list:
#     print(user.name)


# 复杂查询
# user_list2 = db_session.query(Users).filter(text("id<:value and name=:name")).params(value=3,name="ryxiong")
# print(user_list2)


# 查询语句
# user_list3 = db_session.query(Users).filter(text("select * from user id<:value and name=:name")).params(value=3,name="ryxiong")
# print(user_list3)


# 其他查询条件
# ret = db_session.query(Users).filter(Users.id.between(1,3)).all()  # 查询id值在1-3之间，不包含3的
# print(ret)
#
# ret1 = db_session.query(Users).filter(Users.id.in_([1,2])).all()  # 查询id在列表[1,2]中的用户
# print(ret1)
#
# ret2 = db_session.query(Users).filter(~Users.id.in_([1,2])).all()  # 查询用户id不在列表[1,2]中的。
# print(ret2)

# 子查询
# ret3 = db_session.query(Users).filter(Users.id.in_(db_session.query(Users.id).filter_by(name="ryxiong"))).all()
# print(ret3)

# 通配符
# ret4 = db_session.query(Users).filter(Users.name.like("%ong")).all()
# print(ret4)
# ret5 = db_session.query(Users).filter(~Users.name.like("%ong")).all()
# print(ret5)


# 切片
# ret6 = db_session.query(Users)[1:2]
# print(ret6)


# 分组 group_by
from sqlalchemy.sql import func
# ret7 = db_session.query(Users).group_by(Users.name).all()
# print(ret7)


# 聚合函数
ret8 = db_session.query(
    func.max(Users.id),
    func.sum(Users.id),
    func.min(Users.id),
).group_by(Users.name).all()
print(ret8)  # [(3, Decimal('3'), 3), (2, Decimal('2'), 2), (1, Decimal('1'), 1)]


ret9 = db_session.query(
    func.max(Users.id),
    func.sum(Users.id),
    func.min(Users.id),
).group_by(Users.name).having(func.min(Users.id)>2).all()
print(ret9)  # [(3, Decimal('3'), 3)]
```

<br>
<br>

---
相关链接：       
[SQLAlchemy学习](https://www.cnblogs.com/ryxiong-blog/p/11278235.html)