---
layout:        post
title:         "SQL | 常用的 sql 语句"
subtitle:      "工作中常用的 select 查询语句"
date:          2021-07-23
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 数据库
---


###### 1.关联表查询（左外连接）    

**user 表**      

|id|user_name|password|
|:-----|:-----|:-----|
|1289161|张三|2575175508df7d408|
|1289162|李四|2575175508df7d408|
|1289163|王五|2575175508df7d408|
|1289164|赵六|2575175508df7d408|
|1289165|孙七|2575175508df7d408|
|1289166|周九|2575175508df7d408|
|1289167|吴二|2575175508df7d408|

<br>

**rs_user_examine 表**       

|id|user_id|pass|
|:-----|:-----|:-----|
|1|1289161|张三|1|
|2|1289162|李四|2|
|3|1289163|王五|3|
|4|1289164|赵六|1|
|5|1289165|孙七|2|
|6|1289166|周九||
|7|1289167|吴二|1|

<br>

```sql
/*查询结果：分销申请表 rs_user_examine 中 pass = 2 的 user 记录*/

SELECT *                       // 要查询的字段名，* 代表全部
FROM user a                    // 要查询的表
LEFT JOIN rs_user_examine b    // 要连接进行筛选的表
ON a.id = b.user_id            // 两个表连接的条件
WHERE b.pass = 2               // 筛选的条件
``` 

<br>

**查询结果**     

|id|user_name|password|
|:-----|:-----|:-----|
|1289162|李四|2575175508df7d408|
|1289165|孙七|2575175508df7d408|

<br>

###### 2.有条件删除表中的记录                
```sql
/*操作结果：删除 user 表中 nickname = "Haauleon" 的记录*/

DELETE FROM user WHERE nickname = "Haauleon"
```

<br>

###### 3.使用 is null 查询字段值为空的记录       

**user 表**      

|id|user_name|password|
|:-----|:-----|:-----|
|1289161|张三|2575175508df7d408|
|1289162|李四|2575175508df7d408|
|1289163|王五|2575175508df7d408|
|1289164|赵六|2575175508df7d408|
|1289165|孙七|2575175508df7d408|
|1289166|周九|2575175508df7d408|
|1289167|吴二|2575175508df7d408|

<br>

**rs_user_examine 表**       

|id|user_id|pass|shop_no|
|:-----|:-----|:-----|:-----|
|1|1289161|张三|1|878245257|
|2|1289162|李四|2|878245288|
|3|1289163|王五|3|878245257|
|4|1289164|赵六|1|878245277|
|5|1289165|孙七|2|878245777|
|6|1289166|周九||878245288|
|7|1289167|吴二|1|878245777|

<br>

```sql
/*查询结果：存在于分销申请表 rs_user_examine 但不存在于 user 表中的 user 记录*/

SELECT *                                           // 要查询的字段名，* 代表全部
FROM user a                                        // 要查询的表
LEFT JOIN rs_user_examine b                        // 要连接进行筛选的表
ON a.id = b.user_id and b.shop_no = 878245257      // 两个表连接的条件
WHERE b.user_id is null                            // 筛选的条件
ORDER BY a.id desc                                 // 排序的条件
LIMIT 35                                           // 限制的数量
```

<br>

**查询结果**     

|id|user_name|password|
|:-----|:-----|:-----|
|1289162|李四|2575175508df7d408|
|1289164|赵六|2575175508df7d408|
|1289165|孙七|2575175508df7d408|
|1289166|周九|2575175508df7d408|
|1289167|吴二|2575175508df7d408|

<br>

###### 4.有条件更新表中的记录      
```sql
/*操作结果：更新 user 中记录为 1463201≤id≤1463236 的用户密码为 123456*/

UPDATE user 
set password = "e10adc3949ba59abbe56e057f20f883e" , salt = "" 
WHERE id>=1463201 and id <=1463236
```

<br>

###### 5.有条件统计表中字段值的和       
```sql
/*统计结果：rs_user_commission_record 表中 shop_no = 293491245 的记录的 commission 字段值的总和*/

SELECT parent_id, SUM(commission) as total 
FROM rs_user_commission_record 
WHERE shop_no = 293491245 AND commission_bill in ("PREDICT","INVALID")
```

<br>

###### 6.过滤重复的记录       
```sql
/*过滤 share_content_order_user_record 表总重复的订单号 order_no*/

SELECT *
FROM share_content_order_user_record 
WHERE user_id = 109345 AND shop_no = 798189675 AND bill_type = "FINISH" 
GROUP BY `order_no` HAVING count(*)>1 
```

<br>

###### 7.多表连接查询（左外连接）         
```sql
/*多表连接查询店铺员工关联的权限*/

SELECT role.shop_no, role.user_id, role.role_id, rpms.permission_id, bpms.name, bpms.uri
FROM brb_user_role role 
LEFT JOIN brb_role_permission AS rpms ON role.role_id = rpms.role_id
LEFT JOIN brb_permission AS bpms ON rpms.permission_id = bpms.id
WHERE role.shop_no = 486856075 and role.status = 0 and rpms.status = 0 and role.user_id = 1463406
GROUP BY bpms.name HAVING count(*)>=1 
ORDER BY rpms.permission_id ASC
```

<br>

###### 8.替换表中的字段值     
```sql    
/*操作结果：将 user_address 表中记录为 user_id = 1458580 的 status 值由 0 替换为 1*/

UPDATE user_address 
SET status = REPLACE(status, 0, 1)
WHERE user_id = 1458580;
```

<br>

###### 9.关联表查询（内连接）       
```sql
/*查询结果：优惠券关联的优惠券商品*/

SELECT a.id, a.title, a.product_scope, b.product_id
FROM coupon a
INNER JOIN coupon_product b
on a.id = 358 and a.id = b.coupon_id
```

<br>

###### 10.使用 LIKE 进行模糊查询     
```sql
/*查询结果：user 表中 phone 字段值中包含 1397606 的记录*/

SELECT * FROM user where phone LIKE "%1397606%"
```