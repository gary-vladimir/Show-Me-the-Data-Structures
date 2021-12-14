import os


def find_files(suffix, path, files=[]):
    wholePath = suffix
    if path:  # if path exists
        wholePath = suffix + '/' + path  # create full path as a string
    # iterate, for each file in wholePath directory
    for file in os.listdir(wholePath):
        wholePath2 = wholePath + '/' + file  # create full path plus the file name
        # if the file is a file instead of a folder, and ends with ".c"
        if os.path.isfile(wholePath2) and wholePath2.endswith(".c"):
            # append the string path to the files array
            files.append(wholePath2)
        # else, meaning the path it's a folder
        elif os.path.isdir(wholePath2):
            files = find_files(wholePath, file, files)  # use recursion

    return files  # after everything it's done, return the files array containing the string paths


print(find_files('.', 'testdir'))
