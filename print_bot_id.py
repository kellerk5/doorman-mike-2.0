from slackclient import SlackClient
from bot_token import SLACK_BOT_TOKEN

BOT_NAME = 'doorman_mike_2.0'
slack_client = SlackClient(SLACK_BOT_TOKEN)

def get_bot_id():

    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for " + user['name'] + " is " + user.get('id'))
                global bot_id
                bot_id = user.get('id')
                return bot_id
    else:
        print("could not find bot user with the name " + BOT_NAME)

# print('Testing testing testies ', get_bot_id())


