from collections import deque


class LRU_Cache(object):
    def __init__(self, capacity):
        if capacity > 0:
            self.cache_capacity = capacity
        else:
            raise Exception("Cache has a 0 or negative capacity")
        self.cache_dictionary = {}
        self.cache_deque = deque()

    def get(self, key):
        if key != None:
            return self.cache_dictionary.get(key, -1)
        else:
            return -1

    def set(self, key, value):
        if len(self.cache_deque) >= self.cache_capacity:
            del self.cache_dictionary[self.cache_deque.popleft()]

        self.cache_deque.append(key)
        self.cache_dictionary[key] = value


""" Testing """
# ---------------------------------------- #
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))      # returns 3
# ---------------------------------------- #
our_cache = LRU_Cache(1)

our_cache.set(1, 1)
our_cache.set(3, 3)


print(our_cache.get(1))      # returns -1
print(our_cache.get(2))      # returns -1

our_cache.set(5, 5)
our_cache.set(4, 4)

print(our_cache.get(4))      # returns 4
# ---------------------------------------- #
# Throws an exeption because of negative cache capacity
our_cache = LRU_Cache(-2)

our_cache.set(1, 1)
our_cache.set(3, 3)


print(our_cache.get(1))
print(our_cache.get(3))
# ---------------------------------------- #
