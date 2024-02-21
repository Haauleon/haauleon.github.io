---
layout:        post
title:         "Python3 | socket platform psutil os 模块"
subtitle:      "获取当前电脑的基本信息如本地IP地址、登录用户、主机名、内存、操作系统、硬盘等"
author:        "Haauleon"
header-img:    "img/in-post/post-python/bg.jpeg"
header-mask:   0.4
catalog:       true
tags:
    - Python
---


### 代码分享
&emsp;&emsp;获取当前电脑的基本信息，如获取本地IP地址、获取当前登录用户的用户名、获取当前主机名、获取操作系统名称、版本、架构等。      

```python
class Tools:

    @staticmethod
    def get_local_ip():
        """获取本地IP地址"""
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # 不需要真的连接，只是为了获取本地IP
            s.connect(('10.255.255.255', 1))
            ip = s.getsockname()[0]
        except:
            ip = '127.0.0.1'
        finally:
            s.close()

        return ip

    @staticmethod
    def get_computer_username():
        """获取当前登录用户的用户名"""
        import os

        # 方式一：os.getlogin()函数。注意：在某些平台（如Windows）上可能无法正常工作
        # username = os.getlogin()
        # print(username)

        # 方式二：getpass.getuser()
        # import getpass
        # username = getpass.getuser()  # 当前登录用户名

        # 方式三：os.environ
        username = os.environ.get('USERNAME')  # 在Windows上使用
        # username = os.environ.get('USER')  # 在Linux或Mac上使用
        return username

    @staticmethod
    def get_computer_device_name():
        """获取当前主机名"""
        # 方式一：使用platform模块
        # import platform
        # device_name = platform.node()

        # 方式二：使用socket模块
        import socket
        device_name = socket.gethostname()
        return device_name

    @staticmethod
    def get_operating_system_info():
        """使用platform模块获取操作系统名称、版本、架构等"""
        import platform
        system = platform.system()        # 操作系统名称
        release = platform.release()      # 操作系统版本
        machine = platform.machine()      # 硬件架构
        processor = platform.processor()  # 处理器名称
        return system, release, machine, processor

    @staticmethod
    def get_cpu_info():
        """使用psutil库获取CPU的核心数、使用率等"""
        import psutil
        cpu_count = psutil.cpu_count()      # CPU核心数
        cpu_percent = psutil.cpu_percent()  # CPU使用率
        return cpu_count, cpu_percent

    @staticmethod
    def get_memory_info():
        """使用psutil库获取内存总量、已用内存、可用内存"""
        import psutil
        virtual_memory = psutil.virtual_memory()  # 虚拟内存信息
        return virtual_memory

    @staticmethod
    def get_disk_info():
        """使用psutil库获取磁盘使用情况、分区信息等"""
        import psutil
        disk_usage = psutil.disk_usage('/')  # 指定分区的磁盘使用情况
        return disk_usage

    @staticmethod
    def get_screen_info():
        """使用ctypes库获取屏幕分辨率"""
        import ctypes
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
        return f"Screen resolution: {screen_width} x {screen_height}"


if __name__ == '__main__':
    import psutil

    # 获取所有网络接口
    interfaces = psutil.net_if_addrs()

    # 遍历接口并打印IP地址
    for interface_name, interface_addresses in interfaces.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':  # IPv4
                ip_address = address.address
                print(f"{interface_name}: {ip_address}")

```