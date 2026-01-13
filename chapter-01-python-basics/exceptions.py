"""Errors occurs in program, so exception is raised and traceback message appears,
as it indicates the type of error that happen for examples
"""
# def add_and_multiply(x, y):
#     return (x + y) * x

# add_and_multiply(5, "4")
"""we ran this and exception is raised TypeError: unsupported operand type(s) for +: 'int' and 'str', to handle that error properly, we can could use a try-except block """

def add_and_multiply(x, y):
  try: 
     return (x + y) * x
  except TypeError as e:
    print(f"Error: {e}")
    return None
add_and_multiply(5, "4")
result = add_and_multiply(5, 3)
print(result)