---
layout:        post
title:         "环境搭建 | 搭建一个能运行的虚拟机环境"
subtitle:      "使用 Docker 和 Vagrant 安装 Ubuntu"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 操作系统
    - Web开发
    - Docker
    - Vagrant
    - Ubuntu
---

> 本篇所有操作均在 64 位的 Windows 11 系统下执行

<br>
<br>

### 一、VirtualBox
&emsp;&emsp;VirtualBox 是 Oracle 开源的虚拟化系统，支持 Linux 、OS X、Windows 等平台，Docker 和 Vagrant 环境都需要它作为宿主机。     

> 虚拟机安装在主机上，必须在主机上才能运行，主机就是一个宿主，则相对于虚拟机而言，正在使用的计算机就是宿主机。

<br>

#### 1、安装 VirtualBox
（1）进入[官网](https://www.virtualbox.org/)下载最新版       
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-1.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-2.jpg)    
   
<br>
<br>

（2）双击进行安装      
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-3.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-4.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-5.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-6.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-7.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-8.jpg)    

<br>
<br>

（3）进入 VirtualBox 主页    
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-9.jpg)    

<br>
<br>

### 二、Vagrant
&emsp;&emsp;Vagrant 用来操作 VirtualBox、VMWar、AWS 这些虚拟机系统，可以很快地完成一套开发环境的部署。直接启动就好，不需要了解所有相关环境的知识和细节。可以通过 `> vagrant provision` ，使用 Shell 脚本或者主流的配置管理工具（如 Puppet、Ansible等）对软件进行自动安装、更新和配置管理。  

<br>

#### 1、安装 Vagrant
（1）进入[官网](https://www.vagrantup.com/)下载        
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-10.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-11.jpg) 

<br>
<br>

（2）双击进行安装      
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-12.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-13.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-14.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-15.jpg)    

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-16.jpg)    

<br>
<br>

（3）重启     
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-17.jpg)    

<br>
<br>

（4）验证是否安装成功      
```
C:\Users\Haauleon>vagrant --version
Vagrant 2.3.2
```

<br>
<br>

#### 2、Vagrantfile 配置文件
&emsp;&emsp;一个打包好的操作系统在 Vagrant 中称为一个 Box，而这个 Box 实际上是一个 zip 包。这个 zip 包包含了 Vagrant 的虚拟机配置信息和 VirtualBox 的虚拟机镜像文件。Vagrantfile 文件中保存了虚拟机的各项配置，如下：     

```
# coding: utf-8
Vagrant.configure(2) do |config|
  config.vm.box = "dongweiming/web_develop"
  config.vm.hostname = "WEB"
  config.vm.network :forwarded_port, guest: 9000, host: 9000
  config.vm.network :forwarded_port, guest: 3141, host: 3141
  config.vm.network :forwarded_port, guest: 5000, host: 5000
  config.ssh.username = 'ubuntu'
  config.ssh.password = 'ubuntu'
  config.ssh.insert_key = false
  config.ssh.private_key_path = ["~/.ssh/id_rsa"]
  config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/authorized_keys"
  config.vm.synced_folder ".", "/vagrant", disabled: true
  # config.vm.network "public_network", bridge: "en0: Wi-Fi (AirPort)"
  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--name", "web_dev", "--memory", "1536"]
  end
end
```

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-18.jpg)   

<br>
<br>

#### 3、首次启动虚拟机
###### （1）创建 SSH 秘钥     
董老师定制的 Box 需要创建一个 SSH 秘钥用于自动登录。如果之前没有创建过则使用以下命令进行创建：     
```
C:\Users\Haauleon>ssh-keygen
```

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-19.jpg)   

<br>
<br>

###### （2）启动虚拟机     
```
PS D:\gitee\web_develop> vagrant up
Bringing machine 'default' up with 'virtualbox' provider...
==> default: Box 'dongweiming/web_develop' could not be found. Attempting to find and install...
    default: Box Provider: virtualbox
    default: Box Version: >= 0
==> default: Loading metadata for box 'dongweiming/web_develop'
    default: URL: https://vagrantcloud.com/dongweiming/web_develop
==> default: Adding box 'dongweiming/web_develop' (v0.5) for provider: virtualbox
    default: Downloading: https://vagrantcloud.com/dongweiming/boxes/web_develop/versions/0.5/providers/virtualbox.box
    default:
==> default: Successfully added box 'dongweiming/web_develop' (v0.5) for 'virtualbox'!
==> default: Importing base box 'dongweiming/web_develop'...
==> default: Matching MAC address for NAT networking...
==> default: Checking if box 'dongweiming/web_develop' version '0.5' is up to date...
==> default: Setting the name of the VM: web_develop_default_1667878758610_92779
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 9000 (guest) => 9000 (host) (adapter 1)
    default: 3141 (guest) => 3141 (host) (adapter 1)
    default: 5000 (guest) => 5000 (host) (adapter 1)
    default: 22 (guest) => 2222 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2222
    default: SSH username: ubuntu
    default: SSH auth method: password
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
    default: The guest additions on this VM do not match the installed version of
    default: VirtualBox! In most cases this is fine, but in rare cases it can
    default: prevent things such as shared folders from working properly. If you see
    default: shared folder errors, please make sure the guest additions within the
    default: virtual machine match the version of VirtualBox you have installed on
    default: your host and reload your VM.
    default:
    default: Guest Additions Version: 5.0.18
    default: VirtualBox Version: 7.0
==> default: Setting hostname...
==> default: Running provisioner: file...
    default: ~/.ssh/id_rsa.pub => ~/.ssh/authorized_keys
```

<br>

**坑一：vagrant up 报错**      
启动虚拟机之前，需要进入 Vagrantfile 文件所在的目录，否则执行会报错，报错提示：`A Vagrant environment or target machine is required to run this command. Run vagrant init to create a new Vagrant environment. Or, get an ID of a target machine from vagrant global-status to run this command on. A final option is to change to a directory with a Vagrantfile and to try again.`      

**坑二：下载 Box 耗时长**      
启动的时候会检查本地有没有这个 Box，没有的话就会下载，第一次下载的时间较长，将近十分钟。     

<br>
<br>

###### （3）初始化系统环境     
第一次启动完成后需要使用配置脚本来初始化系统环境，`provision` 会执行 Vagrantfile 中定义的 file 命令 `config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/authorized_keys"` ，将本机的 `~/.ssh/id_rsa.pub` 拷贝到目标服务器并保存为 `~/.ssh/authorized_keys`。      

```
PS D:\gitee\web_develop> vagrant provision
==> default: Running provisioner: file...
    default: ~/.ssh/id_rsa.pub => ~/.ssh/authorized_keys
```

<br>
<br>

###### （4）登录虚拟机    
启动完成后就可以登录虚拟机了。     
```
PS D:\gitee\web_develop> vagrant ssh
==> default: The machine you're attempting to SSH into is configured to use
==> default: password-based authentication. Vagrant can't script entering the
==> default: password for you. If you're prompted for a password, please enter
==> default: the same password you have configured in the Vagrantfile.
Welcome to Ubuntu 16.04 LTS (GNU/Linux 4.4.0-34-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

111 packages can be updated.
0 updates are security updates.

New release '18.04.6 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


Last login: Wed Aug 17 16:21:41 2016 from 10.0.2.2

~ ubuntu@WEB
❯
```

<br>
<br>

#### 4、再次启动虚拟机
关闭连接命令：    
```
❯ exit
Connection to 127.0.0.1 closed.
```

<br>

下次启动虚拟机成功后，需要进行登录时可直接使用命令 `> vagrant ssh` ：           
```shell
PS D:\gitee\web_develop> vagrant up
PS D:\gitee\web_develop> vagrant ssh
==> default: The machine you're attempting to SSH into is configured to use
==> default: password-based authentication. Vagrant can't script entering the
==> default: password for you. If you're prompted for a password, please enter
==> default: the same password you have configured in the Vagrantfile.
Welcome to Ubuntu 16.04 LTS (GNU/Linux 4.4.0-34-generic x86_64)

 * Documentation:  https://help.ubuntu.com/

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

111 packages can be updated.
0 updates are security updates.

New release '18.04.6 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


Last login: Tue Nov  8 04:12:02 2022 from 10.0.2.2

~ ubuntu@WEB
❯
```

<br>
<br>

### 三、Docker
&emsp;&emsp;Docker 是用 Go 语言编写的一个基于 Linux 容器（Linux Containers, LXC）的开源容器引擎。跟传统的虚拟机不同，虚拟机都是一个完整的操作系统所以占用计算机资源三件套（CPU、内存、硬盘等）。而 Docker 是 “操作系统级别的虚拟化” ，因此可以达到秒级启动，与虚拟机相比，Docker 容器本身几乎不占用什么开销，可见其性能之卓越。且因 Docker 具有可移植性所以 “一次封装，到处运行” 的优势被众所周知。        

&emsp;&emsp;2014年7月21日，IBM 公司发表过一份全英文报告[《虚拟机与Linux容器的性能比较》](https://pan.baidu.com/s/1v_22iLbWhsjl-Kj0hHdVbA?pwd=lt3w)，可使用[百度翻译](https://fanyi.baidu.com/mtpe-individual/#/editor/quickImport)进行全文档翻译后享用。       

<br>

#### 1、安装 Docker
（1）下载[docker-toolbox](http://mirrors.aliyun.com/docker-toolbox/windows/docker-toolbox/)          
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-20.jpg)    

<br>
<br>

（2）双击 DockerToolbox-18.03.0-ce.exe 进行安装      
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-21.jpg)   

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-22.jpg)     

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-23.jpg)   

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-24.jpg)   

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-25.jpg)   

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-26.jpg)   

<br>
<br>

#### 2、启动 Docker Toolbox 终端
安装完成后双击 Docker QuickStart Terminal 图标来启动 Docker Toolbox 终端即进入 Docker Shell，如下：          
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-27.jpg)   

<br>

首次启动 Docker Toolbox 终端时，会检查本地是否存在 boot2docker.iso 这个镜像文件，如果没有就会从 github 上自动下载最新版本，因此第一次启动时花费的时间较长。在进行一系列的初始化后，最后的提示如下：    
```
docker is configured to use the default machine with IP 192.168.99.100
For help getting started, check out the docs at https://docs.docker.com
```    
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-28.jpg)      

<br>

上面的 192.168.99.100 是 Docker 创建的虚拟机的 IP，之后访问应用其实都是在请求这个 IP。如果忘记了也可以通过如下命令获得：    
```
$ docker-machine ip
192.168.99.100
```

<br>

检查 Docker 是否安装成功：    
```
$ docker --version
Docker version 18.03.0-ce, build 0520e24302
```

<br>
<br>

#### 3、下载镜像
Dockerfile 配置文件内容如下：   
```
FROM ubuntu:16.04

MAINTAINER DongWeiming <ciici123@gmail.com>
ENV DEBIAN_FRONTEND noninteractive

RUN echo 'deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse\n\
    deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse\n\
    deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse\n\
    deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse\n\
    deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse\n\
    deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse\n\
    deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse\n\
    deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse\n\
    deb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse\n\
    deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse\n\
    ' > /etc/apt/sources.list

RUN apt-get update
RUN apt-get install python curl git zsh sudo -yq
RUN useradd -ms /bin/bash ubuntu
RUN echo "ubuntu ALL=(ALL) NOPASSWD: ALL"  >> /etc/sudoers
RUN echo "ubuntu:ubuntu" | chpasswd
USER ubuntu
workdir /home/ubuntu
RUN git clone https://github.com/dongweiming/web_develop
RUN cd /home/ubuntu/web_develop

EXPOSE 9000 3141 22 5000
```

<br>

执行以下命令可以直接下载董老师上传好的基于 Ubuntu:16.04 LTS 的镜像：     
```
$ docker pull dongweiming/web_develop:dev
dev: Pulling from dongweiming/web_develop
5ba4f30e5bea: Pull complete
9d7d19c9dc56: Pull complete
ac6ad7efd0f9: Pull complete
e7491a747824: Pull complete
a3ed95caeb02: Pull complete
e42ba31532a7: Pull complete
92d10652653c: Pull complete
58ad29242685: Pull complete
fd1ea66774c4: Pull complete
da69b3de3c09: Pull complete
1209a5fcd32b: Pull complete
faf8957e629c: Pull complete
Digest: sha256:ff43adf798f27d616ad2c7fec6fd79680cf2205b5996a3841230ba827522e85c
Status: Downloaded newer image for dongweiming/web_develop:dev
```

<br>

下载完成后检查镜像列表是否存在此镜像：    
```
$ docker images
REPOSITORY                TAG                 IMAGE ID            CREATED             SIZE
dongweiming/web_develop   dev                 43fb02d9c1a3        6 years ago         294MB
```

<br>
<br>

#### 4、首次进入容器
使用以下命令可以进入容器，前面的提示是 zsh 新用户安装。进入容器后，默认使用 ubuntu 这个用户，并切换到 `/home/ubuntu/web_develop` 目录下。          
```
$ docker run --name web_dev -it -p 9000:9000 -p 3141:3141 -p 5000:5000 dongweiming/web_develop:dev /bin/zsh
This is the Z Shell configuration function for new users,
zsh-newuser-install.
You are seeing this message because you have no zsh startup files
(the files .zshenv, .zprofile, .zshrc, .zlogin in the directory
~).  This function can help you with a few settings that should
make your use of the shell easier.

You can:

(q)  Quit and do nothing.  The function will be run again next time.

(0)  Exit, creating the file ~/.zshrc containing just a comment.
     That will prevent this function being run again.

(1)  Continue to the main menu.

(2)  Populate your ~/.zshrc with the configuration recommended
     by the system administrator and exit (you will need to edit
     the file by hand, if so desired).

--- Type one of the keys in parentheses ---

Aborting.
The function will be run again next time.  To prevent this, execute:
  touch ~/.zshrc
30ea46d16b2a%
```

<br>
<br>

#### 5、退出容器
使用 `exit` 命令退出即可：   
```
30ea46d16b2a% exit
```

<br>
<br>

#### 6、再次进入容器
使用 `exit` 命令从容器退出后，容器就关闭了，可使用以下命令进行重新登录：     
```
$ docker start web_dev   # 回车一次
web_dev
$ docker attach web_dev  # 回车两次


Aborting.
The function will be run again next time.  To prevent this, execute:
  touch ~/.zshrc
30ea46d16b2a%
```

<br>
<br>

#### 7、Docker 虚拟机端口转发
&emsp;&emsp;在 Docker 环境中访问应用需要使用 http://192.168.99.100:PORT 这个地址，由于 Vagrant 做了端口转发，直接在宿主机上访问 127.0.0.1:PORT 即可。为了使 Docker 和 Vagrant 访问的地址一致，可以使用以下命令实现。          

<br>

（1）获取 Docker 虚拟机的名字        
```
$ docker-machine inspect|grep MachineName
        "MachineName": "default",
```

可知，Docker 虚拟机的名字是 default。      

<br>
<br>

（2）使用 Shell 命令添加本机与容器的端口镜像      
VBoxManage 是 VirtualBox 提供的命令行工具，使用如下命令添加本机与容器的端口镜像成功后，就可以使用 http://127.0.0.1:PORT 来统一访问了。     
```
$ for port in 3141 5000 9000
> do
> VBoxManage controlvm "default" natpf1 "tcp-port$port,tcp,127.0.0.1,$port,,$port"; echo $port
> done
3141
5000
9000
```

<br>

**坑一：VBoxManage 命令不存在**      
```
$ for port in 3141 5000 9000 ; do VBoxManage controlvm "default" natpf1 "tcp-port$port,tcp,127.0.0.1,$port,,$port"; echo $port; done
bash: VBoxManage: command not found
```
需要配置环境变量，在 `环境变量 > 系统变量 > Path` 变量中添加 VBoxManage.exe 所在目录的路径 `D:\Oracle\VirtualBox\` 即可。    
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-29.jpg)   