'''
Problem: Searching in a rotated list.
You are given list of numbers, obtained by rotating a sorted list an unknown number of times. 
You are also given a target number. Write a function to find the position of the target number within the rotated list. 
You can assume that all the numbers in the list are unique.
Example: In the rotated sorted list [5, 6, 9, 0, 2, 3, 4], the target number 2 occurs at position 5.

HINT: One way to solve this problem is to identify two sorted subarrays within the given array (using the count_rotations_binary 
function defined in assignment-1.py), then perform a binary search on each subarray to determine the position of the target element.
'''
def locate_number_linear(nums, target):
    '''
    Description: Uses linear search algorithm to determine the position of a target number in a rotated sorted list of numbers.
    Parameters:
    - nums: the rotated list of numbers.
    - target: the target number whose position in nums is needed.
    Linear Search (aka Brute Force) Algorithm: 
    1. Create variable position = 0 to loop through all indexes of nums list.
    2. Compare nums[position] with target and if equals return position as the answer.
    3. Increment position and repeat steps 2-3 until the end of nums is reached.
    4. If target is not found in nums return -1.
    '''
    position = 0

    while position <= len(nums)-1:
        if nums[position] == target:
            return position
        position += 1
    
    return -1

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
    
def binary_search(lo, hi, condition):

    while lo <= hi:
        mid = (lo + hi)// 2
        
        print(f"Binary Search -> Lo: {lo}, Hi: {hi}, Mid: {mid}")

        result = condition(mid, lo, hi)

        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid
        elif result == 'right':
            lo = mid+1
    return -1

def locate_number_binary(nums, target):
    '''
    Description: Uses binary search algorithm to determine the position of a target number in a rotated sorted list of numbers.
    Parameters:
    - nums: the rotated list of numbers.
    - target: the target number whose position in nums is needed.
    '''
    def condition (mid, lo, hi):
    
        print(f"Condition -> Lo: {lo}, Hi: {hi}, Mid: {mid}")
    
        if mid >=0 and nums[mid] == target:
            return 'found'
        # Handle sorted lists.
        elif nums[mid] < target and nums[mid] < nums[hi] and nums[mid] >= nums[lo]:
            return 'right'
        elif nums[mid] > target and nums[mid] < nums[hi] and nums[mid] >= nums[lo]:
            return 'left'
        # Handle roated lists.
        elif nums[mid] < target and nums[mid] < nums[hi] and nums[mid] < nums[lo]:
            return 'left'
        elif nums[mid] < target and nums[mid] > nums[hi] and nums[mid] > nums[lo]:
            return 'right'
        elif nums[mid] > target and nums[mid] > nums[hi] and nums[mid] >= nums[lo]:
            return 'left'
    return binary_search(0, len(nums)-1, condition)
import dsa

# The structure of a test. The list in test['input']['nums'] was obtained by rotating [12, 45, 77, 81, 92, 101, 235, 400, 505] list 4 times.
# The target=400 is at position 2 in the nums list.
test={
    'input': {
        'nums': [101, 235, 400, 505, 12, 45, 77, 81, 92],
        'target': 400
    },
    'output': 2
}

# Create more test cases.
test0=test

# target is the first number in a list of size 8 rotated 5 times.
test1 = {
    'input': {
        'nums': [12, 15, 18, 21, 28, 4, 9, 10],
        'target': 12
    },
    'output': 0
}

# target is close to the end of a list that wasn't rotated at all (sorted list).
test2 = {
    'input': {
        'nums': [1, 10, 20, 30, 40, 50, 60, 100, 1400],
        'target': 60
    },
    'output': 6
}

# target is the last element in a list that was rotated just once.
test3 = {
    'input': {
        'nums': [47, 20, 28, 35, 45],
        'target': 45
    },
    'output': 4
}

# target is the first element in a list that was rotated n-1 times, where n is the size of the list.
test4 = {
    'input': {
        'nums': [-20, -15, 0, 19, 35, -30],
        'target': -20
    },
    'output': 0
}

# target is in the middle of a sorted list.
test5 = {
    'input': {
        'nums': [1, 2, 3, 4, 5, 6, 7],
        'target': 4
    },
    'output': 3
}

# target is the last element in a sorted list.
test6 = {
    'input': {
        'nums': [10, 20, 30, 40, 50, 60, 70],
        'target': 70
    },
    'output': 6
}

# target is the first element in a sorted list.
test7 = {
    'input': {
        'nums': [10, 20, 30, 40, 50, 60, 70],
        'target': 10
    },
    'output': 0
}

# searching in an empty list.
test8 = {
    'input': {
        'nums': [],
        'target': 5
    },
    'output': -1
}

# target is not found in a list of size 1.
test9 = {
    'input': {
        'nums': [100],
        'target': 500
    },
    'output': -1
}

# Load all test cases into tests list.
tests=[test0, test1, test2, test3, test4, test5, test6, test7, test8, test9]

# Evaluate locate_number_linear against the first test case.
# dsa.evaluate_test_case(function=locate_number_linear, test=test0)

# Evaluate locate_number_linear against all test cases.
# dsa.evaluate_test_cases(function=locate_number_linear, tests=tests)

# Evaluate locate_number_binary against the first test case.
dsa.evaluate_test_case(function=locate_number_binary, test=test3)

# Evaluate locate_number_binary against all test cases.
# dsa.evaluate_test_cases(function=locate_number_binary, tests=tests)
