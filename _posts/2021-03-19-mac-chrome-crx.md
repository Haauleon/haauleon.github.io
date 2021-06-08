---
layout: post
title: "chrome 插件 | Mac 安装 crx 插件"
subtitle: '解决 mac 下安装 crx 插件的解决方法'
author: "Haauleon"
header-style: text
tags:
  - Chrome 扩展
---     

&emsp;&emsp;在 Mac 系统下，很多第三方下载的 `.crx` 后缀的 Chrome 浏览器的插件都无法安装。
<br>   

**解决办法**   
1. 将下载的 `abcdefg.crx` 插件名的后缀更改成 `.zip`     
2. 进入终端，cd 进入此文件所在的目录，执行命令 `unzip abcdefg.zip -d abcdefg` (abcdefg 是解压后的自定义文件目录名)    
3. 打开 chrome 浏览器的标签页，在地址栏输入 `chrome://extensions/` 进入扩展程序页面，启用右上角的开发者模式，然后点击 `加载已解压的扩展程序` 按钮，选择目录 `abcdefg` 即可成功安装此离线插件。