# Active Directory

> Write a function that provides an efficient look up of whether the user is in a group.

## Solution Explanation

My approach to this problem was the following:

1. Copy the provided helper code to my local programming IDE

2. I decided to use recursion to solve this problem, so, the first thing I did, was to write my breaking condition.

```python
if user == group.get_name() or user in group.get_users():
    return True
```

3. If the none of the conditions are True, then procced to iterate for group in groups and use recursion to repeat the process for each group.

```python
for g in group.get_groups():
    return is_user_in_group(user, g)
```

4. If the for loop ends, that means that the user was not found and return False

```python
return False
```

### Run Time Analysis

The complexity of this program is: `O(n)`
