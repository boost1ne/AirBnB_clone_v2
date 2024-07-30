#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False
@app.route('/')
def home():
    """
    Displays Hello HBNB! msg
    """
    return 'Hello HBNB!'
@app.route('/hbnb')
def hbnb():
    """
    Displays HBNB msg
    """
    return 'HBNB'

@app.route('/c/<text>')
def c_pluse_params(text):
    """
    Displays C <text> msg
    """
    without_underscor = text.replace('_',' ')
    return 'C {}'.format(without_underscor)
@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python_pluse_params(text='is_cool'):
    """
    Displays Python <text> msg
    """
    without_underscor = text.replace('_', ' ')
    return 'Python {}'.format(without_underscor)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)