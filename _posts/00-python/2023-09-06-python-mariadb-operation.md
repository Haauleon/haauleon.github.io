---
layout:        post
title:         "数据库 | Mariadb 数据库操作基类"
subtitle:      "可继承该类，使用数据库插入、更新语句"
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

<br>
<br>

### 继承子类使用示例
```python
from common.save_db_base import SaveMariaDBBase


class MariadbOperation(SaveMariaDBBase):

    def __init__(self):
        super().__init__()
        self.maria = maria

    def select_removal_order_list(self):
        """
        构造移除订单列表生成器
        Returns:

        """
        sql = f"""
                SELECT orderId, WarehouseId 
                FROM gerpgo_removal_order_details 
                WHERE isSpider IS NULL
                ORDER BY Details_updateDate DESC
                LIMIT 10
               """
        order_list = self.maria.select_db(sql=sql)
        # print(order_list)
        for index in range(len(order_list)):
            order_id = order_list[index][0]
            warehouse_id = order_list[index][1]
            yield order_id, warehouse_id

    def is_exist_removal_order_shipment(self, shipment_id):
        """
        查询是否已存在相同的物流id
        Args:
            shipment_id: 物流id

        Returns:

        """
        is_exist = False
        sql = f"""SELECT * FROM gerpgo_removal_order_shipment WHERE id={shipment_id}"""
        shipment_list = self.maria.select_db(sql=sql)
        if shipment_list:
            Logger.info(f"数据库移除订单物流信息表 {shipment_id} 物流id已存在")
            is_exist = True
        return is_exist

    def update_removal_order_isspider(self, order_id, warehouse_id):
        """
        更新移除订单列表的isSpider字段值为1
        Args:
            order_id: 订单id
            warehouse_id: 仓库id

        Returns:

        """
        sql = f"""UPDATE gerpgo_removal_order_details SET isSpider=1 WHERE orderId='{order_id}' AND WarehouseId={warehouse_id} """
        self.update_db(sql=sql, table='gerpgo_removal_order_details')

    def insert_removal_order_shipment(self, table_data):
        """
        移除订单物流信息插入数据库
        Args:
            table_data: 要更新的字段名和字段值

        Returns:

        """
        self.insert_db(table='gerpgo_removal_order_shipment', table_data=table_data)

    def update_removal_order_shipment(self, shipment_id, table_date):
        """
        移除订单物流信息更新数据库
        Args:
            shipment_id: 物流id
            table_date: 要更新的字段名和字段值

        Returns:

        """
        sql = f"""UPDATE gerpgo_removal_order_shipment SET %s WHERE id={shipment_id}"""
        self.update_db(sql=sql, table='gerpgo_removal_order_shipment', table_data=table_date)
        
```