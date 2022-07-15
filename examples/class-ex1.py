class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name =name
        self.email = email

    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def introduce_yourself(self, guest_name):
        print(f"Hi {guest_name}! My name is {self.name} and you can contact me at {self.email}")

    def full_info(self, guest_name):
        # If method introduce_yourself is called it needs to be prefixed by self. to avoid NameError exception.
        self.introduce_yourself(guest_name)
        print(f"My user name is {self.username}")

dan = User('danb', 'Dan Brown', 'danb@example.com')

dan.introduce_yourself('David')

dan.full_info('Pamela')


