# Most python language feature are defined by protocols
def compute_cost(unit_price, num_price):
  return unit_price * num_price
# What inputs are allowed? it can work with numbers
result = compute_cost(1.25, 50)
print(result)
#  it can also work with specialised numbers such as fractions and decimals
from fractions import Fraction
fraction_result = compute_cost(Fraction(4, 4), 50)
print(fraction_result) # 50
from decimal import Decimal
decimal_result = compute_cost(Decimal("1.25"), Decimal("50"))
print(decimal_result) # 62.50
#  the function might workd inunexpected ways
unexpected_result = compute_cost("alot", 50)
print(unexpected_result) 
# python does not verify correct program behavior in advance 
# This behavior is determined by dynamic process that involves the dispatch of so-called "special" or Magic methods
# the behavior of any given object depends entirely on the set of special methods that it implements
# Object Behavior = The Magic Methods It Implements
# The car's capabilities = what it physically has
# The object's behavior = what magic methods it implements
