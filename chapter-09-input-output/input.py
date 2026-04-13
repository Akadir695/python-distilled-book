# This chapter describes the essentials of python I/O including data encoding and data representation
#  Python works with two fundemental datatypes: bytes for raw uninterpreted data and text for unicode characters
# bytes are immutable string of integer values, while bytearray is mutable byte array.
"""1. Text (str)
Represents Unicode characters
Human-readable (e.g., "Hello", "£100")
Used when working with text files
---------
Bytes (bytes)
Represents raw binary data
Not human-readable
Used for files like images, videos, network data
"""
text = "Hello"
print(type(text))  # <class 'str'>

a = b'hello'
print(type(a)) # <class 'bytes'>
# Text Encoding and Decoding 
a = 'hello' # text
b = a.encode('utf-8') # this encode to bytes
c = b'world'
d = c.decode('utf-8')
print(d)
# common encoding name include 'ASCII', 'utf-8'
# Text and Byte formatting  to format single value use format()
x = 123.4235
formatted = format(x, '0.2f')
print(formatted)
formatted = format(x, '10.4f')
print(formatted)
formatted = format(x, '*<10.4f')  # left-align, fill with *
# print(formatted)
# the second argument of formatting is format speciafier
name = 'elwood'

print(format(name, "<10"))   
print(format(name, ">10"))  
print(format(name, "^10"))   
print(format(name, "*^10"))

y = 5045

print(format(y, "10d"))   
print(format(y, "10x"))
print(format(y, "10b"))  
print(format(y, "010b")) 

# Zero-padding makes more sense with a wider field:
print(format(y, "016b"))  
# for more string format  format we can use f-strings
n = 123.456
print(f'value is {n:0.2f}')
n = 123.456
print(f'value is {n:0.4f}')