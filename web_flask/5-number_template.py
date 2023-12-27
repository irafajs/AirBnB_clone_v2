#!/usr/bin/python3
"""Shebang to create a python scipt"""


from flask import Flask, abort, render_template


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


@app.route('/number/<n>', strict_slashes=False)
def number_n(n):
    """print out if real number is passed"""
    try:
        return '{} is a number'.format(int(n))
    except ValueError:
        return abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def n_templete_n(n):
    """retun a html page when the location end with a number"""
    try:
        if int(n):
            return render_template('5-number.html', number=n)
    except ValueError:
        return abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
