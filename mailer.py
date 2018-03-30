#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'sourcemail@gmail.com'
email_send = 'destinationmail@hotmail.com'

msg = MIMEMultipart()

msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = 'Subject'
body = 'Message'
msg.attach(MIMEText(body , 'plain'))

filename = 'face.jpg'
attachment = open(filename,'rb')

part = MIMEBase('application' , 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)

part.add_header('Content-Disposition' , 'attachment', filename=filename)
msg.attach(part)

text = msg.as_string()



server = smtplib.SMTP('smtp.gmail.com',587) # you have to enable less secure apps option for SMTP service settings in your gmail account

server.ehlo()

server.starttls()

server.login(email_user, 'yourpassword')

server.sendmail(email_user, email_send, text)

server.close()

print('Mail sent successfully')
