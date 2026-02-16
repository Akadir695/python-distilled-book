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