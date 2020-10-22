#!/usr/bin/env python3

from flask import Flask
from flask import render_template


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
