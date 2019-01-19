import json
from flask import Flask, request, jsonify
from flask_sslify import SSLify
from redis_db.getter_setter import get_all, get_link_on_slack, redis_main


app = Flask(__name__)
ssl = SSLify(app)


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_json():
    with open("answer.json", "r") as read_file:
        data = json.load(read_file)
        return data


@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        write_json(r)
        redis_main(get_json())

        return jsonify(r)
    return '<h1>Hello world</h1>'


if __name__ == '__main__':
    app.run()
