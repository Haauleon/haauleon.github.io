---
layout:        post
title:         "Linux | taskkill 和 pidof 的用法"
subtitle:      "纯代码方式杀死指定进程名的进程（Linux&Windows）"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - 操作系统
    - Ubuntu
    - Linux
    - Debian
    - Windows
---

### 一、命令行方式
1、Linux            
```bash
> pidof chromedriver | xargs kill -9
```

2、Windows           
```bash
> taskkill /f /t /im chromedriver.exe
```

3、合入代码中，linux 可以使用 system，windows 可以使用 system、winexec 等方式执行               
```bash
#ifdef __linux__
system("pidof softwareName | xargs kill -9");
#elif _WIN32
system("taskkill /im softwareName /f"); //会弹出黑框一闪而过
//不弹出黑框，但是若执行完WinExec立即shellexecute或createprocess执行刚刚kill的软件会出现软件被杀的情况。
// 详情请见：https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-winexec
WinExec("taskkill /im softwareName /f",SW_HIDE);
#endif
```

<br>
<br>

### 二、纯代码方式
Windows 下的方案：     
1、使用 CreateToolhelp32Snapshot 获取当前系统中所有进程的快照          
2、使用 Process32Next 循环遍历每一个进程信息             
3、比较进程名若相符，使用 OpenProcess 根据进程信息中的 pid 打开进程句柄               
4、使用 TerminateProcess 终止进程             

Linux 下的方案：         
1、手写 pidof 通过进程名获取 pid 列表           
2、打开 /proc 文件夹             
3、遍历 /proc 文件夹下的文件，若为数字继续执行            
4、使用 readlink 读取 pid 文件夹下的 exe 获取进程名                 
5、判断进程名是否与指定的进程名一致，若一致则将该 pid 放入到 vector 中               
6、使用 kill API 杀死 pid          

```bash
#ifdef __linux__
#include <sys/types.h>
#include <dirent.h>
#include <string>
#include <vector>
#include <string.h>
#include <cstdio>
#include <iostream>
#include <unistd.h>

int pidof(const std::string& procName,std::vector<int>& pids)
{
    DIR *dir = nullptr;
    struct dirent *dEnt = nullptr;
    int pid = 0, i = 0;
    char *s = nullptr;
    int pnlen = 0;

    dir = opendir("/proc");
    if(!dir)
    {
        return -1;
    }
    pnlen = procName.size();
    while((dEnt = readdir(dir)) != nullptr)
    {
        char exe[PATH_MAX + 1] = {0};
        char path[PATH_MAX + 1] = {0};
        int len = 0;
        if((pid = atoi(dEnt->d_name)) == 0)
            continue;
        snprintf(exe,sizeof(exe),"/proc/%s/exe",dEnt->d_name);
        if((len = readlink(exe,path,PATH_MAX)) < 0)
        {
            continue;
        }
        path[len] = '\0';

        s = strrchr(path,'/');
        if(s == nullptr) continue;
        s++;

        if(!strncmp(procName.c_str(),s,pnlen))
        {
            if(s[pnlen] == ' ' || s[pnlen] == '\0'){
                pids.push_back(pid);
            }
        }
    }
    closedir(dir);
    return 0;
}

BOOL KillProcessFromName(const std::string& strProcessName)
{
    std::vector<int> pids;
    pidof(strProcessName,pids);
    for(auto &pid:pids)
    {
        kill(pid,SIGKILL);
    }
}
#elif _WIN32
#include "tlhelp32.h"
BOOL KillProcessFromName(const std::wstring& strProcessName)
{
	//创建进程快照(TH32CS_SNAPPROCESS表示创建所有进程的快照) 
	HANDLE hSnapShot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
	//PROCESSENTRY32进程快照的结构体 
	PROCESSENTRY32 pe;
	//实例化后使用Process32First获取第一个快照的进程前必做的初始化操作 
	pe.dwSize = sizeof(PROCESSENTRY32);
	//下面的IF效果同: 
	//if(hProcessSnap == INVALID_HANDLE_VALUE) 无效的句柄 
	if (!Process32First(hSnapShot, &pe))
	{
		return FALSE;
	}
	//如果句柄有效 则一直获取下一个句柄循环下去 
	while (Process32Next(hSnapShot, &pe))
	{
		//pe.szExeFile获取当前进程的可执行文件名称 
		wstring scTmp = pe.szExeFile;
		if (scTmp == strProcessName)
		{
			//从快照进程中获取该进程的PID(即任务管理器中的PID) 
			DWORD dwProcessID = pe.th32ProcessID;
			HANDLE hProcess = ::OpenProcess(PROCESS_TERMINATE, FALSE, dwProcessID);
			::TerminateProcess(hProcess, 0);
			CloseHandle(hProcess);
			return TRUE;
		}
	}
	return FALSE;
}
#endif
```

<br>
<br>

---

相关链接：    
[纯代码方式杀死指定进程名的进程（Linux&Windows）](https://blog.csdn.net/youzai2017/article/details/128116873)