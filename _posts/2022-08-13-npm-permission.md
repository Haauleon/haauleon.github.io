---
layout:        post
title:         "Nodejs | npm install 权限问题"
subtitle:      "npm ERR! Error: EACCES: permission denied"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Nodejs
---

### 问题描述    
博主最近在使用Angular平台的时候在工程目录下使用 `npm install` 时会遇到问题，屏幕 log 片段：        
```js
npm ERR! Error: EACCES: permission denied, mkdir '/Users/xxxxx/.npm/_cacache/index-v5/ad/a1'
npm ERR!  { [Error: EACCES: permission denied, mkdir '/Users/
xxxxx/.npm/_cacache/index-v5/ad/a1']
npm ERR!   cause:
npm ERR!    { Error: EACCES: permission denied, mkdir '/Users/x x x xx/.npm/_cacache/index-v5/ad/a1'
npm ERR!      errno: -13,
npm ERR!      code: 'EACCES',
npm ERR!      syscall: 'mkdir',
npm ERR!      path: '/Users/xxxxx/.npm/_cacache/index-v5/ad/a1' },
npm ERR!   isOperational: true,
``` 

<br>
<br>

### 解决方法   
显然是在权限上除了问题，解决方式：      
```
$ sudo chown -R $USER:$GROUP ~/.npm
$ sudo chown -R $USER:$GROUP ~/.config
``` 

再次运行npm install即可解决问题。