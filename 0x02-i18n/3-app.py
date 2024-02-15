#!/usr/bin/env python3
"""flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

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
    return render_template('3-index.html',
                           title=gettext('home_title'),
                           text=gettext('home_header'))


@babel.localeselector
def get_locale() -> str:
    """get locale to determine best match for language"""
    return request.accept_languages.best_match(app.config['LANGUAGES']), 200


if __name__ == '__main__':
    app.run()
