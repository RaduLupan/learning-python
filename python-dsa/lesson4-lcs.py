'''
Question: Write a modified version of the lcs() function that returns the longest common subsequence (LCS) of two sequences rather than the length of it.

Example:
seq1 = 'serendiptous'
seq2 = 'precipitation'

lcs = 'reipito'
'''

def lcs(seq1, seq2):
    pass


# Test cases.
# General case 1.
test0 = {
    'input': {
        'seq1': 'serendiptous',
        'seq2': 'precipitation'
    },
    'output': 'reipito'
}

# Evaluate first test case.
assert lcs(**test0['input']) == test0['output']
