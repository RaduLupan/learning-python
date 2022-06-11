'''
---------------------------------------------------------------------------------
This module contains functions to use for Data Structure and Algorithms problems.
---------------------------------------------------------------------------------
'''

def binary_search(lo,hi,condition):
    '''
    Description: Generic algorithm for binary search. The condition argument is a function that determines whether the answer lies before, after or at a given position.
    '''
    while lo <= hi:
        mid = (lo + hi) // 2
        
        result = condition(mid)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        elif result == 'right':
            lo = mid+1
    return -1
