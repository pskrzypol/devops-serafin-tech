#!/usr/bin/env python3

from flask import Flask
from flask import render_template, jsonify


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'there is nothing to see here...'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/ping')
def ping(name=None):
    return 'pong ping pong ping pong'


@app.route('/test/')
def test(name=None):
    return 'test - fancy reply...'

@app.route('/api/sample_data', methods=["GET"])
def get_sample_data():
    sample_data = {
        "col1": "val1",
        "col2": "val2",
    }

    return jsonify(sample_data)


if __name__ == '__main__':
    app.run(debug=True, port=8082, host="0.0.0.0")
