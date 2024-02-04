#!/usr/bin/env python3
"""LFU Basic caching module.
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU caching module that inherits from basecaching"""
    def __init__(self):
        super().__init__()
        self.keys = []
        self.count = {}

    def put(self, key, item):
        """adds item to the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            discard = min(self.count.values())
            for k, v in self.count.items():
                if v == discard:
                    break
            if k in self.cache_data:
                self.cache_data.pop(k)
                self.count.pop(k)
                print("DISCARD: {}".format(k))
        self.cache_data[key] = item
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
        self.count[key] = 0
        for k in self.count:
            self.count[k] += 1

    def get(self, key):
        """gets an item from the cache"""
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
            self.count[key] = 0
        return self.cache_data.get(key, None)
