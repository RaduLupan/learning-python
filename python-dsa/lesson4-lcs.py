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

        if len(option1) >= len(option2):
            return option1
        else:
            return option2
    
# Test cases.
# General case 1.
test0 = {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': ['r', 'e', 'i', 'p', 'i', 't', 'o']
}

# Evaluate first test case.
print(lcs_recursive(**test0['input']))

print(lcs_recursive(**test0['input']) == test0['output'])
