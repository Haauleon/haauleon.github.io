---
layout:        post
title:         "Postman | 在脚本中发送请求"
subtitle:      "在 Postman 脚本中使用 pm.sendRequest 发送请求"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Postman
---

> 原文：https://www.cnblogs.com/superhin/

### 一、背景
&emsp;&emsp;Postman 的 Collection (集合)/Folder (集合的子文件夹)/Request (请求)都有 Pre-request script 和 Tests 两个脚本区域, 分别可以在发送请求前和请求后使用脚本(基于 Javascript 实现各种操作)。

<br><br>

### 二、发送请求
&emsp;&emsp;在遇到有依赖的接口时,比如需要登录或者需要从前一个接口的结果中获取参数时,我们往往需要在该请求前先发送一下所依赖的请求, 我们可以在 Pre-request script 中使用 pm.sendRequest 实现。       

![](\img\in-post\post-postman\2022-04-28-postman-script-1.png)

![](\img\in-post\post-postman\2022-04-28-postman-script-2.png)

![](\img\in-post\post-postman\2022-04-28-postman-script-3.png)

###### 1、发送GET请求
```javascript
const url = 'http://115.28.108.130:5000/api/user/getToken/?appid=136425';
// 发送get请求
pm.sendRequest(url, function (err, res) {
  console.log(err ? err : res.text());  // 控制台打印请求文本
});
```

&emsp;&emsp;可以配合 `pm.environment.set(key:value)` 来将响应中的数据保存到环境变量中以供本次请求使用
示例: 使用请求前脚本获取 token 并使用。      

![](\img\in-post\post-postman\2022-04-28-postman-script-4.png)

<br>

###### 2、发送表单格式POST请求
```javascript
//构造一个登录请求
const loginRequest = {
    url: 'http://115.28.108.130:5000/api/user/login/',
    method: "POST",
    body: {
        mode: 'urlencoded',  // 模式为表单url编码模式
        urlencoded: 'name=张三&password=123456'
    }
};

// 发送请求
pm.sendRequest(loginRequest, function (err, res) {
    console.log(err ? err : res.text());
});
```

&emsp;&emsp;输出信息可以通过点击 Postman菜单栏 -> view -> Show Postman Console, 打开控制台查看(先打开控制台,再发送请求)。     

![](\img\in-post\post-postman\2022-04-28-postman-script-5.png)

<br>

###### 3、发送JSON格式请求
```javascript
// 构造一个注册请求
const regRequest = {
  url: 'http://115.28.108.130:5000/api/user/reg/',
  method: 'POST',
  header: 'Content-Type: application/json',  //注意要在Header中声明内容使用的类型
  body: {
    mode: 'raw',  // 使用raw(原始)格式
    raw: JSON.stringify({ name: '小小', password: '123456' }) //要将JSON对象转为文本发送
  }
};

//发送请求
pm.sendRequest(regRequest, function (err, res) {
  console.log(err ? err : res.json());  // 响应为JSON格式可以使用res.json()获取到JSON对象
});
```

![](\img\in-post\post-postman\2022-04-28-postman-script-6.png)

<br>

###### 4、发送XML格式请求
&emsp;&emsp;发送 XML 格式和发送 JSON 格式差不多, 只要指定内容格式并发送相应的内容即可。     
```javascript
//构造请求
const demoRequest = {
  url: 'http://httpbin.org/post',
  method: 'POST',
  header: 'Content-Type: application/xml',  // 请求头种指定内容格式
  body: {
    mode: 'raw',
    raw: '<xml>hello</xml>'  // 按文本格式发送xml
  }
};

//发送请求
pm.sendRequest(demoRequest, function (err, res) {
  console.log(err ? err : res.json());
});
```