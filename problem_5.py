import datetime
import hashlib


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, time_stamp, value):
        if self.head is None:
            self.head = Block(time_stamp, value, 0)
            self.tail = self.head
        else:
            previous_hash = self.tail
            self.tail = Block(time_stamp, value, previous_hash)
            self.tail.previous_hash = previous_hash


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


def time_stamp_generator():
    return datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")


chain = Linked_List()
chain.append(time_stamp_generator(), "Owls don't have eyeballs")
chain.append(time_stamp_generator(), "In space, metal can weld on its own.")
chain.append(time_stamp_generator(), "Cows kill more people than sharks.")

print(chain.tail.data)
print(chain.tail.previous_hash.data)
print(chain.tail.previous_hash.previous_hash.data)
