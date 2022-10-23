---
layout:        post
title:         "Gitbook | 托管静态资源"
subtitle:      "如何将 Gitbook 集成到 Github Pages？"
date:          2018-10-12
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - Gitbook
---


## Gitbook 生成静态资源
&emsp;&emsp;默认情况下，Gitbook 输出方式是静态网站，只不过另外两种不是很常用。更多情况下我们是使用静态网页搭建个人官网，或托管到第三方平台，或部署到私有云服务器，但不管怎么样还是离不开生成这一步。Gitbook 生成静态资源有两种方式：`$ gitbook build` 和 `$ gitbook serve`。这里主要说说 `$ gitbook build` 。                                    
&emsp;&emsp;其实，Gitbook的输出方式有三种：website，json 和 ebook。默认情况下输出目录是 `_book/`，整个项目的入口文件是 `index.html`。            

```
输出目标文件的语法格式：
$ gitbook build [book] [output]

示例
# 默认输出格式：`website`  
$ gitbook build --format=website  
# 更改输出格式：`json`  
$ gitbook build --format=json  
# 更改输出格式：`ebook`  
$ gitbook build --format=ebook
```
<br>

&emsp;&emsp;这一章节来介绍下如何利用 `Github Pages` 静态网页服务与 `gitbook` 进行集成。                                      

<br><br>

## Github Pages 简介
&emsp;&emsp;Github Pages是Github网站推出的一种**免费**的静态网页托管服务，适合搭建静态的项目主页或个人官网。其中，网站项目的源码直接托管在github仓库中，当仓库文件更新后，该仓库所关联的网站自动更新，从而实现了源码与官网的联动更新。                                       

![](\img\in-post\post-gitbook\2021-03-13-gitbook-github-1.png)                              

<br><br>

###### 两种Pages模式
&emsp;&emsp;每个 Github 账号有且只有一个主页站点，但允许无限制多的项目站点（即两种 Pages 模式）。

* User/Organization Pages 个人或公司站点
    * 使用自己的用户名，每个用户名下面只能创建一个
    * 资源命名必须符合规则 `username/username.github.com`
    * 主干上内容用来构建和发布页面
*  Project Pages 项目站点
    * gh-pages 分支用于构建和发布
    * 如果 user/org pages 使用了独立域名，那么托管在账户下的所有 project pages 将使用相同的域名进行重定向，除非 project pages 使用了自己的独立域名
    * 如果没有使用独立域名，project pages 将通过子路径的形式提供服务 username.github.com/projectname
<br>

&emsp;&emsp;例如，我自己的名下有三个仓库，一个名叫 haauleon.github.io，另外两个分别是 book1 和 book2。如果想对外暴露上述三个仓库作为我的静态网站，那么最终的效果就是：                                  
* 主页站点：https://haauleon.github.io
* 项目1站点：https://haauleon.github.io/book1
* 项目2站点：https://haauleon.github.io/book2

&emsp;&emsp;其实上述规则很好理解，Github 网站作为一个托管中心，有成千上万的用户在使用Github，并且每个用户的用户名都是唯一并且不同的，因此 `*.github.io` 通配符域名刚好充当命名空间。可以预料的是，不仅仅有 `<username>.github.io` 这种二级域名，说不定还有 `api.github.io`，`docs.github.io` 等等。毕竟，只需要购买 `*.github.io` 通配符域名证书就可以支持任意多的二级域名了，感谢 Github 赠送免费的 https 网站。

<br><br>

## Github Pages 集成 Gitbook
&emsp;&emsp;Github Pages 是提供静态网站的免费托管，而 Gitbook 默认生成的内容就是静态网站。Gitbook 默认输出目录 `_book/` 包括了静态网站所需的全部资源，其中就包括 `index.html` 首页文件。因此我们只需要每次生成后将 `_book/` 整个目录复制到项目根目录,那么推送到远程仓库时自然就是输出后静态网站了。
<br>

###### 具体集成步骤                                             
1.github 账户：新建仓库，命名book1，和本地电子书文件夹一致                            
2.本地电脑：进入本地书籍book1目录，使用 `$ gitbook build` 生成静态资源目录 `_book`，然后执行以下命令：                            

```
$ git init
$ git remote add origin https://github.com/Haauleon/book1.git
$ git add .
$ git commit -m "your descprition(自己定义)"
$ git push -u origin master
```                      

3.把书籍目录 book1 的 `_book` 目录拷贝出来放其他任意目录下                        
4.建立并进入 gh-pages 分支                              

```
$ git checkout -b gh-pages
```                       

5.把书籍目录book1的内容清空（**.git不要删除**），把刚拷贝出去的 `\_book` 文件夹里面的所有内容复制到 book1 目录下，然后使用以下命令：                  

```
git add .
git commit -m "the 2nd"
git push origin gh-pages
```                            

&emsp;&emsp;提交成功后在浏览器地址栏输入 https://haauleon.github.io/book1 即可远程访问该电子书。以后的更新——生成的静态网站 cp 到本地 book1 目录，然后 push 到 gh-pages 即可。                                                            

&emsp;&emsp;另外，进入 Github 的 book1 项目设置即可发现：                                      

![](\img\in-post\post-gitbook\2021-03-13-gitbook-github-2.png)