"""Decorator is a function that create wrapper around another function, so we
can alter or enhance the behavior of the object that being wrapped syntatically
"""
def trace(func):
    def call(*args, **kwargs):
        print(f"calling {func.__name__} with {args}")   # before
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")      # after
        return result
    return call
    
# Example use 
@trace
def square(x):
  return x * x
square(5)
print(square.__name__)  # "call"    
print(square.__doc__)   # None       
print(square) 
# the best practice is to use @wraps so we can access function's metdata
from functools import wraps

def trace(func):
    @wraps(func)
    def call(*args, **kwargs):
        print(f"calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return call

@trace          
def square(x):
    """Returns the square of x"""  
    return x * x

square(5)
print(square.__name__)
print(square.__doc__)
print(square)

# A decorator can also accept arguments
def trace(message):          # outer — takes argument
    def decorator(func):     # middle — takes function
        @wraps(func)
        def call(*args, **kwargs):
            print(message)   # use the argument here
            print(f"calling {func.__name__} with {args}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned {result}")
            return result
        return call
    return decorator

@trace("You called  {func.__name__}!")  # ✅ passes message
def square(x):
    """Returns the square of x"""
    return x * x
square(5)

@trace("You called {func.__name__}")
def square_two(x):
    """Returns the square of x"""
    return x * x
square_two(5)
# we can simplify this by reusing the result like 
logged = trace("You called {func.__name__}!")
@logged
def square_two(x):
    """Returns the square of x"""
    return x * x
square_two(5)
@logged
def square(x):
    """Returns the square of x"""
    return x * x
square(5)