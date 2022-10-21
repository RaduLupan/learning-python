'''
The following systematic strategy for solving problems will be used for the problem below.

The method
1. State the problem clearly. Identify the input & output formats.
2. Come up with some examples of inputs and outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem. State it in plain English.
4. Implement the solution and test it using the example inputs. Fix bugs if any.
5. Analyze the algorithm's complexity and identify inefficiencies if any.
6. Apply the right technique to overcome the inefficiencies. Repeat steps 3-6. 

Problem: Reverse a Linked List in Groups of Given Size
Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should be considered as a group and must be reversed
(See Example 2 for clarification).

Example 1:
Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output: 4 2 2 1 8 7 6 5 
Explanation: 
The first 4 elements 1,2,2,4 are reversed first 
and then the next 4 elements 5,6,7,8. Hence, the 
resultant linked list is 4->2->2->1->8->7->6->5.

Example 2:
Input:
LinkedList: 1->2->3->4->5
K = 3
Output: 3 2 1 5 4 
Explanation: 
The first 3 elements are 1,2,3 are reversed 
first and then elements 4,5 are reversed.Hence, 
the resultant linked list is 3->2->1->5->4.

Reference:
https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1?page=3&company[]=Amazon&sortBy=submissions
'''
# 1. State the problem clearly. Identify the input & output formats.
# We are given a list of size N. We need to write a function that reverses every k elements in the list.
# If the number of elements is not a multiple of k then the left-out elements, in the end, should be considered as a group and must be reversed.

# Input: 
#  - arr: a list of integers that needs to be reversed in groups.
#  - k:   an integer representing the number of elements in a group.
# Output:
#  - rev: a list obtained by reversing every k elements in arr.

def reverse_list(arr, k):
    pass

# 2. Come up with some examples of inputs and outputs. Try to cover all edge cases.
# 2.1 General case when N is multiple of k.
test0 = {
    'input': {
        'arr': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'k': 4
    },
    'output': [4, 3, 2, 1, 8, 7, 6, 5, 12, 11, 10, 9]
}

# 2.2 General case when N is not multiple of k.
test1 = {
    'input': {
        'arr': [10, 15, 12, 40, 37, 28, 35, 49, 55, 17, 23],
        'k': 3
    },
    'output': [12, 15, 10, 28, 37, 40, 55, 49, 35, 23, 17]
}

# 2.3 k=N The whole arr list gets reversed.
test2 = {
    'input': {
        'arr': 'reverse me',
        'k': 10
    },
    'output': ['e', 'm', '', 'e', 's', 'r', 'e', 'v', 'e', 'r']
}

# 2.4 k=1 The original list is returned, no elements are reversed.
test3 = {
    'input': {
        'arr': [10, 20, 30, 40, 50, 60],
        'k': 1
    },
    'output': [10, 20, 30, 40, 50, 60]
}

tests = [test0, test1, test2, test3]
