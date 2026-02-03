# identiy f object is a number representing its location in memory
# and object said to be mutable when its value can be modified 
# # IMMUTABLE objects (cannot be modified; operations create NEW objects):
my_int = 10
# print(id(my_int))
my_int = my_int + 5     # Creates a NEW object
# print(id(my_int))
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
# print(sys.getrefcount(a))  # Output: 2 (not 1!)
# del b  # this decreases reference count = 2
# when the object reference count reaches zero it is garbage collected
# however some cases circular dependency may exist in collection of objects that are no longer in use
# a = {}
# b = {}
# a['b'] = b   # a references b
# b['a'] = a
# print(a)
# print(b)
# del a
# del b
 #   Box A  ←─────→  Box B
# - Box A exists because Box B is pointing to it
# - Box B exists because Box A is pointing to it
# references and coipes 
# a = [1, 2, 3, 4]
# b = a 
# print(a is b) # in this case the a is reference to a
# b[2] = -100
# print(a)
# print(b) # [1, 2, -100, 4]
# The is operator checks for identity (whether two variables point to the exact same object in memory), not equality.
"""a and b refer to same to the ob object if we do change to the variable 
a change is reflected in other to avoid we have to create a copy of an object rather than an
new a reference 
"""
# the two types of copies we can use are deep copy and shallow copy
"""A shallow copies creates a new object but populates it with reference to the items 
contained in the original object 
"""
a = [1,2, [3,4]]
b = list(a)
print(a is b )
b.append(100)
print(b) # [1, 2, [3, 4], 100]
print(a) # [1, 2, [3, 4]]
b[2][0] = -100 
print(b) # [1, 2, [-100, 4], 100]
print(a) # [1, 2, [-100, 4]]
# why is this? shallow copy creates: New outer container only does NOT create: Copies of any nested mutable objects
# Deep copy creates a new object and recursively copies all the objects it contains
import copy 
x = [100, 200, [300, 400]]
y = copy.deepcopy(x)
y[2][0] = -100
print(x) # [100, 200, [300, 400]]
print(y) # [100, 200, [-100, 400]]
"""the use of deepcopy is actively discouraged in most programs as it is slow and unnecesary only use them 
  only use for when you dont want your changes to effect the original objects
"""
