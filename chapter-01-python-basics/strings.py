x = "hiaworld"
print(len(x))
# to extract single character

print(x[6])
#  to extract substring  characters
print(x[3: 7])
# we can only use replace method 
y = x.replace("hi", "helloCruel")
print(y)
# split method
txt = "welcome to the jungle"

x = txt.split()

for i in range(len(x)):
  print(x[i])
# String concetenates
x = "4"
y = '3'
g = x + y
print(g)
# we can not do this for exampple
x = "4"
y = 3
g = x + y
#  this is wrong because y is not integer we will have TypeError: can only concatenate str (not "int") to str
print(g)
# to overcome this we can convert x into integer then add them together
x = "4"
y = 3
g = int(x) + y
print(g)
# Example of using str and repr
s = "Hello\nworld"
print(str(s))
# repr
print(repr(s))

