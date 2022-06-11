'''
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
Your function should have the worst-case complexity of O(log N), where N is the length of the list. 
You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
We define "rotating a list" as removing the last element of the list and adding it before the first element. 
E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].
'''
def count_rotations(nums):
    '''
    Description: Determines the minimum number of rotations applied to a sorted list of numbers to obtain the given list.
    Parameters:
    nums: the rotated list of numbers.
    '''

import dsa

# The structure of a test. The list in test['input']['nums'] was obtained by rotating [12, 45, 77, 81, 92, 101, 235, 400, 505] list 4 times.
test={
    'input': {
        'nums': [101, 235, 400, 505, 12, 45, 77, 81, 92]
    },
    'output': 4
}

# Create more test cases.

# A list of size 9 rotated 4 times.
test0=test

# A list of size 8 rotated 5 times.
test1 = {
    'input': {
        'nums': [12, 15, 18, 21, 28, 4, 9, 10]
    },
    'output': 5
}

# A list that wasn't rotated at all.
test2 = {
    'input': {
        'nums': [1, 10, 100, 1400]
    },
    'output': 0
}

# A list that was rotated just once.
test3 = {
    'input': {
        'nums': [47, 20, 28, 35, 45]
    },
    'output': 1
}

# A list that was rotated n-1 times, where n is the size of the list.
test4 = {
    'input': {
        'nums': [-20, -15, 0, 19, 35, -30]
    },
    'output': 5
}

# A list that was rotated n times, where n is the size of the list. 
# A list rotated n times equals to the original sorted list which is rotated 0 times.
# Since the function must return the minimum number of rotations the output for this test case is 0.
test5 = {
    'input': {
        'nums': [1, 2, 3, 4, 5, 6, 7]
    },
    'output': 0
}

# An empty list. An empty list is always sorted so needs to be rotated zero times.
test6 = {
    'input': {
        'nums': []
    },
    'output': 0
}

# A list containing just one element.
test7 = {
    'input': {
        'nums': [100]
    },
    'output': 0
}



