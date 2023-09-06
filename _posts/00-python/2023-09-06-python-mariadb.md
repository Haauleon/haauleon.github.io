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