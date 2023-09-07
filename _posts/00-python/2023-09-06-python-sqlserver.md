---
layout:        post
title:         "Python3 | SQL Server 数据库工具类"
subtitle:      "使用 pymssql 连接 SQL Server 数据库"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - SqlServer
    - 数据库
---

### SQL Server 数据库工具类
```python
# -*- coding: utf-8 -*-#
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   sqlserverControl.py 
@Date    :   2023/4/12 11:45
@Function:   SQL Server 数据库工具类

@Modify Time            @Author      @Version      @Description
-------------------   ----------    ----------    -------------
2023/4/12 11:45         haauleon         1.0           None
"""
import time
import pymssql
import pandas as pd
from common.log import Logger
from common.setting import ConfigHandler
from common.read_data import data
data_file_path = ConfigHandler.config_path
ms_data = data.load_ini(data_file_path)["SqlServer"]

# 数据库配置
DB_CONF = {
    'server': ms_data['host'],
    'user': ms_data['user'],
    'password': ms_data['pwd'],
    'database': ms_data['db'],
    'charset': 'utf8',
    'tds_version': '7.0'
}


class MSSqlDb:
    """
    SQL Server 数据库工具类
    """
    def __init__(self, db_conf=None):
        if db_conf is None:
            db_conf = DB_CONF
        self.conn = pymssql.connect(**db_conf)
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
        for retry_time in range(1, 6):
            try:
                self.cur.execute(sql)
                res_data = self.cur.fetchall()
                return res_data
            except Exception as e:
                time.sleep(20)
                Logger.warn(f'{e} Sqlserver数据库连接失败，尝试重新连接第{retry_time}次')
                self.conn = pymssql.connect(**DB_CONF)
                self.cur = self.conn.cursor()
                if retry_time == 5:
                    Logger.error(e)
                    Logger.error('{} Sqlserver数据库操作失败，关闭连接'.format(sql))
                    raise

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
            except Exception as e:
                time.sleep(20)
                Logger.warn(f'{e} Sqlserver数据库连接失败，尝试重新连接第{retry_time}次')
                self.conn = pymssql.connect(**DB_CONF)
                self.cur = self.conn.cursor()
                if retry_time == 5:
                    Logger.error(e)
                    Logger.error('{} Sqlserver数据库操作失败，执行回滚'.format(sql))
                    self.conn.rollback()
                    raise


ms = MSSqlDb()

```