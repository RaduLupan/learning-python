'''
Problem: We need to create a data structure which can store 100 million records and perform insertion, search, update and list operations efficiently.
Input: User profiles which contain username, name and email for a user.
------------------------------------------------------------------------------------------------------------------------------------------------------
Question: Implement a binary tree using Python, and show its usage with some examples.
'''
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f"User(username={self.username}, name={self.name}, email={self.email})"

class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        
        target = self.find(user.username)

        i = 0

        while i < len(self.users):
            # Find the index for the first username in users greater than the username.
            if self.users[i].username > user.username:
                break
            i += 1
        
        # Only insert if username not found.
        if target == -1:
            self.users.insert(i, user)
        else:
            print(f"A user with username={user.username} already exists. You may want to try the update method.")

    def find(self, username):
        i = 0

        while i < len(self.users):
            
            # print(f"i={i}: users[i].username={self.users[i].username} user.username={username} ")
            if self.users[i].username == username:
                return self.users[i]
            i += 1
        return -1

    def update(self, user):
        
        target = self.find(user.username)

        if target != -1:
            target.name = user.name
            target.email = user.email
        
        # If user is not found insert.
        else:
            self.insert(user)
        
    def list_all(self):
        return self.users

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def tuple_to_tree(data):
    '''
    Description: Helper function that converts a tuple with the structure (left_subtree, key, right_subtree) into a binary tree,
    where left_subtree and right_subtree are tuples themselves.
    '''

    if isinstance(data, tuple) and len(data) == 3:
        
        node = TreeNode(data[1])
        
        # Recursively parse left and right subtrees which are also tuples.
        node.left = tuple_to_tree(data[0])
        node.right = tuple_to_tree(data[2])

        print(f"data={data}, node.key={node.key}")
    
    # Exit recursivity when either None or a number is encountered instead of tuple.
    elif data is None:
        print(f"Encountered None -> data={data}")
        node = None
    else:
        print(f"Encountered a number -> data={data}")
        node = TreeNode(data)
    
    return node

def tree_to_tuple(node):
    '''
    Description: Helper function that converts a tree to a tuple (left_subtree, key, right_subtree) that represents the same tree.
    '''
    key = node.key

    # If node has only a right subtree call tree_to_tuple(node.right).
    if node.left is None and node.right != None:
        left_subtree = None
        right_subtree = tree_to_tuple(node.right)
    
    # If node has only a left subtree call tree_to_tuple(node.left).
    elif node.left != None and node.right is None:
        left_subtree = tree_to_tuple(node.left)
        right_subtree = None
    
    # If node has a left and a right subtree call tree_to_tuple on both. 
    elif node.left != None and node.right != None:
        left_subtree = tree_to_tuple(node.left)
        right_subtree = tree_to_tuple(node.right)
    
    # If node is a leaf return its key.
    elif node.left is None and node.right is None:
        return key
    
    return left_subtree, key, right_subtree

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

def traverse_inorder(node):
    '''
    Description: Performs inorder traversal of a binary tree.
    Inorder Traversal:
     1. Traverse the left subtree recursively inorder.
     2. Visit the current node.
     3. Traverse the right subtree recursively inorder.
    '''

    if node is None:
        return []
    
    return traverse_inorder(node.left) + [node.key] + traverse_inorder(node.right)

def traverse_preorder(node):
    '''
    Description: Performs preorder traversal of a binary tree.
    Preorder Traversal:
     1. Visit the current node.
     2. Traverse the left subtree recursively preorder.
     3. Traverse the right subtree recursively preorder.
    '''

    if node is None:
        return []
    
    return [node.key] + traverse_preorder(node.left) + traverse_preorder(node.right)

def traverse_postorder(node):
    '''
    Description: Performs postorder traversal of a binary tree.
    Postorder Traversal:
     1. Traverse the left subtree recursively postorder.
     2. Traverse the right subtree recursively postorder.
     3. Visit the current node.
    '''

    if node is None:
        return []
    
    return traverse_postorder(node.left) + traverse_postorder(node.right) + [node.key]

def calculate_height(node):
    '''
    Description: Calculates the height of a binary tree as maximum of heights of the left and right subtrees.
    '''

    if node is None:
        return 0
    
    return 1 + max(calculate_height(node.left), calculate_height(node.right))

bobg=User('bobg', 'Bob Green', 'bobg@example.com')
aliceb=User('aliceb', 'Alice Brown', 'aliceb@example.com')
joeb=User('joeb', 'Joe Blue', 'joeb@example.com')
danb=User('danb', 'Dan Black', 'danb@example.com')
pamy=User('pamy', 'Pam Yellow', 'pamy@example.com')
georgeo=User('georgeo', 'George Orange', 'georgeo@example.com')
victorp=User('victorp', 'Victor Pink', 'victorp@example.com')

test_users=[bobg, aliceb, joeb, danb, pamy, georgeo, victorp]

database=UserDatabase()

for user in test_users:
    print(f"Inserting user: {user}")
    database.insert(user)


print(database.list_all())

# Finding danb
#dan=database.find('danb')
#print(dan) 

# Find non existing username.
#raul=database.find('raulp')
#print(raul)

# Update existing user.
#print(f"Before: {database.find('danb')}")
#updated_danb=User('danb', 'Daniel Black', 'danielb@example.com')
#database.update(updated_danb)
#print(f"After: {database.find('danb')}")



# Update not existing user (insert).
#print(f"Before: Finding username=xens {database.find('xens')}")
#xens=User('xens', 'Xen Server', 'xens@example.com')
#database.update(xens)
#print(f"After: {database.find('xens')}")

# Try to insert a user that exists.
#database.insert(danb)


#tree_tuple=((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
# tree_tuple=((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))
           
tree1=tuple_to_tree(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))

#print(tree_to_tuple(tree1))

#display_keys(tree1, ' ')

tree2=tuple_to_tree((((None, 25, (42, 36, 48)), 10, None), 7, ((None, 23, 35), 18, ((43, 39, None), 29, None))))
display_keys(tree2, ' ')

# Alternatively create the left and right subtrees first and then the tree.
#left_subtree=tuple_to_tree(((None, 25, (42, 36, 48)), 10, None))
#right_subtree=tuple_to_tree(((None, 23, 35), 18, ((43, 39, None), 29, None)))
#tree3=tuple_to_tree((tree_to_tuple(left_subtree), 7, tree_to_tuple(right_subtree)))

#display_keys(tree3, ' ')

inorder_traversal=traverse_inorder(tree2)
print(inorder_traversal)

preorder_traversal=traverse_preorder(tree2)
print(preorder_traversal)

postorder_traversal=traverse_postorder(tree2)
print(postorder_traversal)

tree_height = calculate_height(tree2)
print(f"The height of the tree is: {tree_height}")
