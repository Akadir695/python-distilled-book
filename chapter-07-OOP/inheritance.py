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
        # return f"Account({self.owner!r}), {self.balance!r}"# this is magic method that returns string viewing an object
         return f"{type(self).__name__}{self.owner!r}, {self.balance!r}'"
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
# We can use super()
class EvilAccount(Account):
    def inquiry(self):
        if random.randint(0, 4) == 1:
            return 1.10 * super().inquiry()
        else:
            return super().inquiry()
b = EvilAccount("Evil man", 80.0)
b.deposit(10.0)
available = b.inquiry()
print(available)       
# less common : we can use inheritance add additional attributes to instance 
class EvilAccount(Account):
  def __init__(self, owner, balance, factor):
     super().__init__(owner, balance)
     self.factor = factor
  def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.factor * super().inquiry()
        else:
          return super().inquiry()
c = EvilAccount("added attributed", 10.0, 1.10)
c.deposit(10.0)
available = c.inquiry()
print(available)   
# inheritance can break the code in subtle way
c = EvilAccount("john does", 20.0, 1.10)
print(c)   # Account('john does'), 20.0 instead of EvilAccount
# when using inheritance we should avoid the hardcoding class name
# the danger of inheriting from built-in types
class udict(dict):
  def __setitem__(self, key, value):
     return super().__setitem__(key.upper(), value)
u = udict()
u["name"] = "John"
u["number"] = 37
# print(u)
u.update(color ='blue') # this manipulate the dictionary with out ever routing through the redefined __setitem__()
print(u)
# we can use collections module for this exact issue 
from collections import UserDict
class udict(UserDict):
  def __setitem__(self, key, value):
     return super().__setitem__(key.upper(), value)
u = udict(name = 'farah', age = 20)
print(u)
u.update(color = 'red')
print(u)
# class variable and methods
