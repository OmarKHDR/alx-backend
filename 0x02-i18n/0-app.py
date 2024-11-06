#!/usr/bin/env python3
'''Hello world is documented
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    '''Hello world is documented
    '''
    return render_template('0-index.html')
