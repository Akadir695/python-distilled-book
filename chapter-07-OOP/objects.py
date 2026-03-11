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
# attributes access setting, getting and deleting 
# get 
print(a.owner)
# set 
a.balance = 750.0
# del
print(a.balance)
a.balance = 800.0
# everything is dynamic process with few restrictions we can add new attribute to an object after it has been created
a.create_date = '11/03/2026'
a.nickame = 'former BDFL'
print(a.create_date) 
# We can use getattri,  setattri,  delattr functions instead of using dot operator
print(getattr(a, 'owner'))
#  setattri
setattr(a, "balance", 1000.0)
print(getattr(a, 'balance'))
delattr(a, "balance")
# we can use hasattr() to test the existence of an attribute It only returns True or False 
print(hasattr(a, "balance")) # False
# bound method is when we  access attribute through an object
