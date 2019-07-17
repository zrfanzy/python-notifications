# Slack-Notification
Tutorial of how to use python to send slack notifications

## 1. Get your Slack token
Go to  https://api.slack.com/docs/oauth-test-tokens to get your *token*

## 3. Send a Slack message in Python via Slack API
First, install the official Slack Python package:
~~~~
pip install slackclient
~~~~
Then you can use the following example code `send_message_example.py` to send a hello world slack message:
~~~~
from slackclient import SlackClient

def slack_message(message, channel):
    token = 'xxxxxxxx'
    sc = SlackClient(token)    

    sc.api_call('chat.postMessage', channel=channel, 
                text=message, username='My Sweet Bot',
                icon_emoji=':robot_face:')

slack_message(message='hello world', channel='random_discussions')
~~~~
Don't forget to replace the placeholder values for `token` with your unique values. Also you should edit the message and channel.

Once you’ve updated the code sample, you can test it out by running it from the command line:
~~~~
python send_message_example.py
~~~~
