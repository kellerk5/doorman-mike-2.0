#get scripted responses, also starts MikeBot
import scripted_responses

from wit import Wit

def send(request, response):
    print('Sending to user...', response['text'])
    print('testing request ', request)
    print('testing response ', response)
def my_action(request):
    print('Received from user...', request['text'])
    print('testing request ', request)

actions = {
    'send': send,
    'my_action': my_action,
}

client = Wit(access_token='6OFKNQ6FVKXZKUSC4TPSI2GHENUKZGAA', actions=actions)