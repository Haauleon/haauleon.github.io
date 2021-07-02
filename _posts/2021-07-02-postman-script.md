---
layout:        post
title:         "Postman | 常用的测试脚本"
subtitle:      "列出所有常用的前置脚本和后置脚本"
date:          2021-07-02
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Postman
---

## 一、前置脚本
&emsp;&emsp;前置脚本在发送请求前就执行，通常用作生成一个随机数或者当前时间戳等。      

<br><br>

###### 当前时间格式化     
```js
var moment = require('moment');                        
var data = moment().format(" YYYY-MM-DD HH:mm:ss");       
console.log(data);                 // 2021-07-02 13:57:34

pm.globals.set("TIME", data);      // 设置全局变量
// postman.setGlobalVariable("TIME", data) 设置全局变量
```

<br><br>

###### 13 位当前时间戳
```js
var cur = Date.parse(new Date());
```

<br><br>

## 二、后置脚本
&emsp;&emsp;后置脚本在请求完成后才执行，通常用作断言、提取响应数据用作全局变量供耦合接口使用。      

<br><br>

###### 常用断言
```js
var res = pm.response.json();
pm.test("验证接口响应状态码是否等于 200", function () {
    pm.response.to.have.status(200);
});

pm.test("验证接口返回字段 msg 是否等于 '创建成功'", function () {
    pm.expect(res.msg).to.eql("创建成功");
});

pm.test("验证接口返回字段 success 是否等于 'true'", function () {
    pm.expect(res.success).to.eql(true);
});
```

<br><br>

###### 提取数据
```js
var r = res.result.data;
for (i=0; i<r.length; i++) {
    switch (r[i].name) {
        case "账期支付":
            pm.globals.set("delayPaymentId", r[i].id);
            break;
        case "银企付":
            pm.globals.set("offlineBankPayId", r[i].id);
            break;
        case "优惠券":
            pm.globals.set("couponSystemId", r[i].id);
            break;
        case "限时购":
            pm.globals.set("limitSystemId", r[i].id);
            break;
        case "礼品卡":
            pm.globals.set("giftCardSystemId", r[i].id);
            break;
        case "积分":
            pm.globals.set("integralSystemId", r[i].id);
            break;
        case "购物金":
            pm.globals.set("coinSystemId", r[i].id);
            break;
        case "团购":
            pm.globals.set("groupBuySystemId", r[i].id);
            break;
        case "运费模板助手":
            pm.globals.set("freightSystemId", r[i].id);
            break;
        case "全员分销":
            pm.globals.set("distributionSystemId", r[i].id);
            break;
        case "小票打印":
            pm.globals.set("printerSystemId", r[i].id);
            break;
        case "收银台":
            pm.globals.set("cashierSystemId", r[i].id);
            break;
        case "独立微信小程序":
            pm.globals.set("miniprogramSystemId", r[i].id);
            break;
        case "多门店云订货":
            pm.globals.set("manyshopSystemId", r[i].id);
            break;
        case "扫码收款":
            pm.globals.set("scanpaySystemId", r[i].id);
            break;
    }
}
```