#   First class objects
# All object is python said to be first-class meaning it can be assigned to a name and treated as data
items = { 
  "number": 42,
  "text": "hello world"
}
# we can add some unsual items 
items["func"] = abs
import math
items['mod'] = math
# we can even add methods of another object
nums = [1,2,3,4,5]
items['append'] = nums.append
# print(items['mod'].pi)    # Output: 3.141592...
# for example

line = "ACME,100,490.10"
columns_types = [str, int, float]
parts = line.split(',')
row = [ty(val) for ty, val in zip(columns_types, parts)]
print(row)
# Using None for optional or missing data 
"""None is returned by functions that explicity don't return a value or default value of optioanal arguments"""
# if the value is none: 
  # statements
# Optional function arguments (default None):
def greet(name, title= None):
  if title is None:
    print(f"Hello, {name}")
  else:
    print(f"Hello, {title} {name}")
greet("Alice") # Hello, Alice
greet("Alice", "Drs") # Hello, Drs Alice
#   No return statement at all
def says_hello():
  print("hello")
  
result = says_hello()
print(result) # None
