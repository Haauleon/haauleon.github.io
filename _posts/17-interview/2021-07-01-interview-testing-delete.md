---
layout:        post
title:         "测试设计 | 页面删除操作"
subtitle:      "如何设计页面删除操作的测试场景"
date:          2021-07-01
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 软件测试基础
---

## 测试页面
![](\img\in-post\post-test-base\2021-07-01-testing-delete-1.png)

<br><br>

## 设计思路
&emsp;&emsp;如上分销商等级页面的删除操作，设计场景前需要找出其他页面是否有加载/关联此分销商等级，如果有则需要组合条件进行设计删除操作的测试场景，如果无就不考虑。经检查，其他页面如分销商页面有加载且该页面有一条记录关联此分销商等级。                        

![](\img\in-post\post-test-base\2021-07-01-testing-delete-2.png)

<br><br>

## 测试场景

|序号|测试场景|设计背景|
|---|---|---|
|1|无分销商关联此等级。执行删除操作|这个场景的条件是最单一的，由于条件单一因此不需要考虑其他|
|2|有分销商关联此等级。执行删除操作|这个场景属于组合条件删除，前提是要找出是否有关联/加载此记录/列表的页面，然后再进行有条件删除。经常出现在删除已关联商品的分类等|
|3|分销商等级已成功删除。检查分销商页面的等级筛选列表是否仍有此等级|这个场景也经常出现，目的是检查其他加载此列表的页面是否仍存在已删除的记录|