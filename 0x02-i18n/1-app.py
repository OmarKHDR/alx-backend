#!/usr/bin/env python3
'''Hello world
'''
from app import babel, app


@app.route('/')
def sayHi():
    '''Hi is said
    '''
    return render_template('1-index.html')
