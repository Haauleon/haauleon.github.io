---
layout:        post
title:         "删分支、修改远程仓库地址"
subtitle:      ""
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Git
---

### 删除本地分支
`git branch -d [本地分支名]`     

强制删除：      
`git branch -D [本地分支名]`

<br><br>

### 修改远程仓库地址
远程仓库名称： origin     

###### 1、通过命令直接修改远程地址
```
$ git remote                                            # 查看所有远程仓库
$ git remote xxx                                        # 查看指定远程仓库地址
$ git remote set-url origin [要关联的新的远程仓库地址]      # 通过命令直接修改远程地址
```

<br>

###### 2、通过命令先删除再添加远程仓库
```
$ git remote                                            # 查看所有远程仓库
$ git remote xxx                                        # 查看指定远程仓库地址
$ git remote rm origin
$ git remote add origin [要关联的新的远程仓库地址]
```