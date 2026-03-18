# class variable 
class Account:
    """A simple bank account"""
    num_accounts = 0
    owner: str
    balance: float
    def __init__(self, owner, balance): # this is used to initialize state when a new instance is created
        self.owner = owner
        self.balance = balance
        Account.num_accounts += 1

    def deposit(self, amount):      
        self.balance += amount

    def withdraw(self, amount):
        self.deposit(-amount)

    def inquiry(self):
        return self.balance
    def __repr__(self):
        # return f"Account({self.owner!r}), {self.balance!r}"# this is magic method that returns string viewing an object
         return f"{type(self).__name__}{self.owner!r}, {self.balance!r}'"
a = Account("harun", 100.0)
a = Account("faiza", 100.0)
print(Account.num_accounts)
# class variable can be accesed by via instances
print(a.num_accounts)

# A static method is a method that belongs to a class but doesn't need access to the class (cls) or instance (self).
class Ops:
  @staticmethod
  def add(x, y):
    return x + y
  @staticmethod
  def sub(x, y):
    return x - y
a = Ops.add(2, 4)
b = Ops.sub(10, 5)
# in Python all attributes and methods are puplic meaning they can be accesed with out restrictions
class Account:
    """A simple bank account"""
    num_accounts = 0
    owner: str
    balance: float
    def __init__(self, owner, balance): # this is used to initialize state when a new instance is created
        self.owner = owner
        self._balance = balance
        Account.num_accounts += 1

    def deposit(self, amount):      
        self._balance += amount # # _ prefix = "private by convention"

    def withdraw(self, amount):
        self.deposit(-amount)

    def inquiry(self):
        return self._balance
    def __repr__(self):
        # return f"Account({self.owner!r}), {self.balance!r}"# this is magic method that returns string viewing an object
         return f"{type(self).__name__}{self.owner!r}, {self.balance!r}'"
# we can use __underscoure this ensures that priavte names won't be overwritten by identical names in child class
class A:
    def __init__(self):
        self.__x = 3           

    def __spam(self):
        print("A.__spam", self.__x)

    def bar(self):
        self.__spam()

class B(A):
    def __init__(self):
        super().__init__()      
        self.__x = 99           

    def __spam(self):
        print("B.__spam", self.__x)

    def grok(self):
        self.__spam()

b = B()
b.bar()  
b.grok()

  

