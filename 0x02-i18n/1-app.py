#!/usr/bin/env python3
"""flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """index page"""
    return render_template('1-index.html',
                           title='Welcome to Holberton',
                           text='Hello world')


if __name__ == '__main__':
    app.run()
