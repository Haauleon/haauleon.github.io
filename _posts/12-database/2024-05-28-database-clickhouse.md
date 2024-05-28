---
layout:        post
title:         "Python3 | clickhouse 数据库工具类"
subtitle:      "使用 clickhouse_connect 连接 clickhouse 数据库"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - clickhouse
    - 数据库
---

### clickhouse 数据库工具类
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   clickhouseControl.py 
@Date    :   2024-05-27 9:50
@Function:   None

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2024-05-27 9:50         haauleon         1.0           None
"""
import clickhouse_connect
from common.log import Logger
from common.setting import ConfigHandler
from common.read_data import data
data_file_path = ConfigHandler.config_path
clickhouse_data = data.load_ini(data_file_path)["clickhouse"]

# 数据库配置
DB_CONF = {
    'host': clickhouse_data['host'],
    'username': clickhouse_data['user'],
    'password': clickhouse_data['pwd'],
    'database': clickhouse_data['database'],
    'port': clickhouse_data['port']
}


class Clickhousedb:
    """
    Clickhouse 数据库工具类
    """

    def __init__(self, db_conf=None):
        if db_conf is None:
            db_conf = DB_CONF
        self.client = clickhouse_connect.get_client(**db_conf)

    def __del__(self):
        self.client.close()

    def select_db(self, sql):
        """
        查询
        :param sql:
        :return:
        """
        res_data = self.client.query(sql).result_set
        return res_data

    def execute_db(self, sql, data=None):
        """
        更新/新增/删除
        :param sql:
        :param data:
        :return:
        """
        try:
            self.client.command(cmd=sql, parameters=data)
        # 先检测数据库连接的问题，检测无误则执行SQL语句
        except Exception as e:
            Logger.error(e)
            raise


clickhouse = Clickhousedb()

```

<br>
<br>

### clickhouse 数据库操作基类
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   save_db_base.py 
@Date    :   2024-05-27 15:56
@Function:   数据库操作基类

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2024-05-27 15:56         haauleon         1.0           clickhouse数据库新增、更新
"""
from common.log import Logger
from utils.sqlUtils.clickhouseControl import clickhouse


class SaveMariaDBBase:

    def __init__(self):
        self.clickhouse = None

    def insert_db_base(self, sql, table_data):
        cols = ",".join('`{}`'.format(i) for i in table_data.__dict__.keys())
        val_cols = ",".join('%({})s'.format(j) for j in table_data.__dict__.keys())
        news_sql = sql % (cols, val_cols)
        Logger.print(f"news_sql: {news_sql}")
        Logger.print(f"{table_data.__dict__}")
        self.clickhouse.execute_db(news_sql, table_data.__dict__)

    def update_db_base(self, sql, table_data=None):
        if table_data:
            cols = [i for i in table_data.__dict__.keys()]
            val_cols = [i for i in table_data.__dict__.values()]
            sql = sql % (','.join(list(map(lambda x, y: f"{x}='{y}'" if y is not None else f"{x}=NULL", cols, val_cols))))
        Logger.print(sql)
        self.clickhouse.execute_db(sql)

    def insert_db(self, table, table_data):
        sql = f"""insert into {table}(%s) values(%s)"""
        self.insert_db_base(sql, table_data)
        Logger.info(f"{table} 表插入数据成功")

    def update_db(self, sql, table, table_data=None):
        # sql = f"""UPDATE EJ_OrderInfo SET %s WHERE ..."""
        self.update_db_base(sql, table_data)
        Logger.info(f"{table} 表更新数据成功")

```
