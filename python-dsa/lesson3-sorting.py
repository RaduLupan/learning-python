'''
Merge Sort, Quick Sort and Divide-n-Conquer Algorithms in Python

Question 1: You're working on a new feature on Jovian called "Top Notebooks of the Week". 
Write a function to sort a list of notebooks in decreasing order of likes. Keep in mind that up to millions
of notebooks can be created every week, so your function needs to be as efficient as possible.

Question 2: Write a program to sort a list of numbers.
'''
def bubble_sort(nums):
    '''
    Algorithm:
    1. Iterate through the elements of the list starting from the left.
    2. Compare the current element with the one next to it, if they are out of order swap them.
    3. Increment the current position and repeat step 2 until you reach the second last element in the list.
    4. Repeat steps 1-3 until the list is sorted.
    '''

    # Optional make a copy of the list to avoid changing it in place.
    # nums = list(nums)

    # Repeat the process n-1 times.
    for _ in range(len(nums)-1):
        
        # Iterate until the second last element in the list.
        for i in range(len(nums)-1):
            
            # Compare the current element with the one next to it.
            if nums[i] > nums[i+1]:
                # Swap the elements that are out of order.
                nums[i], nums[i+1] = nums[i+1], nums[i]
    return nums

def insert_sort(nums):
    '''
    Description: Simple sorting technique where we keep the initial portion of the list sorted
    and insert the remaining elements one by one at the right position.
    Algorithm:
    1. Loop through the elements of the list starting from the left.
    2. Pop the current element from the list.
    3. Loop through the elements at the left of the current element until you reach the element that is <= than the current element.
    4. Insert the current element in the right position after the smaller element.
    5. Repeat steps 1-4 for all elements of the list. 
    '''

    # Make a copy of the initial list so that we don't sort in place.
    nums = list(nums)

    for i in range(len(nums)):

        # Extract the current element from the list.
        current = nums.pop(i)

        # Calculate position of the element at the left of current.
        j = i - 1

        # Loop through the elements at the left of cur until you find an element <= current.
        while j >= 0 and nums[j] > current:
            j -= 1

        # Insert current at the right position: after the element that's smaller and before the greater element.
        nums.insert(j+1, current)
    return nums
# A list of numbers in random order.
test0 = {
    'input': {
        'nums': [42, 10, 89, 76, 35, 68, 12, 90, 55]
    },
    'output': [10, 12, 35, 42, 55, 68, 76, 89, 90]
}

# A list of numbers in random order.
test1 = {
    'input': {
        'nums': [133, -540, 420, 0, 167, 358, 205, -200]
    },
    'output': [-540, -200, 0, 133, 167, 205, 358, 420]
}

# A list of numbers that's already sorted.
test2 = {
    'input': {
        'nums': [10, 20, 20, 40, 50, 60, 70, 80, 90]
    },
    'output': [10, 20, 20, 40, 50, 60, 70, 80, 90 ]
}

# A list that's sorted in descending order.
test3 = {
    'input': {
        'nums': [400, 325, 280, 145, 98, 75, 64, 50]
    },
    'output': [50, 64, 75, 98, 145, 280, 325, 400]
}

# A list containing repeating elements.
test4 = {
    'input': {
        'nums': [4, 2, 6, 3, 4, 6, 2, 1]
    },
    'output': [1, 2, 2, 3, 4, 4, 6, 6]
}

# An empty list.
test5 = {
    'input': {
        'nums': []
    },
    'output': []
}

# A list containing just one element.
test6 = {
    'input': {
        'nums': [1000]
    },
    'output': [1000]
}

# A list containing one element repeated many times.
test7 = {
    'input': {
        'nums': [500, 500, 500, 500, 500, 500, 500]
    },
    'output': [500, 500, 500, 500, 500, 500, 500]
}

# A really long list 10000 elements.
import random
in_list = list(range(10000))
out_list = list(range(10000))

random.shuffle(in_list)

test8 = {
    'input': {
        'nums': in_list
    },
    'output': out_list
}

# A very long list of 1 milion elements.
in_list_1_mil = list(range(1000000))
out_list_1_mil = list(range(1000000))

random.shuffle(in_list_1_mil)

test9 = {
    'input': {
        'nums': in_list_1_mil
    },
    'output': out_list_1_mil
}

# Add all test cases to the tests list EXCEPT for test9 that has 1 milion numbers.
tests = [test0, test1, test2, test3, test4, test5, test6, test7, test8]

#for i in range(len(tests)):
#    print(f"Test[{i}] -> Input: {tests[i]['input']['nums']}")
#    print(f"Test[{i}] -> Expected Output: {tests[i]['output']}")
#    print(f"Test[{i}] -> Actual Output: {bubble_sort(tests[i]['input']['nums'])}")
#    print(f"Test[{i}] -> Match: {bubble_sort(tests[i]['input']['nums']) == tests[i]['output']}")

import dsa

# Use dsa.evaluate_test_case function to evaluate a particular test.
# dsa.evaluate_test_case(function = bubble_sort, test=test0)

# Use dsa.evaluate_test_cases function to evaluate all test cases.
dsa.evaluate_test_cases(function = insert_sort, tests = tests)
