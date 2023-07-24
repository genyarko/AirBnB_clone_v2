#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, escape, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """
    Route: /
    Returns:
        "Hello HBNB!"
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route: /hbnb
    Returns:
        "HBNB"
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route: /c/<text>
    Args:
        text: URL parameter representing the text variable
    Returns:
        "C " followed by the value of the text variable (replace underscores with spaces)
    """
    return 'C {}'.format(escape(text.replace('_', ' ')))

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    Route: /python/ or /python/<text>
    Args:
        text: URL parameter representing the text variable with a default value 'is cool'
    Returns:
        "Python " followed by the value of the text variable (replace underscores with spaces)
    """
    return 'Python {}'.format(escape(text.replace('_', ' ')))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route: /number/<n>
    Args:
        n: URL parameter representing the number variable (should be an integer)
    Returns:
        "n is a number" if n is an integer
    """
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route: /number_template/<n>
    Args:
        n: URL parameter representing the number variable (should be an integer)
    Returns:
        HTML page with H1 tag: "Number: n" inside the tag BODY
    """
    return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route: /number_odd_or_even/<n>
    Args:
        n: URL parameter representing the number variable (should be an integer)
    Returns:
        HTML page with H1 tag: "Number: n is even|odd" inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
