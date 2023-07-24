#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, escape

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
