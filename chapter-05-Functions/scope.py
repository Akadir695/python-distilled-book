# Scoping Rules
"""Local variable are the names that are used and assigned inside the function and only accessible within that function.
global variable are the names that are used and assigned outside the function """
# def func(x):
#   if x > 0:
#     y = 42
#   return x + y
# result = func(10)
# print(result)
# result = func(-10) # UnboundLocalError: cannot access local variable 'y' where it is not associated with a value
# The variable never change their their scope 
# x = 42   # global variable
# def func_one():
#   print(x)
#   x = 12
# func_one()
#  **Python scans the entire function first** — when it sees `x = 12`, it marks `x` as a **local variable** for the **whole function**, including the lines above it.
x = 42   # global variable
def func_one():
  global x
  x = 13
  print(x)
func_one()
#! note using global statement is usually considered poor Python style
# we should use class defination and modify state my mutating an instance or class variable
class MyClass:
    x = 42                    # class variable

    def func_one(self):
        self.x = 13           # modifies instance variable cleanly
        print(self.x)         # 13
obj = MyClass()
print(obj.x)     # 42
obj.func_one()   # 13
print(obj.x)     # 13
# nonlocal can not be used to refer a global variable
def countdown(start):
  n = start
  def display():
    print("T-minus", n)
  def decrement():
    nonlocal n
    n -= 1
  while n > 0:
    display()
    decrement()
countdown(10)