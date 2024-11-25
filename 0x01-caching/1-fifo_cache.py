#!/usr/bin/env python3
'''Hello World and holberton school
'''
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''HOW to Fuc docummentnw
    '''
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.__queue = deque()

    def put(self, key, item):
        '''This wasnt documented
        '''
        if key is None or item is None:
            return
        if len(self.__queue) >= BaseCaching.MAX_ITEMS\
                and key not in self.__queue:
            del self.cache_data[self.__queue[0]]
            item_del = self.__queue.popleft()
            print("DISCARD:", item_del)
        self.__queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''Neither this was that si lfei
        '''
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
