#!/usr/bin/env python3
"""Last-In First-Out caching module.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initialize the class with the parent's init method"""
        super().__init__()
        self.last_key = None  # To keep track of the last added key

    def put(self, key, item):
        """
        Add an item in the cache. If the cache is over the limit,
        discard the last added item (LIFO).
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        self.last_key = key

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Discard the last added item
            print(f"DISCARD: {self.last_key}")
            del self.cache_data[self.last_key]

    def get(self, key):
        """
        Get an item by key. Return None if the key doesn't exist or is None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]