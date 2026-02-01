# Every piece of data stored in program is an object 
# each object has identity, type and value 
# for example a = 42 this is object and its type is an integer
# while attribute is value that is associated with object that is accesed by dot(.) operator
# compare two objects 
def compare(a, b):
  if a is b:
    print("same object")
  if a == b:
    print("same value")
  if type(a) is type(b):
    print("same type")
a = [1, 2, 3]
b = [1, 2, 3]
compare(a,b) # same value, same type

# identiy f object is a number representing its location in memory
# and object said to be mutable when its value can be modified 
# # IMMUTABLE objects (cannot be modified; operations create NEW objects):
my_int = 10
print(id(my_int))
my_int = my_int + 5     # Creates a NEW object
print(id(my_int))
# References counting and garabge collection
# Python manages objects through automatic garbage collection
# meaning all objects are reference counted, it get increased when we assigned a new name in placed in container 
my_value = 37  # One object in memory, reference count = 1
b = my_value   # Still ONE object in memory, reference count = 2
# When references are removed, the count decreases
# we can obtain the current reference count of an object using sys.getrefcount() function

# Get reference count of an object
import sys
a = [1, 2, 3]
print(sys.getrefcount(a))  # Output: 2 (not 1!)
# del b  # this decreases reference count = 2
# when the object reference count reaches zero it is garbage collected
# however some cases circular dependency may exist in collection of objects that are no longer in use
a = {}
b = {}
a['b'] = b   # a references b
b['a'] = a
print(a)
print(b)
del a
del b
 #   Box A  ←─────→  Box B
# - Box A exists because Box B is pointing to it
# - Box B exists because Box A is pointing to it
