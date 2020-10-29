# -*- coding:utf8 -*-
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.qq.com"
mail_user="357815270@qq.com"
mail_pass=""
mail_port=465

def sendEmail(fromAddr,toAddr,subject,content):
    sender = fromAddr
    receivers = [toAddr]
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(fromAddr,'utf-8')
    message['To'] = Header(toAddr, 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smptObj = smtplib.SMTP_SSL(mail_host,mail_port)
        smptObj.login(mail_user,mail_pass)
        smptObj.sendmail(sender,receivers,message.as_string())
        print("send success")
    except smtplib.SMTPException as e :
        print(e)
        print("Error:send fail")

def main_handler(event, context):
    cmqMsg = None
    if event is not None and "Records" in event.keys():
        if len(event["Records"]) >= 1 and "CMQ" in event["Records"][0].keys():
            cmqMsgStr = event["Records"][0]["CMQ"]["msgBody"]
            cmqMsg = json.loads(cmqMsgStr)
    print(cmqMsg)
    sendEmail(cmqMsg['fromAdrr'],cmqMsg['toAddr'],cmqMsg['title'],cmqMsg['body'])
    return "send email success"
    


