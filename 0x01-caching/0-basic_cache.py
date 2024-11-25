#!/usr/bin/env python3
'''hell is world
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''This is why not how
    '''
    def put(self, key, item):
        '''This wasnt documented
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''Neither this was that si lfei
        '''
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
