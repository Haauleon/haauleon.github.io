---
layout:        post
title:         "面试 | 支付功能如何测试？"
subtitle:      "支付、退款流程和场景设计"
date:          2021-07-20
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 面试
    - 软件测试基础
---



## 一、背景
&emsp;&emsp;支付功能大体上可以从支付流程、退款流程、非功能测试点及支付测试的方法四个方向考虑。

<br><br>

## 二、测试分析
###### 1.支付流程
&emsp;&emsp;支付的测试流程：点击支付 --> 选择支付方式 --> 确认金额 --> 输入密码 --> 成功支付。需要针对支付流程中的每个阶段和步骤分别测试。       

**（1）点击支付**        

|序号|场景描述|
|---|---|
|1|验证点击支付按钮然后取消订单，订单能否正常取消、订单列表和订单详情的信息和状态是否正确|  

<br>

**（2）选择支付方式**          

|序号|场景描述|
|---|---|
|1|大多数应用支持的支付方式：信用卡，储蓄卡，网银支付，余额，第三方支付（微信、支付宝、京东、百度、聚合支付、组合支付），找人代付。验证是否支持这些支付方式、是否可以正常选择并支付|
|2|支付时结合优惠券/折扣券/促销价抵扣进行相关的抵扣，验证规则正确，并且可以正常抵扣和支付|
|3|手机上没有安装微信、支付宝等 APP 时，选择对应的支付方式，系统如何处理|

<br>

**（3）确认支付金额**       

|序号|场景描述|
|---|---|
|1|验证订单支付金额的显示是否有精度问题（前端未处理或者后端接口返回的数值有精度问题）|
|2|验证组合支付条件下是否出现负数情况|
|3|验证在全额抵扣后支付金额为 0 时是否发生支付异常|
|4|验证支付账户余额（支付宝、微信等）小于支付金额时是否发生支付异常|

<br>

**（4）支付密码**        

|序号|场景描述|
|---|---|
|1|可以支持的支付密码类型有：指纹，人脸识别，账号密码，动态获取验证码，手势，信用卡和支付码，小额免密等，确认自己的产品所支持的密码类型，确认可以验证并支付成功|
|2|输入错误的密码，检查有无提示信息且正确|
|3|超过密码错误上限，检查是否冻结等|

<br>

**（5）其他场景测试点**        

|序号|场景描述|
|---|---|
|1|多笔订单合并支付，是否可以成功|
|2|重复点击支付按钮，是否会出现多次购买，并同步检查数据库的数据账目是否正确|
|3|支付失败之后，是否支持补单和退单|
|4|主动中断支付后后期是否支持继续支付且支付成功|
|5|被动中断支付后（电话、低电量、闹钟，断网、切换后台、耳机插拔等）是否可以继续支付|
|6|使用 Fiddler 等抓包篡改价格：不允许抓包或者数据加密，篡改不成功|

<br><br>

###### 2.退款流程

|序号|场景描述|
|---|---|
|1|验证正常的退款流程是否能走通|
|2|退款成功后检查交易状态是否正确，退款金额是否正确且是否到账|
|3|验证使用优惠券/折扣券/促销价抵扣/积分/平台余额等进行抵扣支付时，退款金额金额是否正确|
|4|检查数据库的退款数据和账目是否正确|
|5|提交错误退款（如退款订单号不正确、不存在、其他人的订单号等）或者退款金额错误，验证是否都退款失败（此场景需要借助 postman 进行接口测试或者使用 fiddler、charles 进行接口请求数据篡改）|

<br><br>

###### 3.非功能测试点

**（1）UI测试**       

|序号|场景描述|
|---|---|
|1|支付按钮是否足够明显|
|2|支付的界面是否简洁、美观，符合大众审美|
|3|支付页面的字体大小是否合理|

<br>

**（2）兼容性测试**          

|序号|场景描述|
|---|---|
|1|BS：如果是 BS 架构的产品，需要测试浏览器的兼容性，所以就需要根据浏览器的内核，选择一些主流的浏览器进行测试|
|2|APP：测试手机移动端的兼容性，比如手机型号，系统版本和屏幕大小及分辨率等|

<br>

**（3）易用性测试**       

|序号|场景描述|
|---|---|
|1|是否支持快捷键功能|
|2|点击付款按钮，是否有提示|
|3|取消付款，是否有提示|
|4|输入框是否对齐，大小是否适中等|

<br>

**（4）性能测试**       

|序号|场景描述|
|---|---|
|1|多次点击支付按钮时，是否会出现多次扣款|
|2|如果发生多次扣款，如何通过原支付渠道退回|
|3|如果在双十一、双十二这种支付高峰的时候，支付时是否会排队|
|4|是否会响应超时|
|5|如果响应超时，是否会返回友好提示|

<br>

**（5）安全测试**       

|序号|场景描述|
|---|---|
|1|验证敏感信息是否加密，是否可以篡改|
|2|通过一些工具进行安全扫描，检查是否有安全漏洞或者采用一些其他的手段进行专门的安全测试|
|3|支付请求的伪造，金额的恶意篡改，恶意模拟第三方接口来调用商家接口等，均是我们需要考虑清楚的问题|

<br>

**（6）网络测试**       

|序号|场景描述|
|---|---|
|1|验证各种网络类型：2G、3G, 4G，5G，wifi 下都可以正常支付|
|2|进行网络切换，支付功能正常|
|3|弱网测试下支付功能正常：不会重复支付多次，APP 不会闪退 崩溃，而且页面提示友好|

<br><br>

## 三、测试方法
&emsp;&emsp;支付功能要用真实的钱么？目前提供的思路有以下四种：        

**1.小额支付**       
&emsp;&emsp;让开发修改代码，不管支付多少钱，实际支付都是 1 分钱；不过这种方法只能测试小额支付，就有可能会出现产品小额支付没问题，但是大额支付就错误的漏测情况。     

**2.申请测试金额，走报销流程**       
&emsp;&emsp;这种方式一般会作为小额支付的一种补充，比如测试完小额支付后，再测试一些大额支付，这就需要跟公司申请测试基金，走报销流程。         

**3.把收款方改成自己的收款账号**     
&emsp;&emsp;这样就可以自己支付，自己收款，避免浪费自己的金钱做公司项目的支付测试。但是这也是有风险的，万一扣款成功，但是支付的金额没有到账可该怎么办？      

**4.沙箱支付**     
&emsp;&emsp;沙箱支付是一种虚拟的支付，不是真实的金额。这种方法可以验证小额和大额的支付流程；目前支付宝沙箱比较成熟，推荐使用。