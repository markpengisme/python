import smtplib
from email.mime.text import MIMEText
from email.header import Header

'''
There are three variables in the abc file
sender_gmail_account,sender_gmail_password,recipient_gmail_account
'''
from setup import *

message = MIMEText('我是內容', 'plain', 'utf-8')
message['From'] = Header("我是寄信者", 'utf-8')
message['To'] =  Header("我是收信者", 'utf-8')
subject = '我是主題'
message['Subject'] = Header(subject, 'utf-8')


try:
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.starttls()
	#第一個參數是電郵帳號，第二個參數是密碼
	smtpObj.login(sender_gmail_account,sender_gmail_password) 
	#to = recipient_gmail_account  #收件者的電郵地址，為list資料型態
	#利用sendmail 這個method 來寄出電郵，SMTP.sendmail(from_addr, to_addrs, msg, mail_options=[], rcpt_options=[])
	smtpObj.sendmail(sender_gmail_account,recipient_gmail_account,message.as_string()) 
	#關閉本地端對遠端郵件伺服器的連線
	smtpObj.quit()
	print("Send Mail success")
except smtplib.SMTPException:
	print("Send Mail Error")