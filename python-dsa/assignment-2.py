'''
Asignement Objective: Implement HashTable class that supports the following operations:
1. Insert: insert a new key-value pair.
2. Find: find the value associated with a key.
3. Update: update the value associated with a key.
4. List: list all the keys stored in the hash table.
'''
def get_index(data_list, a_string):
    '''
    Description: Simple hashing function that uses the ord() function to convert all characters in a string into numbers.
    Algorithm:
    1. Iterate over the string, character-by-character.
    2. Convert each character to a number using Python's built-in ord function.
    3. Add the numbers for each character to obtain the hash for the entire string.
    4. Take the reminder of the result with the size of the data list.
    '''
    # Variable to store the result (updated for each iteration).
    result = 0

    for a_character in a_string:
        # Convert the character to a number using ord().
        a_number = ord(a_character)
        # Add the number to the result.
        result += a_number

    # Get the remainder of the result with the size of the data list.
    list_index = result % len(data_list)

    return list_index

def get_index2 (data_list, a_string):
    '''
    Description: Simple hashing function that uses the ord() function to convert all characters in a string into numbers multiplied by powers of 2 that reflect the position in the string.
    By factoring in the character position in the calculation of the index, it ensures that indeces for strings consisting of permutations of the same characters are different. 
    Algorithm:
    1. Iterate over the string, character-by-character.
    2. Convert each character to a number by multiplying its ord() number by 2 at the power of its position in the string.
    3. Add the numbers for each character to obtain the hash for the entire string.
    Example: 
    'abc' -> ord('a') * 2**0 + ord('b') * 2**1 + ord('c') * 2**2 = 97 + 98 * 2 + 99 * 4 = 689
    'cba' -> ord('c') * 2**0 + ord('b') * 2**1 + ord('a') * 2**2 = 99 + 98 * 2 + 97 * 4 = 683

    4. Take the reminder of the result with the size of the data list.
    '''
    result = 0
    n = len(a_string)

    for i in range(n):
        a_number = ord(a_string[i]) * 2**i
        result += a_number
    
    list_index = result % len(data_list)

    return list_index

MAX_HASH_TABLE_SIZE = 4096

class BasicHashTable:
    def __init__(self, max_size = MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def get_valid_index(self, key):
        '''
        Uses Python ord() function to calculate the hash and linear probing to handle colisions.
        '''
        
        result = 0

        for char in key:
            result += ord(char)

        idx = result % len(self.data_list) 

        while True:
            
            kv = self.data_list[idx]

            # If the element at the idx position is None then return idx as the valid index.
            if kv is None:
                return idx
            
            # If the key at the idx position matches the given key return idx as the valid index.
            if kv[0] == key:
                return idx

            # Check the next position in the list.
            idx += 1

            # If the end of the list is reached go to the beginning of the list.
            if idx == len(self.data_list):
                idx = 0

    
    def __getitem__(self, key):
        '''
        Returns the value associated with a given key.
        '''
        # Calculate a valid index for the given key.
        idx = self.get_valid_index(self.data_list, key)

        kv = self.data_list[idx]

        return kv[1] if kv is not None else None 
    
    def __setitem__(self, key, value):
        '''
        Upsert: Updates the value of a given key if the key exists or inserts the key-value if the key does not exist.
        '''
        pass


#data_list = [None] * MAX_HASH_TABLE_SIZE

#print(len(data_list) == 4096)

#print(get_index(data_list, 'abc') == get_index(data_list, 'cba'))
#print(get_index(data_list, 'listen') == get_index(data_list, 'silent'))

#print(f"get_index2(data_list, 'abc'={get_index2(data_list, 'abc')}")
#print(f"get_index2(data_list, 'cba'={get_index2(data_list, 'cba')}")

#print(get_index2(data_list, 'listen') == get_index2(data_list, 'silent'))

basic_hash_table = BasicHashTable(max_size=10)

print(basic_hash_table.data_list)

print(basic_hash_table.get_valid_index('listen'))
print(basic_hash_table.get_valid_index('silent'))

#print(basic_hash_table.__getitem__('Dan'))
