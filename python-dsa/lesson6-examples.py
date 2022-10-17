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
# sum(arr[i:j]) == target so j is 4 in the above example!
# output1 = 1, 4

# 2. Come up with some examples of inputs and outputs. Try to cover all edge cases.
# 2.1 General case: the subarray is in the middle of the arr list.
test0 = {
    'input': {
        'arr': [1, 4, 7, 5, 10, 13],
        'target': 16
    },
    'output': (1,4)
}

# 2.2 The subarray is at the end of arr list.
test1 = {
    'input': {
        'arr': [5, 10, 3, 15, 9, 20, 7],
        'target': 51
    },
    'output': (3, 7)
}

# 2.3 The subarray is at the beginning of arr list. Also the second subarray that meets the target (2, 4) is ignored.
test2 = {
    'input': {
        'arr': [5, 10, 3, 15, 9, 20, 7],
        'target': 18
    },
    'output': (0, 3)
}

# 2.4 The subarray has only 1 element.
test3 = {
    'input': {
        'arr': [5, 10, 3, 15, 9, 20, 7],
        'target': 10
    },
    'output': (1, 2)
}

# 2.5 The subarray has zero elements.
test4 = {
    'input': {
        'arr': [5, 10, 3, 15, 9, 20, 7],
        'target': 1000
    },
    'output': (None, None)
}

# 2.6 The array is empty.
test5 = {
    'input': {
        'arr': [],
        'target': 10
    },
    'output': (None, None)
}

tests = [test0, test1, test2, test3, test4, test5]

# 3. Come up with a correct solution for the problem. State it in plain English.
# 4. Implement the solution.
def find_subarray1(arr, target):
    '''
    Brute force - Time complexity is O(n^3)
    Algorithm:
    1. Start with two indices i, j that track the start and end for the subarray.
    2. For each idx1 in range(0, n) evaluate all subarrays with idx2 going from idx1+1 to n+1.
    3. If sum(arr[idx1:idx2]) == target return idx1, idx2-1.
    4. Else return None, None.
    '''

    n = len(arr)

    for i in range(n):
        for j in range(i, n+1):
            if sum(arr[i:j]) == target:
                return i, j

    return None, None

import dsa

# 4. Test the solution using example inputs.
# Evaluate one test case.
dsa.evaluate_test_case(find_subarray1, test0)

# Evaluate all test cases.
dsa.evaluate_test_cases(find_subarray1, tests)

# 5. Analyze algorithm's complexity and identify inefficiencies if any.
# Time complexity: O(n^3) where n is the lenght of the array.

def find_subarray2(arr, target):
    '''
    Improved brute force version of find_subarray1() which overcomes the inefficiency of adding up the elements repeatedly.
    Time complexity is O(n^2).
    '''

    n = len(arr)
    
    # Variable to keep the current sum of the subarray elements.
    

    for i in range(n):

        s = 0

        for j in range(i+1, n+1):
        
            sub_arr = arr[i:j]
            
            s += arr[j-1]

            if s == target:
                return i, j
            # No point in going further if the target is exceeded.
            elif s > target:
                break
            print(f"i, j: {i}, {j}")
            print(f"arr[i:j]: {sub_arr}, sum: {s}")
            
            
    return None, None

def find_subarray3(arr, target):
    '''
    Further improvment upon find_subarray2() which uses a greedy aproach.
    '''
dsa.evaluate_test_case(find_subarray2, test1)
dsa.evaluate_test_cases(find_subarray2, tests)
