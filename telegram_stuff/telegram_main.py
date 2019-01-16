import json
from flask import Flask, request, jsonify
from flask_sslify import SSLify


app = Flask(__name__)
ssl = SSLify(app)


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        write_json(r)
        return jsonify(r)
    return '<h1>Hello world</h1>'


if __name__ == '__main__':
    app.run()
