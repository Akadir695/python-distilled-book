# for loop 
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
  print(f'2 to the poweer {n} is {2**n}')
# we can use shortcut 
for n in range(1, 10):
  print(f'2 to the poweer {n} is {2**n}')

# for loop can be used to iterate over many kinds of objects like strings,lists dict and files
message = "hello world"
#this prints individual characters in message
for c in message:
  print(c)
  
# loopin through a list
names = ["Ahmed", "Ali", "Amed", "Aisha", "Ramlo"]
# printing out the member of group 
for name in names:
  print(name)
# we can also loop through a dictionary
my_dict = {
    'apple': 1,
    'banana': 2,
    'cherry': 3
}
# printing out all of the member of a dictioanary 
# print(my_items.items())
for key, value in my_dict.items():
 print(key, "=", value)