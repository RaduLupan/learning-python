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
    '''
    Description: Removes elements that are None in a list or tuple.
    '''
    return [x for x in nums if x is not None]

def is_bst(node):
    '''
    Description: Checks whether a binary tree is a BST or not while also returning the minimum and maximum keys in the binary tree.
    '''

    if node is None:
        return True, None, None
    
    is_bst_left, min_left, max_left = is_bst(node.left)
    is_bst_right, min_right, max_right = is_bst(node.right)

    is_bst_node = is_bst_left and is_bst_right and (max_left is None or max_left < node.key) and (min_right is None or min_right > node.key)
    
    min_key = min(remove_none([min_left, node.key, min_right]))
    max_key = max(remove_none([max_left, node.key, max_right]))

    # print(node.key, min_key, max_key, is_bst_node)

    return is_bst_node, min_key, max_key 
import dsa

tree1 = dsa.TreeNode.parse_tuple((((None, 25, (42, 36, 48)), 10, None), 7, ((None, 23, 35), 18, ((43, 39, None), 29, None))))
print(tree1)

is_bst_tree = is_bst(tree1)
print(is_bst_tree)

bobg=dsa.User('bobg', 'Bob Green', 'bobg@example.com')
aliceb=dsa.User('aliceb', 'Alice Brown', 'aliceb@example.com')
joeb=dsa.User('joeb', 'Joe Blue', 'joeb@example.com')
danb=dsa.User('danb', 'Dan Black', 'danb@example.com')
pamy=dsa.User('pamy', 'Pam Yellow', 'pamy@example.com')
georgeo=dsa.User('georgeo', 'George Orange', 'georgeo@example.com')
victorp=dsa.User('victorp', 'Victor Pink', 'victorp@example.com')

tree2 = dsa.BSTNode(bobg.username, bobg)
print(tree2.key, tree2.value)

# Create tree2 example - Level 1
tree2.left = dsa.BSTNode(aliceb.username, aliceb)
tree2.right = dsa.BSTNode(pamy.username, pamy)

# Create tree2 example - Level 2 -> Left
tree2.left.left = dsa.BSTNode(joeb.username, joeb)
tree2.left.right = dsa.BSTNode(danb.username, danb)

# Create tree2 example - Level 2 -> Right
tree2.right.left = dsa.BSTNode(georgeo.username, georgeo)
tree2.right.right = dsa.BSTNode(victorp.username, victorp)

# Check if tree2 is a BST
is_bst_tree2 = is_bst(tree2)
print(is_bst_tree2)

# Add user elenab to replace aliceb and create a BST
elenab=dsa.User('elenab', 'Elena Brown', 'elenab@example.com')

# Create BST example tree3 - Level 0
tree3 = dsa.BSTNode(georgeo.username, georgeo)

# Create BST example tree3 - Level 1
tree3.left = dsa.BSTNode(danb.username, danb)
tree3.right = dsa.BSTNode(pamy.username, pamy)

# Create BST example tree3 - Level 2 -> Left
tree3.left.left = dsa.BSTNode(bobg.username, bobg)
tree3.left.right = dsa.BSTNode(elenab.username, elenab)

# Create BST example tree3 - Level 2 -> Right
tree3.right.left = dsa.BSTNode(joeb.username, joeb)
tree3.right.right = dsa.BSTNode(victorp.username, victorp)

# Check if tree3 is a BST
is_bst_tree3 = is_bst(tree3)
print(is_bst_tree3)
