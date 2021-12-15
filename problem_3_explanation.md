# Huffman Coding

> You will have to implement the logic for both encoding and decoding in the following template. Also, you will need to create the sizing schemas to present a summary.

## Solution Explanation

My approach to this problem was the following:

1. Copy the provided helper code to my local programming IDE

2. I decided to start with the encoding function by initializing a `huffman_dictionary` and for each character in the passed data, add the character to the dictionary:

```python
huffman_dictionary = {}
for character in data:
    huffman_dictionary[character] = huffman_dictionary.get(
        character, 0) + 1
```

3. Then, I created the tree:

```python
tree = {}
temp = '1'
for num in sorted(huffman_dictionary.items(), key=lambda x: x[1]):
    tree[num[0]] = temp
    temp = '0' + temp
```

4. Finally, create the final `encode` variable and return it along with the tree

```python
encode = ''
for i in data:
    encode += tree[i]
return encode, tree
```

5. After finishing the `huffman_encoding` function, it was time to start the `huffman_decoding` procedure by creating a `huffman` dictionary, and iterating for each character in the passed tree to add the character to the `huffman` dictionary

```python
huffman = {}
for character in tree:
    huffman[tree[character]] = character

```

6. Then, I proceded to initialize `temp` and `decode` variables to an empty string

```python
temp = ''
decode = ''
```

7. Next, I iterated for each letter in the passed encoded data and decoded them

```python
temp = ''
decode = ''
for d in data:
    if d == '1':
        decode += huffman[temp + d]
        temp = ''
    else:
        temp += d
```

8. After the loop it's done, simply return the decode string result

```python
return decode
```

### Run Time Analysis

The complexity of this program is: `O(n)`
