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

concurrently@6.2.0 | MIT | deps: 9 | versions: 37
Run commands concurrently
https://github.com/kimmobrunfeldt/concurrently#readme

keywords: bash, concurrent, parallel, concurrently, command, sh

bin: concurrently

dist
.tarball: https://registry.npmjs.org/concurrently/-/concurrently-6.2.0.tgz
.shasum: 587e2cb8afca7234172d8ea55176088632c4c56d
.integrity: sha512-v9I4Y3wFoXCSY2L73yYgwA9ESrQMpRn80jMcqMgHx720Hecz2GZAvTI6bREVST6lkddNypDKRN22qhK0X8Y00g==
.unpackedSize: 98.9 kB

dependencies:
chalk: ^4.1.0           lodash: ^4.17.21        rxjs: ^6.6.3            supports-color: ^8.1.0  yargs: ^16.2.0
date-fns: ^2.16.1       read-pkg: ^5.2.0        spawn-command: ^0.0.2-1 tree-kill: ^1.2.2

maintainers:
- kimmobrunfeldt <kimmo.brunfeldt+public@gmail.com>
- gustavohenke <guhenke@gmail.com>

dist-tags:
latest: 6.2.0

published a month ago by gustavohenke <guhenke@gmail.com>
```

<br><br>

###### 全局安装 npm 包
格式：`$ npm install -g <包名>`      

示例：          
```
haauleon@LAPTOP-EA7BF21I:~$ sudo npm install -g concurrently
[sudo] password for haauleon:
/usr/local/bin/concurrently -> /usr/local/lib/node_modules/concurrently/bin/concurrently.js
+ concurrently@6.2.0
added 59 packages from 55 contributors in 19.474s
```

<br><br>

###### 查看 npm 包所有版本号
格式：`$ npm view <包名> versions`      

示例：           
```
haauleon@LAPTOP-EA7BF21I:~$ npm view dayjs versions

[ '1.0.0',
  '1.0.1',
  '1.1.0',
  '1.2.0',
  '1.3.0',
  '1.4.0',
  '1.4.1',
  '1.4.2',
  '1.4.3',
  '1.5.0',
  '1.5.1',
  '1.5.2',
  '1.5.3',
  '1.5.4',
  '1.5.5',
  '1.5.6',
  '1.5.8',
  '1.5.9',
  '1.5.10',
  '1.5.11',
  '1.5.12',
  '1.5.13',
  '1.5.14',
  '1.5.15',
  '1.5.16',
  '1.5.17',
  '1.5.18',
  '1.5.19',
  '1.5.20',
  '1.5.21',
  '1.5.22',
  '1.5.23',
  '1.5.24',
  '1.6.0',
  '1.6.1',
  '1.6.2',
  '1.6.3',
  '1.6.4',
  '1.6.5',
  '1.6.6',
  '1.6.7',
  '1.6.8',
  '1.6.9',
  '1.6.10',
  '1.7.0',
  '1.7.1',
  '1.7.2',
  '1.7.3',
  '1.7.4',
  '1.7.5',
  '1.7.6',
  '1.7.7',
  '1.7.8',
  '1.8.0',
  '1.8.1',
  '1.8.2',
  '1.8.3',
  '1.8.4',
  '1.8.5',
  '1.8.6',
  '1.8.7',
  '1.8.8',
  '1.8.9',
  '1.8.10',
  '1.8.11',
  '1.8.12',
  '1.8.13',
  '1.8.14',
  '1.8.15',
  '1.8.16',
  '1.8.17',
  '1.8.18',
  '1.8.19',
  '1.8.20',
  '1.8.21',
  '1.8.22',
  '1.8.23',
  '1.8.24',
  '1.8.25',
  '1.8.26',
  '1.8.27',
  '1.8.28',
  '1.8.29',
  '1.8.30',
  '1.8.31',
  '1.8.32',
  '1.8.33',
  '1.8.34',
  '1.8.35',
  '1.8.36',
  '1.9.0',
  '1.9.1',
  '1.9.2',
  '1.9.3',
  '1.9.4',
  '1.9.5',
  '1.9.6',
  '1.9.7',
  '1.9.8',
  '1.10.0',
  '1.10.1',
  '1.10.2',
  '1.10.3',
  '1.10.4',
  '1.10.5' ]
```

<br><br>

###### 查看 npm 包最新版本号
格式：`$ npm view <包名> version`       

示例：              
```
haauleon@LAPTOP-EA7BF21I:~$ npm view dayjs version
1.10.5
```

<br><br>

###### 指定版本安装 npm 包
格式：`$ npm install <包名>@<版本号>`      

示例：           
```
haauleon@LAPTOP-EA7BF21I:~$ sudo npm install -g dayjs@1.10.4
+ dayjs@1.10.4
added 1 package from 1 contributor in 1.997s
```

<br><br>

###### 查看全局包的安装路径
格式：`$ npm root -g`      

示例：          
```
haauleon@LAPTOP-EA7BF21I:~$ npm root -g
/usr/local/lib/node_modules
haauleon@LAPTOP-EA7BF21I:~$ ls /usr/local/lib/node_modules -al
total 0
drwxr-xr-x 1 root root 4096 Jul  2 15:01 .
drwxr-xr-x 1 root root 4096 Mar 31 09:32 ..
drwxr-xr-x 1 root root 4096 Mar 31 09:33 newman
drwxr-xr-x 1 root root 4096 Mar 31 10:33 newman-reporter-html
drwxr-xr-x 1 root root 4096 Jul  1 17:56 publish-sftp
drwxr-xr-x 1 root root 4096 Jul  1 17:55 sftp-publish
haauleon@LAPTOP-EA7BF21I:~$ ls /usr/local/lib/node_modules/newman -al
total 92
drwxr-xr-x 1 root root  4096 Mar 31 09:33 .
drwxr-xr-x 1 root root  4096 Jul  2 15:01 ..
-rw-r--r-- 1 root root 16070 Oct 26  1985 CHANGELOG.yaml
-rw-r--r-- 1 root root 11357 Oct 26  1985 LICENSE.md
-rw-r--r-- 1 root root 15670 Oct 26  1985 MIGRATION.md
-rw-r--r-- 1 root root 40581 Oct 26  1985 README.md
drwxr-xr-x 1 root root  4096 Mar 31 09:32 bin
drwxr-xr-x 1 root root  4096 Mar 31 09:32 docker
-rw-r--r-- 1 root root   649 Oct 26  1985 index.js
drwxr-xr-x 1 root root  4096 Mar 31 09:32 lib
drwxr-xr-x 1 root root  4096 Mar 31 09:33 node_modules
-rw-r--r-- 1 root root  3495 Mar 31 09:33 package.json
```

<br><br>

###### 查看所有已安装的全局包
格式：`$ npm list -g`

示例：（注：--depth 0 表示仅查看一级目录）            
```
haauleon@LAPTOP-EA7BF21I:~$ npm list -g --depth 0
/usr/local/lib
├── concurrently@6.2.0
├── dayjs@1.10.4
├── UNMET PEER DEPENDENCY newman@5.2.2
├── newman-reporter-html@1.0.5
├── publish-sftp@1.0.6
└── sftp-publish@0.1.31

npm ERR! peer dep missing: newman@4, required by newman-reporter-html@1.0.5
```

<br><br>

###### 查看已安装的指定全局包
格式：`$ npm list -g --depth 0 <包名>`       

示例：              
```
haauleon@LAPTOP-EA7BF21I:~$ npm list -g --depth 0 dayjs
/usr/local/lib
└── dayjs@1.10.4
```

<br><br>

###### 查看已安装的指定包的当前版本
格式：`$ npm ls <包名>`     

示例：（注：-g 表示全局包）           
```
haauleon@LAPTOP-EA7BF21I:~$ npm ls -g dayjs
/usr/local/lib
└── dayjs@1.10.4
```

<br><br>

###### 更新 npm 全局安装包
格式：`$ npm update -g <包名>`     

示例：            
```
haauleon@LAPTOP-EA7BF21I:~$ sudo npm update -g dayjs
+ dayjs@1.10.5
updated 1 package in 2.17s
```

<br><br>

###### 卸载 npm 全局安装包
格式：`$ npm uninstall -g <包名>`       

示例：            
```
haauleon@LAPTOP-EA7BF21I:~$ sudo npm uninstall -g dayjs
removed 1 package in 0.193s
haauleon@LAPTOP-EA7BF21I:~$ npm ls -g dayjs
/usr/local/lib
└── (empty)
```