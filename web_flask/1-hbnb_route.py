#!/usr/bin/python3
""" Starts a Flask application that MUST be lisening on 0.0.0.0, port 5000.
    Required
        routes: /:display "Hello HBNB!" & /hbnb: display "HBNB"
        MUST use the option 'strict_slashes=False in route definition
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Returns 'Hello HBNB' """
    return "Hello HBNB!"


@app.route('/hbnb')
def hello_hbnb2():
    """ Returns 'HBNB' """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
