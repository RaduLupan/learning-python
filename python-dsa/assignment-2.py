from dataclasses import dataclass


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


