# Finding Files

> For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

## Solution Explanation

My approach to this problem was the following:

1. Copy the provided helper code to my local programming IDE

2. Initialize the `files` array that's going to save the returned string paths

```python
def find_files(suffix, path, files=[]):
```

3. Initialize `wholePath` variable that's going to be set to the suffix, in the first iteration, it's going to be a "."

```python
wholePath = suffix
```

4. Check if a path was passed and exists, if that condition it's `True`, make the whole path have the suffix + the "/" + the passed path, for the first iteration, the value of `wholePath` it's going to be equal to:

`"./testdir"`

```python
if path:  # if path exists
    wholePath = suffix + '/' + path  # create full path as a string
```

5. Iterate, for each file in the `wholePath` directory

```python
for file in os.listdir(wholePath):
```

6. add the file name to the path and save the value in the new path variable, this would become the full path to each file, this could be the path to another directory or a file

```python
wholePath2 = wholePath + '/' + file  # create full path plus the file name
```

7. Check if the `wholePath2` it's a file or a directory, and if it's a file, then check if it ends with ".c", if it does, append the `wholePath2` to the files array we declared in the second step

```python
# if the file is a file instead of a folder, and ends with ".c"
if os.path.isfile(wholePath2) and wholePath2.endswith(".c"):
    # append the string path to the files array
    files.append(wholePath2)
```

8. If the path does not lead to a file but instead to a directory, use recursion to repeat the process but with an updated path.

```python
# else, meaning the path it's a folder
elif os.path.isdir(wholePath2):
    files = find_files(wholePath, file, files)  # use recursion
```

9. After the recursion process it's done, and the code has traversed through all directories and their sub-directories, return the `files` array containing our paths to all files that end with ".c"

```python
return files  # after everything it's done, return the files array containing the string paths
```

### Run Time Analysis

The complexity of this program is: `O(depth * average number of dictionaries in each level)`
