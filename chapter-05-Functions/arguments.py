# Arguments passing in callpack functions
import time 
def after(sec, func):
  time.sleep(sec)
  func()
  
# the func  is hardwired to be called with no extra arguments
def add(x, y):
  print(f"{x} + {y} -> {x + y}")
  return x+ y
# after(10, add(3, 4)) # TypeError: 'int' object is not callable
after(2, lambda: add(2, 5))
# A small zero-argument function like this is called thunk
# alternative way is to use functools.partials 
from functools import partial
after(3, partial(add, 2, 3))

# More example of using partials
def func(a, b, c, d):
  print(a, b, c, d)
f = partial(func, 1, 2)
f(3, 4)
# the diference between lambda and partial 
f = lambda: add(2, 3) #  # always 2 and 3, no way to pass new arguments
f()
f = partial(add, 2)
f(3)      
f(5)
# Partial function closely relates to a concept called currying 
"""Currying is functional programming technique where multiple-arguments function is expressed 
 as chain of nested single argument functions
"""
# three-arguments functions 
def f(x, y, z):
  return x + y + z
# curried version
def fc(x):
  return lambda y: (lambda z: x + y +z)
# Example use
a = f(2, 3, 4)
b = fc(2)(3)(4)
print(a)
print(b)
add2 = fc(2)        # locked in x=2, reuse it!
add2(3)(4)  # 9
add2(5)(1)  # 8
add2(1)(1)  # 4
# OR We can *ARGS
def after(sec, func, *args):
  time.sleep(sec)
  func(*args)
  
after(2, add, 10, 10)