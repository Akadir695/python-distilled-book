#  generator expressions generate values lazily (one at a time) instead of creating the entire list in memory.
nums = [1,2,3,4]
squares = (x*x for x in nums)
print(squares) # <generator object <genexpr> at 0x1048f1e50>
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
# generator expression is only used once, we can not iterate second time
# they are great for memory use and performance 
for n in squares:
  print(n)
# we can convert them to list 
our_list = list(squares)
print(our_list) # this gave me [] list because # Second use - generator is now empty/exhausted
# To use it again, recreate the generator
squares = (x*x for x in nums)
our_list = list(squares)
print(our_list)
