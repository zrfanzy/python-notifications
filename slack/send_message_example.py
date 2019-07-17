from slackclient import SlackClient

def slack_message(message, channel):
    token = 'xxxxxxxxxxxxxxxxxxxxx'
    sc = SlackClient(token)    

    sc.api_call('chat.postMessage', channel=channel, 
                text=message, username='My Sweet Bot',
                icon_emoji=':robot_face:')

slack_message('hello world', 'random_discussions')
