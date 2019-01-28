import re
import requests
from telegram_stuff.settings import main_url


def parse_slack_link(url: str):
    """
    Parse link on slack channel and return slack channel id

    Args:
        url: link on slack channel

    Returns:
        str: slack_channel_id

    """

    match = re.search(r'[^https?\://[a-z0-9\.-]{0,21}slack\.com/messages/[a-zA-Z0-9]{0,}[^.\/]{0,}', url)
    match = re.search(r'[^slack.com/messages/][A-Za-z0-9]{0,}', match[0])

    return match[0]


def get_link_on_slack(json_dict: dict):
    """
    Check message if it has link on slack channel. If True function parses link and returns list with telegram and
    slack ids. That allows to add these ids in redis db.

    Args:
        json_dict: dict with telegram updates

    Returns:
        list:
            - first element is telegram_channel_id
            - second element is slack_channel_id

    """

    try:
        if json_dict['channel_post']['entities'][0]['type'] == 'bot_command':

            text_string = json_dict['channel_post']['text']

            if text_string.split()[0] == '/add_link':

                telegram_chat_id = json_dict['channel_post']['chat']['id']  # get telegram chat id from
                # json_dict(type: dict)

                slack_link = json_dict['channel_post']['text']  # get text of message from telegram channel
                slack_link = slack_link.split()[1]  # get slack link

                check_correct_form = re.search(r'https?\://[a-z0-9-]{0,}\.slack\.com/messages/[A-Z0-9]{0,}/.{0,}',
                                               slack_link)  # check if link is valid

                # print('yes' if check_correct_form else 'no')

                if check_correct_form:
                    slack_id = parse_slack_link(slack_link)  # parse link
                    telegram_message_id = json_dict['channel_post']['message_id']
                    delete_slack_link_message(telegram_chat_id, telegram_message_id)
                    return [telegram_chat_id, slack_id]

                else:
                    slack_link_error = 'Sorry, please write link in correct form'
                    print(slack_link_error)

                    return slack_link_error

            else:

                return 'Unknown bot command but I`m not sure'

    except KeyError:
        return None


def delete_slack_link_message(telegram_chat_id: int, telegram_message_id: int):
    """
    Delete message with slack link to not make a mess in telegram channel

    Args:
        telegram_chat_id: telegram chat id
        telegram_message_id: telegram message id

    """

    method = 'deleteMessage'
    params = {'chat_id': telegram_chat_id, 'message_id': telegram_message_id}
    resp = requests.get(main_url + method, params)
