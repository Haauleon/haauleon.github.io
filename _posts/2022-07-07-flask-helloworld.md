---
layout:        post
title:         "Flask | 构造 post 请求"
subtitle:      ""
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Python
    - 小而美脚本
    - Flask
---

### 代码实现
构造 post 请求，参数是 form-data 格式示例代码如下：       
```
# coding:utf-8
from flask import Flask
from flask import jsonify
from flask import request
# 创建对象
app = Flask(__name__)

users_list = {"1001":["123","张三",19],
         "1002":["234","李四",22],
         "1003":["345","王二小",8]}

# 编写路由，构建url与函数的映射关系（将函数与url绑定）
@app.route("/users",methods=["GET"])
def users():
    return jsonify({"code":10000,"message":"success","data":users_list})

#构造post请求
@app.route("/login",methods=["POST"])
def login():
    # request.form.get：获取post请求的参数，
    account = request.form.get("account")
    password = request.form.get("password")
    if account and password:
        if account in users_list:
            info = users_list[account]
            if password == info[0]:
                return jsonify({"code":10000,"message":"success"})
            else:
                return jsonify({"code":10001,"message":"密码不正确"})
        else:
            return  jsonify({"code":10002,"message":"用户不存在"})
    else:
        return   jsonify({"code":10003,"message":"用户名或密码为空"})

if __name__ == '__main__':
    # 默认方式启动
    # app.run()
    # 解决jsonify中文乱码问题
    app.config['JSON_AS_ASCII'] = False
    # 以调试模式启动,host=0.0.0.0 ,则可以使用127.0.0.1、localhost以及本机ip来访问
    app.run(host="0.0.0.0",port=8899,debug=True)
```