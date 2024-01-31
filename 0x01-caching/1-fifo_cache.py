#!/usr/bin/env python3
"""Basic fifo caching module.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """fifo caching system that inherits from basecaching"""
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first = next(iter(self.cache_data))
            self.cache_data.pop(first)
            print("DISCARD: {}".format(first))

    def get(self, key):
        """Retrieves an item by key"""
        return self.cache_data.get(key, None)
