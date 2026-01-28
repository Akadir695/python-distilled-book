"""One of most common operation is involving transforming a collection of data into another
anoher data collecion"""
# List comprehension 
# Transform: square each number
"""A list comprehension is a concise way to create a new list by transforming and/or filtering elements from an existing collection (like a list, tuple, set, or range)."""
numbers = [1, 2, 3, 4, 5]
squares = []
# Traditional loop approach:
for x in numbers:
  squares.append(x**2)
print(squares)
# More concise way 
squares = [x**2 for x in numbers]
print(squares)
# we can apply filters to the operation
squares = [x**2 for x in numbers if x > 1]
# squares = [x**2 for x in numbers]
print(squares)
# Attribute (.) operator is used to access the attributes of an object
