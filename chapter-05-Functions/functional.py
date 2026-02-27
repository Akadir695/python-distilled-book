# Map, filter and reduce 
# we can use list-compresention 
def square(x):
  'the function is squaring the the given x'
  return x * x
result = square(5)
print(result)
#  we can use list compresention 
nums = [1, 2, 3, 4, 5]
square_list = [square(x) for x in nums]
# short way
square_list = [ x * x for x in nums]
print(square_list)
# we can perform filtering with list-compresention
a = [x for x in nums if x > 2]
print(a) # [3, 4, 5]
# Python provides built-in map function 
nums = [1, 2, 3, 4, 5]
mapped = map(lambda x: x * x, nums)
# reduce is used to accumalate or reduce values
from  functools import reduce
total = reduce(lambda x, y: x + y, nums)
print(total)
for n in filter(lambda x: x > 2, nums):
  print(n)
# In general reduce() accepts a two-argument function, an iterable and an initial value
total = reduce(lambda x, y: x + y, nums)
total = sum(nums)
print(total)
produce = total = reduce(lambda x, y: x * y, nums, 1)
print(produce)
# Instead we can use built in function like sum, min and max
# Function  intropection, attributes and signtures
"""Functions are object as they can assigned to and used in the same way
as any other kind of of data in program and it has attributes
"""
# function attributes
print(square.__name__)
print(square.__doc__)
print(square.__qualname__)
print(square.__module__)
# for example
def add(x , y):
  def do_add():
    return x + y
  return do_add
added = add(5, 4)
print(added())
print(added.__closure__)
print(added.__closure__[0].cell_contents)
print(added.__closure__[1].cell_contents)
# Environment inspection
# funcs can inspect their execution environment using the built-in function globals() and locals()
x = 10  # global variable
# def add(a, b):
#     c = a + b  # local variable
#     print(locals())   # {'a': 5, 'b': 4, 'c': 9}
#     print(globals())  # {'x': 10, 'add': <function>, ...}
#     return c

# add(5, 4)
