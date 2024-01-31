#!/usr/bin/env python3
"""Basic cache dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class BaseCache(BaseCaching):
    """inherits from BaseCaching class"""
    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
