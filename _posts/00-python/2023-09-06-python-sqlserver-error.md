---
layout:        post
title:         "Python3 | SQL Server 连接池链接失败"
subtitle:      "(20047, b'DB-Lib error message 20047, severity 9:\nDBPROCESS is dead or not enabled\n')"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - SqlServer
    - 数据库
---

### 报错信息
sqlserver 连接池链接失败，报错：                
```bash
(20047, b'DB-Lib error message 20047, severity 9:\nDBPROCESS is dead or not enabled\n')
```

<br>
<br>

### 解决方法
究其原因：          
参数填写不完整，原来有个参数：`tds_version = "7.0"` ！！！（kwargs）              
```python
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
            except Exception as e:
                time.sleep(20)
                Logger.warn(f'{e} Sqlserver数据库连接失败，尝试重新连接第{retry_time}次')
                if retry_time == 5:
                    Logger.error(e)
                    Logger.error('{} Sqlserver数据库操作失败，执行回滚'.format(sql))
                    self.conn.rollback()
                    raise


ms = MSSqlDb()

```

<br>
<br>

---

相关链接：      
[报错总结](https://www.cnblogs.com/pythonwl/p/14314796.html)