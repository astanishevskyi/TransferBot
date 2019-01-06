from telegram_stuff.settings import auth_token, main_url
import requests
from datetime import datetime
from flask import Flask, request


app = Flask(__name__)


def get_updates():
    method = 'getUpdates'
    response = requests.get(main_url + method)
    response_json = response.json()['result']
    return response_json


last_update = get_updates()[-1]


def get_channel_id():

    return last_update['channel_post']['chat']['id']


def get_author_signature():

    return last_update['channel_post']['author_signature']


def get_converted_date_of_message():
    timestamp = last_update['channel_post']['date']
    converted_time = datetime.fromtimestamp(timestamp)
    return converted_time


def get_text_of_message():

    return last_update['channel_post']['text']


# print(get_channel_id())
# print(get_author_signature())
# print(get_converted_date_of_message())
# print(get_text_of_message())


@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        pass
    return '<h1>Hello world</h1>'


if __name__ == '__main__':
    app.run(host='localhost', port=5000)


