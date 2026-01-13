# we use def statement define a functions
def remainder(a, b):
  q = a // b
  r = a - q * b
  return r
# to invoke a function we use its name by it is arguments in parenthesis for example
result = remainder(37, 15)
print(result)
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")