---
layout:        post
title:         "Jmeter | 使用 Jmeter 测试 Dubbo 接口"
subtitle:      "Jmeter 本身不支持 Dubbo 接口测试，需要下载扩展的插件"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Jmeter
    - API 测试
---

### 一、Dubbo
&emsp;&emsp;Apache Dubbo (incubating) 是一款高性能、轻量级的开源 Java RPC 框架，它提供了三大核心能力：面向接口的远程方法调用，智能容错和负载均衡，以及服务自动注册和发现。官网：[http://dubbo.apache.org/](http://dubbo.apache.org/)。      

&emsp;&emsp;服务发现即消费端自动发现服务地址列表的能力，是微服务框架需要具备的关键能力，借助于自动化的服务发现，微服务之间可以在无需感知对端部署位置与 IP 地址的情况下实现通信。      

&emsp;&emsp;Dubbo 基于消费端的自动服务发现能力。为了提高效率，研发团队为 Dubbo 框架实现了一套数据交互协议，利用这种协议传输数据的接口就是 Dubbo 接口，其对应的就是一个个 Dubbo 服务中的方法。Dubbo 接口的使用方式就是通过消费者“消费”生产者提供的一个个服务，这也是我们测试 Dubbo 基本原理，即测试端充当消费者，测试对象是生产者提供的服务方法。        

目前主要的测试方式有三种：    
1. 第一种是通过编程语言实现一个消费者，通过消费者方法来测试服务提供者。这种方式要求测试人员有一定的编程能力，门槛较高。    
2. 第二种是通过 Dubbo 提供的命令行工具来消费生产者提供的服务方法实现测试。    
3. 第三种是使用第三方工具或框架进行测试，包括 JMeter、MeterSphere 等。

<br>
<br>

### 二、操作步骤
###### 1、下载扩展插件
Apache 为 JMeter 提供了 Dubbo 测试的插件，可在其 Github 仓库中下载，地址如下：              
[https://github.com/thubbo/jmeter-plugins-for-apache-dubbo/releases](https://github.com/thubbo/jmeter-plugins-for-apache-dubbo/releases)      

备用下载：        
链接: https://pan.baidu.com/s/1p6WlGz6tU6e9Ck08zeBt4Q?pwd=2nov        
提取码: 2nov      

Jmeter版本：当前使用 JMeter5.5     
下载后将 jar 包放入 JMeter5.5 安装目录的 `/lib/etc` 中，重启 JMeter。在取样器中，可以看到多了 Dubbo 相关的取样器。       

![](\img\in-post\post-jmeter\2022-07-20-jmeter-dubbo-1.png)    

<br>

###### 2、Dubbo 接口测试  
&emsp;&emsp;在 Dubbo Sample 对话框中配置注册中心地址、服务接口名（Java interface 类名）、方法名、参数类型和参数值等信息，配置完成后，可执行。       

![](\img\in-post\post-jmeter\2022-07-20-jmeter-dubbo-2.png) 