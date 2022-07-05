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

    def height(self):
        if self is None:
            return 0
        return max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return TreeNode.traverse_in_order(self.left) + [self.key] + TreeNode.traverse_in_order(self.right)
    
    def traverse_pre_order(self):
        if self is None:
            return []
        return [self.key] + TreeNode.traverse_pre_order(self.left) + TreeNode.traverse_pre_order(self.right)

    def traverse_post_order(self):
        if self is None:
            return []
        return TreeNode.traverse_post_order(self.left) + TreeNode.traverse_post_order(self.right) + [self.key]

    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        display_keys(self.left,space, level+1)   

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod    
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

class BSTNode:
    def __init__ (self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
