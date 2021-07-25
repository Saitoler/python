# -*- coding: utf-8 -*-

import yagmail

"""
***--用于邮件告警
*  - 内存大于 20MB - 发送邮件
*  - 句柄大于 700  - 发送邮件
*  - CPU 大于 15%  - 发送邮件
"""

# 测试邮件发送失败，有可能是网卡设置的问题：
# 参考： https://blog.csdn.net/weixin_38428827/article/details/104223207

sendUser = "Sailer@163.com"
sendPwd  = "MGMJSSACLDJPYPM"
host = "smtp.163.com"

receiver = "Sailer@163.com"
topic = "准入客户端资源占用告警专用"

def emailNotify(content):
    yag = yagmail.SMTP(user=sendUser, password=sendPwd, host=host)
    content = ["准入客户端稳定性环境资源占用红线：CPU 占用不超过 15%， 内存占用不超过 20MB，句柄数不超过 700 ==> "+content]
    yag.send(receiver, topic, content)
    yag.close()

