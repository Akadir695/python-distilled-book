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
# print(y)
# These are not considered expressions, instead there are systactic convenience for updating value in place
a = 3
a += 5
a -= 2
# print(a)
# Mutable objects can use operators
b = [2, 9, 8, 2]
z = b
# print(z) # this now refer to a
z += [99, 99]
# print(z) # this updates the list with out creating new list

# Object Comparison, equality operator == test values x and y for equality 
# obj = 2
# obj2 = 3
# if obj == obj2:
#   print("equal values ")
# else:
#   print("notequal values ")
  
# in the case list and tubles they must have the same elements 
# the + operator concatenates two sequence of same type for example
a = [3, 53, 3, 5]
b = [5, 67]
c = a + b 
# print(c)
""" While s * n operator makes n copies of sequence, these shallows copies that replicate elemenents by reference"""
reference_1 = [1,2, 3, 5]
m = [reference_1]
n = 4  * m
# print(m)
# print(n)
# We can construct the replicated sequence by duplicating the contents of a 
list_1 = [3, 4, 6]
list_2 = (list(list_1) for _ in range(4))
print(list_1)
# Now modify list_1
list_1.append(999)
print(list_2)
print(list_1)
