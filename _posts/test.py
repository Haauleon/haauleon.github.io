# -*- coding:utf-8 -*-
"""
@Author  :   haauleon
@Contact :   753494552@qq.com
@File    :   ssl_check.py
@Date    :   2021-08-20 16:56:00
@Function:   SSL 证书过期检查
"""
import socket
import ssl
import datetime


class SSLCheck:
    '''SSL 证书过期检查'''

    def __init__(self, hostname):
        self.hostname = hostname
        self.ssl_date_fmt = r'%b %d %H:%M:%S %Y %Z'
        self.expired_time = None

    def ssl_expiry_datetime(self):
        '''获取证书到期时间'''
        context = ssl.create_default_context()
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET),
            server_hostname=self.hostname,
        )
        # 5 秒超时，因为 Lambda 有运行时限制
        conn.settimeout(5.0)

        conn.connect((self.hostname, 443))
        ssl_info = conn.getpeercert()
        # 将证书中的字符串解析为 Python datetime 对象 
        return datetime.datetime.strptime(ssl_info['notAfter'], self.ssl_date_fmt)
    
    def ssl_valid_time_remaining(self):
        '''获取证书生命周期中剩余的天数'''
        expires = self.ssl_expiry_datetime()
        #logger.debug(
        #    'SSL cert for %s expires at %s',
        #    hostname, expires.isoformat()
        #)
        return expires - datetime.datetime.utcnow()
    
    def ssl_expires_in(self, buffer_days=20):
        '''
        检查 `hostname` SSL 证书是否在 `buffer_days` 内过期。
        如果证书过期，则引发 AlreadyExpired 异常
        '''
        remaining = self.ssl_valid_time_remaining()
        # print(remaining)
        # print(type(remaining))
        self.expired_time = str(remaining).split(',')[0]

        # 如果证书在两周内到期，我们应该重新颁发
        if remaining < datetime.timedelta(days=0):
            # 证书已经过期
            raise Exception('证书已经过期 %s 天' % remaining.days)
        elif remaining < datetime.timedelta(days=buffer_days):
            # 比缓冲期 buffer_days 更早到期 
            return True
        else:
            # 一切都很好
            return False


class SSLMonitor:
    '''SSL 证书监控类'''

    def __init__(self):
        self.content = None
        self.hosts = [
            'baidu.com',
            'haauleon.com',
        ]
        
    def check_all_hosts_ssl(self):
        '''检查所有域名的证书到期情况'''
        for host in self.hosts:
            # print(host)
            ssl_check = SSLCheck(host)
            is_expired = ssl_check.ssl_expires_in(buffer_days=100)      # 自定义缓冲期为100天
            self.content = '域名: %s\nSSL证书剩余: %s\n' %(host, ssl_check.expired_time)
            # print(self.content)
            yield is_expired


if __name__ == '__main__':
    s = SSLMonitor()
    c = s.check_all_hosts_ssl()
    ssl_msg = []

    for _ in range(len(s.hosts)):
        if next(c):
            ssl_msg.append(s.content)
    
    ssl_msg = ''.join(ssl_msg)
    print(ssl_msg)

# 域名: saas.merchant.bringbuys.com
# SSL证书剩余: 56 days