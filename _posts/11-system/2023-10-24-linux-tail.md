---
layout:        post
title:         "Linux | tail 命令详解"
subtitle:      "监视文件内容有无变化，新增内容会继续输出"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - 操作系统
    - Ubuntu
    - Linux
    - Debian
---

### 一、tail 命令介绍
<mark>tail</mark> 命令可以将文件指定位置到文件结束的内容写到标准输出。如果你不知道tail命令怎样使用，可以在命令行执行命令 `tail --help` 就能看到 tail 命令介绍和详细的参数使用介绍，内容如下（我帮大家翻译了一下）。               

```bash
[root@yanggongzi ~]# tail --help
Usage: tail [OPTION]... [FILE]...
Print the last 10 lines of each FILE to standard output.
With more than one FILE, precede each with a header giving the file name.
With no FILE, or when FILE is -, read standard input.
将每个文件的最后10行打印到标准输出。
如果有多个文件，在每个文件之前都有一个给出文件名的头文件。
没有文件，或者当文件为-时，读取标准输入。

Mandatory arguments to long options are mandatory for short options too.
长选项必须用的参数在使用短选项时也是必须的。
  -c, --bytes=K            output the last K bytes;
                           or use -c +K to output bytes starting with the Kth of each file
                           输出最后的 K 个字节;
			               或者使用 -c +K 从每个文件的第K字节开始打印。
  -f, --follow[={name|descriptor}]
                           output appended data as the file grows;
                           an absent option argument means 'descriptor'
                           随着文件的增长，输出附加数据;（动态输出最新的信息）;
                           没有选项参数意味着“描述符”
                           
  -F                       same as --follow=name --retry
                           与 --follow=name --retry 作用相同
                           
  -n, --lines=K            output the last K lines, instead of the last 10;
                           or use -n +K to output starting with the Kth
                           输出最后的K行，而不是最后的10行;
                           或者使用-n +K从第K个开始输出
                           
      --max-unchanged-stats=N
                           with --follow=name, reopen a FILE which has not changed size after N (default 5) iterations to see if it has been unlinked or renamed (this is the usual case of rotated log files);
                           with inotify, this option is rarely useful
                           使用——follow=name，在N次(默认为5次)迭代后，重新打开一个大小没有改变的文件，看看它是否被解除链接或重命名(这是旋转日志文件的常见情况);
                           对于inotify，这个选项很少有用
                             
      --pid=PID            with -f, terminate after process ID, PID dies
                           与“-f”选项连用，当指定的进程号的进程终止后，自动退出tail命令
                           
  -q, --quiet, --silent    never output headers giving file names
                           当有多个文件参数时，不输出各个文件名
                           
      --retry              keep trying to open a file if it is inaccessible
                           即是在tail命令启动时，文件不可访问或者文件稍后变得不可访问，都始终尝试打开文件。使用此选项时需要与选项“——follow=name”连用
                           
  -s, --sleep-interval=N   
                           with -f, sleep for approximately N seconds (default 1.0) between iterations;
                           with inotify and --pid=P, check process P at least once every N seconds
                           与“-f”选项连用，指定监视文件变化时间隔的秒数（默认为1.0）;
			               使用inotify和-pid=P，每N秒检查进程P至少一次
			               
  -v, --verbose            always output headers giving file names
                           当有多个文件参数时，总是输出各个文件名
                           
      --help               display this help and exit
                           显示此帮助信息并退出
                           
      --version            output version information and exit
                           显示版本信息并退出

If the first character of K (the number of bytes or lines) is a '+',
print beginning with the Kth item from the start of each file, otherwise,
print the last K items in the file.  K may have a multiplier suffix:
b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,
GB 1000*1000*1000, G 1024*1024*1024, and so on for T, P, E, Z, Y.
如果K前面的字符(字节数或行数)是'+'，每个文件从第K项开始打印，否则，打印文件中最后的K项。K可能有一个乘数后缀:b 512，kB 1000，K 1024，MB 1000 1000，M 1024 1024，GB 1000 1000，G 1024 1024 1024，等等，对于T，P，E，Z，y。

With --follow (-f), tail defaults to following the file descriptor, which
means that even if a tail"ed file is renamed, tail will continue to track
its end.  This default behavior is not desirable when you really want to
track the actual name of the file, not the file descriptor (e.g., log
rotation).  Use --follow=name in that case.  That causes tail to track the
named file in a way that accommodates renaming, removal and creation.
使用——follow (-f)， tail默认跟随文件描述符，这意味着即使重命名了尾部文件，tail也将继续跟踪其尾部。
当您真正想要跟踪文件的实际名称而不是文件描述符(例如，日志旋转)时，这种默认行为是不可取的。
在这种情况下使用——follow=name。这将导致tail以一种适合重命名、删除和创建的方式跟踪已命名文件。

```

<br>
<br>

### 二、tail 命令使用示例
1、输出最后200个字符         
```bash
> tail -c 200 test.log
```

2、从第900个字符开始输出，一直到最后             
```bash
> tail -c +900 test.log
```

3、输出最后20行          
```bash
> tail -n 20 test.log
```

4、从第36行开始输出，一直到最后           
```bash
> tail -n +36 test.log
```

5、输出指定文件的最后十行，同时继续监视文件内容有无变化，新增内容会继续输出，直到按下 `[Ctrl-C]` 组合键退出              
```bash
> tail -f test.log
```

6、指定多个文件并输出文件名           
```bash
> tail -v test.log test2.log
```

7、指定多个文件不输出文件名            
```bash
> tail -q test.log test2.log
```

<br>
<br>

### 三、tailf、tail -f、tail -F 的区别
1、`tail -f`         
等同于 `–follow=descriptor`，根据文件描述符进行追踪，当文件改名或被删除，追踪停止                  

2、`tail -F`            
等同于 `–follow=name --retry`，根据文件名进行追踪，并保持重试，即该文件被删除或改名后，如果再次创建相同的文件名，会继续追踪                

3、`tailf`            
等同于 `tail -f -n 10`（貌似 `tail -f` 或 `-F` 默认也是打印最后10行，然后追踪文件），与 `tail -f` 不同的是，如果文件不增长，它不会去访问磁盘文件，所以 `tailf` 特别适合那些便携机上跟踪日志文件，因为它减少了磁盘访问，可以省电             

&emsp;&emsp;当我们设置了滚动日志时，需要持续实时监控最新的日志输出，那么就要用 `tail -F`，而不能用 `tailf` 和 `tail -f`。因为当日志 xxx.log 达到了设定阈值重命名成了 xxx01.log 时，后两个命令追踪的还是 xxx01.log 文件而不是新创建的 xxx.log 文件，这时就不能继续监控最新日志了。                   

<br>
<br>

### 四、常用快捷键
【Ctrl】+【S】 暂停刷新。            
【Ctrl】+【Q】继续刷新。           
【Ctrl】+【C】退出 tail 命令。               

<br>
<br>

---

相关链接：    
[tail 命令详解](https://blog.csdn.net/big_data1/article/details/112668965)