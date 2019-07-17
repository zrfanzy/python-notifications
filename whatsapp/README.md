# Whatsapp-Notification
Tutorial of how to use python and Twilio send whatsapp notifications

## 1. Sign up for a Twilio account
Go to https://www.twilio.com/ to sign up a free Twilio account. Once signed up, head over to your Console(https://www.twilio.com/console) and grab your *Account SID* and your *Auth Token*, these two values are needed for sending message.

## 2. Get a Whatsapp sandbox
Go to WhatsappSandbox(https://www.twilio.com/console/sms/whatsapp/learn), follow the instructions to setup your sandbox. Take note of your *sandbox testing number*.

## 3. Send an SMS message in Python via the REST API
First, install the Twilio helper library:
~~~~
pip install twilio	
~~~~
Then you can use the following example code `send_sms_example.py` to send a hello world whatsapp message:
~~~~
from twilio.rest import Client

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
account_sid = 'ACxxxxxxxx'
auth_token = 'xxxxxxxx'
client = Client(account_sid, auth_token)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+1xxxxxxxx'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+xxxxxxxx'

client.messages.create(body='Hello, World!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
~~~~
Don't forget to replace the placeholder values for `account_sid` and `auth_token` with your unique values. You can find these in your Twilio console(https://www.twilio.com/console). You also need to modify the `from_whatsapp_number` to your Twilio sandbox number(which you should find it here: https://www.twilio.com/console/sms/whatsapp/sandbox), and replace the `to_whatsapp_number` to the Whatsapp number that you want to send the message to.

Once you’ve updated the code sample, you can test it out by running it from the command line:
~~~~
python send_sms_example.py
~~~~
