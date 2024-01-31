#!/usr/bin/env python3
"""lifo Basic caching module.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """lifo caching module that imports from basecaching"""
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """adds an item in the cache"""
        if key is None or item is None:
            return
        self.cache_dat[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = next(reversed(self.cache_data))
            self.cache_data.pop(last)
            print("DISCARD: {}".format(last))

    def get(self, key):
        """gets an item from the cache"""
        return self.cache_data.get(key, None)
