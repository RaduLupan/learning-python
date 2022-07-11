def get_index(key):
    '''
    Description: Simple hashing function that calculates the index of a key by adding up all Unicode numbers for all characters.
    '''
    index = 0

    for i in range(len(key)-1):
        index += ord(key[i])

    return index
