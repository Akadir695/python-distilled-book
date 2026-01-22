mylist = ["apple", "banana", "cherry", "blueberry"]
# the indexing operator s[n] returns the nth object from sequence and it starts with 0,1,2,3 
# print(mylist[1])
# print(mylist[-1]) 
""" this returns the last item or otherwise attempts to access elements that are out of range 
of result in  IndexError
"""
# the slicing operator
# print(mylist[1: 2])
# How slicing works: `mylist[start:end]

#? - `start` = 1 (start at index 1, which is "banana")
#! - `end` = 2 (stop BEFORE index 2, which is "cherry")
#? - So you get only index 1
# slicing operator can be optional stride 
mylist2 = ["apple", "banana", "cherry", "blueberry", "mango", "orange"]
# Normal slicing (stride = 1 by default)
print(mylist[0:4])      # ['apple', 'banana', 'cherry', 'blueberry']
# With stride = 2 (every other item)
print(mylist[0:4:2])    # ['apple', 'cherry']
# stride causes to skip elements  of lists
myNumber = [0,1,2,3,4,5,6,7,8,9]
myNumber[2:5]
myNumber[:3]
myNumber[-3:]
myNumber[::2]
myNumber[::-2]
myNumber[::2]
myNumber[0:5:2]
myNumber[0:5:-2]
# Operations on mutable sequences
#  strings and tuples are immutable, and can not be modified after creation



