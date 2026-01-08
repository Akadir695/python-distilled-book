# Dictionaries are used to store data values in key:value pairs
# we can create emprty dic in two ways 
prices = {
} # or 
our_prices = dict()
my_dict = {
    'name': 'Akadir',
    'age': 22,
    'city': 'Somali'
    
}
# To access it we can index operator like this
print(my_dict["name"])
print(my_dict["age"])

if "name" in my_dict:
  print("Great, we got your name")
else:
  print("please, provide your name")
  
# we can use del statement to remove elements in dictionary
del my_dict['city']
print(my_dict)
# to get list of dict keys convet dict into list
# Example dictionary
my_dict = {
    'apple': 1,
    'banana': 2,
    'cherry': 3
}
my_data = list(my_dict.keys())
print(my_data)
# or we can use .keys method using this methods it directly refelcts on changes made to dict
#? 
my_items = {"x": 1, 
            "y": 2,
            "z": 3}
my_data = list(my_items.keys())
del my_items["x"]
print(my_items.keys())
print(my_data)
# to obtain key,values pairs we use .items method 
print(my_items.items())
