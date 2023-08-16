#!/usr/bin/python3

"""
Begins a Flask web application
"""

from flask import Flask
app = Flask(__name__)

# Route for the custom route (/airbnb-onepage/)
@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_airbnb():
    return "Hello from /airbnb-onepage!\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

