---
layout:        post
title:         "Postman | 保姆级实操总结"
subtitle:      "总结工作中常用的功能、脚本和工具等"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Postman
---

### Postman 功能概览
1. 下载安装     
2. 接口测试
    2.1 拿到接口文档（现成apifox接口文档搬过来即可）
    2.2 创建环境变量
    2.3 根据文档的模块创建集合
    2.4 根据文档创建请求
    2.5 使用 pre-request script 创建全局变量，然后在发送请求的参数中使用
    2.6 使用 tests 创建响应内容的测试断言，根据业务创建全局变量供下一个请求使用
3. 自动化测试
    3.1 方式一：以集合为维度，使用 Collection Runner 执行批量请求并输出报告
    3.2 方式二：使用 newman 命令行执行批量请求并输出报告
4. 稳定性测试
    以集合为维度，使用 Collection Runner 设置 iterations （循环执行次数）和 Delay （延迟时间）来完成单接口或者流程的稳定性测试
5. 其他自用功能
    5.1 获取 python 代码
    5.2 mock 请求
    5.3 使用接口批量生成随机测试数据

<br><br>

### 一、下载安装
**win 系统**     
&emsp;&emsp;百度网盘链接: https://pan.baidu.com/s/1OEJa5IS989XFgoqqUQe2zw 提取码: c0j2        

**mac 系统**     
&emsp;&emsp;百度网盘链接: https://pan.baidu.com/s/1LqdTkqqKGlcSR3ee4tv_nw 提取码: 59rf 

<br><br>

### 二、接口测试
###### 步骤一：拿到接口文档    
&emsp;&emsp;一般是开发同事提供，或者使用现成 apifox 接口文档搬过来。      

![](images/screenshot_1644462730544.png)

<br>

###### 步骤二：创建环境变量  
&emsp;&emsp;使用环境变量的好处在于，仅需同一个变量名即可实现接口可以在不同的域名下运行，比如接口可以在测试环境域名和生产环境域名之间切换运行。         
&emsp;&emsp;我一般是创建两个环境，环境名分别是`测试环境`和`生产环境`。而两个环境的`环境变量名`均使用 `baseUrl` ，然后写入各自环境的变量值。这样即可实现在 postman 主页面切换环境来达到修改域名的效果，避免了手动挨个去更改接口的前缀 `host` 。    

![](images/screenshot_1644464709016.png)    

![](images/screenshot_1644462904841.png)

<br>

###### 步骤三：根据文档的模块创建集合
&emsp;&emsp;一种是导入 OpenAPI 格式的 json 文档自动创建集合，一种是手动创建。       

![](images/screenshot_1644480821998.png)

<br>

###### 步骤四：根据文档创建请求
&emsp;&emsp;用的最多的是 GET、POST 请求，其中GET 请求的参数都是在地址栏的，POST 请求是包在请求体 body 里面的。       

![](images/screenshot_1644481465024.png)      

![](images/screenshot_1644481834395.png)     

![](images/screenshot_1644482455507.png)     

![](images/screenshot_1644482586233.png)

<br>

###### 步骤五：创建并使用全局变量  
&emsp;&emsp;使用 pre-request script 创建全局变量，然后在发送请求的参数中使用。      

常用的前置脚本如下：              
- 获取当前时间并格式化
    ```
    var moment = require('moment');                        
    var data = moment().format(" YYYY-MM-DD HH:mm:ss");       
    console.log(data);                 // 2021-07-02 13:57:34
    ```
- 获取 13 位 当前时间的时间戳
    ```
    var cur = Date.parse(new Date());
    ```
- 使用随机下标选取数组的一个元素
    ```
    var  imgs  = [
        "http://zhkjs-party.oss-cn-shenzhen.aliyuncs.com/892CBD73DC524BBF9DB1727278A79EA2.jpeg",
        "http://zhkjs-party.oss-cn-shenzhen.aliyuncs.com/1D47059EA2344145B79867E621AE4861.jpeg",
    ];
    
    var  img  =  imgs[Math.floor(Math.random()*imgs.length-1)];
    ```
- 循环三次拼接成长度为3的随机字符串
    ```
    var  titles  =  "赵钱孙李周吴郑王马美丽漂亮一二三四五六七八九十安全健康保障长度宽度难度美白";
    var  infoTitle  =  "";
    for (var  i  =  3; i>  0; --i){
        // 把循环三次的随机字符拼接成三个字的标题
        infoTitle  +=  titles[Math.floor(Math.random()*titles.length-1)+1];
        console.log(infoTitle);          // 美王周
    }
    ```
- 随机数范围 [0, 1]
    ```
    var  isTop  =  Math.floor(Math.random()*2);
    ```
- 创建全局变量
    ```
    // 第一种
    pm.globals.set("变量名", 变量值);   
    // 第二种
    postman.setGlobalVariable("变量名", 变量值); 
    ```
-  使用 md5 加密字符串
    ```
    var  sign  =  "123456";    // 要加密的字符串
    var  signmd5  =  CryptoJS.MD5(sign).toString();
    ```

<br>

###### 步骤六：使用测试断言
&emsp;&emsp;使用 tests 创建响应内容的测试断言，根据业务创建全局变量供下一个请求使用。     

常用的后置脚本如下：     
- 创建全局变量通用格式 
    ```
    // 定义一个响应体res，获取body中所有的参数并以json格式返回
    var res = JSON.parse(responseBody);
    
    // 获取字段res.key的值并存在全局变量中
    postman.setGlobalVariable("全局变量名", res.key)
    ```
- 常用的响应断言脚本
    ```
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
- 当前接口请求成功后延迟 5 分钟请求下一个接口
    ```
    // 延迟时间 = 5分钟 × 60秒 × 1000
    setTimeout(function(){postman.setNextRequest("请求名", "延迟时间")
    // 例如 setTimeout(function(){postman.setNextRequest("根据商品id获取已上架的门店列表");}, "300000");
    ```
- 根据当前请求返回的响应字段值判断执行下一个接口
    ```
    var  res  =  JSON.parse(responseBody);
    if (res.result.customer  ===  null){
        postman.setNextRequest('提交买家认证表单');
    }else{
        postman.setGlobalVariable("attestationsUserId", res.result.customer.id);
        var  pass  =  res.result.customer.pass;
        if (pass  ===  1){
        postman.setNextRequest('买家认证通过审核');
        }else{
        postman.setNextRequest('更新买家认证表单');
        }
    }
    ```
- 根据当前请求返回的响应字段值判断并提取数据
    ```
    var r = res.result.data;
    for (i=0; i<r.length; i++) {
        switch (r[i].name) {
            case "账期支付":
                pm.globals.set("delayPaymentId", r[i].id);
                break;
            case "银企付":
                pm.globals.set("offlineBankPayId", r[i].id);
                break;
        }
    }
    ```

<br><br>

### 三、自动化测试
###### 1. Collection Runner
**方式一：以集合为维度，使用 Collection Runner 执行批量请求并输出报告**          

![](images/screenshot_1644484474162.png)          

![](images/screenshot_1644484623603.png)         

<br>

###### 2. newman
**方式二：使用 newman 命令行执行批量请求并输出报告**      

详见 [https://haauleon.gitee.io/2021/04/12/postman-newman/](https://haauleon.gitee.io/2021/04/12/postman-newman/)

<br><br>

### 四、稳定性测试
&emsp;&emsp;以集合为维度，使用 Collection Runner 设置 iterations （循环执行次数）和 Delay （延迟时间）来完成单接口或者流程的稳定性测试。          

![](images/screenshot_1644647114407.png)        

<br><br>

### 五、其他自用功能
###### 1. 获取 python 代码       
![](images/screenshot_1644647332978.png)        

<br>

###### 2. mock 请求       
详见 [https://haauleon.gitee.io/2021/04/12/postman-mock/](https://haauleon.gitee.io/2021/04/12/postman-mock/)