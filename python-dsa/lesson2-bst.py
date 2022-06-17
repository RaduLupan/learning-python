'''
Problem: We need to create a data structure which can store 100 million records and perform insertion, search, update and list operations efficiently.
Input: User profiles which contain username, name and email for a user.
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
        i = 0

        while i < len(self.users):
            # Find the index for the first username in users greater than the username.
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)

    def find(self, username):
        i = 0

        while i < len(self.users):
            
            print(f"i={i}: users[i].username={self.users[i].username} user.username={username} ")
            if self.users[i].username == username:
                return self.users[i]
            i += 1
        return -1
    def update(self, user):
        pass
    def list_all(self):
        print(self.users)

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


database.list_all()

# Finding danb
dan=database.find('danb')
print(dan) 

# Fin non existing username.
raul=database.find('raulp')
print(raul)
