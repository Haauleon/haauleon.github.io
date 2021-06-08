---
layout: post
title: "为学习目标设置验收标准"
subtitle: "写写自己近期要学习及巩固的一些东西"
author: "Haauleon"
header-style: text
tags:
  - 学习任务
---

&emsp;&emsp;想来给自己的学习目标设置验收标准，以便检查自己的学习效果。类似于做需求分析并进行功能分解，分得越细越好，最好细化到一个个可以完成的小任务，这样比较有成就感。但初来乍到，第一次写这玩意，暂且先来练练手。      
&emsp;&emsp;虽然很多东西在工作中用不到，但不代表在以后的工作中用不到，只要跟紧潮流，不至于说太落后。要实在在工作中用不到，那就自己做项目学习吧，总是会有办法解决的。 <br><br><br>    


---

**目标一、 学会使用 k6 服务端性能测试工具**    
* 验收标准：使用 [k6](https://k6.io/
) 对服务端 http 接口进行负载测试    
* 过程分解  
    * 阅读[文档](https://k6.io/blog/load-testing-with-postman-collections)学习如何将导出的 Postman 集合转换为 [k6](https://k6.io/
) 脚本   
        * 学习 postman-to-k6 转换器的使用技巧
        * 理解 postman-to-k6 转换器应用的场景
    * 阅读[实例文档](https://test-api.k6.io/)和[官方文档](https://k6.io/docs/using-k6/http-requests)根据实例学习 [k6](https://k6.io/
) 脚本的编写    
    * 学习通过命令行运行 [k6](https://k6.io/
) 脚本并输出结果     

<br><br>

**目标二、 学会使用 wrk 服务端性能测试工具**
* 验收标准：使用 wrk 对服务端 http 接口进行负载测试     
* 过程分解   
    * [参考文档](http://itindex.net/detail/53734-wrk-http-%E6%80%A7%E8%83%BD)安装 [wrk](https://github.com/wg/wrk/issues/103) 工具   
    * [参考文档](https://www.runoob.com/lua/lua-environment.html)安装 Lua 环境   
    * [参考文档](https://www.cnblogs.com/l199616j/p/12156600.html)学习 wrk 单机压测    
    * [参考文档](https://www.cnblogs.com/quanxiaoha/p/10661650.html)学习使用 wrk 工具     

<br><br>

**目标三、 学会使用 perfdog 移动端性能测试工具**    
* 验收标准：使用 perfdog 采集 ios 和 android 的性能指标     
* 过程分解    
    * [下载和安装](https://perfdog.qq.com/)     

<br><br>

**目标四、 学会使用 instrument 移动端性能测试工具**  
* 验收标准：使用 ios 系统自带的性能测试套件 instrument 的leaks 工具检测内存泄漏       
* 过程分解   
    * [参考文档](https://www.jianshu.com/p/c0aa12d91f05)学习使用 Instruments 定位 iOS 应用的Memory Leaks
    * [疑问解答](https://www.jianshu.com/p/ae0a5d5225ad)      