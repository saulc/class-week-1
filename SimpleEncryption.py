# Simple Encryption

def input():
    # Get input
    key = input("Enter key: ")

    key_dict = dict()
    # Clean input
    order = 0;
    for i in key:
        if i not in key_dict:
            key_dict[i] = order
            order += 1

    print(key_dict.keys())