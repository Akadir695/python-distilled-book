# context manager and with statement
# raised exception can cause control flow to bypass statement to excute inside a runtime context
# What happened:
#  "context" = a managed block of code where setup and cleanup are handled for you automatically.
# Entering: File was opened
# Inside: You can use the file
# Exiting: File was automatically closed (cleanup)
with open('myinfo.txt') as f:
    data = f.read()
    print(data)
# File auto-closed here
# Without context (manual cleanup)
f = open('myinfo.txt', 'w')
try:
    f.write('this is additional info that we need to that in our system')
finally:
    f.close()  # Must remember to close!
# assertions and __dubug__
# Assertions are used to check conditions that should always be true during development
# we use them in testing
def factorial(n):
  result = 1
  while n > 1:
    result *= n
    n -= 1
  return result 
assert factorial(5) == 120
