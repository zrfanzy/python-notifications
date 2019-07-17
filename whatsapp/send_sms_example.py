from twilio.rest import Client
account_sid = 'ACxxxxxx'
auth_token = 'xxxxxx'
# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
client = Client(account_sid, auth_token)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+1xxxxxx'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+xxxxxx'

client.messages.create(body='Hello, World!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)


