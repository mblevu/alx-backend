#!/usr/bin/env python3
"""basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext, format_datetime
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    """index page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
