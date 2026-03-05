# Classes are used to create objects
"""All most all python involves creating and performing actions on the objects
"""
s = "hello world"
print(s.upper())       
print(s.split())
print(type(s))
# class statements
# class defination can hav string decumentation string and type hints
class Account:
    """A simple bank account"""
    owner: str
    balance: float
    def __init__(self, owner, balance): # this is used to initialize state when a new instance is created
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):      
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def inquiry(self):
        return self.balance
    def __repr__(self):
        return f"Account({self.owner!r}), {self.balance!r}" # this is magic method that returns string viewing an object
# Intstances
a = Account("Alia", 100.0)
b = Account("Hamid", 200.0)
c = Account("Hadif", 300.0)
a.deposit(100)
b.withdraw(50)
print(a.__repr__())
print(b.__repr__())
# each intance has it is own state we can view it using vars()
print(vars(a))
