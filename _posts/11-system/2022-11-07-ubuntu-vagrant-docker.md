---
layout:        post
title:         "Ubuntu | 使用Docker和Vagrant安装Ubuntu"
subtitle:      "搭建一个能运行的虚拟机环境"
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
    - 操作系统
    - Web开发
    - Docker
    - Vagrant
---

> 本篇所有操作均在 64 位的 Windows 11 系统下执行

<br>
<br>

### 一、VirtualBox
&emsp;&emsp;VirtualBox 是 Oracle 开源的虚拟化系统，支持 Linux 、OS X、Windows 等平台，Docker 和 Vagrant 环境都需要它作为宿主机。     

> 虚拟机安装在主机上，必须在主机上才能运行，主机就是一个宿主，则相对于虚拟机而言，正在使用的计算机就是宿主机。

<br>

###### 1、安装 VirtualBox
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

###### 1、安装 Vagrant
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

### 三、Vagrantfile 配置文件
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

### 四、首次使用 Vagrant
###### 1、创建 SSH 秘钥     
董老师定制的 Box 需要创建一个 SSH 秘钥用于自动登录。如果之前没有创建过则使用以下命令进行创建：     
```
C:\Users\Haauleon>ssh-keygen
```

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-19.jpg)   

<br>
<br>

###### 2、启动虚拟机     
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

###### 3、初始化系统环境     
第一次启动完成后需要使用配置脚本来初始化系统环境，`provision` 会执行 Vagrantfile 中定义的 file 命令 `config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/authorized_keys"` ，将本机的 `~/.ssh/id_rsa.pub` 拷贝到目标服务器并保存为 `~/.ssh/authorized_keys`。      

```
PS D:\gitee\web_develop> vagrant provision
==> default: Running provisioner: file...
    default: ~/.ssh/id_rsa.pub => ~/.ssh/authorized_keys
```

<br>
<br>

###### 4、登录虚拟机    
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

### 五、下次使用 Vagrant
关闭连接命令：    
```
❯ exit
Connection to 127.0.0.1 closed.
```

<br>

下次进行登录时，直接使用命令 `> vagrant ssh` 即可。     
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


Last login: Tue Nov  8 04:12:02 2022 from 10.0.2.2
```

<br>
<br>

### 六、Docker
&emsp;&emsp;Docker 是用 Go 语言编写的一个基于 Linux 容器（Linux Containers, LXC）的开源容器引擎。跟传统的虚拟机不同，虚拟机都是一个完整的操作系统所以占用计算机资源三件套（CPU、内存、硬盘等）。而 Docker 是 “操作系统级别的虚拟化” ，因此可以达到秒级启动，与虚拟机相比，Docker 容器本身几乎不占用什么开销，可见其性能之卓越。且因 Docker 具有可移植性所以 “一次封装，到处运行” 的优势被众所周知。        

&emsp;&emsp;2014年7月21日，IBM 公司发表过一份全英文报告[《虚拟机与Linux容器的性能比较》](https://pan.baidu.com/s/1v_22iLbWhsjl-Kj0hHdVbA?pwd=lt3w)，可使用[百度翻译](https://fanyi.baidu.com/mtpe-individual/#/editor/quickImport)进行全文档翻译后享用。       

<br>

###### 1、安装 Docker
（1）进入[官网](https://www.docker.com/)下载     
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-20.jpg)    

<br>
<br>

（2）双击 Docker Desktop Installer.exe 进行安装      
![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-21.jpg)   

<br>

![](\img\in-post\post-system\2022-11-07-ubuntu-docker-vagrant-22.jpg)   