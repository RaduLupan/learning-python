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

def merge(nums1, nums2):
    '''
    Description: Performs merge operation of two sorted lists nums1 and nums2.
    '''
    # Create the target list of the right size to accomodate the two sublists.
    nums = [None] * (len(nums1) + len(nums2))

    i = 0

    # Repeat: compare the elements on position 0 on the two lists, and add the smaller one to the target list.
    while True:

        # If nums1 list was exhausted, simply eliminate the None elements from target list and add the remainder of nums2.
        if len(nums1) == 0 and len(nums2) > 0:
            nums = [x for x in nums if x is not None]
            nums += nums2
            break
        
        # If nums2 list was exhausted, simply eliminate the None elements from target list and add the remainder of nums1.
        if len(nums2) == 0 and len(nums1) > 0:
            nums = [x for x in nums if x is not None]
            nums += nums1
            break

        # Pop the smaller element from the first position and add it to the target list.
        if nums1[0] < nums2[0]:
            nums[i] = nums1.pop(0)
        else:
            nums[i] = nums2.pop(0)
        i += 1

    return nums 

def merge2(nums1, nums2):
    '''
    Description: Another implementation of merge function that combines two sorted lists. 
    '''

    # List to store the result.
    merged = []

    # Iteration indices.
    i, j = 0, 0

    # Loop over the two lists.
    while i < len(nums1) and j < len(nums2):

        # Include the smaller element in the result and move to the next element.
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Get the remaining parts.
    nums1_tail = nums1[i:]
    nums2_tail = nums2[j:]

    # Return the final merged list.
    return merged + nums1_tail + nums2_tail
def merge_sort(nums):
    '''
    Description Performs sorting of a list by applying a Divide and Conquer strategy called Merge Sort.
    Algorithm:
    1. If the list is empty or has only one element return the list as it is sorted.
    2. If not, devide the list in two roughly equal sublists.
    3. Recursively sort the two sublists using merge sort. Return the two sorted sublists.
    4. Combine the two sorted sublists into one sorted list by merging the two sublists.
    '''

    # If nums has one element or it's empty return it as it is sorted.
    if len(nums) <= 1:
        return nums
    
     # Calculate the mid index.
    mid = len(nums) // 2

     # Divide the nums list in two sublists.
    left = nums[:mid]
    right = nums[mid:]

    # Sort the left and right sublists recursively with merge_sort.
    sorted_left, sorted_right = merge_sort(left), merge_sort(right)

    # Merge the two sorted lists.
    sorted = merge2(sorted_left, sorted_right)

    return sorted
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

# A very long list of 100k elements.
in_list_100k = list(range(100000))
out_list_100k = list(range(100000))

random.shuffle(in_list_100k)

test9 = {
    'input': {
        'nums': in_list_100k
    },
    'output': out_list_100k
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
dsa.evaluate_test_case(function = merge_sort, test=test9)

# Use dsa.evaluate_test_cases function to evaluate all test cases.
#dsa.evaluate_test_cases(function = merge_sort, tests = tests)

# nums1=[1,3,5,7,9]
# nums2=[2,4,6,8,10]
# print(f"nums1={nums1}")
# print(f"nums2={nums2}")

# print(f"Merged lists: {merge(nums1, nums2)}")


