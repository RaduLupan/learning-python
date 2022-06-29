'''
----------------------------------------------------------------------------------------
This module contains functions aasses to use for Data Structure and Algorithms problems.
----------------------------------------------------------------------------------------
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

def evaluate_test_case(function, test):
    '''
    Description: Compares actual output of a function with test case.
    Parameters:
    - function: the name of the function whose output is evaluated against test output.
    - test: test case in the form of a dictionary where test['input'] must match the arguments of function and test['output'] containes the tested output.
    TODO: Add measure of execution time for the function tested.
    '''    
    print(f"Input: {test['input']}")

    print (f"Expected Output: {test['output']}")
    
    result = function(**test['input'])

    print(f"Actual Output: {result}")
    
    if result == test['output']:
        print("Test Result: PASSED\n")
    else:
        print ("Test Result: FAILED\n")


def evaluate_test_cases(function, tests):
    '''
    Description: Uses evaluate_test_case to compare actual output of a function with a series of test cases.
    Parameters:
    - function: the name of the function whose output is evaluated against test output.
    - tests: a list of test dictionaries where test['input'] must match the arguments of function and test['output'] containes the tested output.
    '''
    pass_count = 0
    fail_count = 0

    for test in tests:
        print(f"TEST#: {tests.index(test)}")
        
        print(f"Input: {test['input']}")

        print (f"Expected Output: {test['output']}")
    
        result = function(**test['input'])

        print(f"Actual Output: {result}")   
        
        if result == test['output']:
            print("Test Result: PASSED\n")
            pass_count += 1
        else:
            print ("Test Result: FAILED\n")
            fail_count += 1
    
    print(f"SUMMARY\n TOTAL: {len(tests)}, PASSED: {pass_count}, FAILED: {fail_count}")

class TreeNode():
    def __init__(self, key):
        self.left, self.key, self.right = None, key, None
