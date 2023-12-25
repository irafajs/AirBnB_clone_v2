#!/usr/bin/python3
"""Shebang to create a python scipt"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """function to print hello HBNB! at location /"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function to print HBNB at location /"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """print text at c location plus passed argumenr /"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """print text at c location plus passed argumenr /"""
    if text:
        text = text.replace('_', ' ')
        return 'Python {}'.format(text)
    else:
        return 'Python is cool'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
