# Scoping rules 
class AccountScoping:
  def __init__(self, owner, balance):
   self.owner = owner
   self.balance = balance
  def __repr__(self):
   return f"Account({self.owner!r}, {self.balance!r})" # this is magic method that returns string viewing an object
  def deposit(self, amount):
    self.balance += amount
  def withdraw(self, amount):
    self.balance -= amount
  def withdraw(self):
    return self.balance
  def greet(self):
        # print(owner)     Python can't find it
        print(self.owner)  # ✅ works — self points to the object
  
  
# Python lacks a class-level scope 
# This means methods cannot see class-level variables directly — unlike Java/C++.
# Operator overloading and protocols
