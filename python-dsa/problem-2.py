'''
Find First and Last Position of Element in Sorted Array:
--------------------------------------------------------
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Source:
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
def locate_start_position(array, target):
    pass

def locate_end_position(array, target):
    pass 

def locate_start_end_position(array, target):

    start = locate_start_position(array, target)
    end = locate_end_position(array, target)

    return [start, end]

def binary_search(lo,hi,condition):
    '''
    Description: Generic algorithm for binary search. The condition argument is a function that determines whether the answer lies before, after or at a given position.
    Use in conjunction with locate_card function.
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


tests = []

test = {
    'input': {
        'array': [1, 3, 3, 3, 7, 10, 15],
        'target': 1
    },
    'output': [0, 0]
}

tests.append({
    'input'
})
