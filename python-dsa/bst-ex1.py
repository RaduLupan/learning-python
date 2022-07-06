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

def bst_insert(bst, node):
    '''
    Description: Inserts a new node into a Binary Search Tree (BST).
    Parameters:
    - bst: the root node of the BST to insert to
    - node: the node to be inserted, instance of the User class.
    Algorithm:
    1. Starting from the root node, compare the key to be inserted with the current node's key.
    2. If the key is smaller, recursively insert it in the left subtree (if it exists) or attach it as the left child if no left subtree exists.
    3. If the key is greater, recursively insert it in the right subtree (if it exists) or attach it as the right child if no right subtree exists.
    '''
    key = node.username

    if key < bst.key:
        if bst.left is None:
            bst.left = dsa.BSTNode(node.username, node)
            print(f"Inserted node with key={node.key} as the left child of {bst}")
        else:
            bst_insert(bst.left, node)
    elif key > bst.key:
        if bst.right is None:
            bst.right = dsa.BSTNode(node.username, node)
            print(f"Inserted node with key={key} as the right child of {bst.key}")
        else:
            bst_insert(bst.right, node)

def display_keys(node, space='\t', level=0):
    '''
    Description: Helper function that prints all keys of a tree using tab indentation to create a tree-like visual structure.
    '''    

    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)    

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

# Display BST before insertion.
display_keys(node=tree3)

# Create a node to be inserted in BST tree3.
frankv = dsa.User('frankv', 'Frank Violet', 'frankv@example.com')

# Insert node in BST.
bst_insert(tree3, frankv)

# Check if tree3 is still a BST after insertion.
is_bst_tree3 = is_bst(tree3)
print(is_bst_tree3)

# Display BST after insertion.
display_keys(node=tree3)
