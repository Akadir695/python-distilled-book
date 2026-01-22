# Sets are unordered collection with unique values 
a = {"a", "b", "c"}
b = {"c", "d"}
print(a | b)
print(a & b) # It returns a new set containing only the elements that appear in both sets. {'c'}
print(a - b) # It returns a new set containing elements that are in the first set but not in the second set. {'b', 'a'}
print(a ^ b) #  It returns a new set containing elements that are in either set, but not in both.
print(len(a)) # the number items in the list
a.add("s")
b.remove("d") # this removes an element if exist otherwise an error
a.discard("a")








