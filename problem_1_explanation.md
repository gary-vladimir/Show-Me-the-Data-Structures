# Least Recently Used Cache

> For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both `get` and `set` operations as an use operation.

## Solution Explanation

My approach to this problem was the following:

1. Copy the provided helper code to my local programming IDE

2. Initialize class variables - In this case, after reading the problem, I concluded that a `cache_capacity`, `cache_dictionary`, and a `cache_deque` variables were going to be needed.

```python
self.cache_capacity = capacity
self.cache_dictionary = {}
self.cache_deque = deque()
```

3. Code `get()` method - First thing I did, was to check if the passed key was not `None` if the condition it's `True`, then proceed to use the python dictionary `get` method, to, as his name says, get the desired value from the dictionary.

```python
if key != None:
    return self.cache_dictionary.get(key, -1)
else:
    return -1
```

4. Code `set()` method - First thing I did, was to check if the cache_deque had exceeded the set capacity, if so, the code deletes the oldest value to create space. After making sure we have space, the code appends the passed key to the cache_deque and finally, adds a new element to the cache_dictionary with the key and value.

```python
if len(self.cache_deque) >= self.cache_capacity:
    del self.cache_dictionary[self.cache_deque.popleft()]

self.cache_deque.append(key)
self.cache_dictionary[key] = value
```

### Run Time Analysis

The time complexity of this program is: `O(1)`

The space complexity of this program is: `O(capacity)`
