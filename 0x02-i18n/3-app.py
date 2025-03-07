#!/usr/bin/env python3
"""File docs is here"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
from babel import Locale
import pytz


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.init_app(app, locale_selector=get_locale)

@app.route('/')
def home():
    """Home function route"""
    return render_template('3-index.html')


if __name__ == '__main__':
    """Module level docs"""
    app.run()
