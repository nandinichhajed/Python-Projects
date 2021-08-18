# more modified version we have written the main content in the html 
# file and we and customize names accourding to our need

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Nandini Chhajed'
email['to'] = 'Email ID'
email['subject'] = 'Helloo Nandini here'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Email ID', 'Password')
    smtp.send_message(email)
    print('all good boss!')
