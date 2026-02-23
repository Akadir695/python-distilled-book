""" This Chapter describes function definations,application, scoping protocols, closure, decorators
 functions definations(we use def statements)
the body of function is sequence of statements that execute when the func is called or executed
"""
def add(x, y): 
  return x+ y
a = add(4, 2)
print(a)
"""Arguments are valued to left-to-right before executing the functions
this is called application evalutiion order:
the order and number of arguments must match the parameters given in the function
 b = add(4, 2, 4)
print(b) # TypeError: add() takes 2 positional arguments but 3 were given
 Default Arguments(we can attach default values to function parameter assigning values in func definations)
"""
 
# WITH default arguments
def add_with_defaults(x, y=0):
    return x + y
result_with_defaults = add_with_defaults(5, 10)
print(result_with_defaults)
# default parameter values are evaluated once when the function is first defined not each time the function is called 
def func(x, items= []):
  items.append(x)
  return items
our_list = func(1)
print(our_list)
our_list_two = func(2)
print(our_list_two)
our_list_three = func(3)
print(our_list_three)
# WHY? The empty list [] is created ONCE when the function is defined
# Every call reuses the SAME list object!
# the correct is to use None Keyword as general don't use mutable object(list, dect, )
def func(x, items= None):
  if items is None:
    items = []
  items.append(x)
  return items
# Vardiac Arguments(*)
def product(first, *args):
  result = first
  for x in args:
    result = result * x
  return result
our_revenue = product(3, 3, 3)
print(our_revenue)
# Keyword Arguments
"""Functions arguments can be supplied by explicity naming each parameter and specifying value
where you explicitly name the parameters when calling a function.
"""
def sum_value(x=3, y=22, w="hello", z=[1, ]):
    print(f"x={x}, y={y}, w={w}, z={z}")
    return x + y
sum_value()
# Vardiac keyword arguments(if the last arguments is prefixed with **
"""all additional arguments(those that don't match any of the other other parameter name)
are placed in dictionary and passed to the function
"""
def build_profile(first, last, **user_info):
    # 'first' and 'last' are required.
    # everything else goes into the 'user_info' dictionary.
    print(f"User: {first} {last}")
    print(f"Additional Data: {user_info}")

build_profile('Aris', 'Thorne', location='London', field='AI')
# Functions that acceptdef accepts()
def accept_all(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:   ", kwargs)
accept_all(1, 2, 3, name="Alice", age=25)

# the name of function should be lowercase with an underscore(_) used as word seperator
# the name of function can obtained via __name__ attribute
def square(x, y):
  return x* y
squared_number = square(4, 4)
print(squared_number)
# Functions Applications and parameter passing (care is required if mutable objects are passed)
def square_items(items):
    for i, x in enumerate(items):
        items[i] = x * x
numbers = [1, 2, 3, 4, 5]
square_items(numbers)

print(numbers)  # Output: [1, 4, 9, 16, 25]
"""in this case if the function mutate their input values or the change the state of other parts program 
are said to have side effects, as general rule the side effects must be avoided
"""
# modifying an object and resasigning a variable name 
def sum_squares(items):
  items = [x*x for x in items]
  return sum(items)
a = [1, 2, 3, 4, 5]
result = sum_squares(a)
print(result)
# Return values (Return return value from the function if no value the None is return )

#  Returning a single value
def add(a, b):
    return a + b
result = add(3, 5)
print(result)  
# Returning multiple values (as a tuple)
def get_user():
  name = "Alice"
  age = 25
  return name, age 

name, age = get_user()
print(name, age)
# Early return (exit function before the end)
def check_age(age):
  if age < 0:
    return "Invalid age"
  return f"age is {age}"
# Error Handling 
# What course of action should be taken if input value is malformed 
def check_age(age):
  if age > 0:
    return f"age is {age}"
  else:
    raise ValueError("bad value")
for value in [5, 0, -2]:
    try:
        print(check_age(value))
    except ValueError as e:
        print(f"Error for {value}: {e}")
