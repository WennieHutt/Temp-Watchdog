import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def message():
    email_user = 'temperautre.alert@gmail.com'        #Enter sender's mail.
    email_password = 'cxeqhwlijhmepmmc'#Enter sender's mail email_password
    email_send = 'nellyperez1111@gmail.com'   #Enter reveiver's email.

    subject = 'Temperature'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send  
    msg['Subject'] = subject

    body = 'ALERT! Temperature exceeding 30°C'

    msg.attach(MIMEText(body,'plain'))

    text = msg.as_string()

    smtpServer = ["smtp.mail.yahoo.com", "smtp.gmail.com", "smtp.live.com"]
    smtpPort = [465, 587, 465]

    try:
        server = smtplib.SMTP(smtpServer[1],smtpPort[1]) #Write the corresponding server from the above list.
        server.starttls()
        server.login(email_user,email_password)
        server.sendmail(email_user,email_send,text)

    except Exception as e:
        print(e)

    finally:
         server.quit()

