# generator, genarator delegation, generator-based corouritines
# The primary function is produce values for use in iteration
def countdown(n):
  print("Counting down from", n)
  while n > 0:
    yield n #  yield makes it produce values one at a time instead of all at once:
    n -= 1 
for x in countdown(10):
  print("T-minus ", x)
  
c = countdown(10)
print(next(c))
print(next(c))
print(next(c))
# The difference is in memory — a normal function loads everything at once, a generator loads one value at a time
# def func():
#   yield 34
#   return 42
# f = func()
# print(next(f))
# print(next(f)) # StopIteration: 42
# StopIteration is the exception Python raises when a generator has no more values to produce:
# genarator function execute at once normally
y = countdown(3)
for a in y:
   print("T-minus ", a)
for a in y:
   print("T-minus ", a)
#  Generator delegation
def countup(stop):
  n = 1
  while n <= stop:
     yield n
     n +=1 
     
def countdown(start):
  n = 1
  while n <= start:
     yield n
     n -=1 
    
def up_and_down(n):
  yield from countup(n)
  yield from countdown(n)
  
  
    
      
