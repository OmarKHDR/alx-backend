#!/usr/bin/env python3
'''This is a doc for [py]
'''


def index_range(page=0, page_size=0):
    '''This will return a tuple
    '''
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
