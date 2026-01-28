# Exceptions indicate errors and break out the normal control flow of program 
# for example
# Without try-except the  Program crashes:
"""
Instead of letting your program crash, we can:

Catch the error (with try-except)
Handle it gracefully (show a message, retry, log it, etc.)
Keep the program running (or exit cleanly)"""
file = open("myinfo.txt", "r")  # If file doesn't exist...
content = file.read()
print(content)
# The program crashes completely and the user sees an ugly error message.
try:
    file = open("myinfo.txt", "rt") 
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError as e:
    print("Error: File not found!")
    print(e)  # Print the error details
# we can use pass statement to exceptions 
numbers = [1, 2, "three", 4, "five", 6]
total = 0
for i in numbers:
  try:
    total += i
  except TypeError:
    pass  # Skip non-numbers, continue with next item
print(total) 
# finally statement defines a cleanup action that must execute regardless of what happens in try-except block
try:
    file = open("myinfo.txt", "rt")  
except FileNotFoundError as e:
    print("Error: File not found!")
    print(e)  # Print the error details
else: 
    content = file.read()
    print(content)
finally:
  file.close()