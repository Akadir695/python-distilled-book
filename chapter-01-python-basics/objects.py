# All values used in program are objects
class Stack:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def pop(self):
        return self._items.pop()
    
    def __repr__(self):
        return f'<{type(self).__name__} at 0x{id(self):x}, size = {len(self)}>'
    
    def __len__(self):
        return len(self._items)
      
s = Stack()
s.push("Dave ")
s.push("Ali ")
print(s)
result = s.__len__()
print(result)
"""Python does not have any mechanism for hiding or protecting data. However,t there is programming convention
with in names procecced by single underscore are taken to be private 
"""
#  BAD PRACTICE - Directly accessing "private" attribute:

class BankAccount:
    def __init__(self):
        self._balance = 0
        self._transaction_count = 0
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transaction_count += 1  # Tracks transactions
            print(f"Deposited ${amount}. Total transactions: {self._transaction_count}")

account = BankAccount()

#  Correct way:
account.deposit(100)  # Deposited $100. Total transactions: 1

#  Direct access bypasses the logic:
account._balance += 50  # Balance updated but transaction_count is NOT!

print(account._balance)           # 150 (correct)
print(account._transaction_count) # 1 (WRONG! Should be 2)

# *Inheritance is way we can add or redefince the capabilities of existing classes
# Example 
class Employee:
  def __init__(self, name, salary):
     self.name = name
     self.salary = salary
  
  def work(self):
    return f'{self.name} is working' 
  
  def get_salary(self):
    return self.salary
  
    
class Manager(Employee):
  def __init__(self, name, salary, team_size):
     self.name = name
     self.salary = salary
     self.team_size = team_size
     
  # We can redefine the work method
  def work(self):
    return f'{self.name} is managing {self.team_size} people' 
  
  def hold_meeting(self):  # New capability
        return f"{self.name} is holding a meeting"
  
manager = Manager("Alice", 90000, 5)
print(manager.work())
print(manager.hold_meeting()) 
print(manager.get_salary())    