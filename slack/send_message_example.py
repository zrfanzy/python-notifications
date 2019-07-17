from slackclient import SlackClient

def slack_message(message, channel):
    token = 'xoxp-260448886196-259752523888-696536901092-017922652de4435bde7b97b4d75a88c0'
    sc = SlackClient(token)    

    sc.api_call('chat.postMessage', channel=channel, 
                text=message, username='My Sweet Bot',
                icon_emoji=':robot_face:')

slack_message('hello world from rzhou', 'random_discussions')