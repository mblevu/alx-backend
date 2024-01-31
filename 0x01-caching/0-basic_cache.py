#!/usr/bin/env python3
"""Basic cache dictionary"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))


class BasicCache(BaseCaching):
    """inherits from BaseCaching class"""
    def put(self, key, item):
        """assigns to the dictionary"""
        if key and item:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """must return the value linked to key"""
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
