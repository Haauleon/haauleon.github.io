---
layout:        post
title:         "Jmeter | JMeter 测试 Web Service"
subtitle:      "JMeter 测试 Web 服务(应用案例)"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
---

### 一、应用案例
###### 1、案例说明
这里以天气预报服务为例     

Endpoint       
http://www.webxml.com.cn/WebServices/WeatherWebService.asmx          
Disco     
http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?disco       
WSDL     
http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl   

● 操作： getSupportCity      
● 功能： 查询本天气预报 Web Services 支持的国内外城市或地区信息      
● 请求方式： HTTP/POST     
● 接口地址： http://ws.webxml.com.cn/WebServices/WeatherWebService.asmx     
● 输入参数： byProvinceName = 指定的洲或国内的省份，若为 ALL 或空则表示返回全部城市     
● 返回数据： 一个一维字符串数组 String()，结构为：城市名称(城市代码)      

<br>

###### 2、操作步骤
1.添加线程组（相当于 postman 中的接口集合）           
![](\img\in-post\post-jmeter\2022-07-18-jmeter-webservice-1.png)     
![](\img\in-post\post-jmeter\2022-07-18-jmeter-webservice-2.png)          

2.添加 HTTP请求取样器 并配置 （取样器相当于 postman 中的请求）     
```xml
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <getSupportCity xmlns="http://WebXml.com.cn/">
            <byProvinceName>ALL</byProvinceName>
        </getSupportCity>
    </soap:Body>
</soap:Envelope>
```    

![](\img\in-post\post-jmeter\2022-07-18-jmeter-webservice-3.png)     
![](\img\in-post\post-jmeter\2022-07-18-jmeter-webservice-4.png)

3.在取样器节点下添加“HTTP Header Manager”并配置        
&emsp;&emsp;POST 请求传递数据为 SOAP 消息，格式为 XML。需要将 SOAP 消息放入 Body Data 中发送给服务器，并且需要告诉服务器对应的Content-Type。故需要添加一个“HTTP Header Manager”配置元件，在其中添加两个首部“Content-Type”与“SOAPAction”，其中“SOAPAction”用来标识 SOAP HTTP 请求的目的地，其值是个 URI 地址。在 SOAP1.1 中这个首部若其值为空串("")，表示 SOAP 消息的目的地由 HTTP 请求的 URI 标识;无值则表示没有指定这条消息的目的地。       
```
Content-Type: text/xml; charset=utf-8
SOAPAction: http://WebXml.com.cn/getSupportCity
```   

![](\img\in-post\post-jmeter\2022-07-18-jmeter-webservice-5.png)     
![](\img\in-post\post-jmeter\2022-07-18-jmeter-webservice-6.png)    

4.在取样器节点下添加查看结果树       
![](\img\in-post\post-jmeter\2022-07-18-jmeter-webservice-7.png)      

5.执行查看结果         
![](\img\in-post\post-jmeter\2022-07-18-jmeter-webservice-8.png) 

---
参考自 [https://zhuanlan.zhihu.com/p/522421631](https://zhuanlan.zhihu.com/p/522421631)

<br>
<br>

### 二、免费 webservice 接口
###### 天气预报
天气预报Web服务，数据来源于中国气象局      
Endpoint        
http://www.webxml.com.cn/WebServices/WeatherWebService.asmx       

Disco       
http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?disco       

WSDL       
http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl       

<br>

###### IP地址来源 
IP地址来源搜索 WEB 服务（是目前最完整的IP地址数据）      
Endpoint       
http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx      

Disco      
http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?disco     

WSDL      
http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl        

<br>

###### 随机英文、数字和中文简体字
随机英文、数字和中文简体字 WEB 服务        
Endpoint       
http://www.webxml.com.cn/WebServices/RandomFontsWebService.asmx      

Disco      
http://www.webxml.com.cn/WebServices/RandomFontsWebService.asmx?disco      

WSDL       
http://www.webxml.com.cn/WebServices/RandomFontsWebService.asmx?wsdl       

<br>

###### 中国邮政编码地址信息双向查询/搜索
中国邮政编码 <-> 地址信息双向查询/搜索 WEB 服务      
Endpoint       
http://www.webxml.com.cn/WebServices/ChinaZipSearchWebService.asmx       

Disco       
http://www.webxml.com.cn/WebServices/ChinaZipSearchWebService.asmx?disco       

WSDL      
http://www.webxml.com.cn/WebServices/ChinaZipSearchWebService.asmx?wsdl       

<br>

###### 验证码图片
验证码图片 WEB 服务 支持中文、字母、数字 图像和多媒体       
Endpoint       
http://www.webxml.com.cn/WebServices/ValidateCodeWebService.asmx     

Disco      
http://www.webxml.com.cn/WebServices/ValidateCodeWebService.asmx?disco      

WSDL      
http://www.webxml.com.cn/WebServices/ValidateCodeWebService.asmx?wsdl      

<br>

###### Email 电子邮件地址验证
Email 电子邮件地址验证 WEB 服务        
Endpoint       
http://www.webxml.com.cn/WebServices/ValidateEmailWebService.asmx       

Disco      
http://www.webxml.com.cn/WebServices/ValidateEmailWebService.asmx?disco      

WSDL      
http://www.webxml.com.cn/WebServices/ValidateEmailWebService.asmx?wsdl       

<br>

###### 中文简体繁体转换
中文简体字 <-> 繁体字转换 WEB 服务      
Endpoint      
http://www.webxml.com.cn/WebServices/TraditionalSimplifiedWebService.asmx      

Disco      
http://www.webxml.com.cn/WebServices/TraditionalSimplifiedWebService.asmx?disco      

WSDL      
http://www.webxml.com.cn/WebServices/TraditionalSimplifiedWebService.asmx?wsdl     

<br>

###### 中文英文双向翻译
中文 <-> 英文双向翻译 WEB 服务       
Endpoint      
http://www.webxml.com.cn/WebServices/TranslatorWebService.asmx     

Disco       
http://www.webxml.com.cn/WebServices/TranslatorWebService.asmx?disco      

WSDL      
http://www.webxml.com.cn/WebServices/TranslatorWebService.asmx?wsdl     

<br>

###### 火车时刻表
火车时刻表 WEB 服务 （第六次提速最新列车时刻表）       
Endpoint       
http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx      

Disco      
http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx?disco     

WSDL      
http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx?wsdl     

<br>

###### 中国股票行情数据
中国股票行情数据 WEB 服务（支持深圳和上海股市的基金、债券和股票）       
Endpoint        
http://www.webxml.com.cn/WebServices/ChinaStockWebService.asmx      

Disco       
http://www.webxml.com.cn/WebServices/ChinaStockWebService.asmx?disco       

WSDL      
http://www.webxml.com.cn/WebServices/ChinaStockWebService.asmx?wsdl      

<br>

###### 即时外汇汇率数据
即时外汇汇率数据 WEB 服务      
Endpoint      
http://www.webxml.com.cn/WebServices/ExchangeRateWebService.asmx     

Disco      
http://www.webxml.com.cn/WebServices/ExchangeRateWebService.asmx?disco      

WSDL      
http://www.webxml.com.cn/WebServices/ExchangeRateWebService.asmx?wsdl      

<br>

###### 腾讯QQ在线状态
腾讯QQ在线状态 WEB 服务       
Endpoint       
http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx      

Disco      
http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx?disco     

WSDL     
http://www.webxml.com.cn/webservices/qqOnlineWebService.asmx?wsdl     

<br>

###### 中国电视节目预告
中国电视节目预告（电视节目表） WEB 服务      
Endpoint      
http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx     

Disco     
http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx?disco     

WSDL    
http://www.webxml.com.cn/webservices/ChinaTVprogramWebService.asmx?wsdl    

<br>

###### 外汇-人民币即时报价
外汇-人民币即时报价 WEB 服务      
Endpoint     
http://www.webxml.com.cn/WebServices/ForexRmbRateWebService.asmx    

Disco    
http://www.webxml.com.cn/WebServices/ForexRmbRateWebService.asmx?disco     

WSDL    
http://www.webxml.com.cn/WebServices/ForexRmbRateWebService.asmx?wsdl    

<br>

###### 中国股票行情分时走势预览缩略图
中国股票行情分时走势预览缩略图 WEB 服务    
Endpoint      
http://www.webxml.com.cn/webservices/ChinaStockSmallImageWS.asmx    

Disco    
http://www.webxml.com.cn/webservices/ChinaStockSmallImageWS.asmx?disco    

WSDL    
http://www.webxml.com.cn/webservices/ChinaStockSmallImageWS.asmx?wsdl    

<br>

###### 国内飞机航班时刻表
国内飞机航班时刻表 WEB 服务     
Endpoint       
http://www.webxml.com.cn/webservices/DomesticAirline.asmx    

Disco     
http://www.webxml.com.cn/webservices/DomesticAirline.asmx?disco     

WSDL     
http://www.webxml.com.cn/webservices/DomesticAirline.asmx?wsdl     

<br>

###### 中国开放式基金数据
中国开放式基金数据 WEB 服务        
Endpoint     
http://www.webxml.com.cn/WebServices/ChinaOpenFundWS.asmx     

Disco    
http://www.webxml.com.cn/WebServices/ChinaOpenFundWS.asmx?disco    

WSDL    
http://www.webxml.com.cn/WebServices/ChinaOpenFundWS.asmx?wsdl    

<br>

###### 股票行情数据
股票行情数据 WEB 服务（支持香港、深圳、上海基金、债券和股票；支持多股票同时查询）      
Endpoint      
http://www.webxml.com.cn/WebServices/StockInfoWS.asmx     

Disco     
http://www.webxml.com.cn/WebServices/StockInfoWS.asmx?disco     

WSDL    
http://www.webxml.com.cn/WebServices/StockInfoWS.asmx?wsdl    

<br>

###### API市场
云市场      
https://market.aliyun.com/data     

聚合数据    
https://www.juhe.cn/    

极速数据    
https://www.jisuapi.com/
