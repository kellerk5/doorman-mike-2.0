import time
from slackclient import SlackClient

#grabs bot token
import bot_token
import print_bot_id

slack_bot_id = print_bot_id.get_bot_id()
slack_client = SlackClient(bot_token.SLACK_BOT_TOKEN)

AT_BOT = "<@" + slack_bot_id + ">:"
EXAMPLE_COMMAND = "do"
TEST_COMMAND = "sayHi"
READ_WEBSOCKET_DELAY = 1

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
        print('testing out the command obj ', command)
    else:
        response = "MORNIN MORNIN BAYBEHHH!"
        print('testing out the command obj ', command)
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

if slack_client.rtm_connect():
    print('MikeBot 2.0 is connected and running!')
    while True:
        command, channel = parse_slack_output(slack_client.rtm_read())
        if command and channel:
            handle_command(command, channel)
        time.sleep(READ_WEBSOCKET_DELAY)
else:
    print('Connection failed. Invalid Slack token or bot ID?')