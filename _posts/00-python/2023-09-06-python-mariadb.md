---
layout:        post
title:         "数据库 | Mariadb 数据库工具类"
subtitle:      "使用 mariadb 连接 Mariadb 数据库"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - 爬虫
    - 数据库
    - Mariadb
---

### Mariadb 数据库工具类
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   mariadbControl.py 
@Date    :   2023/4/12 16:35
@Function:   Mariadb 数据库工具类

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2023/4/12 16:35         haauleon         1.0           None
"""
import time
import mariadb
from common.log import Logger
from common.setting import ConfigHandler
from common.read_data import data

data_file_path = ConfigHandler.config_path
mariadb_data = data.load_ini(data_file_path)["Mariadb"]

# 数据库配置
DB_CONF = {
    'host': mariadb_data['host'],
    'user': mariadb_data['user'],
    'password': mariadb_data['pwd'],
    'database': mariadb_data['db'],
    'port': 3306
}


class Mariadb:
    """
    Mariadb 数据库工具类
    """

    def __init__(self, db_conf=None):
        if db_conf is None:
            db_conf = DB_CONF
        self.conn = mariadb.connect(**db_conf)
        self.cur = self.conn.cursor()
        if not self.cur:
            raise (NameError, "连接数据库失败")

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def select_db(self, sql):
        """
        查询
        :param sql:
        :return:
        """
        self.cur.execute(sql)
        res_data = self.cur.fetchall()
        return res_data

    def execute_db(self, sql, data=None):
        """
        更新/新增/删除
        :param sql:
        :param data:
        :return:
        """
        for retry_time in range(1, 6):
            try:
                self.cur.execute(sql, data)
                self.conn.commit()
                break
            # # 先检测数据库连接的问题，检测无误则执行SQL语句
            # except mariadb.OperationalError as e:
            #     Logger.error(f'{e} Mariadb数据库连接失败，尝试重新连接')
            #     # 重新连接数据库
            #     self.conn = mariadb.connect(**DB_CONF)
            #     self.cur = self.conn.cursor()
            #     # 重新执行SQL语句
            #     try:
            #         self.cur.execute(sql, data)
            #         Logger.info('SQL语句重新执行成功')
            #     # 捕获SQL语句执行的错误
            #     except mariadb.ProgrammingError as e:
            #         Logger.error(f'{e} Mariadb捕获SQL语句执行的错误')
            #         # 重新执行SQL语句
            #         self.cur.execute(sql, data)
            except Exception as e:
                time.sleep(20)
                Logger.warn(f'{e} Mariadb数据库连接失败，尝试重新连接第{retry_time}次')
                self.conn = mariadb.connect(**DB_CONF)
                self.cur = self.conn.cursor()
                if retry_time == 5:
                    Logger.error('Mariadb数据库操作失败，执行回滚')
                    self.conn.rollback()
                    raise


maria = Mariadb()

```

<br>
<br>

### Mariadb 数据库操作基类
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   save_db_base.py 
@Date    :   2023-09-04 15:56
@Function:   数据库操作基类

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2023-09-04 15:56         haauleon         1.0           mariadb数据库新增、更新
"""
from common.log import Logger


class SaveMariaDBBase:

    def __init__(self):
        self.maria = None

    def insert_db_base(self, sql, table_data):
        cols = ",".join('`{}`'.format(i) for i in table_data.__dict__.keys())
        val_cols = ",".join('%({})s'.format(j) for j in table_data.__dict__.keys())
        news_sql = sql % (cols, val_cols)
        Logger.print(f"{table_data.__dict__}")
        self.maria.execute_db(news_sql, table_data.__dict__)

    def update_db_base(self, sql, table_data=None):
        if table_data:
            cols = [i for i in table_data.__dict__.keys()]
            val_cols = [i for i in table_data.__dict__.values()]
            sql = sql % (','.join(list(map(lambda x, y: f"{x}=N'{y}'" if y is not None else f"{x}=NULL", cols, val_cols))))
        Logger.print(sql)
        self.maria.execute_db(sql)

    def insert_db(self, table, table_data):
        sql = f"""insert into {table}(%s) values(%s)"""
        self.insert_db_base(sql, table_data)
        Logger.info(f"{table} 表插入数据成功")

    def update_db(self, sql, table, table_data=None):
        # sql = f"""UPDATE EJ_OrderInfo SET %s WHERE ..."""
        self.update_db_base(sql, table_data)
        Logger.info(f"{table} 表更新数据成功")

```
