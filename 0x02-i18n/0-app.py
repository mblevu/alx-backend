#!/usr/bin/env python3
"""flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """index page"""
    return render_template('0-index.html',
                           title='Welcome to Holberton',
                           text='Hello world')


if __name__ == '__main__':
    app.run()
