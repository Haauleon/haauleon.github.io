---
layout:        post
title:         "python3 | 腾讯云SMS服务"
subtitle:      ""
date:          2021-09-01
author:        "Haauleon"
header-style:  text
catalog:       true
tags:
  - 小而美脚本
  - Python
---

&emsp;&emsp;最近有接短信服务的需求，目前使用的是腾讯云短信服务，新用户可以获得 200 条免费短信，首次购买 1000 条短信才40块钱可以发两年。具体的需要到官网进行查看：[https://console.cloud.tencent.com/smsv2](https://console.cloud.tencent.com/smsv2)。      

<br>

```python
from qcloudsms_py import SmsMultiSender, SmsSingleSender, sms
from qcloudsms_py.httpclient import HTTPError

# 腾讯云短信配置
TENCENT_SMS_APP_ID = '1400xxxxxx'             # 自己应用ID
TENCENT_SMS_APP_KEY = 'c0be97xxxxxxxxxxxx'    # 自己应用Key
TENCENT_SMS_SIGN = 'xxxxxxxxxxx公众号'        # 自己腾讯云创建签名时填写的签名内容（使用公众号的话这个值一般是公众号全称或简称）

# 短信接收者
phone = [
    '1397606xxxx',     # 陈xx
]


class SMSNotice:
    '''短信发送类'''

    def __init__(self):
        self.appid = TENCENT_SMS_APP_ID     # 自己应用ID
        self.appkey = TENCENT_SMS_APP_KEY   # 自己应用Key
        self.sms_sign = TENCENT_SMS_SIGN    # 自己腾讯云创建签名时填写的签名内容（使用公众号的话这个值一般是公众号全称或简称）
    
    def send_sms_single(self, phone_num, template_id, template_param_list):
        """
        单条发送短信
        :param phone_num: 手机号(字符串格式，如 '111111')
        :param template_id: 腾讯云短信模板ID
        :param template_param_list: 短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
        :return:
        """
        sender = SmsSingleSender(self.appid, self.appkey)
        try:
            response = sender.send_with_param(86, phone_num, template_id, template_param_list, sign=self.sms_sign)
        except HTTPError as e:
            response = {'result': 1000, 'errmsg': "网络异常发送失败"}
        return response

    def send_sms_multi(self, phone_num_list, template_id, param_list):
        """
        批量发送短信
        :param phone_num_list: 手机号列表(列表格式，如 ['11111', '22222'])
        :param template_id: 腾讯云短信模板ID
        :param param_list: 短信模板所需参数列表，例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
        :return:
        """
        sender = SmsMultiSender(self.appid, self.appkey)
        try:
            response = sender.send_with_param(86, phone_num_list, template_id, param_list, sign=self.sms_sign)
        except HTTPError as e:
            response = {'result': 1000, 'errmsg': "网络异常发送失败"}
        return response


if __name__ == '__main__':
    sms = SMSNotice()
    sms_msg = [888, 666]       # 正文模板例如:【验证码：{1}，描述：{2}】，则传递参数 [888,666]按顺序去格式化模板
    sms_result = sms.send_sms_multi(phone, 1093459, sms_msg)
```