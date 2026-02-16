# This Chapter describes function definations,application, scoping protocols, closure, decorators
# functions definations(we use def statements)
def add(x, y): # the body of function is sequence of statements that execute when the func is called or executed
  return x+ y

a = add(4, 2)
print(a)
# Arguments are valued to left-to-right before executing the functions
# this is called application evalutiion order:
# the order and number of arguments must match the parameters given in the function
# b = add(4, 2, 4)
# print(b) # TypeError: add() takes 2 positional arguments but 3 were given
# Default Arguments(we can attach default values to function parameter assigning values in func definations)

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
def sum(x=3, y=22, w="hello", z=[1, ]):
    print(f"x={x}, y={y}, w={w}, z={z}")
    return x + y
sum()
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
