from collections import OrderedDict

class LRUCache:
    'class definition for least recently used cache'
    def __init__(self, capacity):
        # imp part is to use the right data structure, OrderedDict() is a dict that preserves order of insertion
        # order of insertion is needed here for LRU
        # if this was not available, linked hashmap would be built, like a queue
        # This is because OrderedDict in Python is implemented as a combination 
        # of a doubly linked list and a hash table
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1

        # pop key out of cache
        val = self.cache.pop(key)    
        # reinsert into to cache, since it's a LRU
        self.cache[key] = val
        return val
    
    def put(self, key, value):
        # remove key so it can be refreshed
        if key in self.cache:
            self.cache.pop(key)

        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # remove the earliest inserted key
            self.cache.popitem(last=False)