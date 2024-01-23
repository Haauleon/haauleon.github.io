---
layout:        post
title:         "Python3 | SQLAlchemy组装SQL查询语句"
subtitle:      "使用 SQLAlchemy 连接 Mysql 数据进行 SQL 查询"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
    - SQLAlchemy
---


### 一、背景


<br>
<br>

### 二、使用方法
#### 1、环境安装
```text
# python3版本
Python 3.8.10

# pip3版本
pip 21.1.1

# pip包安装
pymssql==2.2.7
PyMySQL==0.9.3
SQLAlchemy==1.4.4
```


<br>

#### 2、获取表字段
进入 Navicat 主界面，找到对应的表，右键点击 `转储SQL文件` > `仅结构`，保存后打开 sql 文件获取表结构信息：    
```text
/*
 Navicat Premium Data Transfer

 Source Server         : 开发数据库 192.168.1.18
 Source Server Type    : MariaDB
 Source Server Version : 100808
 Source Host           : 192.168.1.18:3306
 Source Schema         : mydb

 Target Server Type    : MariaDB
 Target Server Version : 100808
 File Encoding         : 65001

 Date: 23/01/2024 10:16:46
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for rpa_report_jd_dailybill
-- ----------------------------
DROP TABLE IF EXISTS `rpa_report_jd_dailybill`;
CREATE TABLE `rpa_report_jd_dailybill`  (
  `ID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '主键，采用 GUID',
  `Base_ShopInfoID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '业务中台店铺 ID',
  `BatchNO` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '由“数据处理工具”读取的上传文件的完整文件名组成（不含扩展名）',
  `CheckStatus` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '核对状态 True:已核对 False 或 NULL：未核对',
  `CheckUserID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '业务中台用于 ID（Base_User）,核对人 ID',
  `orderNO` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '订单编号',
  `receiptNO` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '单据编号',
  `receiptType` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '单据类型',
  `productID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '商品编号',
  `merchantOrderNO` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '商户订单号',
  `productName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '商品名称',
  `settleState` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '结算状态',
  `costTime` datetime NULL DEFAULT NULL COMMENT '费用发生时间',
  `billTime` datetime NULL DEFAULT NULL COMMENT '费用计费时间',
  `settleTime` datetime NULL DEFAULT NULL COMMENT '费用结算时间',
  `costItem` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '费用项',
  `amount` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '金额',
  `currency` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '币种',
  `merchantPaymentState` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '商家应收/应付',
  `settleRemark` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '钱包结算备注',
  `shopID` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '店铺号',
  `JD_storeNO` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '京东门店编号',
  `brandStoreNO` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '品牌门店编号',
  `storeName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '门店名称',
  `remark` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '备注',
  `billType` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '收支方向',
  `productNum` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL COMMENT '商品数量',
  PRIMARY KEY (`ID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;

```

<br>

#### 3、连接数据库
安装完开发环境后，尝试使用以下语句连接 MySQL 数据库，目前已知 MariaDB 和 MySQL 使用的是同一个数据库引擎。       
```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

# 在python3以上版本中，MySQLdb模块已经废弃了，目前主要是使用pymysql模块连接数据库，可使用以下方法解决
pymysql.install_as_MySQLdb()

# engine = create_engine('mysql://{账号}:{密码}@{地址}/{数据库}')
engine = create_engine('mysql://root:123456@192.168.1.18/mydb')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
```

<br>

#### 4、创建表模型
**SQLAlchemy 常用数据类型：**                          
- Integer：整形，映射到数据库中是 <mark>int</mark> 类型           
- Float：浮点类型，映射到数据库中是 <mark>float</mark> 类型。它占据的32位           
- Double：双精度浮点类型，映射到数据库中是 <mark>double</mark> 类型，占据64位              
- String：可变字符类型，映射到数据库中是 <mark>varchar</mark> 类型             
- Boolean：布尔类型，映射到数据库中是 <mark>tinyint</mark> 类型              
- Decimal：定点类型，是专门为了解决浮点类型精度丢失的问题的，一般作用于金钱类型               
- Enum：枚举类型，指定某个字段只能是枚举中指定的几个值，不能为其他值            
- Date：存储时间，只能存储年月日，映射到数据库中是 <mark>date</mark> 类型           
- Datetime：存储时间，可以存储年月日时分秒              
- Time：存储时间，存储时分秒             
- Text：存储长字符串，映射到数据库是 <mark>text</mark> 类型              
- Longtext：长文本类型，映射到数据库中是 <mark>longtext</mark> 类型                

<br>

根据以上字段映射关系，创建以下表模型：      
```python
class JD(Base):
	__tablename__ = 'rpa_report_jd_dailybill'

	ID = Column(String, primary_key=True)
    Base_ShopInfoID = Column(String)
	BatchNO = Column(String)
    CheckStatus = Column(String)
    CheckUserID = Column(String)
    orderNO = Column(String)
    receiptNO = Column(String)
    receiptType = Column(String)
    productID = Column(String)
    merchantOrderNO = Column(String)
    productName = Column(String)
    settleState = Column(String)
    costTime = Column(DateTime)
    billTime = Column(DateTime)
    settleTime = Column(DateTime)
    costItem = Column(String)
    amount = Column(String)
    currency = Column(String)
    merchantPaymentState = Column(String)
    settleRemark = Column(String)
    shopID = Column(String)
    JD_storeNO = Column(String)
    brandStoreNO = Column(String)
    storeName = Column(String)
    remark = Column(String)
    billType = Column(String)
    productNum = Column(String)

```

<br>

#### 5、使用SQL查询语句
创建完表模型，如无误，可使用以下 SQL 查询语句：    
```python
# 查询所有记录
result = session.query(JD).all()
for res in result:
    print(res.ID, res.BatchNO)
```

输出结果：    
```
05cac2ee-712e-4f65-aa44-7b341a282a0b 京东_日账单_20231217
0a31f547-9279-4642-a5dd-648fbd6b9b39 京东_日账单_20240102
0c362657-b68a-4564-9053-fe7b0b450aca 京东_日账单_20231215
0c9b96c7-98f0-498a-9e68-d5f5fb6fcd14 京东_日账单_20231217
0caddb61-82dd-49d4-8828-c20f1e53f67a 京东_日账单_20231216
0cb1aac5-6ff3-4f3d-b285-a45cc6d06fc0 京东_日账单_20231223
0d7b20a5-9545-4eaa-8857-16e176c7c7f0 京东_日账单_20231129
0f62f771-f9ca-4d64-b0ec-cfd202298af2 京东_日账单_20231213
1665b73d-ce44-461f-abfb-c8c0804a82d3 京东_日账单_20231217
18adf65a-60cd-4719-856e-f1e44c5e1bfe 京东_日账单_20231217
19c7c6f8-6893-497e-8141-747d5d41ba5c 京东_日账单_20231217
1b03b7d3-1bbe-404a-8358-7b2091671ffb 京东_日账单_20231207
1c7497e8-fee5-4e34-8f83-353740142e53 京东_日账单_20231220
1d85fe6d-7e9d-4a61-8b57-311ec2786fc0 京东_日账单_20231216
1dea9679-e067-45b3-9c75-60051563f3c9 京东_日账单_20231226
2348d544-85c5-43a9-924b-3f4b62e21975 京东_日账单_20231217
270ac153-7b3e-4357-b7ad-5ae3c0d61812 京东_日账单_20231213
......
......
......
......
......
......
```

<br>
<br>

---

相关链接：    
[SQLAlchemy常用数据类型](https://www.cnblogs.com/LeYu/p/10176060.html)              
[__init__() got an unexpected keyword argument 'bind'](https://stackoverflow.com/questions/42955172/typeerror-init-got-an-unexpected-keyword-argument-username/52129426)      
[No module named 'MySQLdb'](https://blog.csdn.net/m0_37886429/article/details/83540314)       