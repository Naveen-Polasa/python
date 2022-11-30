from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'naveenpolasa98@gmail.com'
email_password = ''

email_reciever = 'naveenpolasa99@gmail.com'

subject = "Email Sender"

body = """
This mail is sent using Email Sender app made with Python
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())
