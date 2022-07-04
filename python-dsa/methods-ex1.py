'''
Instance, Class, and Static Methods - An Overview
See the full tutorial here:
https://realpython.com/instance-class-and-static-methods-demystified/
'''
class MyClass:
    def method(self):
        return 'instance method called', self
    
    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    
    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()

# Call the instance method.
obj.method()

# Call the class method.
obj.classmethod()

# Call the static method.
obj.staticmethod()
