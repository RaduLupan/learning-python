'''
Recursion and Dynamic Programming
Question 1: Write a function to find the length of the longest common subsequence between two sequences.
Example: Given the strings "serendipitous" and "precipitation", the longest common subsequence is "reipito" and the length is 7.
'''

def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
    '''
    Description: Computes the longest common subsequence of two sequences recursively.
    Algorithm:
    1. Define two counters idx1 for seq1 and idx2 for seq2 that are both zero initially. Compute the LCS of seq1[idx1:] and seq2[idx2:].
    2. If seq1[idx1] is equal with seq2(idx2) then this character belongs to the LCS of seq1[idx1:] and seq2[idx2:]. Further the LCS of seq1[idx1:]
    and seq2[idx2:] is 1 + the LCS of seq1[idx1+1:] and seq2[idx2+1:].
    3. If not, compute the LCS of seq1[idx1+1:] and seq2[idx2:] and the LCS of seq1[idx1:] and seq2[idx2+1:] the maximum of which is the solution.
    4. If either seq1[idx1:] or seq2[idx2:] is empty then their LCS is also empty.
    '''
    pass
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
