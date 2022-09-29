---
layout:        post
title:         "Nodejs | npm 常用命令"
subtitle:      "列出所有日常使用命令集"
date:          2021-07-02
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Nodejs
---

## npm 命令
###### 查看 npm 版本
格式：`$ npm -v`      

示例：         
```
haauleon@LAPTOP-EA7BF21I:~$ npm -v
6.14.4
```

<br><br>

###### 查看 npm 包的信息
格式：`$ npm info <包名>`     

示例：         
```
haauleon@LAPTOP-EA7BF21I:~$ npm info concurrently
```

<br><br>

###### 全局安装 npm 包
格式：`$ npm install -g <包名>`      

示例：          
```
haauleon@LAPTOP-EA7BF21I:~$ sudo npm install -g concurrently
```

<br><br>

###### 查看 npm 包所有版本号
格式：`$ npm view <包名> versions`      

示例：           
```
haauleon@LAPTOP-EA7BF21I:~$ npm view dayjs versions
```

<br><br>

###### 查看 npm 包最新版本号
格式：`$ npm view <包名> version`       

示例：              
```
haauleon@LAPTOP-EA7BF21I:~$ npm view dayjs version
```

<br><br>

###### 指定版本安装 npm 包
格式：`$ npm install <包名>@<版本号>`      

示例：           
```
haauleon@LAPTOP-EA7BF21I:~$ sudo npm install -g dayjs@1.10.4
```

<br><br>

###### 查看全局包的安装路径
格式：`$ npm root -g`      

示例：          
```
haauleon@LAPTOP-EA7BF21I:~$ npm root -g
haauleon@LAPTOP-EA7BF21I:~$ ls /usr/local/lib/node_modules -al
haauleon@LAPTOP-EA7BF21I:~$ ls /usr/local/lib/node_modules/newman -al
```

<br><br>

###### 查看所有已安装的全局包
格式：`$ npm list -g`

示例：（注：--depth 0 表示仅查看一级目录）            
```
haauleon@LAPTOP-EA7BF21I:~$ npm list -g --depth 0
```

<br><br>

###### 查看已安装的指定全局包
格式：`$ npm list -g --depth 0 <包名>`       

示例：              
```
haauleon@LAPTOP-EA7BF21I:~$ npm list -g --depth 0 dayjs
```

<br><br>

###### 查看已安装包的当前版本
格式：`$ npm ls <包名>`     

示例：（注：-g 表示全局包）           
```
haauleon@LAPTOP-EA7BF21I:~$ npm ls -g dayjs
```

<br><br>

###### 更新全局安装包
格式：`$ npm update -g <包名>`     

示例：            
```
haauleon@LAPTOP-EA7BF21I:~$ sudo npm update -g dayjs
```

<br><br>

###### 卸载全局安装包
格式：`$ npm uninstall -g <包名>`       

示例：            
```
haauleon@LAPTOP-EA7BF21I:~$ sudo npm uninstall -g dayjs
```