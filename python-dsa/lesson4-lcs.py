'''
Question: Write a modified version of the lcs() function that returns the longest common subsequence (LCS) of two sequences rather than the length of it.

Example:
seq1 = 'serendiptous'
seq2 = 'precipitation'

lcs = ['r', 'e', 'i', 'p', 'i', 't', 'o']
'''

def lcs_recursive(seq1, seq2, idx1 = 0, idx2 = 0):
    '''
    Description: Computes the longest common subsequence (LCS) of two sequences using the recursive method.
    '''

    lcs=[]

    # Check if either sequence is exhausted.
    if idx1 == len(seq1) or idx2 == len(seq2):
        return []

    # If the current elements in both sequences are equal, append the element to the result and compute recursively LCS for seq1[idx1+1:] and seq2[idx2+1:]. 
    elif seq1[idx1] == seq2[idx2]:
        
        lcs.append(seq1[idx1])
        return  lcs + lcs_recursive(seq1, seq2, idx1+1, idx2+1)
    
    # Skip the current element from each sequence and compute LCS for the two subproblems and return the LCS with the greater length.
    else:
        option1 = lcs_recursive(seq1, seq2, idx1, idx2+1)
        option2 = lcs_recursive(seq1, seq2, idx1+1, idx2)

        # The caveat here is that when there are multiple common susequences with the same length, only the first one is returned.
        # See test case test7.
        if len(option1) >= len(option2):
            return option1
        else:
            return option2
    
# Test cases.
# General case - string.
test0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': ['r','e','i','p','i','t','o']
}

# 2. General case - list.
test1 = {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': [1,5,6,2,3]
}

# 3. Another general case - string.
test2 = {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': ['o','n','e']
}

# 4. No common subsequence.
test3 = {
    'input': {
        'seq1': 'qwerty',
        'seq2': 'asdfgh'
    },
    'output': []
}

# 5. One is a subsequence of the other.
test4 = {'input': {'seq1': 'dense', 'seq2': 'condensed'}, 'output': ['d','e','n','s','e']}

# 6. One sequence is empty.
test5 = {'input': {'seq1': '', 'seq2': 'abcdef'}, 'output': []}

# 7. Both sequences are empty.
test6 = {'input': {'seq1': '', 'seq2': ''}, 'output': []}

# 8. Multiple sequences with same length.
test7 = {'input': {'seq1': 'abcdef', 'seq2': 'badcfe'}, 'output': ['a', 'c', 'e']}

tests = [test0, test1, test2, test3, test4, test5, test6, test7]

# Evaluate one test case.
import dsa
dsa.evaluate_test_case(lcs_recursive, test0)

# Evaluate all test cases.
dsa.evaluate_test_cases(lcs_recursive, tests)

