'''
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
Your function should have the worst-case complexity of O(log N), where N is the length of the list. 
You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.
We define "rotating a list" as removing the last element of the list and adding it before the first element. 
E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

Optional Questions:
-------------------
1. Implement the solution using the generic binary_search function defined in the dsa module.
2. Rewrite the solution to handle repeating numbers in the nums list.
3. Searching in a rotated list.
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
You are also given a target number. Write a function to find the position of the target number within the rotated list. 
You can assume that all the numbers in the list are unique.
Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], the target number 2 occurs at position 5.
'''
def count_rotations_linear(nums):
    '''
    Description: Uses linear search algorithm to determine the minimum number of rotations applied to a sorted list of numbers to obtain the given list.
    The number of rotations is given by the index of the smallest number in the nums list. For example if the smallest number in the list
    is at position k (counting from zero) then the list was rotated k times.
    Parameters:
    - nums: the rotated list of numbers.
    Linear Search (aka Brute Force) Algorithm: 
    1. Create variable position = 0 to loop through all indexes of nums list.
    2. Compare nums[position] with its predecessor nums[position-1] and if it is smaller return position as the answer.
    3. If no number in nums list is smaller than its predecessor return 0 as nums is sorted in ascending order and therefore rotated zero times.
    '''
    position = 0

    while position <= len(nums)-1:
        if position > 0 and nums[position] < nums[position-1]:
            return position
        position += 1
    
    return 0 

def count_rotations_binary(nums):
    '''
    Description: Uses binary search algorithm to determine the minimum number of rotations applied to a sorted list of numbers to obtain the given list.
    Parameters:
    - nums: the rotated list of numbers.
    Binar Search Algorithm:
    1. Set the left and right indexes to 0 and len(nums)-1 respectively.
    2. Calculate the mid position of the search interval.
    3. Compare the number at the mid position with the number at the right end of the interval. 
    4. If the number at the mid position is smaller than the number at the right end of the interval, the answer lies in the left half.
    5. If the number at the mid position is greater than the number at the right end of the interval, the answer lies in the right half.
    6. If the number at the mid position equals the number at the right end of the interval, return the mid position as the answer.
    7. Repeat steps 2-6 until left and right indexes are equal.
    8. If no answer return 0 as the nums list is sorted in ascending order and therefore was rotated zero times.
    '''
    lo = 0
    hi = len(nums)-1
    
    while lo <= hi:
        mid = (lo+hi)//2
        mid_number = nums[mid]
        
        # Uncomment the next line for logging the values and fixing errors.
        # print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid > 0 and mid_number == nums[hi]:
            # The middle position is the answer.
            return mid
        
        elif mid_number < nums[hi]:
            # Answer lies in the left half.
            hi = mid
        
        else:
            # Answer lies in the right half.
            lo = mid + 1
    
    return 0

import dsa

# The structure of a test. The list in test['input']['nums'] was obtained by rotating [12, 45, 77, 81, 92, 101, 235, 400, 505] list 4 times.
test={
    'input': {
        'nums': [101, 235, 400, 505, 12, 45, 77, 81, 92]
    },
    'output': 4
}

# Create more test cases.

# A list of size 9 rotated 4 times.
test0=test

# A list of size 8 rotated 5 times.
test1 = {
    'input': {
        'nums': [12, 15, 18, 21, 28, 4, 9, 10]
    },
    'output': 5
}

# A list that wasn't rotated at all.
test2 = {
    'input': {
        'nums': [1, 10, 100, 1400]
    },
    'output': 0
}

# A list that was rotated just once.
test3 = {
    'input': {
        'nums': [47, 20, 28, 35, 45]
    },
    'output': 1
}

# A list that was rotated n-1 times, where n is the size of the list.
test4 = {
    'input': {
        'nums': [-20, -15, 0, 19, 35, -30]
    },
    'output': 5
}

# A list that was rotated n times, where n is the size of the list. 
# A list rotated n times equals to the original sorted list which is rotated 0 times.
# Since the function must return the minimum number of rotations the output for this test case is 0.
test5 = {
    'input': {
        'nums': [1, 2, 3, 4, 5, 6, 7]
    },
    'output': 0
}

# An empty list. An empty list is always sorted so needs to be rotated zero times.
test6 = {
    'input': {
        'nums': []
    },
    'output': 0
}

# A list containing just one element.
test7 = {
    'input': {
        'nums': [100]
    },
    'output': 0
}

# Load all test cases into tests list.
tests=[test0, test1, test2, test3, test4, test5, test6, test7]

# Evaluate count_rotations_linear against the first test case.
# dsa.evaluate_test_case(function=count_rotations_linear, test=test0)

# Evaluate count_rotations_linear against all test cases.
# dsa.evaluate_test_cases(function=count_rotations_linear, tests=tests)

# Evaluate count_rotations_binary against the first test case.
dsa.evaluate_test_case(function=count_rotations_binary, test=test0)

# Evaluate count_rotations_binary against all test cases.
dsa.evaluate_test_cases(function=count_rotations_binary, tests=tests)
