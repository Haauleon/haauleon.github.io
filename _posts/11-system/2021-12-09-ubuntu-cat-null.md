---
layout:        post
title:         "Ubuntu | 清空文件内容的三种方法"
subtitle:      ""
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 操作系统
    - Ubuntu
---


### linux 系统中清空文件内容的三种方法

1.使用 vi/vim 命令打开文件后，输入 "%d" 清空，后保存即可。但当文件内容较大时，处理较慢，命令如下：     
```
vim file_name
:%d
:wq
```

<br>

2.使用 cat 命令情况，命令如下：          
```
cat /dev/null > file_name
```

<br>

3.使用 echo 命令清空，此时会在文件中写入一个空行 "\n"，命令如下：         
```
echo "">file_name
```

<br>

推荐使用 cat 命令，亲测有用。