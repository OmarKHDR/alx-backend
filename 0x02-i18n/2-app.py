#!/usr/bin/env python3
'''Hello world
'''
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    '''This is docs
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''Hello m y Deer
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def sayHi():
    '''Hi is said
    '''
    return render_template('2-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
