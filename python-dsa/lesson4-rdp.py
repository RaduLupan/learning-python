'''
Recursion and Dynamic Programming
Question 1: Write a function to find the length of the longest common subsequence between two sequences.
Example: Given the strings "serendipitous" and "precipitation", the longest common subsequence is "reipito" and the length is 7.
'''

# Test cases.

# 1. General case - string.
test0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7 
}

# 2. General case - list.
test1 = {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
}

# 3. Another general case - string.
test2 = {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
}

# 4. No common subsequence.
test3 = {
    'input': {
        'seq1': 'qwerty',
        'seq2': 'asdfgh'
    },
    'output': 0
}

# 5. One is a subsequence of the other.
test4 = {'input': {'seq1': 'dense', 'seq2': 'condensed'}, 'output': 5}

# 6. One sequence is empty.
test5 = {'input': {'seq1': '', 'seq2': 'abcdef'}, 'output': 0}

# 7. Both sequences are empty.
test6 = {'input': {'seq1': '', 'seq2': ''}, 'output': 0}

# 8. Multiple sequences with same length.
test7 = {'input': {'seq1': 'abcdef', 'seq2': 'badcfe'}, 'output': 3}

tests = [test0, test1, test2, test3, test4, test5, test6, test7]
