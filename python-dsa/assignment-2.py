def get_index(key):
    '''
    Description: Simple hashing function that calculates the index of a key by adding up all Unicode numbers for all characters.
    '''
    index = ord(key[0])

    for i in range(1,len(key)-1):
        index += ord(key[i])

    return index

print(get_index('Dan'))
print(f"get_index('a'): {get_index('a')}")
