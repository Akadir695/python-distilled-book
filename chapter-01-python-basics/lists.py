# we use lists to store ordered lists
# we can create list in two ways 

names = []
info = list()
info.append("we can add info")
print(info)
names = ["Ahmed", "Ali", "Amed", "Aisha", "Ramlo"]
# to access speciafic item in a list we use index operator and it starts with 0,1,2...
print(names[2])
# to add new items to list we append() method
names.append("Halimo")
print(names)
# to insert new item in speciafic index  to list we insert() method
names.insert(2, 'Akadir')
print(names)
# we can iterate through lists
for name in names:
  print(name)
  
# We can extract a portion of a list
names = ["Ahmed", "Ali", "Amed", "Aisha", "Ramlo"]
print(names[2 : 4])
# We can concetenate two list 
add_names = ['Abdikafi', "abdikadir"]
completed_names = names + add_names
print(completed_names)
# Nested Lists
nested_list = [1, "dave", ['Mark', 7, 9], [100, 101], 10]
print(nested_list[3][1])