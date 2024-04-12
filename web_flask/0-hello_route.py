#!/usr/bin/python3
"""
A script that starts a Flask web application with route /
"""
from flask import Flask



app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
     Displays a Hello string
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
