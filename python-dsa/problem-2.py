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
    def condition(mid):
        if array[mid] == target:
            if mid > 0 and array[mid-1] == target:
                return 'left'
            else:
                return 'found'
        elif array[mid] < target:
            return 'right'
        elif array[mid] > target:
            return 'left'
    return binary_search(0, len(array)-1, condition)


def locate_end_position(array, target):
    def condition(mid):
        if array[mid] == target:
            if mid < len(array)-1 and array[mid+1] == target:
                return 'right'
            else:
                return 'found'
        elif array[mid] < target:
            return 'right'
        elif array[mid] > target:
            return 'left'
    return binary_search(0, len(array)-1, condition)

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

def evaluate_test_case(function, test):
    
    print(f"Input: {test['input']}")

    print (f"Expected Output: {test['output']}")
    
    result = function(**test['input'])

    print(f"Actual Output: {result}")
    
    if result == test['output']:
        print("Test Result: PASS\n")
    else:
        print ("Test Result: FAIL\n")

def evaluate_test_cases(function, tests):
    for test in tests:
        print(f"TEST#: {tests.index(test)}")
        evaluate_test_case(function=function, test=test)        

tests = []

test = {
    'input': {
        'array': [1, 3, 3, 3, 7, 10, 15],
        'target': 1
    },
    'output': [0, 0]
}

tests.append(test)

# target is the last element in array.
tests.append({
    'input': {
        'array': [1, 5, 8, 10, 10, 13],
        'target': 13
    },
    'output': [5, 5]
})

# target is repeated at the end of the array.
tests.append({
    'input': {
        'array': [-100, 0, 5, 8, 10, 10, 13, 13, 13],
        'target': 13
    },
    'output': [6, 8]
})

# target is the first unique element in the array.
tests.append({
    'input': {
        'array': [2, 5, 8, 10, 10, 13, 13, 13],
        'target': 2
    },
    'output': [0, 0]
})

# target is a repeating element at the beginning of the array.
tests.append({
    'input': {
        'array': [2, 2, 2, 2, 2, 2, 5, 8, 10, 10, 13, 13, 13],
        'target': 2
    },
    'output': [0, 5]
})

# array is an empty list.
tests.append({
    'input': {
        'array': [],
        'target': 100
    },
    'output': [-1, -1]
})

# target is not found in the array.
tests.append({
    'input': {
        'array': [1, 7, 11, 15, 15, 25, 30, 30, 30],
        'target': 100
    },
    'output': [-1, -1]
})

#evaluate_test_case(function=locate_start_end_position, test=test)

evaluate_test_cases(function=locate_start_end_position, tests=tests)
