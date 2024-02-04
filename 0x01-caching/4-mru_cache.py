#!/usr/bin/env python3
"""MRU Basic caching module.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching module that inherits from basecaching"""
    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, items):
        """adds an items to the cache"""
        if key is None or items is None:
            return
        self.cache_data[key] = items
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.keys.remove(key)
            self.cache_data.pop(last)
            print("DISCARD: {}".format(last))

    def get(self, key):
        """gets an item from the cache"""
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key, None)
