class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f"User(username={self.username}, name={self.name}, email={self.email})"
        
    def __str__(self):
        return f" The User with username = {self.username} has the following properties: name = {self.name} and email = {self.email}"


user1=User('bobg', 'Bob Green', 'bobg@example.com')

print(user1.__repr__())
print(user1.__str__())

