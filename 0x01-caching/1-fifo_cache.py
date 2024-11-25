#!/usr/bin/env python3
'''Hello World and holberton school
'''
BaseCaching = __import__('base_caching').BaseCaching
from collections import deque


class FIFOCache(BaseCaching):

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
        if len(self.__queue) >= BaseCaching.MAX_ITEMS and key not in self.__queue:
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


my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
