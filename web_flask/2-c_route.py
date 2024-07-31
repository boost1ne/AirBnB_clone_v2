#!/usr/bin/python3
""" Starts a Flask application that MUST be lisening on 0.0.0.0, port 5000.
"""
from flask import Flask, escape


app = Flask(__name__)
app.url_map.strict_slashes = False  # override default globally


@app.route('/')
def hello_world():
    """ Returns 'Hello HBNB' """
    return "Hello HBNB!"


@app.route('/hbnb')
def hello_world_2():
    """ Returns 'HBNB' """
    return "HBNB"


@app.route('/c/<text>')
def hello_world_3(text):
    """ Returns 'C' followed by (space replaced underscores) text """
    return "C {}".format(escape(text).replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
