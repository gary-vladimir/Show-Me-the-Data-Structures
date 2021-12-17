import sys


def huffman_encoding(data):
    huffman_dictionary = {}
    for character in data:
        huffman_dictionary[character] = huffman_dictionary.get(
            character, 0) + 1

    tree = {}
    temp = '1'
    for num in sorted(huffman_dictionary.items(), key=lambda x: x[1]):
        tree[num[0]] = temp
        temp = '0' + temp

    encode = ''
    for i in data:
        encode += tree[i]
    return encode, tree


def huffman_decoding(data, tree):
    huffman = {}
    for character in tree:
        huffman[tree[character]] = character

    temp = ''
    decode = ''
    for d in data:
        if d == '1':
            decode += huffman[temp + d]
            temp = ''
        else:
            temp += d
    return decode


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"  # <= test 1

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = "AAAAAB"  # <= test 2

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = " "  # <= test 3

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
