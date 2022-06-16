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
    def insert(self, user):
        pass
    def find(self, username):
        pass
    def update(self, user):
        pass
    def list_all(self):
        pass

bobg=User('bobg', 'Bob Green', 'bobg@example.com')
aliceb=User('aliceb', 'Alice Brown', 'aliceb@example.com')
joeb=User('joeb', 'Joe Blue', 'joeb@example.com')
danb=User('danb', 'Dan Black', 'danb@example.com')
pamy=User('pamy', 'Pam Yellow', 'pamy@example.com')
georgeo=User('georgeo', 'George Orange', 'georgeo@example.com')
victorp=User('victorp', 'Victor Pink', 'victorp@example.com')

users=[bobg, aliceb, joeb, danb, pamy, georgeo, victorp]

for user in users:
    print(user)



