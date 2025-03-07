#!/usr/bin/env python3
"""File docs is here"""
from flask import Flask, render_template
from flask_babel import Babel
from babel import Locale
import pytz


class Config:
    LANGUAGES = ["en", "fr"]
    default_timezone = pytz.timezone('UTC')
    default_local = Locale('en')


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def home():
    """Home function route"""
    return render_template('1-index.html')


if __name__ == '__main__':
    """Module level docs"""
    app.run()
