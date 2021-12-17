# Blockchain

> Use your knowledge of linked lists and hashing to create a blockchain implementation.

## Solution Explanation

My approach to this problem was the following:

1. Copy the provided helper code to my local programming IDE and import useful `datetime` library

```python
import datetime
```

2. Proceed to move the provided `calc_hash` function to become a method of the `Block` class for convenience purposes.

```python
class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, data): # <====
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
```

3. Code and initialize the `Linked_List` class

```python
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
```

4. Code `append()` method:

```python
    def append(self, time_stamp, value):
        if self.head is None:
            self.head = Block(time_stamp, value, 0)
            self.tail = self.head
        else:
            previous_hash = self.tail
            self.tail = Block(time_stamp, value, previous_hash)
            self.tail.previous_hash = previous_hash
```

5. Code a `time_stamp_generator` that uses the `datetime` library

```python
def time_stamp_generator():
    return datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")

```

### Run Time Analysis

The time complexity for appending a new value to the chain is: `O(1)`

The space complexity is: `O(n)`
