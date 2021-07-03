# Made with twillo
from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='Twillo Phone Number',
    messaging_service_sid='',
    body='Helloooooo Sending You This From Python ',
    to='Your Phone Number'
)

print(message.sid)
