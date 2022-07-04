'''
A Binary Search Tree (BST) is a binary tree that satisfies the following conditions:
1. The left subtree of any node only contains nodes with keys less than the node's key.
2. The right subtree of any node only contains nodes with keys greater than the node's key.

It follows that any subtree of a binary search tree must also be a BST.

Question 1: Write a function that checks whether a binary tree is a BST.
Question 2: Write a function that finds the maximum key in a binary tree.
Question 3: Write a function that finds the minimum key in a binary tree.
'''
def remove_none(nums):
    return [x for x in nums if x is not None]

import dsa

tree = dsa.TreeNode.parse_tuple((((None, 25, (42, 36, 48)), 10, None), 7, ((None, 23, 35), 18, ((43, 39, None), 29, None))))
print(tree)

