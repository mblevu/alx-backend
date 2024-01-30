#!/usr/bin/env python3
"""Basic cache dictionary"""


BaseCaching = __import__('base_caching').BaseCaching

class BaseCache(BaseCaching):
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
