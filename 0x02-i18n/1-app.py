#!/usr/bin/env python3
"""File docs is here"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"


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
