# Sets are group of unordered uniqure objects are an essential feature for dealing with collections of data where uniqueness matters.
name1 = {"IBM", "MSFT", "A"}
name2 = {"IBM", "MSFT", "AA", "IBM", "CAT"}
print(name1)
print(name2)
#  When you create a set and add elements to it, any duplicate elements are discarded.
# We can add elements to set by using `add()` method.
name1.add("OpenAI")
# You can remove elements using the `remove()` or `discard()` methods. Note that `remove()` 
# will raise an error if the element is not present, while `discard()` will not. for instance
name1.remove("Azure")
print(name1)
name1.discard("Azure")
print(name1)