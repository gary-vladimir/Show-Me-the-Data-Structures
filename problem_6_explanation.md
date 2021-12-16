# Union and Intersection

> You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively.

## Solution Explanation

My approach to this problem was the following:

1. Copy the provided helper code to my local programming IDE

2. I decided to start with the `union` function by creating a new `set()` and traverse the first passed linked list and for each node, append the value to the set.

```python
my_set = set()

node = llist_1.head
while node:
    my_set.add(node.value)
    node = node.next
```

4. After the first list is traversed, traverse the second list and for each node, append the value to the same `my_set` set

```python
node = llist_2.head
while node:
    my_set.add(node.value)
    node = node.next
```

5. Up until now, we have a set with the first linked list values and the second list values. Now, we need to create a new Linked list and for each element in the set, append the value to the new linked list

```python
linked_list = LinkedList()
for value in my_set:
    linked_list.append(value)
```

6. Lastly, return the linked list

```python
return linked_list
```

7. Code `intersection` function by doing exactly the same showed above with the differences that we create two sets for each list and before creating the final `linked_list` use the python `.intersect` method to create a final set

```python
set1 = set()
current = llist_1.head
while current:
    set1.add(current.value)
    current = current.next

set2 = set() # <-- new line
current = llist_2.head
while current:
    set2.add(current.value)
    current = current.next

final_set = set1.intersection(set2) # <-- new line

linked_list = LinkedList()
for value in final_set:
    linked_list.append(value)
return linked_list
```

### Run Time Analysis

The time complexity for union and intersection is: `O(n)`
