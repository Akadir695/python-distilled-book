""" Expression values to conrete value for instance it contains
 literals, names, operators and function or method calls
"""
# Function call expressions
len("hello")    # Evaluates to 5
max(5, 10, 3)   # Evaluates to 10
abs(-42)        # Evaluates to 42
# Arithmetic expressions
x = 12
2 + 3           # Evaluates to 5
x * 2           # Evaluates to 20
(10 + 5) / 3    # Evaluates to 5.0
# In place Assignment
y = 10
y += 4
print(y)
# These are not considered expressions, instead there are systactic convenience for updating value in place
a = 3
a += 5
a -= 2
print(a)
# Mutable objects can use operators
b = [2, 9, 8, 2]
z = b
print(z) # this now refer to a
z += [99, 99]
print(z) # this updates the list with out creating new list

# Object Comparison, equality operator == test values x and y for equality 
obj = 2
obj2 = 3
if obj == obj2:
  print("equal values ")
else:
  print("notequal values ")
  
# in the case list and tubles they must have the same elements 


