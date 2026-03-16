"""Inheritace is the mechanism for creating a new class that modifies or specializes the
behavior of existing class, the existing class is called base class, superclass or parent class 
while the new class is class derived class, subclass, subtype,
when a class is created the via inheritance it inherits the attributes of parent class
one use of inheritance is to  extend an existing class with new methods.
"""
import random
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
class MyAccount(Account):
  def panic(self):
    self.withdraw(self.balance)
a = MyAccount("faiza", 100)
a.withdraw(24.0)
print(a.inquiry())
# we can also use inheritance to redifine the already existing methods
class EvilAccount(Account):
  def inquiry(self):
     if random.randint(0, 4) == 1:
       return self.balance * 1.10
     else:
       return self.balance
b = EvilAccount("Evil man", 80.0)
b.deposit(10.0)
available = b.inquiry()
print(available)