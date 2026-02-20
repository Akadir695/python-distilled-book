# An anonymous --unnamed function can be defined with lambda function
# lambda args: expression, args are separeted by comm, while expression is expressions involving those arguments
a = lambda x, y: x +y 
r = print(a(3, 4))

"""multiple expressions are not allowed such as try and while, lambda expressions follows the same scoping rules as functions"""
# Sort a list of words by the number of unique letters
words = ["apple", "banana", "kiwi", "fig", "cherry"]
# set(word) Converts the word into a set, which automatically removes duplicate
print(set("apple") ) # {'e', 'p', 'a', 'l'}
result = sorted(words, key=lambda word: len(set(word)))
print(result)
# Caution is required when a lambda expression contains free variable(not specified as parameter)
x = 2
f = lambda y: x * y
x = 3
g = lambda y: x * y
print(g(10)) # 30
print(f(10)) # 30
"""in this case as free variable  print(f(10)) uses x whatever happens to have at the time of of evalution a
and this behavior is called late-binding"""

# if it is important to capture the value of variable at the time of defination we use default argument 
x = 2
f = lambda y, x =x: x * y
x = 3
g = lambda y: x * y
print(g(10)) # 30
print(f(10)) # 20 — early binding, captured x=2
# the choice of using lambda is personal preference and a matter of code clarity