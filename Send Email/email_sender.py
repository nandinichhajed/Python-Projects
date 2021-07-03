import smtplib
from email.message import EmailMessage

email = EmailMessage()
# object    class
email['from'] = 'Nandini Chhajed'
email['to'] = 'Email ID'
email['subject'] = 'Helloo Nandini here'

email.set_content('sending you this from python')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:  # smtp is a protocol
    smtp.ehlo()
    smtp.starttls()  # tls is an encription mechenism
    smtp.login('Email ID', 'Password')
    smtp.send_message(email)
    print('all good boss!')
