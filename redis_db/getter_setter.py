from datetime import datetime
import re
import redis


uri = 'https://mycursor.slack.com/messages/CFAJE9XHA/?asf12ASDqwe=+123'


def parse_slack_link(url: str):

    match = re.search(r'[^https?\://[a-z0-9\.-]{0,21}slack\.com/messages/[a-zA-Z0-9]{0,}[^.\/]{0,}', url)
    match = re.search(r'[^slack.com/messages/][A-Za-z0-9]{0,}', match[0])

    return match[0]


def get_link_on_slack(json_dict: dict):

    try:
        if json_dict['channel_post']['entities'][0]['type'] == 'bot_command':

            text_string = json_dict['channel_post']['text']

            if text_string.split()[0] == '/add_link':

                telegram_chat_id = json_dict['channel_post']['chat']['id']
                slack_link = json_dict['channel_post']['text']
                slack_link = slack_link.split()[1]
                match = re.search(r'https?\://[a-z0-9-]{0,}\.slack\.com/messages/[A-Z0-9]{0,}/.{0,}', slack_link)
                print('yes' if match else 'no')
                if match:
                    return [telegram_chat_id, slack_link]
                else:
                    slack_link_error = 'Sorry, please write link in correct form'
                    print(slack_link_error)
                    return slack_link_error
    except KeyError:
        return None


def get_all(json_dict: dict):

    timestamp = json_dict['channel_post']['date']
    converted_date = datetime.fromtimestamp(timestamp)
    output_data = {'time': converted_date}

    try:

        text = json_dict['channel_post']['text']
        output_data['text'] = text

    except KeyError:
        pass

    try:

        author = json_dict['channel_post']['author_signature']
        output_data['author'] = author

    except KeyError:
        pass

    return output_data


def redis_main(json_dict):

    conn_pool = redis.ConnectionPool(host='localhost', port=6379, db=0)  # creation connection to redis
    redis_cli = redis.Redis(connection_pool=conn_pool)  # creation connection to redis

    try:
        list_tg_id_slack_link = get_link_on_slack(json_dict)
        telegram_channel_id = list_tg_id_slack_link[0]  # getting telegram channel id
        slack_link = list_tg_id_slack_link[1]  # getting link on slack channel
        slack_channel_id = parse_slack_link(slack_link)  # getting slack channel id
        redis_cli.set(telegram_channel_id, slack_channel_id)  # setting in redis_db telegram and slack id

    except TypeError:
        pass
