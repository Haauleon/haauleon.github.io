---
layout:        post
title:         "Postman | 导入 OpenAPI 格式的接口文档"
subtitle:      "前提：其他接口测试工具可以导出 OpenAPI 格式的数据"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Postman
---

### 背景
&emsp;&emsp;最近换了个接口测试工具 Apifox 用作团队内部接口测试，理由是因为他是为团队而生，支持建立以团队为维度的接口项目。但因为我还是习惯用 postman，因为他真的很强大，它可以结合 newman 做小型的接口自动化测试，newman 可以用命令行执行所以可以集成到 jenkins。      

&emsp;&emsp;由于接口项目在 Apifox ，而我又想在 Postman 也有一个一模一样的项目给我自己用作备份，因此有了这篇博文。    

<br>
<br>

### 解决
1. 在 Apifox 中，进入项目 > 项目设置 > 导出数据，导出 OpenAPI 格式的 json 文件     
2. 在 Postman 中，点击导入按钮，将上述导出的 json 文件进行导入即可