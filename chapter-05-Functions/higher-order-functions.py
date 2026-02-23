"""Python supports the ideas functions that are passed as arguments to other arguments
functions are called first-class objects because they can do everything a regular object (like a number or string) can do
 here is example that accepts another functions as arguments """
import time 
def after(seconds, func):
  time.sleep(seconds)
  func()
def greeting():
  print("hello, world")

after(1, greeting)
"""here is is example of what is known as callback function"""
after(1, lambda: print("hello, world"))  # no need to define a separate function
"""When a functions is passed, it implicitly carries information related to that environment
in which the function was defined
"""
def main():
    name = "Ali"
    def greeting():
        print("Hi", name)
    after(1, greeting)  # calls itself again after 1 second
main()
"""the functions remembers its environment and uses the value of the required name value,
this is known as closures, Closure is function along with an environment containning all of the variable needed
to excute the function body, these are useful for delayed evaluation
like key presses, mouse movement 
"""
# We can write a function that create and return  another functions
def make_greeting(name):
  def greeting():
    print("Hi", name)
  return greeting()
  
make_greeting("ahmed")
#! one caution
def make_greeting(names):
  funcs = []
  for name in names:
    funcs.append(lambda: print("Hello", name))
  return funcs
a, b, c = make_greeting(["ada", "Farah", "Margaret"])
a()
b()
c()
# Hello Margaret
# Hello Margaret
# Hello Margaret
# we use default-arguments
#! one caution
def make_greeting(names):
  funcs = []
  for name in names:
    funcs.append(lambda name=name: print("Hello", name))
  return funcs
a, b, c = make_greeting(["ada", "Farah", "Margaret"])
a()
b()
c()



  
