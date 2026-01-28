# if, else, elif satements 
"""if expression: 
    statements
    """
"""elif expression: 
    statements
    """
"""elif expression: 
    statements
    """
"""else:
    statements
    """
# no action is is to be taken, we can omit both the else and elif clauses of conditional
# if expression:
  #  pass
# else:
#   statements
# loops and iteration
# while expresion:
#   statements
count = 1
while count <= 5:
    print(count)
    count += 1  # Important! Increment to avoid infinite loo
# for i in s:
#   statements
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)
#  while excuces statements untill the associated expression evaluates to false
#  for statements iterates over all elements untill no elements available
# if elements produced by by iteration are iterable of idenntical size, 
# we can uppack their values into separate iteration variable
# for example
s = [(1,2, 3), (4,5, 6)]
# Unpacking the tuple elements directly in the loop
for a, b, c in s:
    print(f"a: {a}, b: {b}, c: {c}")
# we can use throw-away variable is used while unpacking 
# Example of tuple unpacking
data = ("Alice", 30, "Engineer")
# We only want the name and age, not the profession.
name, age, _ = data
print(f"Name: {name}, Age: {age}")
# if we have varriying sizes we can use wildcard to uppack to place multiples values into variable
# Example with a list of varying sizes

values = [1, 2, 3, 4, 5]
# Unpack first two values and collect the rest
a, b, *rest = values
print(a)    # Output: 1
print(b)    # Output: 2
print(rest) # Output: [3, 4, 5]
# The enumerate() function is a built-in Python function that adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object.
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))
# Sometimes you need to know both the position AND the value of items in a list.
menu_items = ['Pizza', 'Burger', 'Salad', 'Pasta']
for index, item in enumerate(menu_items, start=1):
  print(f"{index}. {item}")