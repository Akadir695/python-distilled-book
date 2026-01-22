# Operations on mapping 
# Creating a mapping from names to ages
ages = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}

print(ages["Alice"])  # 25
del ages["Alice"] # this deletes item by keys"
ages["Joe"] = 40 # This assignment by key
if  "Alice" in ages:
  print("we got her details")
else:
  print("nope") # this test membership
print(ages) 
print(len(ages)) # Number of items in the mappings
print(ages.values()) # dict_values([30, 35, 40])
print(ages.keys()) # dict_keys(['Bob', 'Charlie', 'Joe'])
print(ages.items()) # dict_items([('Bob', 30), ('Charlie', 35), ('Joe', 40)])
 