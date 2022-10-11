'''
The following systematic strategy for solving problems will be used for the two problems below.

The method
1. State the problem clearly. Identify the input & output formats.
2. Come up with some examples of inputs and outputs. Try to cover all edge cases.
3. Come up with a crrect solution for the problem. State it in plain English.
4. Implement the solution and test it using the example inputs. Fix bugs if any.
5. Analyze the algorithm's complexity and identify inefficiencies if any.
6. Apply the right technique to overcome the inefficiencies. Repeat steps 3-6. 

Problem1: You are given an array of numbers (non-negative). Find a continuous subarray of the list which adds up to a given sum.

'''


# 1. State the problem clearly. Identify the input & output formats.

# Input: arr - a list of positive numbers, target - a number representing the target sum.
# Example:
# arr = [1, 4, 7, 5, 10, 13]
# target = 16

# Output: (i, j) - a tuple representing the start and end indices for the subarray in arr whose elements add up to target.
# output1 = 1, 3 

# 2. Come up with some examples of inputs and outputs. Try to cover all edge cases.
# 2.1 General case: the subarray is in the middle of the arr list.
test0 = {
    'input': {
        'arr': [1, 4, 7, 5, 10, 13],
        'target': 16
    },
    'output': (1,3)
}

# 2.2 The subarray is at the end of arr list.
test1 = {
    'input': {
        'arr': [5, 10, 3, 15, 9, 20, 7],
        'target': 51
    },
    'output': (3, 6)
}

# 2.3 The subarray is at the beginning of arr list.
test2 = {
    'input': {
        'arr': [5, 10, 3, 15, 9, 20, 7],
        'target': 18
    },
    'output': (0, 2)
}

# 2.4 The subarray has only 1 element.
test3 = {
    'input': {
        'arr': [5, 10, 3, 15, 9, 20, 7],
        'target': 10
    },
    'output': (1, 1)
}

# The subarray has zero elements.
test4 = {
    'input': {
        'arr': [5, 10, 3, 15, 9, 20, 7],
        'target': 1000
    },
    'output': (None, None)
}

tests = [test0, test1, test2, test3, test4]

# 3. Come up with a correct solution for the problem. State it in plain English.
# 4. Implement the solution.
def find_subarray1(arr, target):
    '''
    Algorithm:
    1. Start with two indices idx1, idx2 that track the start and end for the subarray.
    2. For each idx1 in range(0, n) evaluate all subarrays with idx2 going from idx1+1 to n+1.
    3. If sum(arr[idx1:idx2]) == target return idx1, idx2-1.
    4. Else return None, None.
    '''

    # idx1, idx2 = 0, 0
    n = len(arr)

    for idx1 in range (0, n):
        for idx2 in range(idx1+1, n+1):
            sub_arr = arr[idx1:idx2]
            # print(f"Subarray: {sub_arr}, sum: {sum(sub_arr)}")
            if sum(sub_arr) == target:
                return idx1, idx2-1

    return None, None

import dsa

# 4. Test the solution using example inputs.
# Evaluate one test case.
dsa.evaluate_test_case(find_subarray1, test0)

# Evaluate all test cases.
# dsa.evaluate_test_cases(find_subarray1, tests)

# 5. Analyze algorithm's complexity and identify inefficiencies if any.
# Time complexity: O(n^3) where n is the lenght of the array.

def find_subarray2(arr, target):
    '''
    Improved version of find_subarray1() which overcomes the inefficiency of adding up the elements repeatedly.
    '''

    n = len(arr)
    
    for i in range (0, n):
        
        # Variable to keep the current sum of the subarray elements.
        s = arr[i]
        
        for j in range(i+1, n+1):
            sub_arr = arr[i:j]
            
            if len(sub_arr) > 1:
                s += arr[j-1]
            
            print(f"Subarray: {sub_arr}, sum: {s}")
            
            if s == target:
                return i, j-1

    return None, None

dsa.evaluate_test_case(find_subarray2, test0)
