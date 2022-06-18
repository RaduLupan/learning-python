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

def parse_tuple(data):
    '''
    Description: Helper function that converts a tuple with the structure (left_subtree, key, right_subtree) into a binary tree,
    where left_subtree and right_subtree are tuples themselves.
    '''

    if isinstance(data, tuple) and len(data) == 3:
        
        node = TreeNode(data[1])
        
        # Recursively parse left and right subtrees which are also tuples.
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])

        print(f"data={data}, node.key={node.key}")
    
    # Exit recursivity when either None or a number is encountered instead of tuple.
    elif data is None:
        print(f"Encountered None -> data={data}")
        node = None
    else:
        print(f"Encountered a number -> data={data}")
        node = TreeNode(data)
    
    return node

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
           
tree=parse_tuple(((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8))))

print(tree.left.key, tree.right.key)
