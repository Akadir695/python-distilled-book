# json module can be used to encode and decode data in json format
# and it commanly used in API of microservices and web application
# There are two basic functions for converting data(dumps(), loads())
import json
data = {'name': 'Mary', 'age': 23, 'email': 'mary@gmail.com'} # this is python dictionary to convert to json we use dumps()
s = json.dumps(data)
print(s)
# JSON string → dict
back = json.loads(s)
print(type(back))  # <class 'dict'>

print(data == back)