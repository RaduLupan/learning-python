'''
The following systematic strategy for solving problems will be used for the two problems below.

The method
1. State the problem clearly. Identify the input & output formats.
2. Come up with some examples of inputs and outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem. State it in plain English.
4. Implement the solution and test it using the example inputs. Fix bugs if any.
5. Analyze the algorithm's complexity and identify inefficiencies if any.
6. Apply the right technique to overcome the inefficiencies. Repeat steps 3-6. 

Problem2: Given two strings A and B, find the minimum number of steps required to convert A to B. You have the following 3 operations permitted on a word:
-> Insert a character
-> Delete a character
-> Replace a character
Eeach operation is counted as 1 step.
'''

# 1. State the problem clearly. Identify the input & output formats.
# Input: str1, str2 are the two strings to process.
# Output: an integer representing the minimum number of operations (insert/delete/replace) applied to str1 string in order to convert it str2 string.
# Example:
# str1 = 'intention'
# str2 = 'execution'
# output = 5

def min_steps(str1, str2):
    pass

# 2. Come up with some examples of inputs and outputs. Try to cover all edge cases.
# 2.1 General case.
test0 = {
    'input': {
        'str1': 'intention',
        'str2': 'execution'
    },
    'output': 5
}

# 2.2 No change required (str1 and str2 are equal).
test1 = {
    'input': {
        'str1': 'algorithm',
        'str2': 'algorithm'
    },
    'output': 0
}

# 2.3 All characters in str1 need to be changed.
test2 = {
    'input': {
        'str1': 'morning',
        'str2': 'summer'
    },
    'output': 7
}

# 2.4 The two strings have equal length.
test3 = {
    'input': {
        'str1': 'fog',
        'str2': 'dog'
    },
    'output': 1
}

# 2.5 The two strungs have unequal length.
test4 = {
    'input': {
        'str1': 'nation',
        'str2': 'equation'
    },
    'output': 3
}

# 2.6 One of the strings is empty.
test5 = {
    'input': {
        'str1': '',
        'str2': 'reality'
    },
    'output': 7
}

# 2.7 Only one type of operation is required: one deletion, or one substitution or one insertion.
test6 = {
    'input': {
        'str1': 'fog',
        'str2': 'frog'
    },
    'output': 1
}

tests = [test0, test1, test2, test3, test4, test5, test6]
