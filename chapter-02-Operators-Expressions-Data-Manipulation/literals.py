# Literals is value that are directely typed in the program such as 43, 3, "45"
# Examples:
number = 42          # Integer literal
price = 19.99        # Float literal
name = "Abdul"       # String literal
is_active = True     # Boolean literal
items = [1, 2, 3]    # List literal
point = (5, 10)      # Tuple literal
"""#? we can use the builtin function like bin(x), oct(x) or hex(x) to convert an integer to string"""
print(bin(number))
print(hex(number))
# We can use single underscore to separate between numbers
long_number = 100_000_00
print(long_number)

# Boolean literls are written True and False
is_active = True
is_active = False

# while string literals are written with enclosing with single, double and triple qoutes
name = 'Ali'
name2 = "Ali"
name3 = """ali mohamed"""
print(name3)
# Why different quote types?

# 1. Single quotes when string contains double quotes
message = 'He said "Hello"'
print(message)

# 2. Double quotes when string contains single quotes
message2 = "It's a nice day"

# 3. Triple quotes for multi-line strings
paragraph = """This is a long
multi-line string that
spans multiple lines"""
print(paragraph)
# Mutable objects can use operators
