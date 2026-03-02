# Dynamic code exucution and creation
a = [2, 34, 3, 45]
exec("for i in  a: print(i)")
# Changes to local variable have no effect
def func():
  x = 10
  exec("x = 20")
  print(x)

func()