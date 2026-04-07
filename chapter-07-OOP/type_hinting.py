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
# we can set an attribute to anything we want 
a = Account("faizo", 50.0)
print(a.owner)
a.owner = 50
print(a.owner)
b = Account("faizo", "alott")
b.balance = "i am rich"
print(b.balance)
# one possible solution is we should not do that or we can owner: str   balance:   balance: float to give the users information
print(type(Account))

