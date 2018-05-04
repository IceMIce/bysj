# coding:utf-8
'''
用于发送邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "944426045@qq.com"  # 用户名
mail_pass = "myervdzgdnpibbed"  # 口授权码

sender = '944426045@qq.com' # 发送者

def send_email(mail_address, mail_message):
    """
    :param address: 对方的地址
    :param message: 输入的内容
    :return: True/False
    """
    receivers = [mail_address]
    message = MIMEText(mail_message, 'plain', 'utf-8')
    message['From'] = Header("预约挂号服务邮箱", 'utf-8')
    message['To'] = Header(mail_address, 'utf-8')

    subject = 'my test'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print u"邮件发送成功"
    except smtplib.SMTPException, e:
        print e

send_email("411775793qq.com", "测试")