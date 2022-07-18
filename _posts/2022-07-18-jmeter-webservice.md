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

### 应用案例
###### 案例说明
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

###### 操作步骤
1.添加线程组;

2.添加HTTP请求取样器并配置;

3.在取样器节点下添加“HTTP Header Manager”并配置;

4.在取样器节点下添加查看结果树;

5.执行看结果。

<br>
<br>

### 免费 webservice 接口
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
