from slack_stuff.settings import token
from slackclient import SlackClient


def slack_sender(message_data: list, slack_id: str):
    slack_client = SlackClient(token=token)

    message_data[0] = str(message_data[0])

    message = f'{message_data[1]}\n\n Author: {message_data[2]}\n Date: {message_data[0]}'

    channels = slack_client.api_call('chat.postMessage',
                                     channel=slack_id,
                                     text=message)
